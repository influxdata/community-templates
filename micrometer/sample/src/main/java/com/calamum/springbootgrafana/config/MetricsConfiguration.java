package com.calamum.springbootgrafana.config;

import io.micrometer.core.instrument.Clock;
import io.micrometer.core.lang.NonNullApi;
import io.micrometer.influx.InfluxConfig;
import io.micrometer.influx.InfluxMeterRegistry;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import io.micrometer.core.aop.TimedAspect;
import io.micrometer.core.instrument.MeterRegistry;

import java.time.Duration;

@Configuration
public class MetricsConfiguration {

    @Bean
    InfluxConfig influxConfig() {
        return new InfluxConfig() {
            @Override
            public String get(String key) {
                return null;
            }

            @Override
            public Duration step() {
                return Duration.ofSeconds(2);
            }

            @Override
            public String org() {
                return "<YOUR_ORG_ID>";
            }

            @Override
            public String bucket() {
                return "jvm_micrometer";
            }

            @Override
            public String token() {
                return "<YOUR_TOKEN>";
            }

            @Override
            public String uri() {
                return "https://us-central1-1.gcp.cloud2.influxdata.com";
            }
        };
    }

    /**
     * Enable @Timed annotation support.
     * 
     * @param registry
     * @return
     */
    @Bean
    public TimedAspect timedAspect(MeterRegistry registry) {
        return new TimedAspect(registry);
    }
}
