#!/usr/bin/env bash

docker ps -a --format "{{.Names}}"
