#!/bin/bash
DOCKERNAME="ValB"
REPONAME="Assignment"
CLONELINK="https://github.com/shubhpy/Assignment.git -b Backend"
RUNSCRIPT=$REPONAME"/manage.py runserver 0.0.0.0:8000"

docker exec -d $DOCKERNAME /bin/sh -c "pkill -SIGINT python;rm -rf "$REPONAME"/;git clone "$CLONELINK";python3.5 "$RUNSCRIPT

#Test Again
#Test Again