# 🚀 Nexlayer YAML: Developer's Quick Start Guide

Hello developers! Welcome to the Nexlayer YAML guide that gets you from zero to deployed in minutes. Whether you're a freelancer, indie developer, creator, or startup founder, this guide will help you deploy lightning-fast on Nexlayer AI Cloud.

## 📋 Table of Contents

1. [What is Nexlayer?](#-what-is-nexlayer)
2. [Quick Start: Deploy in 5 Minutes](#-quick-start-deploy-in-5-minutes)
3. [YAML Building Blocks](#-yaml-building-blocks)
4. [Visual Diagrams](#-visual-diagrams)
5. [Common App Patterns](#-common-app-patterns)
6. [Cheat Sheet: Pod Configuration](#-cheat-sheet-pod-configuration)
7. [How Pods Talk to Each Other](#-how-pods-talk-to-each-other)
8. [Storing Data with Volumes](#-storing-data-with-volumes)
9. [Keeping Secrets Safe](#-keeping-secrets-safe)
10. [Using Private Images](#-using-private-images)
11. [Common Mistakes to Avoid](#-common-mistakes-to-avoid)
12. [Full Example: Gaming Leaderboard App](#-full-example-gaming-leaderboard-app)
13. [Real-World Use Cases](#-real-world-use-cases)
14. [Pro Tips](#-pro-tips)
15. [Next Steps](#-next-steps)
16. [Detailed Schema Reference](#-detailed-schema-reference)
17. [Important Distinctions](#-important-distinctions)

##  🦾 ☁ What is Nexlayer?
Nexlayer is an AI-powered cloud built for developers who want to ship faster, scale effortlessly, and skip the DevOps headaches.

Define your app’s structure in a simple YAML file, and Nexlayer automates everything—provisioning, scaling, networking, and security—so you can focus on building, not configuring. No Kubernetes wrangling, no complex infra setup.

Unlike legacy platforms, Nexlayer is AI-native and designed for modern apps, AI models, and scalable backends—without vendor lock-in or unnecessary complexity. Write YAML, deploy, and go.


## ⚡️ Why Nexlayer?
- ✅ Zero DevOps – Write YAML, deploy, done.
- ✅ Auto-Scaling – Handles traffic spikes automatically.
- ✅ Built-in Security – Secrets management & encrypted storage.
- ✅ AI & ML Ready – Deploy AI models with zero friction.
- ✅ Effortless Networking – Services auto-discover, no networking configs.
- ✅ Simple Deployments – No infra setup, no YAML nightmares.
- ✅ Stack-Agnostic – Works with APIs, web apps, AI services, and more.

🚀 Less setup, more shipping.

## 🔥 Quick Start: Deploy in 5 Minutes

Let's get your first app running on Nexlayer right now:

### Step 1: Create a file named `nexlayer.yaml`

### Step 2: Copy this starter template

```yaml
application:
  name: "my-first-app"
  pods:
    - name: webapp
      image: nginx:latest
      path: /
      servicePorts:
        - 80
```

**💡 Tip**: If you prefer a more interactive way to create your `nexlayer.yaml`, try our **Template Builder** at [app.nexlayer.io/template-builder](https://app.nexlayer.io/template-builder). It lets you visually configure your application and generates the YAML for you—no manual coding needed!

### Step 3: Deploy it!

That's it! You just deployed a web service to Nexlayer. Let's understand what you did...

## 🧩 YAML Building Blocks

Nexlayer YAML has a simple structure:

```
application
├── name: Your app's name
├── url: Your app's URL (optional)
├── registryLogin (optional for private images)
└── pods: List of containers
    ├── Pod 1 (like a web server)
    │   ├── name: pod name
    │   ├── image: container image
    │   ├── path: web route
    │   ├── servicePorts: exposed ports
    │   │   └── - port number
    │   ├── vars: environment variables
    │   │   ├── ENV_VAR1: value1
    │   │   └── ENV_VAR2: value2
    │   ├── volumes: persistent storage
    │   │   └── - name: volume name
    │   │       ├── size: storage size
    │   │       └── mountPath: storage location
    │   └── secrets: sensitive data
    │       └── - name: secret name
    │           ├── data: secret content
    │           ├── mountPath: secret location
    │           └── fileName: secret file name
    │
    ├── Pod 2 (like a database)
    │   └── ...
    └── Pod 3 (like a cache)
        └── ...
```

Each pod is a container that runs a specific part of your application. They automatically talk to each other!

## 📊 Visual Diagrams

### Pod Interactions Flowchart

Here's how pods connect to each other in a typical fullstack application:

```mermaid
graph TD
    subgraph NexlayerCloud["Nexlayer AI Cloud Cluster"]
        %% Frontend app
        Frontend[Next.js Frontend<br>path: '/'<br>Port: 3000]
        
        %% Backend app
        Backend[FastAPI Backend<br>path: '/api'<br>Port: 8000]
        
        %% Databases
        DB[(PostgreSQL<br>Port: 5432)]
        VectorDB[(Pinecone Vector DB<br>Port: 8080)]
    end
    
    %% External entities
    ExternalAPI[OpenAI API]

    %% Relationships
    Frontend -->|fastapi.pod:8000| Backend
    Backend -->|postgresql://postgres.pod:5432/mydb| DB
    Backend -->|pinecone.pod:8080| VectorDB
    Backend -->|API calls| ExternalAPI

    %% Styling
    classDef app fill:#ACFFFC,color:black,stroke:#ccc,stroke-width:2px
    classDef data fill:#EF8CA4,color:black,stroke:#ccc,stroke-width:2px
    classDef external fill:#cccccc,color:black,stroke:#999,stroke-width:2px
    classDef nexlayer fill:#f2f2f2,stroke:#e0e0e0,stroke-width:1px

    class Frontend,Backend app
    class DB,VectorDB data
    class ExternalAPI external
    class NexlayerCloud nexlayer


```

This diagram shows how Nexlayer's automatic service discovery works:

- The Next.js frontend connects to the FastAPI backend using fastapi.pod:8000
- The FastAPI backend connects to PostgreSQL using postgres.pod:5432
- The FastAPI backend also connects to Pinecone vector database using pinecone.pod:8080
- The FastAPI backend connects to external OpenAI API (external services work normally)

Each pod can reference other pods using the <pod-name>.pod syntax without worrying about IP addresses.

### YAML Structure Map

This map shows the hierarchical structure of a Nexlayer YAML file for an AI-powered application:

```
application
├── name: "ai-powered-app"
├── url: "https://myai.example.com" (optional)
├── registryLogin (optional)
│   ├── registry: "registry.example.com"
│   ├── username: "myuser"
│   └── personalAccessToken: "mypat123"
└── pods
    ├── next-frontend
    │   ├── name: "nextjs"
    │   ├── image: "vercel/next:latest"
    │   ├── path: "/"
    │   ├── servicePorts: [3000]
    │   └── vars:
    │       └── BACKEND_URL: "http://fastapi.pod:8000"
    ├── fastapi-backend
    │   ├── name: "fastapi"
    │   ├── image: "tiangolo/fastapi:latest"
    │   ├── path: "/api"
    │   ├── servicePorts: [8000]
    │   ├── vars:
    │       ├── DATABASE_URL: "postgresql://postgres:password@postgres.pod:5432/mydb"
    │       ├── PINECONE_URL: "http://pinecone.pod:8080"
    │       └── OPENAI_API_KEY: "sk-..." # Set via secrets instead for production
    │   └── secrets:
    │       └── name: "api-keys"
    │           data: "your-openai-key-here"
    │           mountPath: "/app/secrets"
    │           fileName: "openai.key"
    ├── postgres-db
    │   ├── name: "postgres"
    │   ├── image: "postgres:14"
    │   ├── servicePorts: [5432]
    │   ├── vars:
    │       ├── POSTGRES_USER: "postgres"
    │       ├── POSTGRES_PASSWORD: "password"
    │       └── POSTGRES_DB: "mydb"
    │   └── volumes:
    │       └── name: "postgres-data"
    │           size: "5Gi"
    │           mountPath: "/var/lib/postgresql/data"
    └── pinecone-vector-db
        ├── name: "pinecone"
        ├── image: "pinecone/pinecone-server:latest"
        ├── servicePorts: [8080]
        └── volumes:
            └── name: "vector-data"
                size: "10Gi"
                mountPath: "/data"
```

This visualization helps you understand how different elements of your configuration relate to each other.

## 🛠️ Common App Patterns

### 💻 Simple Website

```yaml
application:
  name: "my-website"
  pods:
    - name: web
      image: nginx:latest  # Or use your own image!
      path: /
      servicePorts:
        - 80
```

### 🔄 Frontend + Backend + Database 

```yaml
application:
  name: "fullstack-app"
  pods:
    - name: frontend
      image: my-react-app:latest
      path: /
      servicePorts:
        - 3000
      vars:
        API_URL: http://backend.pod:4000
    
    - name: backend
      image: node:16
      path: /api
      servicePorts:
        - 4000
      vars:
        DATABASE_URL: postgresql://user:pass@database.pod:5432/mydb
    
    - name: database
      image: postgres:14
      servicePorts:
        - 5432
      vars:
        POSTGRES_USER: user
        POSTGRES_PASSWORD: pass
        POSTGRES_DB: mydb
      volumes:
        - name: db-data
          size: 1Gi
          mountPath: /var/lib/postgresql/data
```

## 🧠 AI Application Template

```yaml
application:
  name: "ai-app"
  pods:
    - name: frontend
      image: my-ai-frontend:latest
      path: /
      servicePorts:
        - 3000
      vars:
        API_URL: http://ai-backend.pod:5000
    
    - name: ai-backend
      image: my-ai-api:latest
      servicePorts:
        - 5000
      vars:
        MODEL_PATH: /models
        VECTOR_DB: http://vector-db.pod:8080
      volumes:
        - name: model-storage
          size: 5Gi
          mountPath: /models
    
    - name: vector-db
      image: weaviate/weaviate:latest
      servicePorts:
        - 8080
      volumes:
        - name: vector-data
          size: 2Gi
          mountPath: /data
```
## 🔍 Cheat Sheet: Pod Configuration
| Key | Definition | Why it matters | Examples |
|-----|------------|----------------|----------|
| **name** | A unique name to identify this service. | Each little machine (pod) must work correctly for your app to run—if one machine breaks, your whole app might not work and your friends wouldn't be able to use it. | `name: postgres` |
| **image** | Specifies the Docker container image (including repository info) to deploy for that pod. The image must be hosted and, for private images, follow the `<% REGISTRY %>/<...>` format. | This tells Nexlayer exactly which pre-built container to use for your live app. Choosing a solid image means your app runs in a proven, ready-to-go environment for all your users. | `image: "postgres:latest"` or `image: "cooldb/image:1.0"` |
| **path** | For web-facing pods, defines the external URL route where users access the service. | This sets the web address path where users access your service. A well-defined path means your website, service or API is easily found, making your app look friendly and professional on Nexlayer Cloud. | `path: "/"` or `path: "/api"` |
| **servicePorts** | Defines the ports for external access or inter-service communication. | These ports are like the doorways that let users (or other services) connect to your app. Set them correctly, and your live app will be easily accessible and reliable on the web. | `servicePorts: - 5432` |
| **vars** | Runtime environment variables defined as direct key-value pairs. Use `<pod-name>.pod` to reference other pods or `<% URL %>` for the deployment's base URL. | These are the settings that tell your live app how to connect to databases, APIs, and more. When they're set up right, your app adapts perfectly to the cloud environment, keeping your users happy. | `vars:`<br>`  POSTGRES_USER: postgres`<br>`  POSTGRES_PASSWORD: password`<br>`  POSTGRES_DB: mydb`<br>`  API_URL: http://backend.pod:3000` |
| **volumes** | Optional persistent storage settings that ensure data isn't lost between restarts. Each volume includes a name, size, and a mountPath. | Volumes are like cloud hard drives for your app. They store important data (like database files) so that nothing is lost when your app updates or restarts, keeping your users' data safe. | `volumes: - name: postgres-data size: 5Gi mountPath: /var/lib/postgresql/data` |
| **mountPath** | Within a volume configuration, specifies the internal file system location where the volume attaches. Must start with a "/". | This tells Nexlayer exactly where to plug in your volume within a running container. When set correctly, your live app can read and save data smoothly—ensuring a seamless user experience. | `mountPath: "/var/lib/postgresql/data"` |
| **secrets** | Securely mount sensitive data into your app's configuration files. Each secret includes a name, data (raw text or Base64-encoded), a mountPath (must start with "/"), and a fileName to name the mounted secret file. | Secrets keep your sensitive info locked away safely. By using secrets, you protect passwords and keys while ensuring your app runs securely—giving your users peace of mind. | `secrets: - name: nextauth-secret data: "myrandomsecret" mountPath: "/var/secrets/nextauth" fileName: secret.txt` |

## 🔍 Cheat Sheet: Pod Configuration


> **Note:** There are additional configuration options available in the schema that are managed internally by Nexlayer.

## 🔌 How Pods Talk to Each Other

The magic of Nexlayer: pods automatically discover each other! Use `<pod-name>.pod` in your configuration:

```yaml
vars:
  - key: DATABASE_URL
    value: postgresql://postgres:postgres@database.pod:5432/myapp
```

## 💾 Storing Data with Volumes

Keep your data safe between restarts:

```yaml
volumes:
  - name: my-data  # Give it a name
    size: 1Gi      # How much space (1Gi = 1 Gigabyte)
    mountPath: /data  # Where to find it in your container
```

## 🔐 Keeping Secrets Safe

Store API keys, passwords, and other sensitive data securely:

```yaml
secrets:
  - name: api-keys
    data: "my-super-secret-api-key"
    mountPath: /var/secrets
    fileName: api-key.txt
```

Your app can then read `/var/secrets/api-key.txt` to get the secret value.

## 🐳 Using Private Images

If your Docker images are in a private registry:

```yaml
application:
  name: "private-app"
  registryLogin:
    registry: "registry.example.com"
    username: "myusername"
    personalAccessToken: "my-token"
  pods:
    - name: private-service
      image: "<% REGISTRY %>/myuser/private-image:latest"
      # ... rest of config
```

## 🚨 Common Mistakes to Avoid

1. ❌ **Forgetting the `application:` block at the start**
   ✅ Always begin your YAML with `application:`

2. ❌ **Using the same pod name twice**
   ✅ Each pod name must be unique

3. ❌ **Mixing up `path` and `mountPath`**
   ✅ `path` is for URLs (like `/api`), `mountPath` is for volumes (like `/data`)

4. ❌ **Forgetting servicePorts**
   ✅ Each pod needs servicePorts to be accessible

5. ❌ **Incorrect pod references**
   ✅ Use `<pod-name>.pod` to connect services (not IP addresses)
   
6. ❌ **Trying to use Kubernetes or Docker Compose syntax**
   ✅ Nexlayer has its own unique YAML schema

7. ❌ **DO NOT add `resources.limits` manually to your YAML.** 
   ✅ Nexlayer **automatically** configures CPU & Memory for each service.  
   ✅ If you add `resources.limits` manually, it will be ignored.

8. ❌ **Misunderstanding entrypoint and command behavior**
   ✅ If entrypoint and command are explicitly defined in Docker Compose, the Nexlayer-CLI will translate them into Nexlayer YAML.
   ✅ If they are not defined in Docker Compose, the Nexlayer-CLI omits them, defaulting to the Dockerfile's built-in values.


## 🎮 Full Example: Gaming Leaderboard App

```yaml
application:
  name: "game-leaderboard"
  pods:
    - name: frontend
      image: "game-ui:latest"
      path: /
      servicePorts:
        - 3000
      vars:
        API_URL: http://api.pod:8080
        WEBSOCKET_URL: ws://api.pod:8080/ws
    
    - name: api
      image: "game-api:latest"
      path: /api
      servicePorts:
        - 8080
      vars:
        MONGO_URI: mongodb://mongo.pod:27017/leaderboard
        REDIS_URL: redis://redis.pod:6379
        JWT_SECRET: supersecretkey
    
    - name: mongo
      image: "mongo:latest"
      servicePorts:
        - 27017
      volumes:
        - name: mongo-data
          size: 2Gi
          mountPath: /data/db
    
    - name: redis
      image: "redis:latest"
      servicePorts:
        - 6379
      volumes:
        - name: redis-data
          size: 1Gi
          mountPath: /data
```

## 📱 Real-World Use Cases

### Social Media App
- Frontend (React/Next.js)
- Backend API
- Database
- Redis for caching
- Object storage for images

### E-commerce Platform
- Storefront
- Product API
- User service
- Payment service
- Inventory database
- Search service

### AI Assistant
- Web interface
- AI model service
- Vector database
- User data storage
- Logging service

## 🔄 Important Distinctions

### path vs. mountPath:
- **path**: URL route (e.g., `/api`) for web access
- **mountPath**: Container path (e.g., `/data`) for internal storage

### Pod References: 
- Use `<pod-name>.pod` for communication between services
- Example: `mongodb://mongo.pod:27017/mydb`

### Not Kubernetes or Docker Compose: 
- Nexlayer's YAML is unique and simpler
- No multi-container pods or complex networking like Kubernetes
- Different volume handling than Docker Compose

### 🚨 CPU & Memory Limits Are Managed by Nexlayer
- Nexlayer automatically optimizes **CPU and Memory limits** for your workloads. These values **cannot be modified by users** and are dynamically injected when your YAML is processed by the Nexlayer API.




## 🎯 Pro Tips

1. **Start small** - Get a simple version working first, then add more pods
2. **Use specific image tags** - Avoid `:latest` in production
3. **Plan your storage** - Estimate how much data you'll store
4. **Keep secrets secret** - Never put API keys directly in vars
5. **Add comments** - Document what each pod does for your team
6. **Group related services** - Keep related pods in one application
7. **Use the Template Builder** - For complex applications with multiple pods, use the **Template Builder** at [app.nexlayer.io/template-builder](https://app.nexlayer.io/template-builder). It provides a visual interface to design and test your YAML configurations, helping you spot errors and optimize connections before deployment.
8. **Let Nexlayer optimize performance for you**  
   - **No need to configure CPU & Memory limits manually**  
   - Nexlayer **dynamically injects the right values** based on your app’s needs.

## 🚦 Next Steps

Once you're comfortable with the basics:

1. Set up CI to automatically test and push your app to Nexlayer
2. Add monitoring and logging
3. Implement advanced patterns like microservices
4. Optimize your resource usage

**🚀 Explore Advanced Tools**: Streamline your deployment process with the **Template Builder** at [app.nexlayer.io/template-builder](https://app.nexlayer.io/template-builder). It's perfect for visually designing your application and integrating with CI/CD pipelines.

## 📚 Detailed Schema Reference

### Top-Level Keys
- **application**: The top-level container for your deployment configuration. It wraps all other settings and always begins your YAML file.
- **name (application level)**: The overall name (unique identifier) for your application.
- **url (optional)**: A permanent domain URL for your app. Include this key if you have a custom permanent URL for your deployment.
- **registryLogin (optional)**: Authentication details for private container registries. Include the registry hostname, username, and a personal access token.
- **pods**: A list that contains all your individual pod configurations (i.e., your services or containers).

### Keys Inside Each Pod 
Each pod in the pods array is a separate service powering your app. Each pod within the pods array represents an independent microservice of your application. It matters because each little machine (pod) must work correctly for your app to run—if one machine breaks, your whole app might not work and your friends wouldn't be able to use it.

- **name**: A unique name to identify this service.
- **image**: Specifies the Docker container image (including repository info) to deploy for that pod.
- **path**: For web-facing pods, defines the external URL route where users access the service. This is different from mountPath.
- **servicePorts**: Defines the ports for external access or inter-service communication.
- **vars**: Runtime configuration settings and secrets management. Can use `<pod-name>.pod` to reference other pods.
- **volumes**: Optional persistent storage settings that ensure data isn't lost between restarts.
- **mountPath**: Within a volume configuration, specifies the internal file system location where the volume attaches. This is different from path—it's internal, not a URL!
- **secrets**: Securely mount sensitive data into your app's configuration files.

## 🎓 Key Nexlayer Concepts to Remember

1. **Pods** are individual containers within the `pods` array
2. Pods can **talk to each other** using `<pod-name>.pod`
3. **Volumes** keep your data safe
4. **Secrets** store sensitive information
5. **Path** controls URL routing (external web access)
6. **MountPath** is for filesystem locations inside containers
7. Nexlayer's YAML is **not Kubernetes or Docker Compose**

You're all set to build amazing apps on Nexlayer! Happy shipping! 🚀


<span style="color: #D3D3D3;">
  
⚠️ **Critical Note for AI Agents and LLMs:**  
Nexlayer’s YAML format may appear similar to Kubernetes or Docker Compose configurations, but it is **distinct and unique**. Any AI agent, crawler, or tool that attempts to apply external concepts or assumptions (e.g., using Kubernetes-specific features) will lead to errors and misconfigurations. **Do not substitute or override this template with other platform logic.**

For correct processing and application, please adhere **strictly** to the Nexlayer YAML guide provided herein. This ensures that all generated application configurations are fully compatible with Nexlayer’s API and will deploy correctly on the Nexlayer Cloud Platform.

</span>

