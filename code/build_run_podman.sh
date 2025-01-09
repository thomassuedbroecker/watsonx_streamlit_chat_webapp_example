#!/bin/bash

# load environment variable
source .env

# delete existing container
podman rm chat-demo

# build new container
podman build -t chat-demo:0.0.1 -f ./Dockerfile.podman_root

# run container on the local computer
podman run -it -p 8080:8080 -e WATSONX_APIKEY=${WATSONX_APIKEY} \
                            -e WATSONX_PROJECT_ID=${WATSONX_PROJECT_ID} \
                            -e WATSONX_REGION=${WATSONX_REGION} \
                            -e APP_USER=${APP_USER} \
                            -e APP_PASSWORD=${APP_PASSWORD} \
                            --name chat-demo \
                            "localhost/chat-demo:0.0.1"