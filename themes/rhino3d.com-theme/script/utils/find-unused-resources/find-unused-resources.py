import os
import re

def find_files(root_folder, extensions):
    files = []
    for root, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                files.append(os.path.join(root, filename))
    return files

def find_references_in_source_files(root_folder, extensions):
    references_patterns = [
        re.compile(r'\[.*?\]\((.*?)\)'),  # Markdown links
        re.compile(r'thumbnail\s*=\s*["\'](.*?)["\']'),  # Frontmatter thumbnail
        re.compile(r'banner\s*=\\s*["\'](.*?)["\']'),  # Frontmatter banner
        re.compile(r'<a\s+(?:[^>]*?\s+)?href=["\'](.*?)["\']'),  # HTML links
        re.compile(r'<img\s+(?:[^>]*?\s+)?src=["\'](.*?)["\']'),  # HTML images
        re.compile(r'["\'](.*?\.(?:' + '|'.join([ext.lstrip('.') for ext in extensions]) + r'))["\']'),  # Any reference to files with specified extensions
        re.compile(r'url\s*=\s*["\'](.*?)["\']'),  # TOML url
        re.compile(r'path\s*=\s*["\'](.*?)["\']'),  # TOML path
        re.compile(r'\{\{<\s*image\s+.*?\s+["\'](.*?)["\']\s+.*?>\}\}'),  # Hugo image shortcode
        re.compile(r'\{\{\s*<\s*image\s+.*?\s+["\'](.*?)["\']\s+.*?>\s*\}\}'),  # Hugo image shortcode with spaces
        re.compile(r'\{\{\s*<\s*image\s+["\'](.*?)["\']\s+.*?>\}\}'),  # Hugo image shortcode without spaces
        re.compile(r'image\s*=\s*["\'](.*?)["\']'),  # Generic image reference
        re.compile(r'url\(["\']?(.*?)["\']?\)'),  # SCSS url
        re.compile(r'\{\{\s*<\s*image\s+([^\s]+)\s+.*?>\s*\}\}'),  # Hugo image shortcode without quotes
        re.compile(r'\{\{\s*<\s*figure\s+src=["\'](.*?)["\']\s+.*?>\}\}')  # Hugo figure shortcode
    ]
    
    references = []
    for root, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.md') or file.endswith('.html') or file.endswith('.toml') or file.endswith('.scss'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    for pattern in references_patterns:
                        references.extend(pattern.findall(content))
    
    # Filter references to include only those with the specified extensions
    filtered_references = [reference for reference in references if any(reference.endswith(ext) for ext in extensions)]
    return filtered_references

def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../..', 'content'))
    file_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.ico', '.pdf', '.bmp', '.tiff', '.tif', '.heic', '.avif', '.zip', '.3dm', '.mp4']
    
    all_files = find_files(base_dir, file_extensions)
    all_references = find_references_in_source_files(base_dir, file_extensions)
    
    # Use basenames for comparison
    all_files_basenames = [os.path.basename(file) for file in all_files]
    all_references_basenames = [os.path.basename(reference) for reference in all_references]
    
    unused_files = [file for file, basename in zip(all_files, all_files_basenames) if basename not in all_references_basenames]
    
    print("Unused files:")
    for file in unused_files:
        print("content/" + os.path.relpath(file, base_dir))
    
    print(f"\nSummary: {len(unused_files)} unused files found.  NOTE: Some may be used in templates or other files not checked by this script or may be referenced dynamically.")

if __name__ == "__main__":
    main()