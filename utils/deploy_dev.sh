#!/bin/bash
docker-compose run --rm \
-e AWS_ACCESS_KEY_ID \
-e AWS_SECRET_ACCESS_KEY \
api \
bash -c "bash ./utils/deploy_dev_docker_script.sh"
