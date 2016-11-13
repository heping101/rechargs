#!/bin/sh

BASEDIR=$(dirname $(readlink -f $0)) ;

cd ${BASEDIR}/.. && ./manage.py run_crontask_hourly
