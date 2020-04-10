#!/bin/bash
USERNAME=sriramsrinivas
HOSTS="odin.unomaha.edu"
SCRIPT="cd public_html;cd CIST1300-sriramsrinivas;ls;git pull"
for HOSTNAME in ${HOSTS} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
done
