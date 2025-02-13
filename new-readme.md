# Nexlayer YAML Schema Documentation (v1.2)

<div align="center">
  <h3>🚀 Simplified Kubernetes Deployment for Modern Applications</h3>
  <p><em>Deploy your applications in seconds with a single YAML file</em></p>
</div>

## 📖 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Basic Structure](#basic-structure)
- [Application Configuration](#application-configuration)
- [Pod Configuration](#pod-configuration)
- [Environment Variables](#environment-variables)
- [Service Ports](#service-ports)
- [Secrets Management](#secrets-management)
- [Registry Authentication](#registry-authentication)
- [Examples](#examples)
- [Deployment Guide](#deployment-guide)

## Overview

Nexlayer YAML schema simplifies deployment configuration, eliminating complex Kubernetes YAML files. This template is optimized for both developers and automation tools, making cloud deployment straightforward and efficient.

## Key Features

- 🔄 **Pod Configuration**: Define individual containers for your application
- 💾 **Persistent Storage**: Automatic volume management for data retention
- 🔐 **Secrets Management**: Secure storage of sensitive information
- 🌍 **Environment Variables**: Application-specific configuration settings
- 🔌 **Service Ports**: Inter-container and external communication setup
- 🤖 **Pod Discovery**: Automatic networking between components
- 🏭 **Container Commands**: Customizable startup behaviors

## Basic Structure

The basic YAML structure follows this pattern:

```yaml
application:
  name: "Your App Name"
  url: "your-domain.com"  # Optional

pods:
  - name: frontend
    image: your-image:tag
    path: /
    servicePorts:
      - 3000

  - name: backend
    image: backend-image:tag
    servicePorts:
      - 8080
```

## Application Configuration

### Required Fields

| Field | Description | Required |
|-------|-------------|----------|
| `application.name` | Your application name | ✅ |
| `pods` | List of pod configurations | ✅ |

### Optional Fields

| Field | Description | Default |
|-------|-------------|---------|
| `application.url` | Application domain | Auto-generated |
| `registry` | Private registry config | None |

## Pod Configuration

Each pod represents a container in your application. Here's a detailed pod configuration:

```yaml
pods:
  - name: web-service
    image: nginx:latest
    path: /
    servicePorts:
      - 80
    vars:
      API_URL: http://api.pod:3000
    volumes:
      - name: data
        size: 1Gi
        mountPath: /data
```

### Pod Fields Explained

| Field | Description | Required |
|-------|-------------|----------|
| `name` | Pod identifier | ✅ |
| `image` | Container image | ✅ |
| `path` | URL path for routing | ❌ |
| `servicePorts` | Exposed ports | ❌ |
| `vars` | Environment variables | ❌ |
| `volumes` | Persistent storage | ❌ |

## Environment Variables

Define environment variables using the `vars` field:

```yaml
vars:
  DATABASE_URL: postgresql://user:pass@db.pod:5432/dbname
  API_KEY: ${SECRET_API_KEY}  # Reference to a secret
  NODE_ENV: production
```

## Service Ports

Configure network ports for your containers:

```yaml
servicePorts:
  - 8080  # Simple port
  - port: 80    # Detailed configuration
    targetPort: 8080
```

## Secrets Management

Store sensitive information securely:

```yaml
secrets:
  - name: API_KEY
    data: base64_encoded_value
  - name: DATABASE_URL
    data: base64_encoded_connection_string
```

## Registry Authentication

Configure private registry access:

```yaml
registry:
  url: registry.example.com
  username: your_username
  personalAccessToken: pat_token_here
```

## Examples

### Basic Web Application

```yaml
application:
  name: "web-app"

pods:
  - name: frontend
    image: nginx:latest
    path: /
    servicePorts:
      - 80
    vars:
      API_URL: http://api.pod:3000

  - name: api
    image: node:16
    servicePorts:
      - 3000
    vars:
      DATABASE_URL: postgresql://db.pod:5432/app
```

### Full-Stack Application with Database

```yaml
application:
  name: "full-stack-app"

pods:
  - name: frontend
    image: nextjs-app:latest
    path: /
    servicePorts:
      - 3000
    vars:
      API_URL: http://api.pod:4000

  - name: api
    image: express-api:latest
    servicePorts:
      - 4000
    vars:
      DATABASE_URL: postgresql://postgres:pass@db.pod:5432/app
      REDIS_URL: redis://cache.pod:6379

  - name: db
    image: postgres:14
    servicePorts:
      - 5432
    vars:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - name: postgres-data
        size: 10Gi
        mountPath: /var/lib/postgresql/data

  - name: cache
    image: redis:7
    servicePorts:
      - 6379
```

## Deployment Guide

1. **Create Configuration**
   - Save your configuration as `nexlayer.yaml`
   - Validate your configuration:
     ```bash
     nexlayer validate
     ```

2. **Deploy Application**
   ```bash
   nexlayer deploy
   ```

3. **Monitor Deployment**
   ```bash
   nexlayer status
   ```

4. **Access Logs**
   ```bash
   nexlayer logs <pod-name>
   ```

## Best Practices

1. **🔐 Security**
   - Always use secrets for sensitive data
   - Use specific image tags instead of `latest`
   - Implement least privilege access

2. **🚀 Performance**
   - Configure appropriate resource limits
   - Use persistent volumes for stateful applications
   - Implement health checks

3. **🔄 Maintenance**
   - Document all environment variables
   - Use meaningful pod names
   - Keep configurations version controlled

## Need Help?

- 📚 [Official Documentation](https://docs.nexlayer.cloud)
- 💬 [Community Support](https://community.nexlayer.cloud)
- 🐛 [Bug Reports](https://github.com/nexlayer/issues)

---

<div align="center">
  <p>Made with ❤️ by the Nexlayer Team</p>
</div>
```
