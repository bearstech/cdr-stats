#!/bin/bash
! [ -d cdr_stats/cdr/migrations/ ] && bin/manage schemamigration cdr --initial
bin/manage collectstatic --noinput -v 0
bin/manage syncdb --noinput
bin/manage migrate --noinput
bin/touch-wsgi

#enable crontab for actifry cms-services

cron=`tempfile --prefix=csc-`

cat << EOF > $cron
*/10 * * * * LIMIT=200 $PWD/bin/manage sync_cdr_asterisk > /dev/null
EOF

#crontab $cron

