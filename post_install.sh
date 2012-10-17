#!/bin/bash
bin/manage collectstatic --noinput -v 0
bin/manage syncdb --noinput
bin/manage migrate --noinput
bin/touch-wsgi
