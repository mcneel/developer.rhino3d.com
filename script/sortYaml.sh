#!/bin/sh

# script/sortYaml.sh: Sort the Yaml fields in all content in all .md files in
#					  _guide_topics
#                     _samples

xbuild SortYaml/SortYaml.sln
mono SortYaml/bin/Debug/SortYaml.exe ../_guide_topics/
mono SortYaml/bin/Debug/SortYaml.exe ../_samples/
