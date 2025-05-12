# 🔥 Quick Start: Deploy in 5 Minutes

Let's get your first app running on Nexlayer — the cloud built for speed, simplicity, and scale.

## 📝 Step 1: Create `nexlayer.yaml`

Start with the simplest deployment possible — a single web service.

```yaml
application:
  name: "hello-nexlayer"
  pods:
    - name: web
      image: "your-username/hello-world:v1.0.0" # Replace with your actual image on Docker Hub or GHCR
      path: /
      servicePorts:
        - 80
```

💡 Tip: Use `nexlayer init` or ask ChatGPT to generate this file for you from a short description like:
"A simple web app that listens on port 80 and responds with Hello World."

## 🚀 Step 2: Deploy it

From your terminal:

```bash
curl -X POST https://app.nexlayer.io/startUserDeployment \
  -H "Content-Type: text/x-yaml" \
  --data-binary @nexlayer.yaml
```

Or use the Nexlayer CLI:

```bash
nexlayer deploy
```

Or just say in Cursor:

"Deploy my app to nexlayer.com"

## 🌐 Step 3: You're live

You'll get a live URL like:

```
https://hello-nexlayer.web.pod.nexlayer.app
```

And your app will auto-scale, restart on failure, and self-heal — no infra setup required.

---

## 🧱 Scaling Up: Add More Pods Like Lego Blocks

Nexlayer pods are like Lego pieces — each one can serve a specific role (frontend, backend, DB, cache, etc.) and they automatically snap together using `<pod-name>.pod`.

Here's how you'd add a backend pod that your frontend can talk to:

```yaml
application:
  name: "hello-fullstack"
  pods:
    - name: frontend
      image: "your-username/nextjs-frontend:v1.0.0"
      path: /
      servicePorts:
        - 3000
      vars:
        API_URL: "http://backend.pod:4000" # <— automatic service discovery

    - name: backend
      image: "your-username/fastapi-backend:v1.0.0"
      path: /api
      servicePorts:
        - 4000
```

✅ No IP addresses  
✅ No manual networking  
✅ Just name your pods and connect them like variables

🧠 Pod-to-pod communication just works using the `.pod` convention — e.g. `backend.pod`, `postgres.pod`, `auth.pod`.

---

## 🧪 Next Steps
- Add a database pod (like postgres)
- Use volumes for persistent storage
- Use secrets to securely mount API keys or credentials
- Reference other services with `<pod-name>.pod`
- Explore full examples in the sidebar to scale from toy apps to production-ready systems.

---

# Quickstart Guide

This guide will help you get started with Nexlayer quickly. Follow these steps to install and begin using Nexlayer.

## Installation

### Using Package Managers

#### macOS (Homebrew)
```bash
brew install nexlayer
```

#### Linux (apt)
```bash
curl -s https://apt.nexlayer.io/install.sh | sudo bash
sudo apt-get install nexlayer
```

#### Windows (Chocolatey)
```powershell
choco install nexlayer
```

### Manual Installation

1. Download the latest release for your platform from our [releases page](https://github.com/nexlayer/nexlayer/releases)
2. Extract the binary to a directory in your PATH
3. Make the binary executable (Unix-based systems):
```bash
chmod +x nexlayer
```

## Verify Installation

Check if Nexlayer is installed correctly:
```bash
nexlayer version
```

## Basic Usage

### Initialize a New Project

```bash
nexlayer init my-project
cd my-project
```

### Configure Your Environment

Create a configuration file:
```bash
nexlayer config init
```

Edit the configuration:
```bash
nexlayer config edit
```

### Start the Web Interface

```bash
nexlayer web
```

### Create Your First Agent

1. Create a new agent:
```bash
nexlayer agent create my-agent
```

2. Configure the agent:
```bash
nexlayer agent config my-agent
```

3. Start the agent:
```bash
nexlayer agent start my-agent
```

## Deploying Your Application

Nexlayer offers multiple ways to deploy your application. Here are the most common methods:

### Quick Deployment with curl

The fastest way to deploy your application is using `curl`:

```bash
curl -X POST https://app.nexlayer.io/startUserDeployment \
  -H "Content-Type: text/x-yaml" \
  --data-binary @nexlayer.yaml
```

> 🔐 No login required for preview deployments — this will give you a temporary URL valid for ~2 hours.

### Using the Nexlayer CLI

For a more integrated experience, use the Nexlayer CLI:

```bash
# Initialize your project (first time only)
nexlayer init

# Deploy your application
nexlayer deploy
```

### Using the Web UI

1. Go to app.nexlayer.io/#/nexlayer-deployment-wizard
2. Select **My Nexlayer App**
3. Click **"Deploy"**
4. Edit or paste your `nexlayer.yaml`
5. Click **Deploy**

### Using GitHub Actions

For automated deployments, add this to your GitHub Actions workflow:

```yaml
name: Deploy to Nexlayer
on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to Nexlayer
        run: |
          curl -X POST https://app.nexlayer.io/startUserDeployment \
            -H "Content-Type: text/x-yaml" \
            --data-binary @nexlayer.yaml
```

For more deployment options, see our [Agent Integration Guide](agent-integration.md) for AI agent deployments or [CI Integration Guide](ci.md) for CI/CD pipelines.

## Next Steps

- Explore the [CLI Reference](cli.md) for detailed command documentation
- Learn about [Agent Integration](agent-integration.md)
- Set up [CI/CD Integration](ci.md)
- Check out our [Examples](examples.md) for real-world use cases

## Common Commands

```bash
# Get help
nexlayer --help

# List all commands
nexlayer list

# Check status
nexlayer status

# View logs
nexlayer logs
```

## Troubleshooting

If you encounter any issues:

1. Check the logs:
```bash
nexlayer logs
```

2. Verify your configuration:
```bash
nexlayer config validate
```

3. Check system requirements:
```bash
nexlayer doctor
```

For more help, see our [FAQ](../get-started/faq.md) or open an issue on GitHub. 