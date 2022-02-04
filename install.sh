#!/usr/bin/bash

sudo apt install python3-pip nodejs npm

# Install python dependencies
python3 -m pip install -r ./api/movie_database/requirements.txt

# Install Vue 3
cd ./web
npm install
