#!/bin/bash
########################################
# Create a file based on the environment variables
# given by the dockerc run -e parameter
########################################
cat <<EOF
# watsonx
export WATSONX_REGION=${WATSONX_REGION}
export WATSONX_PROJECT_ID=${WATSONX_PROJECT_ID}
export WATSONX_APIKEY=${WATSONX_API_KEY}

# Application
export APP_USER=${APP_USER}
export APP_PASSWORD=${APP_PASSWORD}
EOF