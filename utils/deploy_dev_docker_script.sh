#!/usr/bin/env bash

echo -e "\e[32m\e[1mActivate virtualenv\e[0m"
virtualenv ve
source ve/bin/activate \
    && pip install -r /requirements.txt \
    && pip install -r /requirements-dev.txt
zappa update dev
zappa manage dev migrate
zappa manage dev "collectstatic --noinput"