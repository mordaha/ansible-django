#!/bin/sh

export APP_ENV=test
coverage run --source="apps" --omit=*migrations*,*tests* manage.py test -v 2 $@

RESULT=$?

if test -n "$TEAMCITY_TESTS"; then
    coverage html
else
    if test "${RESULT}" = "0"; then
        coverage report
    fi
fi
