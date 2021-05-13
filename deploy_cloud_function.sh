#!/bin/bash

# set GCP_PROJECT (env) variable
CLOUD_FUNCTION_NAME=cf-jn

gcloud functions deploy $CLOUD_FUNCTION_NAME \
  --project $GCP_PROJECT \
  --entry-point main \
  --runtime python37 \
  --trigger-http \
  --memory 512Mi \
  --timeout 180 \
  --allow-unauthenticated
