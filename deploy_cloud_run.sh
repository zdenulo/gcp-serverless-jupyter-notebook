#!/bin/bash

gcloud beta run deploy cr-jn \
  --memory 512Mi \
  --source . \
  --platform managed \
  --allow-unauthenticated
