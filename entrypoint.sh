#!/bin/bash

# Login to Prefect Cloud
prefect cloud login --key "$PREFECT_API_KEY" --workspace "$PREFECT_WORKSPACE"

python deploy.py
