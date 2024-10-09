#!/usr/bin/env python3
import os
import argparse

# Translators often copy the contents of a page bundle to a localized folder and then translate the content. 
# This script helps to identify resources that are present in the English folder and exactly match those in the Localized folder. 
# It also identifies resources that are present in both folders but have different sizes...which likely means they were edited
# The script can optionally delete the matching localized resources if the --delete flag is passed.

def find_resources(content_dir):
    resources = set()
    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.ico', '.pdf', '.bmp', '.tiff', '.tif', '.heic', '.avif', '.zip', '.3dm')):
                relative_path = os.path.relpath(os.path.join(root, file), content_dir)
                resources.add(relative_path)
    return resources

def check_localized_resources(base_dir, localized_dirs, resources):
    present_resources = {}
    mismatched_resources = {}
    
    for loc_dir in localized_dirs:
        loc_present = []
        loc_mismatched = []
        for resource in resources:
            localized_resource_path = os.path.join(base_dir, loc_dir, resource)
            english_image_path = os.path.join(base_dir, 'en', resource)
            if os.path.exists(localized_resource_path):
                if os.path.getsize(localized_resource_path) == os.path.getsize(english_image_path):
                    loc_present.append(resource)
                else:
                    loc_mismatched.append(resource)
        if loc_present:
            present_resources[loc_dir] = loc_present
        if loc_mismatched:
            mismatched_resources[loc_dir] = loc_mismatched
    
    return present_resources, mismatched_resources

def main():
    parser = argparse.ArgumentParser(description="Check and optionally delete matching localized resources.")
    parser.add_argument('--delete', action='store_true', help="Delete matching localized resources")
    args = parser.parse_args()

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../..', 'content'))
    en_dir = os.path.join(base_dir, 'en')
    localized_dirs = ['fr']  # Add other localized directories as needed
    
    resources = find_resources(en_dir)
    present_resources, mismatched_images = check_localized_resources(base_dir, localized_dirs, resources)
    
    total_matched_files = 0
    for loc, rsces in present_resources.items():
        if not args.delete:
            print(f"Present matching resources in {loc}:")
            for img in rsces:
                print(f"  {img}")
        for img in rsces:
            if args.delete:
                localized_resource_path = os.path.join(base_dir, loc, img)
                os.remove(localized_resource_path)
                print(f"Deleted matching resource: {localized_resource_path}")
        total_matched_files += len(rsces)
    
    print(f"\nSummary: {total_matched_files} files matched between English and localized folder(s).")
    print("\n")
    
    total_mismatched_files = 0
    for loc, rsces in mismatched_images.items():
        print(f"Mismatched resources in {loc}:")
        for rcs in rsces:
            print(f"  {rcs}")
        total_mismatched_files += len(rsces)
    
    print(f"\nSummary: {total_mismatched_files} files did not match between English and localized folder(s) (which means they were edited).")

if __name__ == "__main__":
    main()