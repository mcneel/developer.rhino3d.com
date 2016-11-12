import os
import sys
import subprocess
import fileinput

walk_dir = sys.argv[1]

print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    for filename in files:
        file_path = os.path.join(root, filename)

        if (filename.endswith('.md')) or (filename.endswith('.png')) or (filename.endswith('.snagproj')):
            if "_" in filename:
                new_filename = filename.replace("_", "-")
                new_file_path = os.path.join(root, new_filename)
                output = subprocess.check_output(["git", "mv", file_path, new_file_path])

                #for root_c, subdirs_c, files_c in os.walk(walk_dir):
                #    for filename_c in files_c:
                #        file_path_c = os.path.join(root_c, filename_c)

                #        if filename_c.endswith('.md'):

                #            old_title = ''
                #            new_title = ''

                #            if filename.endswith('.md'):
                #                old_title = filename[:-3]
                #                new_title = new_filename[:-3]
                #            elif filename.endswith('.png'):
                #                old_title = filename[:-4]
                #                new_title = new_filename[:-4]
                #            elif filename.endswith('.snagproj'):
                #                old_title = filename[:-9]
                #                new_title = new_filename[:-9]

                            #print('checking ' + filename_c + ' for ' + old_title + ' to replace with ' + new_title)

                #            replacements = {old_title: new_title}
                #            lines = []
                #            with open(file_path_c) as infile:
                #                for line in infile:
                #                    for src, target in replacements.iteritems():
                #                        line = line.replace(src, target)
                #                    lines.append(line)
                #            with open(file_path_c, 'w') as outfile:
                #                for line in lines:
                #                    outfile.write(line)
