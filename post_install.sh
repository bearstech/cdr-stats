#!/bin/bash
! [ -d cdr_stats/cdr/migrations/ ] && bin/manage schemamigration cdr --initial
bin/manage collectstatic --noinput -v 0
bin/manage syncdb --noinput
bin/manage migrate --noinput
bin/touch-wsgi
