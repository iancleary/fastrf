#!/usr/bin/env bash

set -e
set -x

mypy fastrf --disallow-untyped-defs
black fastrf tests --check
isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --combine-as --line-width 88 --check-only --project fastrf --project tests fastrf tests
