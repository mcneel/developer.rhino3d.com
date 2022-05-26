#!/usr/bin/env bash

rm -f _s3_sync.*

# Make S3 Uploads Really Fast(TM)
aws configure set default.s3.max_concurrent_requests 20
aws configure set default.s3.use_accelerate_endpoint true

# verify installed hugo version:
export INSTALLED_HUGO_VERSION=`./hugo version | sed -E "s/.*v([0-9\.]+).*/\1/g"`
export FORESTRY_HUGO_VERSION=`grep -e "- HUGO_VERSION=" .forestry/settings.yml | sed -E "s/.*HUGO_VERSION=//" | sed -E "s/\n//"`

if [ $INSTALLED_HUGO_VERSION = $FORESTRY_HUGO_VERSION ]
then
    echo "Building with hugo $INSTALLED_HUGO_VERSION"
else
    echo "Hugo is out of date! $INSTALLED_HUGO_VERSION != $FORESTRY_HUGO_VERSION"
    export PLATFORM=`uname -s`
    rm -rf hugo
    if [ $PLATFORM = "Darwin" ]
    then
        wget https://github.com/gohugoio/hugo/releases/download/v$FORESTRY_HUGO_VERSION/hugo_extended_${FORESTRY_HUGO_VERSION}_macOS-64bit.tar.gz -O hugo.tar.gz
    else
        wget https://github.com/gohugoio/hugo/releases/download/v$FORESTRY_HUGO_VERSION/hugo_extended_${FORESTRY_HUGO_VERSION}_Linux-64bit.tar.gz -O hugo.tar.gz
    fi
    tar -xf hugo.tar.gz hugo
    # mv hugo /usr/bin/hugo
    rm -rf hugo.tar.gz
fi

# Generate admin pages
# python3 script/utils/localization-police.py

hugo_log_file="hugo.log"
rm -f $hugo_log_file

# Build static content
function build() {
    # write stderr to stderr and file (hugo.log)
    # use TERM=dumb to prevent hugo colorising its output
    TERM=dumb ./hugo -e production $@ 2> >(tee -a $hugo_log_file >&2)
}

hugo_build_results=0
# TEST builds; before overwriting production
build -d public/
((hugo_build_results += $?))

echo "Builds complete with exit code: $hugo_build_results"

if [ $hugo_build_results = 0 ]
then
    echo "Build succeeded!"

else
    echo "Error Detected In Build!"
    exit 1
fi
