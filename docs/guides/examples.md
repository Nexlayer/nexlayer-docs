# Examples Guide

This guide provides real-world examples and use cases for Nexlayer.

## Basic Examples

### Project Setup

```bash
# Initialize a new project
nexlayer init my-project

# Configure the project
nexlayer config init

# Create a basic agent
nexlayer agent create my-agent
```

### Simple Task Automation

```yaml
# config.yaml
agent:
  name: backup-agent
  tasks:
    - name: daily-backup
      schedule: "0 0 * * *"
      command: |
        tar -czf backup.tar.gz /data
        aws s3 cp backup.tar.gz s3://my-backups/
```

## Advanced Examples

### CI/CD Pipeline

```yaml
# ci.yaml
version: "1.0"
ci:
  triggers:
    - type: push
      branches: [main]
  stages:
    - name: build
      steps:
        - name: build
          command: make build
    - name: test
      steps:
        - name: test
          command: make test
    - name: deploy
      steps:
        - name: deploy
          command: make deploy
```

### Monitoring Setup

```yaml
# monitoring.yaml
monitoring:
  metrics:
    - name: cpu
      interval: 15s
    - name: memory
      interval: 15s
  alerts:
    - name: high-cpu
      condition: cpu > 80
      action: notify
```

## Real-World Use Cases

### 1. Automated Deployment

```yaml
# deployment.yaml
deployment:
  stages:
    - name: validate
      steps:
        - name: check-dependencies
          command: make check-deps
    - name: build
      steps:
        - name: build-app
          command: make build
    - name: deploy
      steps:
        - name: deploy-staging
          command: make deploy-staging
        - name: deploy-prod
          command: make deploy-prod
          when: branch == 'main'
```

### 2. Database Management

```yaml
# database.yaml
database:
  backup:
    schedule: "0 0 * * *"
    retention: 7d
    storage:
      type: s3
      bucket: db-backups
  maintenance:
    schedule: "0 2 * * 0"
    tasks:
      - name: vacuum
        command: vacuumdb
      - name: analyze
        command: analyze
```

### 3. Log Management

```yaml
# logging.yaml
logging:
  rotation:
    max-size: 100MB
    max-age: 7d
  aggregation:
    type: elasticsearch
    index: nexlayer-logs
  alerts:
    - name: error-rate
      condition: error.count > 100
      action: notify
```

### 4. Security Monitoring

```yaml
# security.yaml
security:
  monitoring:
    - name: auth-failures
      threshold: 10
      window: 5m
    - name: suspicious-ips
      threshold: 5
      window: 1h
  alerts:
    - name: auth-alert
      condition: auth.failures > 10
      action: block-ip
```

## Integration Examples

### 1. GitHub Actions Integration

```yaml
# .github/workflows/ci.yml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Nexlayer CI
        uses: nexlayer/action@v1
        with:
          config: .nexlayer/ci.yaml
```

### 2. Slack Integration

```yaml
# notifications.yaml
notifications:
  - type: slack
    channel: alerts
    events:
      - name: deployment
        template: |
          Deployment ${status}
          Project: ${project}
          Environment: ${env}
          Duration: ${duration}
```

### 3. Prometheus Integration

```yaml
# metrics.yaml
metrics:
  prometheus:
    enabled: true
    port: 9090
    path: /metrics
    labels:
      app: nexlayer
      env: production
```

## Configuration Examples

### 1. Multi-Environment Setup

```yaml
# environments.yaml
environments:
  development:
    api_url: http://dev-api.example.com
    debug: true
  staging:
    api_url: http://staging-api.example.com
    debug: false
  production:
    api_url: https://api.example.com
    debug: false
```

### 2. Resource Management

```yaml
# resources.yaml
resources:
  limits:
    cpu: 2
    memory: 4Gi
  requests:
    cpu: 1
    memory: 2Gi
  scaling:
    min: 2
    max: 10
```

### 3. Network Configuration

```yaml
# network.yaml
network:
  ingress:
    - host: api.example.com
      port: 443
      tls: true
  egress:
    - host: *.example.com
      port: 443
      tls: true
```

## Best Practices Examples

### 1. Error Handling

```yaml
# error-handling.yaml
error-handling:
  retry:
    attempts: 3
    delay: 5s
    max-delay: 60s
  fallback:
    - action: notify
      channel: alerts
    - action: rollback
      steps: [deploy]
```

### 2. Security Configuration

```yaml
# security-config.yaml
security:
  auth:
    type: jwt
    expiry: 24h
  rbac:
    roles:
      - name: admin
        permissions: [all]
      - name: operator
        permissions: [read, execute]
```

### 3. Monitoring Setup

```yaml
# monitoring-config.yaml
monitoring:
  metrics:
    - name: request-rate
      type: counter
    - name: response-time
      type: histogram
  alerts:
    - name: high-latency
      condition: response_time > 1s
      action: notify
```

## Support

For additional help:
- Check the [FAQ](../get-started/faq.md)
- Review other [Guides](.)
- Open GitHub issues
- Join community discussions 