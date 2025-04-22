# Nexlayer YAML Schema Template Documentation (v1.0)

# 🚀 What is Nexlayer?

Nexlayer is an AI-powered kubernetes cloud platform that enables seamless scalable deployments through a specialized YAML template schema. 
It's designed for startups, developers, creators and AI agents, making complex production deployments simple and accessible without deep cloud infrastructure expertise.

## ✨ Key Features

- **Pod Management**: Define individual containers for your application  
- **Storage Configuration**: Persistent volumes for data retention  
- **Security Controls**: Secure storage of secrets, API keys, and sensitive data  
- **Environment Management**: Application-specific configuration settings  
- **Network Configuration**: Service ports for inter-container and external communication  
- **Registry Authentication**: Private registry login support  
- **Auto-Discovery**: Automatic networking between components  
- **Container Controls**: Customize startup behavior with entrypoints and commands  
- **AI/ML Support**: Specialized configurations for AI-powered applications  


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


## Basic Structure

Nexlayer base YAML template structure follows this pattern:

```yaml
application:
  name: The name of the deployment (must be lowercase, alphanumeric, '-', '.')
  url: Permanent domain URL (optional). No need to add this key if this is not going to be a permanent deployment.
  registryLogin:
    registry: The registry where private images are stored.
    username: Registry username.
    personalAccessToken: Read-only registry Personal Access Token.
  pods:
    - name: Pod name (must start with a lowercase letter and can include only alphanumeric characters, '-', '.')
      path: Path to render pod at (such as '/' for frontend). Only required for forward-facing pods.
      image: Docker image faor the pod. 
        # For private images, use the following schema exactly as shown: '<% REGISTRY %>/some/path/image:tag'.
        # Images will be tagged as private if they include '<% REGISTRY %>', which will be replaced with the registry specified above.
      volumes:
        # Array of volumes to be mounted for this pod. Example:
        - name: Name of the volume (lowercase, alphanumeric, '-')
          size: 1Gi  # Required: Volume size (e.g., "1Gi", "500Mi").
          mountPath: /var/some/directory  # Required: Must start with '/'.
      secrets:
        # Array of secret files for this pod. Example:
        - name: Secret name (lowercase, alphanumeric, '-')
          data: Raw or Base64-encoded string for the secret (e.g., JSON files should be encoded).
          mountPath: Mount path where the secret file will be stored (must start with '/').
          fileName: Name of the secret file (e.g., "secret-file.txt"). 
            # This will be available at "/var/secrets/my-secret-volume/secret-file.txt".
      vars:
        # Array of environment variables for this pod. Example:
        - key: ENV_VAR_NAME
          value: Value of the environment variable.
        # Can use <pod-name>.pod to reference other pods dynamically. Example:
        - key: API_URL
          value: http://express.pod:3000  # Where 'express' is the name of another pod.
        # Can use <% URL %> to reference the deployment’s base URL dynamically. Example:
        - key: API_URL
          value: <% URL %>/api
    servicePorts:
      # Array of ports to expose for this pod. Example:
      - 3000  # Exposing port 3000.
  entrypoint: Custom container entrypoint (optional).
  command: Custom container command (optional).

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

### Fullstack App with Next.js, Prisma, and Postgres

```yaml
application:
  name: hello-world-nextjs    # Required: Application name (lowercase, alphanumeric, '-', '.')
  url: <% URL %>              # Optional: Custom domain URL (omit if not needed)
  registryLogin:              # Optional: Required only for private images (Docker Hub assumed by default)
    registry: myregistry.com  # Required if registryLogin present: Registry hostname
    username: myusername      # Required if registryLogin present: Registry username
    personalAccessToken: myaccesstoken  # Required if registryLogin present: Read-only registry PAT

  pods:  # Required: List of pod configurations
  - name: web-app           # Required: Pod name (lowercase, alphanumeric, '-', '.')
    path: /
    image: <% REGISTRY %>/nextjs/app:latest  # Required: Full image URL following <registry>/repo:<tag> format
    volumes:  # Optional: List of persistent storage volumes
    - name: nextjs-cache    # Required: Volume name (lowercase, alphanumeric, '-')
      size: 1Gi             # Required: Volume size (e.g., "1Gi", "500Mi")
      mountPath: /app/.next/cache  # Required: Volume mount path (must start with '/')
    
    secrets:  # Optional: List of secret configurations
    - name: nextauth-secret  # Required: Secret name (lowercase, alphanumeric, '-')
      data: myrandomsecret   # Required: Raw or Base64-encoded secret content
      mountPath: /var/secrets/nextauth  # Required: Secret mount path (must start with '/')
      fileName: secret.txt   # Required: Secret file name
    
    vars:  # Optional: Environment variables
    - key: API_URL
      value: http://backend.pod:3001  # Reference another pod dynamically
    - key: NEXTAUTH_URL
      value: http://web-app.pod:3000
    - key: DATABASE_URL
      value: postgresql://postgres:postgres@database.pod:5432/mydb
    - key: NEXTAUTH_SECRET
      value: <% URL %>/secrets/nextauth
    - key: GITHUB_CLIENT_ID
      value: ${GITHUB_CLIENT_ID}  # GitHub OAuth Client ID (stored securely)
    - key: GITHUB_CLIENT_SECRET
      value: ${GITHUB_CLIENT_SECRET}  # GitHub OAuth Client Secret
    
    servicePorts:  # Required: List of port configurations (shorthand supported)
    - 3000  # Exposing Next.js frontend on port 3000

  - name: backend  # Required: Backend service (Next.js API routes)
    image: <% REGISTRY %>/node/api:latest
    volumes:
    - name: prisma-migrations
      size: 1Gi
      mountPath: /app/prisma/migrations
    vars:
    - key: DATABASE_URL
      value: postgresql://postgres:postgres@database.pod:5432/mydb
    - key: NEXTAUTH_SECRET
      value: <% URL %>/secrets/nextauth
    - key: GITHUB_CLIENT_ID
      value: ${GITHUB_CLIENT_ID}
    - key: GITHUB_CLIENT_SECRET
      value: ${GITHUB_CLIENT_SECRET}
    servicePorts:
    - 3001  # Exposing backend API on port 3001

  - name: database  # Required: PostgreSQL database pod
    image: <% REGISTRY %>/postgres:latest
    volumes:
    - name: postgres-data
      size: 5Gi
      mountPath: /var/lib/postgresql/data
    vars:
    - key: POSTGRES_USER
      value: postgres
    - key: POSTGRES_PASSWORD
      value: postgres
    - key: POSTGRES_DB
      value: mydb
    servicePorts:
    - 5432  # Exposing PostgreSQL database on port 5432

```
| **Pod Name**  | **Exposed Port(s)** | **Intended Service**                | **Consistent?** |
|--------------|------------------|--------------------------------|--------------|
| `web-app`   | `3000`            | Next.js frontend               | ✅ Yes |
| `backend`   | `3001`            | API backend (Next.js API routes) | ✅ Yes |
| `database`  | `5432`            | PostgreSQL database            | ✅ Yes |

### 📌 Port Explanation:
- **Frontend (`web-app`)**: Uses **port `3000`**, which is standard for **Next.js apps**.
- **Backend (`backend`)**: Uses **port `3001`**, aligning with your structure for an **API backend**.
- **Database (`database`)**: Uses **port `5432`**, which is **PostgreSQL's default port**.



# Example Fullstack AI-Powered Web Application Architecture

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

| **Pod Name**      | **Exposed Port(s)** | **Intended Service**                     | **Consistent?** |
|------------------|------------------|---------------------------------|--------------|
| `web-app`       | `3000`            | Next.js frontend & API           | ✅ Yes |
| `ai-model`      | `5000`            | AI model inference service       | ✅ Yes |
| `data-worker`   | `4000`            | Data processing worker           | ✅ Yes |
| `vector-db`     | `8080`            | Vector embeddings database       | ✅ Yes |
| `redis`        | `6379`            | Caching & message queue          | ✅ Yes |
| `postgres`      | `5432`            | Relational database (PostgreSQL) | ✅ Yes |
| `minio`        | `9000, 9001`      | Object storage & UI console      | ✅ Yes |

### 📌 Port Explanation:
- **Frontend (`web-app`)**: Uses **port `3000`**, standard for **Next.js frontend & API**.
- **AI Model (`ai-model`)**: Uses **port `5000`**, for **inference API endpoint**.
- **Data Worker (`data-worker`)**: Uses **port `4000`**, for **processing and analytics tasks**.
- **Vector Database (`vector-db`)**: Uses **port `8080`**, for **storing vector embeddings**.
- **Redis (`redis`)**: Uses **port `6379`**, for **caching and message queueing**.
- **PostgreSQL (`postgres`)**: Uses **port `5432`**, **default for relational databases**.
- **MinIO (`minio`)**: Uses **ports `9000` (API) & `9001` (Console UI)**, for **S3-compatible object storage**.


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
