#!/bin/bash
while true
do
	curl -s http://localhost:8080/actuator/metrics/hello | jq .
  curl -s http://localhost:8080/actuator/metrics/cache.gets | jq .
  curl -s "http://localhost:8080/actuator/metrics/cache.gets?tag=cache:mycache&tag=result:hit" | jq .
	curl -s http://localhost:8080/actuator/metrics/hello | jq .
  curl -s http://localhost:8080/actuator/metrics/cache.gets | jq .
  curl -s "http://localhost:8080/actuator/metrics/cache.gets?tag=cache:mycache&tag=result:hit" | jq .
	curl -s http://localhost:8080/actuator/metrics/hello | jq .
  curl -s http://localhost:8080/actuator/metrics/cache.gets | jq .
  curl -s "http://localhost:8080/actuator/metrics/cache.gets?tag=cache:mycache&tag=result:hit" | jq .
	curl -s http://localhost:8080/actuator/metrics/hello | jq .
  curl -s http://localhost:8080/actuator/metrics/cache.gets | jq .
  curl -s "http://localhost:8080/actuator/metrics/cache.gets?tag=cache:mycache&tag=result:hit" | jq .

#  sleep $[ ( $RANDOM % 10 )  + 1 ]s

  curl -i http://localhost:8080/rest/hello
  curl -i http://localhost:8080/rest/hello
  curl -i http://localhost:8080/rest/hello
  curl -i http://localhost:8080/rest/hello
  curl -i http://localhost:8080/rest/hello
  curl -i http://localhost:8080/rest/hello


#  sleep $[ ( $RANDOM % 10 )  + 1 ]s
sleep 0.1
done
