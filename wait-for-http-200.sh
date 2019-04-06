#!/usr/bin/env bash

timeout 75 bash -c 'while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' https://localhost:8443/api-docs/apiLive.htm)" != "200" ]]; do echo ''waiting for fineract instance'' && sleep 5; done' || false