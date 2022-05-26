export EXPECTED_S5CMD_VERSION=1.3.0
export INSTALLED_S5CMD_VERSION=`./s5cmd version | sed -E "s/.*v([0-9\.]+).*/\1/g"`
if [ $INSTALLED_S5CMD_VERSION = $EXPECTED_S5CMD_VERSION ]
then
    echo "Uploading with s5cmd $INSTALLED_S5CMD_VERSION"
else
    echo "s5cmd is out of date! $INSTALLED_S5CMD_VERSION != $EXPECTED_S5CMD_VERSION"
    export PLATFORM=`uname -s`
    rm -rf hugo
    if [ $PLATFORM = "Darwin" ]
    then
        wget https://github.com/peak/s5cmd/releases/download/v$EXPECTED_S5CMD_VERSION/s5cmd_$EXPECTED_S5CMD_VERSION\_macOS-64bit.tar.gz -O s5cmd.tar.gz
    else
        wget https://github.com/peak/s5cmd/releases/download/v$EXPECTED_S5CMD_VERSION/s5cmd_$EXPECTED_S5CMD_VERSION\_Linux-64bit.tar.gz
    fi
    tar -xf s5cmd.tar.gz s5cmd
    rm -rf s5cmd.tar.gz
    chmod 700 s5cmd
fi

rm -f _rsync_diff.txt
rm -f _local_sync.sh
rm -f _s5cmd.txt

# public-last-run folder not found; do a full sync with S3
echo "Full Upload to S3 starting"
./s5cmd --log error cp public/ s3://source-developer-rhino3d-com/
echo "Full Upload to S3 complete"

echo "Invalidating cloudfront cache"
# aws cloudfront create-invalidation --distribution-id E119D0O6VEEKO8 --paths "/*"

