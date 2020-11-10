#!/bin/bash

curl -s -X GET -H "Content-Type: application/json" -H "Authorization: Bearer $DO_TOKEN" "https://api.digitalocean.com/v2/customers/my/balance"


