> NOTE that this application was originally created by [Fredrik Kjellberg](https://github.com/fkjellberg) and was slightly modified to work with InfluxDB v2. Original project is [here](https://github.com/fkjellberg/spring-boot-micrometer-influxdb-grafana).

## Info

This application was created to demonstrate a Spring Boot application using Micrometer to push metrics to InfluxDB and Grafana.

InfluxDB integration is using a StepRegistry that step-normalizes counts and sums to a rate/second over the publishing interval, i.e. it
will set any counter back to zero every step/publishing interval.

Please read the README.md file in the grafana-influxdb folder on how to start and stop the Grafana stack. Once the stack has been started
the Spring Boot application can be started and it will start to push metrics to InfluxDB and Grafana. A dashboard to show JVM metrics
from Java 11 is automatically provisioned when the Grafana docker stack is launched.

## Test

Call REST endpoint:

    curl -i http://localhost:8080/rest/hello

Actuator:

    curl -s http://localhost:8080/actuator/metrics/hello | jq .
    curl -s http://localhost:8080/actuator/metrics/cache.gets | jq .
    curl -s "http://localhost:8080/actuator/metrics/cache.gets?tag=cache:mycache&tag=result:hit" | jq .
