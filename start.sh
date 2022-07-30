#!/usr/bin/env bash

# https://stackoverflow.com/questions/3349105/how-can-i-set-the-current-working-directory-to-the-directory-of-the-script-in-ba
dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)

python3 lights.py
