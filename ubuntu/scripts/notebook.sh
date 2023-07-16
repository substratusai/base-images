#!/usr/bin/env sh

set -xe

NOTEBOOK_TOKEN="${NOTEBOOK_TOKEN:-default}"

jupyter lab --allow-root --ip=0.0.0.0 --NotebookApp.token=$NOTEBOOK_TOKEN --notebook-dir=/content
