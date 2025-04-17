# Continuous Integration Guide

This guide explains how to set up and configure continuous integration (CI) for your Nexlayer projects.

## Overview

Nexlayer CI provides automated testing, building, and deployment capabilities for your applications.

## Setting Up CI

### Basic Configuration

Create a `.nexlayer/ci.yaml` file in your project root:

```yaml
version: 1
stages:
  - name: test
    commands:
      - go test ./...
  - name: build
    commands:
      - go build -o app
  - name: deploy
    commands:
      - nexlayer deploy
```

### Advanced Configuration

```yaml
version: 1
stages:
  - name: test
    commands:
      - go test ./...
    environment:
      GO_VERSION: 1.16
      NODE_VERSION: 14
    timeout: 300
    retries: 3

  - name: build
    commands:
      - go build -o app
    artifacts:
      - app
    cache:
      - .go
      - node_modules

  - name: deploy
    commands:
      - nexlayer deploy
    conditions:
      - branch == main
      - test.success == true
    notifications:
      - type: slack
        channel: deployments
```

## GitHub Actions Integration

### Basic Workflow

Create `.github/workflows/nexlayer.yml`:

```yaml
name: Nexlayer CI/CD

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Go
        uses: actions/setup-go@v2
        with:
          go-version: 1.16
          
      - name: Install Nexlayer CLI
        run: |
          curl -fsSL https://get.nexlayer.io | sh
          
      - name: Run Tests
        run: go test ./...
        
      - name: Build
        run: go build -o app
        
      - name: Deploy to Nexlayer
        if: github.ref == 'refs/heads/main'
        run: |
          curl -X POST https://app.nexlayer.io/startUserDeployment \
            -H "Content-Type: text/x-yaml" \
            --data-binary @nexlayer.yaml
        env:
          NEXLAYER_API_KEY: ${{ secrets.NEXLAYER_API_KEY }}
```

### Advanced Workflow with Caching

```yaml
name: Nexlayer CI/CD

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Go
        uses: actions/setup-go@v2
        with:
          go-version: 1.16
          cache: true
          cache-dependency-path: go.sum
          
      - name: Install Nexlayer CLI
        run: |
          curl -fsSL https://get.nexlayer.io | sh
          
      - name: Run Tests
        run: go test ./...
        
      - name: Build
        run: go build -o app
        
      - name: Cache Build Artifacts
        uses: actions/cache@v2
        with:
          path: app
          key: ${{ runner.os }}-build-${{ hashFiles('**/go.sum') }}
          restore-keys: |
            ${{ runner.os }}-build-
            
      - name: Deploy to Nexlayer
        if: github.ref == 'refs/heads/main'
        run: |
          DEPLOY_URL=$(curl -X POST https://app.nexlayer.io/startUserDeployment \
            -H "Content-Type: text/x-yaml" \
            --data-binary @nexlayer.yaml | jq -r '.url')
          echo "Deployed to: $DEPLOY_URL"
        env:
          NEXLAYER_API_KEY: ${{ secrets.NEXLAYER_API_KEY }}
          
      - name: Notify Deployment
        if: success()
        uses: rtCamp/action-slack-notify@v2
        env:
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
          SLACK_MESSAGE: 'Deployment successful!'
          SLACK_COLOR: good
```

## Environment Variables

### Required Variables

```yaml
NEXLAYER_API_KEY: Your API key
NEXLAYER_ENV: production
```

### Optional Variables

```yaml
NEXLAYER_REGION: us-west-2
NEXLAYER_TIMEOUT: 300
NEXLAYER_RETRIES: 3
```

## Artifacts and Caching

### Artifact Configuration

```yaml
artifacts:
  - path: app
    retention: 7d
  - path: coverage.out
    retention: 30d
```

### Cache Configuration

```yaml
cache:
  - path: .go
    key: go-mod-${{ hashFiles('go.sum') }}
  - path: node_modules
    key: node-mod-${{ hashFiles('package-lock.json') }}
```

## Notifications

### Slack Integration

```yaml
notifications:
  - type: slack
    channel: deployments
    events:
      - deploy.success
      - deploy.failure
```

### Email Notifications

```yaml
notifications:
  - type: email
    recipients:
      - team@example.com
    events:
      - deploy.success
      - deploy.failure
```

## Security

### Secrets Management

```yaml
secrets:
  - name: NEXLAYER_API_KEY
    value: ${NEXLAYER_API_KEY}
  - name: SLACK_WEBHOOK
    value: ${SLACK_WEBHOOK}
```

### Access Control

```yaml
access:
  roles:
    - name: admin
      permissions: [all]
    - name: operator
      permissions: [read, execute]
```

## Best Practices

1. **Version Control**
   - Keep CI configuration in version control
   - Use branches for feature development
   - Protect main branch

2. **Testing**
   - Run tests before deployment
   - Use code coverage
   - Implement integration tests

3. **Security**
   - Use secrets for sensitive data
   - Implement role-based access
   - Regular security audits

4. **Monitoring**
   - Set up deployment notifications
   - Monitor build times
   - Track success rates

## Troubleshooting

### Common Issues

1. **Build Failures**
   - Check dependencies
   - Verify environment
   - Review logs

2. **Deployment Issues**
   - Check API key
   - Verify permissions
   - Review configuration

3. **Performance Problems**
   - Optimize caching
   - Review resource usage
   - Check network connectivity

## Support

For additional help:
- Check the [FAQ](../get-started/faq.md)
- Review [Examples](examples.md)
- Open GitHub issues
- Join community discussions 