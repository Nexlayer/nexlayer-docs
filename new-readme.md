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

# AI-Powered Application Architecture

A typical AI-powered application consists of:

- **Web Interface (Frontend & API)** - Next.js, React, or FastAPI  
- **AI Model Inference** - Hugging Face, OpenAI, or custom LLMs  
- **Data Processing Worker** - Python jobs, Spark, or analytics  
- **Vector Database** - Pinecone, Weaviate, or FAISS  
- **Message Queue & Caching** - Redis or Kafka  
- **Relational Database** - PostgreSQL or MySQL  
- **Object Storage** - MinIO for large datasets  

## 1. Web Application Pod (Frontend & API)
```yaml
pods:
  - name: web-app
    image: mycompany/web-app:latest
    path: /
    servicePorts:
      - 3000
    vars:
      DATABASE_URL: postgresql://postgres:postgres@postgres.pod:5432/postgres
      AI_API_URL: http://ai-model.pod:5000
      REDIS_HOST: redis.pod
      REDIS_PORT: "6379"
      REDIS_AUTH: myredissecret
```
### Connection Table
| Connection | Description |
|------------|-------------|
| postgres.pod:5432 | Main database connection |
| ai-model.pod:5000 | AI model inference service |
| redis.pod:6379 | Caching and message queue |

## 2. AI Model Inference Pod
```yaml
pods:
  - name: ai-model
    image: huggingface/transformers:latest
    servicePorts:
      - 5000
    vars:
      MODEL_NAME: bert-base-uncased
      GPU_ENABLED: "true"
```
### Connection Table
| Connection | Description |
|------------|-------------|
| vector-db.pod:8080 | Vector embeddings storage |
| :5000 | Exposed inference API endpoint |

## 3. Data Processing Worker Pod
```yaml
pods:
  - name: data-worker
    image: mycompany/data-processor:latest
    servicePorts:
      - 4000
    vars:
      VECTOR_DB_URL: http://vector-db.pod:8080
      REDIS_HOST: redis.pod
```
### Connection Table
| Connection | Description |
|------------|-------------|
| vector-db.pod:8080 | Vector database for embeddings |
| redis.pod | Task queue and caching |

## 4. Vector Database Pod
```yaml
pods:
  - name: vector-db
    image: weaviate/weaviate:latest
    servicePorts:
      - 8080
    vars:
      PERSISTENCE_MODE: disk
      ENABLE_MODULES: text2vec-transformers
```
### Connection Table
| Connection | Description |
|------------|-------------|
| :8080 | Vector search and storage API |

## 5. Redis Pod (Caching & Message Queue)
```yaml
pods:
  - name: redis
    image: redis:7
    command: --requirepass myredissecret
    servicePorts:
      - 6379
    vars:
      REDIS_AUTH: myredissecret
```
### Connection Table
| Connection | Description |
|------------|-------------|
| :6379 | Redis server port |
| REDIS_AUTH | Authentication for secure access |

## 6. PostgreSQL Pod (Relational Database)
```yaml
pods:
  - name: postgres
    image: postgres:latest
    servicePorts:
      - 5432
    vars:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: ai_application
    volumes:
      - name: postgres-data
        size: 10Gi
        mountPath: /var/lib/postgresql
```
### Connection Table
| Connection | Description |
|------------|-------------|
| :5432 | PostgreSQL server port |
| postgres-data | Persistent volume for database |

## 7. MinIO Pod (Object Storage)
```yaml
pods:
  - name: minio
    image: minio/minio:latest
    entrypoint: /bin/sh
    command: -c "mkdir -p /data/appdata && minio server --address ':9000' --console-address ':9001' /data"
    servicePorts:
      - 9000
      - 9001
    vars:
      MINIO_ROOT_USER: minio
      MINIO_ROOT_PASSWORD: miniosecret
    volumes:
      - name: minio-data
        size: 10Gi
        mountPath: /data
```
### Connection Table
| Connection | Description |
|------------|-------------|
| :9000 | MinIO S3 API endpoint |
| :9001 | MinIO Console UI |
| minio-data | Persistent volume for objects |

## Pod Communication Flow
- **Web App → AI Model:** Sends inference requests `(web-app → ai-model.pod:5000)`  
- **AI Model → Vector DB:** Retrieves embeddings `(ai-model → vector-db.pod:8080)`  
- **Web App → PostgreSQL:** Stores application data `(web-app → postgres.pod:5432)`  
- **Web App → Redis:** Caches results `(web-app → redis.pod:6379)`  
- **Data Worker → MinIO:** Processes large datasets `(data-worker → minio.pod:9000)`

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
