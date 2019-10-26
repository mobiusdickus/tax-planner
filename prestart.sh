#!/bin/sh

VENV=$(pipenv --venv)
echo $VENV

echo virtualenv=$VENV >> tax-planner.ini
