#!/bin/bash
export TESTING=False

export TWITTER_CONSUMER_KEY=""
export TWITTER_CONSUMER_SECRET=""
export TWITTER_ACCESS_TOKEN=""
export TWITTER_ACCESS_TOKEN_SECRET=""

cd ~/PollutionTracker/
source venv/bin/activate
python main.py
deactivate
