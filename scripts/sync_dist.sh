#!/bin/sh

if [ -L $0 ] ; then
    BASEDIR=$(dirname $(readlink -f $0)) ;
else
    BASEDIR=$(dirname $0) ;
fi ;

`which rsync` -vzcrlptD --no-g --progress --stats --rsh=ssh -e "ssh -p 81 -l root" ${BASEDIR}/../dist/recharge/ 45.76.100.193:/export0/recharge/
