#!/usr/bin/env bash

# the api generation takes a long time to generate locally.
# during local editing, as long as you don't want to edit the api
# contents, use this script to temporarily exclude the api during
# site generation.

printf 'exclude: ['/api']' >> _config.yml
jekyll serve
cp _config.yml _config.yml.tmp
sed '$ d' _config.yml.tmp > _config.yml
rm -f _config.yml.tmp
