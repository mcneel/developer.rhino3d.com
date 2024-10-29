#!/usr/bin/env python3
import os
import tomlkit
import argparse

# This script helps to identify and fix aliases that are not localized.

def find_and_fix_unlocalized_aliases(content_dir, fix=False):
    mismatches_found = False
    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if content.startswith('+++'):
                        end = content.find('+++', 3)
                        if end != -1:
                            toml_content = content[3:end]
                            post = tomlkit.parse(toml_content)
                        else:
                            post = tomlkit.document()
                    else:
                        post = tomlkit.document()
                    
                    if 'aliases' in post:
                        # Determine the language folder from the file path
                        relative_path = os.path.relpath(file_path, content_dir)
                        lang_folder = relative_path.split(os.sep)[0]
                        updated_aliases = tomlkit.array()
                        for alias in post['aliases']:
                            if not alias.startswith(f'/{lang_folder}/'):
                                print(f"Alias mismatch in {file_path}: {alias} should start with /{lang_folder}/")
                                mismatches_found = True
                                if fix:
                                    # Fix the alias
                                    corrected_alias = f'/{lang_folder}{alias}'
                                    updated_aliases.append(corrected_alias)
                                else:
                                    updated_aliases.append(alias)
                            else:
                                updated_aliases.append(alias)
                        
                        if fix:
                            # Update the post with corrected aliases
                            post['aliases'] = updated_aliases
                            
                            # Write the updated content back to the file
                            new_toml_content = tomlkit.dumps(post).strip()
                            new_content = f'+++\n{new_toml_content}\n+++' + content[end+3:]
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(new_content)
    
    if not mismatches_found:
        print("No mismatched aliases found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find and optionally fix unlocalized aliases in markdown files.')
    parser.add_argument('--fix', action='store_true', help='Fix mismatched aliases with the proper alias.')
    args = parser.parse_args()

    content_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../content'))
    find_and_fix_unlocalized_aliases(content_dir, args.fix)
