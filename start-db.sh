#!/bin/bash

docker run --name redisForScrap -p 6379:6379 -d redis redis-server --requirepass "abc123"
