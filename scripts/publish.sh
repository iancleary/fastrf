#!/usr/bin/env bash

set -e

poetry build
poetry publish
