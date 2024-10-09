#!/usr/bin/env python3

import os

def delete_ds_store_files(root_folder):
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename == '.DS_Store':
                file_path = os.path.join(dirpath, filename)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

if __name__ == "__main__":
    root_folder = os.path.abspath(os.path.join(__file__, "../../../../.."))
    delete_ds_store_files(root_folder)