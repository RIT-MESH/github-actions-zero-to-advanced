# Solution 21 — Service containers

```yaml
services:
  redis:
    image: redis:7
    ports:
      - 6379:6379
    options: >-
      --health-cmd "redis-cli ping"
      --health-interval 10s
      --health-timeout 5s
      --health-retries 5
steps:
  - uses: actions/checkout@v4
  - name: Ping Redis
    run: redis-cli -h localhost -p 6379 ping
```

Expected output: `PONG`. No cloud resources are created; Redis runs only on the runner for the job.