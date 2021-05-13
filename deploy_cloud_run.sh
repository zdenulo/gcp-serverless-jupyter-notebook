#!/bin/bash

# set GCP_PROJECT (env) variable
CLOUD_RUN_NAME=cr-jn

gcloud beta run deploy $CLOUD_RUN_NAME \
  --project $GCP_PROJECT \
  --memory 512Mi \
  --source . \
  --platform managed \
  --allow-unauthenticated
