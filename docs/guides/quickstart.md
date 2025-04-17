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