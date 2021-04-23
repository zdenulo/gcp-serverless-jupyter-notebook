#!/bin/bash

gcloud functions deploy cf-jn \
  --entry-point main \
  --runtime python37 \
  --trigger-http \
  --memory 512Mi \
  --timeout 180 \
  --allow-unauthenticated
