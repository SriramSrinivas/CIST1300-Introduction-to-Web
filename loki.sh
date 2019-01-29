#!/bin/bash
USERNAME=sriramsrinivas
HOSTS="loki.ist.unomaha.edu"
SCRIPT="cd public_html;cd CIST1300-001;ls;git pull; publish-public-html"
for HOSTNAME in ${HOSTS} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
done

