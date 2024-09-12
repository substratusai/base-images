#!/usr/bin/env sh

set -xe

jupyter lab --allow-root --ip=0.0.0.0 --NotebookApp.token='' --notebook-dir='/content'
