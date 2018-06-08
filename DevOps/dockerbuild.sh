#!/bin/bash
DOCKERNAME="ValB"
REPONAME="Assignment"
CLONELINK="https://github.com/shubhpy/Assignment.git"
RUNSCRIPT=$REPONAME

docker exec -d $DOCKERNAME /bin/sh -c "pkill -SIGINT python;rm -rf "$REPONAME"/;git clone "$CLONELINK" -b Backend;python3.5 "$RUNSCRIPT"/manage.py runserver 0.0.0.0:8000"

#Test Again
#Test Again