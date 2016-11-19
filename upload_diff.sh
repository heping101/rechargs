#!/bin/sh
# Script to upload local changed files to remote server for test
#######################################################################

if test $# -ne 1
then
    echo "<--------------------------------------------------------------->"
    echo "< Usage: $0 HOST_NAME"
    echo "<--------------------------------------------------------------->"
    exit 1
fi

SYNC_HOST_NAME=${1}

diff_files=`git status -s . | grep '^M  ' | sed 's/M  //'`
for diff_file in ${diff_files}
do
    scp ${diff_file} root@${SYNC_HOST_NAME}:/export0/recharge/${diff_file}
done

new_files=`git status -s . | grep '^A  ' | sed 's/A  //'`
for new_file in ${new_files}
do
    scp ${new_file} root@${SYNC_HOST_NAME}:/export0/recharge/${new_file}
done
