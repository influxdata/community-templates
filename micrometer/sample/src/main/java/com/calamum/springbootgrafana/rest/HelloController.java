package com.calamum.springbootgrafana.rest;

import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeUnit;

import javax.annotation.PostConstruct;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.google.common.cache.CacheBuilder;
import com.google.common.cache.CacheLoader;
import com.google.common.cache.LoadingCache;

import io.micrometer.core.annotation.Timed;
import io.micrometer.core.instrument.Counter;
import io.micrometer.core.instrument.MeterRegistry;
import io.micrometer.core.instrument.binder.cache.GuavaCacheMetrics;

@RestController
public class HelloController {
    @Autowired
    private MeterRegistry registry;

    private LoadingCache<String, String> cache;

    private Counter helloCounter;

    @PostConstruct
    public void init() {
        cache = CacheBuilder.newBuilder()
                .maximumSize(1000)
                .expireAfterWrite(900, TimeUnit.SECONDS)
                .recordStats()
                .build(
                        new CacheLoader<String, String>() {
                            @Override
                            public String load(String key) throws Exception {
                                return key + "-value";
                            }
                        });

        GuavaCacheMetrics.monitor(registry, cache, "mycache");

        helloCounter = registry.counter("hello");
    }

    @GetMapping("/rest/hello")
    @Timed
    public String hello() throws ExecutionException {
        helloCounter.increment();

        int rand = (int) (Math.random() * 100);
        if (rand < 30) {
            throw new RuntimeException("random error");
        }


        return cache.get("key");
    }
}
