#!/bin/sh

COMMIT_ID=HEAD

if test $# -eq 1
then
  echo "Using commit: $1"
  COMMIT_ID=$1
fi

if [ -L $0 ] ; then
    BASEDIR=$(dirname $(readlink -f $0)) ;
else
    BASEDIR=$(dirname $0) ;
fi ;

mkdir -p ${BASEDIR}/../dist

cd ${BASEDIR}/.. && git archive --prefix=recharge/ --format=tar ${COMMIT_ID} | tar -xvf - -C dist/
