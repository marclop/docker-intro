#!/usr/bin/env bash

pip install -r requirements.txt

passenger start --no-install-runtime --no-compile-runtime
