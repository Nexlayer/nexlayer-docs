# Nexlayer Templates

Welcome to Nexlayer Templates, the fastest way to deploy full-stack applications with ease. Our platform ensures you can go from configuration to deployment in just a few clicks.

**Why Nexlayer?**

- 🚀 **Speed**: Pre-configured templates for popular tech stacks.
- ⚙️ **Flexibility**: Fully customizable YAML configurations.
- 📈 **Scalability**: Built-in support for horizontal scaling and load balancing.

Use this guide to explore, customize, and deploy templates that match your application needs.

---

## 🚀 Quick Start

1. **Choose a Template**: Pick the template that suits your app or stack.
2. **Customize the Template**: Modify the provided YAML as needed.
3. **Deploy**: Use Nexlayer's web UI or CLI to launch your app in seconds.

---

## 📂 General Template Structure

Each Nexlayer template follows a consistent structure for seamless deployment:

### Template Fields

- **`application.template.name`**: Identifier for the application template stack.
- **`application.template.deploymentName`**: Your deployment's name in Nexlayer.
- **`application.template.registryLogin`**: Login credentials for private Docker registries.

### Pods Configuration

Define the components of your app using the `pods` array:

| Field        | Description                                                     | Example                               |
| ------------ | --------------------------------------------------------------- | ------------------------------------- |
| `type`       | The pod type (`database`, `llm`, `django`, `react`, etc.).      | `django`                              |
| `name`       | Specific name for the pod (e.g., `postgres`, `mongodb`, `vue`). | `vue`                                 |
| `tag`        | Docker image used for the pod.                                  | `node:14-alpine`                      |
| `privateTag` | Boolean to indicate if the image is from a private registry.    | `true`                                |
| `vars`       | Environment variables for the pod.                              | `[{"name": "PORT", "value": "3000"}]` |

### Supported Pod Types and Names

- **Database**: `postgres`, `mysql`, `neo4j`, `redis`, `mongodb`
- **Frontend**: `react`, `angular`, `vue`
- **Backend**: `django`, `fastapi`, `express`
- **Others**: `nginx`, `llm` (custom naming allowed)

### Expose HTTP

Set `exposeHttp: true` to make the pod accessible via HTTP.

---

## 🔧 Nexlayer-Provided Environment Variables

Templates include predefined environment variables to simplify configuration:

| Variable Value               | Description                                                                                                              | Example                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| `PROXY_URL`                  | The URL of your created Nexlayer site.                                                                                   | `https://your-site-name.alpha.nexlayer.ai`    |
| `PROXY_DOMAIN`               | The domain of your created Nexlayer site.                                                                                | `your-site-name.alpha.nexlayer.ai`            |
| `DATABASE_HOST`              | The hostname of your database.                                                                                           | -                                             |
| `NEO4J_URI`                  | The URI of your Neo4j database.                                                                                          | -                                             |
| `DATABASE_CONNECTION_STRING` | The connection string to connect to your database.                                                                       | `postgresql://user:password@host:port/dbname` |
| `FRONTEND_CONNECTION_URL`    | The URL to connect to your frontend. Connects to your `react`, `angular`, or `vue` pod. Prefixed with `http://`          | -                                             |
| `BACKEND_CONNECTION_URL`     | The URL to connect to your backend. Connects to your `django`, `fastapi`, or `express` pod. Prefixed with `http://`      | -                                             |
| `LLM_CONNECTION_URL`         | The URL to connect to your LLM. Connects to your `llm` pod. Prefixed with `http://`                                      | -                                             |
| `FRONTEND_CONNECTION_DOMAIN` | The domain to connect to your frontend. Connects to your `react`, `angular`, or `vue` pod. Does NOT include a prefix     | -                                             |
| `BACKEND_CONNECTION_DOMAIN`  | The domain to connect to your backend. Connects to your `django`, `fastapi`, or `express` pod. Does NOT include a prefix | -                                             |
| `LLM_CONNECTION_DOMAIN`      | The domain to connect to your LLM. Connects to your `llm` pod. Does NOT include a prefix                                 | -                                             |




---

## 🔄 Github Actions Workflow for Docker Images

To build and push your Docker images for Nexlayer:

1. Create a `.github/workflows/docker-publish.yml` file.
2. Add the following workflow code:

```yaml
name: Build and Push Docker Image

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    permissions:
      contents: read
      packages: write

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Log in to GitHub Container Registry
      uses: docker/login-action@v2
      with:
        registry: ghcr.io
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}

    - name: Set repository owner lowercase # Necessary for Docker image tagging
      id: owner_lowercase
      run: echo "owner_lowercase=$(echo '${{ github.repository_owner }}' | tr '[:upper:]' '[:lower:]')" >> $GITHUB_ENV

    - name: Build and Push Docker Image
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ghcr.io/${{ env.owner_lowercase }}/my-image-name:v0.0.1
```
3. Replace `my-image` with your Docker image name.

---

## 📚 Template Catalog

Explore our ready-to-use full-stack templates:

### 🛠 Template Overview

| Template Name       | Frontend Framework | Backend Framework | Database       | Best For                             |
| ------------------- | ------------------ | ----------------- | -------------- | ------------------------------------ |
| **MERN Todo List**  | React              | Express           | MongoDB        | Task management with React frontend. |
| **MEAN Todo List**  | Angular            | Express           | MongoDB        | Responsive to-do list with Angular.  |
| **MEVN Todo App**   | Vue.js             | Express           | MongoDB        | User-friendly Vue.js task manager.   |
| **MNFA User Store** | Angular            | FastAPI, Neo4j    | MongoDB, Neo4j | User management and authentication.  |
| **PERN Todo List**  | React              | Express           | PostgreSQL     | Full-stack app with PostgreSQL DB.   |

---

### 🌐 How Nexlayer Templates Work

```mermaid
graph TD
    A[Select Template] --> B[Customize YAML Configuration]
    B --> C[Validate with Nexlayer CLI or UI]
    C --> D[Deployment Process in Kubernetes Cluster]
    D --> E[Autoscaling and Load Balancing]
    E --> F[Application Ready and URL Provided]
    F --> G[Monitor and Scale Resources Dynamically]
```

---

### MERN Todo List

**[GitHub Repository](https://github.com/Nexlayer/MERN-Todo-List)**\
**Description**: A React-based template for task management.\
**Snippet**:

```yaml
application:
  template:
    name: "mongodb-express-react-nodejs"
    deploymentName: "My MERN Todo App"
    registryLogin:
      registry: ghcr.io
      username: <Github username>
      personalAccessToken: <Github Packages Read-Only PAT>
    pods:
    - type: database
      exposeHttp: false
      name: mongoDB
      tag: <ghcr.io/myLowercaseUsername/mern-mongo-todo:v0.0.1>
      privateTag: true
      vars:
      - key: MONGO_INITDB_ROOT_USERNAME
        value: mongo
      - key: MONGO_INITDB_ROOT_PASSWORD
        value: passw0rd
    - type: express
      exposeHttp: false
      name: express
      tag: <ghcr.io/myLowercaseUsername/mern-express-todo:v0.0.1>
      privateTag: true
      vars:
      - key: MONGODB_URL
        value: DATABASE_CONNECTION_STRING
    - type: nginx
      exposeHttp: true
      name: nginx
      tag: <ghcr.io/myLowercaseUsername/mern-react-todo:v0.0.1>
      privateTag: true
      vars:
      - key: EXPRESS_URL
        value: BACKEND_CONNECTION_URL
```

### MEAN Todo List

**[GitHub Repository](https://github.com/Nexlayer/MEAN-Todo-List)**\
**Description**: Angular-powered template for a responsive to-do list.\
**Snippet**:

```yaml
application:
  template:
    name: "mongodb-express-angular-nodejs"
    deploymentName: "My MEAN Todo App"
    registryLogin:
      registry: ghcr.io
      username: <Github username>
      personalAccessToken: <Github Packages Read-Only PAT>
    pods:
    - type: database
      exposeHttp: false
      name: mongoDB
      tag: <ghcr.io/myLowercaseUsername/mean-mongo-todo:v0.0.1>
      privateTag: true
      vars:
      - key: MONGO_INITDB_ROOT_USERNAME
        value: mongo
      - key: MONGO_INITDB_ROOT_PASSWORD
        value: passw0rd
      - key: MONGO_INITDB_DATABASE
        value: mongo
    - type: express
      exposeHttp: false
      name: express
      tag: <ghcr.io/myLowercaseUsername/mean-express-todo:v0.0.1>
      privateTag: true
      vars:
      - key: MONGODB_URL
        value: DATABASE_CONNECTION_STRING
    - type: nginx
      exposeHttp: true
      name: nginx
      tag: <ghcr.io/myLowercaseUsername/mean-angular-todo:v0.0.1>
      privateTag: true
      vars:
      - key: EXPRESS_URL
        value: BACKEND_CONNECTION_URL
```

### MEVN Todo App

**[GitHub Repository](https://github.com/Nexlayer/MEVN-Todo-App)**\
**Description**: Vue.js-based template for a user-friendly task manager.\
**Snippet**:

```yaml
application:
  template:
    name: "mongodb-express-vue-nodejs"
    deploymentName: "My MEVN Todo App"
    registryLogin:
      registry: ghcr.io
      username: <Github username>
      personalAccessToken: <Github Packages Read-Only PAT>
    pods:
    - type: database
      exposeHttp: false
      name: mongoDB
      tag: <ghcr.io/myLowercaseUsername/mevn-mongo-todo:v0.0.1>
      privateTag: true
      vars:
      - key: MONGO_INITDB_ROOT_USERNAME
        value: mongo
      - key: MONGO_INITDB_ROOT_PASSWORD
        value: passw0rd
      - key: MONGO_INITDB_DATABASE
        value: todo
    - type: express
      exposeHttp: false
      name: express
      tag: <ghcr.io/myLowercaseUsername/mevn-express-todo:v0.0.1>
      privateTag: true
      vars:
      - key: MONGO_URL
        value: DATABASE_CONNECTION_STRING
    - type: nginx
      exposeHttp: true
      name: nginx
      tag: <ghcr.io/myLowercaseUsername/mevn-vue-todo:v0.0.1>
      privateTag: true
      vars:
      - key: EXPRESS_URL
        value: BACKEND_CONNECTION_URL
```

### MNFA User Store App

**[GitHub Repository](https://github.com/Nexlayer/MNFA-User-Store-App)**\
**Description**: FastAPI backend for user management and authentication.\
**Snippet**:

```yaml
application:
  template:
    name: "mongodb-neo4j-fastAPI-angular"
    deploymentName: "My MNFA User Store"
    registryLogin:
      registry: ghcr.io
      username: <Github username>
      personalAccessToken: <Github Packages Read-Only PAT>
    pods:
    - type: database
      exposeOn80: false
      name: mongoDB
      tag: <ghcr.io/myLowercaseUsername/mnfa-mongo-user-store:v0.0.1>
      privateTag: true
      vars:
      - key: MONGO_INITDB_ROOT_USERNAME
        value: mongo
      - key: MONGO_INITDB_ROOT_PASSWORD
        value: passw0rd
      - key: MONGO_INITDB_DATABASE
        value: mongo
    - type: neo4j
      exposeOn80: false
      name: neo4j
      tag: neo4j:5.23.0
      vars:
      - key: NEO4J_AUTH
        value: neo4j/passw0rd
    - type: fastAPI
      exposeOn80: false
      name: fastAPI
      tag: <ghcr.io/myLowercaseUsername/mnfa-fastapi-user-store:v0.0.1>
      privateTag: true
      vars:
      - key: NEO4J_URL
        value: NEO4J_URI
      - key: NEO4J_USERNAME
        value: neo4j
      - key: NEO4J_PASSWORD
        value: passw0rd
      - key: MONGODB_URL
        value: DATABASE_CONNECTION_STRING
      - key: MONGODB_DB
        value: mongo
    - type: nginx
      exposeOn80: true
      name: nginx
      tag: <ghcr.io/myLowercaseUsername/mnfa-angular-user-store:v0.0.1>
      privateTag: true
      vars:
      - key: EXPRESS_URL
        value: BACKEND_CONNECTION_URL
```

### PDN Todo List

**[GitHub Repository](https://github.com/Nexlayer/PDN-Todo-List)**\
**Description**: Django-powered backend for to-do apps.

### PERN Todo List

**[GitHub Repository](https://github.com/Nexlayer/PERN-Todo-List)**\
**Description**: A PostgreSQL, Express, React, and Node.js stack template.

---

## 🤝 Contribute

Found a bug or have ideas for improvement? Submit feedback or issues directly on our [GitHub Issues Page](https://github.com/Nexlayer/templates/issues).

---

## 💡 Pro Tips

- **Short Deployment Times**: Use the provided `vars` to preconfigure services and skip manual setup.
- **Flexible Scaling**: Leverage Nexlayer’s HPA and caching mechanisms for high-traffic apps.
- **One-Click Deploy**: Modify and deploy directly from the YAML editor on Nexlayer.

