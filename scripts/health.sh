#!/bin/sh

curl --fail http://localhost:8000/health || exit 1
