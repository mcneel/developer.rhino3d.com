#!/usr/bin/env python3.10

# theme-sync.py - dan@mcneel.com
# created: December 3rd, 2021
# see: https://mcneel.myjetbrains.com/youtrack/issue/WWW-1645
#
# This script reads synchronizes the rhino3d.com theme across the various sites that use it. It is rather brutal, as it
# simply obliterates the old (if there are no changes) and copies the current theme version from this repo to the other
# repositiories. It does not commit anything, but rather presumes that the diffs will be viewed and tested before
# the change is made across multiple site.

import subprocess
from subprocess import Popen, PIPE
import sys
import os
import shutil

# sites - sites must reside in folder that are parallel to each other. For example:
# /dev/mcneel/rhino3d.com
# /dev/mcneel/rhino3d.com-bongo
# are parallel to each other.
sites = ["rhino3d.com", "rhino3d.com-bongo", "developer-rhino3d-com-hugo"] 

# colors for terminal reporting
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_warning_message(warning_message):
    warning_prefix = " warning: "
    print(bcolors.BOLD + bcolors.FAIL + warning_prefix.upper() + bcolors.ENDC + bcolors.FAIL + warning_message + bcolors.ENDC)


def print_error_message(error_message):
    error_prefix = " error: "
    print(bcolors.BOLD + bcolors.FAIL + error_prefix.upper() + bcolors.ENDC + bcolors.FAIL + error_message + bcolors.ENDC)


def print_ok_message(ok_message):
    ok_prefix = " ok: "
    print(bcolors.BOLD + bcolors.OKBLUE + ok_prefix.upper() + bcolors.ENDC + bcolors.OKBLUE + ok_message + bcolors.ENDC)


def main():
    # Figure out which of the sites we're running in
    print("Checking which site this script is running in...")
    script_folder = os.path.dirname(os.path.abspath(__file__))    
    site_root_folder_path = os.path.abspath(os.path.join(script_folder, "..", "..", ".."))
    site_root_folder = os.path.basename(site_root_folder_path)
    root_folder_path = os.path.abspath(os.path.join(site_root_folder_path, ".."))

    running_in_site = ""
    if site_root_folder in sites:
        running_in_site = site_root_folder
        print_ok_message("This script is running in " + running_in_site)
    else:
        print_error_message("You appear to be running this script in a site that is not yet supported.")
        sys.exit(1)

    # Check to make sure the other sites exist
    print("Checking for other sites...")
    for site in sites:
        if running_in_site == site:
            continue
        
        site_to_check_path = os.path.abspath(os.path.join(root_folder_path, site))

        if os.path.exists(site_to_check_path):
            print_ok_message("Found " + site)
        else:
            print_error_message("Could not find " + site + ". Did you clone it? It needs to be a folder parallel to that which you are working in.")
            sys.exit(1)


    # Synchronize the rhino3d.com-theme
    changes_were_made = False
    print("Synchronizing theme in other sites...")
    for site in sites:
        if running_in_site == site:
            continue
        
        target_site_path = os.path.abspath(os.path.join(root_folder_path, site))
        path_to_theme = os.path.abspath(os.path.join(target_site_path, "themes", "rhino3d.com-theme"))

        # Check if there are chan ges in this folder - if so, bail
        os.chdir(target_site_path)
        p_git_status = subprocess.Popen(['git', 'status', 'themes/rhino3d.com-theme'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        git_status, err = p_git_status.communicate()
        if 'nothing to commit, working tree clean' in str(git_status):
            # Delete the theme folder
            try:
                shutil.rmtree(path_to_theme)
            except OSError as e:
                print_error_message("Error: %s : %s" % (path_to_theme, e.strerror))
                sys.exit(1)

            # Copy the theme from this site to the other sites
            source_theme = os.path.abspath(os.path.join(root_folder_path, running_in_site, "themes", "rhino3d.com-theme"))
            try:
                shutil.copytree(source_theme, path_to_theme)
            except OSError as e:
                print_error_message("Error: %s : %s" % (path_to_theme, e.strerror))
                continue
        else:
            print_warning_message(site + " contains changes that would be lost. Skipping.")
            continue

        # Check to make sure each site contains the /static/scss/_overrides.scss file
        path_to_site_scss_path = os.path.abspath(os.path.join(target_site_path, "static", "scss"))
        path_to_site_scss_overrides_path = os.path.abspath(os.path.join(path_to_site_scss_path, "_overrides.scss"))
        if not os.path.exists(path_to_site_scss_overrides_path):
            print_warning_message(path_to_site_scss_overrides_path + ' does not exist. Creating it now...')
            if not os.path.exists(path_to_site_scss_path):
                os.makedirs(path_to_site_scss_path)
            overrides_file = open(path_to_site_scss_overrides_path, "w")
            overrides_content = '/* DO NOT DELETE THIS FILE - even if empty - as it contains the site-specific scss overrides (if any) used by the rhino3d.com-theme and gets compiled in by the theme. */'
            overrides_file.write(overrides_content)
            overrides_file.close()

        p_git_status = subprocess.Popen(['git', 'status', 'themes/rhino3d.com-theme'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        git_status, err = p_git_status.communicate()
        if 'nothing to commit, working tree clean' in str(git_status):
            print_ok_message(site + " was already in sync. No changes were made.")
        else:
            print_ok_message(site + "'s theme/rhino3d.com theme updated.")
            changes_were_made = True

    if changes_were_made:
        print_warning_message("DONE: theme synchronization finished without commiting changes. Please review changes and commit/push or revert the changes.")        
    else:
        print("DONE: theme synchronization done. No changes were made (themes were already in sync or skipped)")

    sys.exit(0)


if __name__ == "__main__":
    main()