#! /usr/bin/env bash

# Let the DB start
env PYTHONPATH="/workspace" python ./src/backend_pre_start.py

# Run migrations
env PYTHONPATH="/workspace" alembic upgrade head

# Create initial data in DB
env PYTHONPATH="/workspace" python ./src/initial_data.py
