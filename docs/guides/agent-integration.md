# Agent Integration Guide

This guide explains how to create, configure, and manage Nexlayer agents for automation and task execution.

## Understanding Agents

Nexlayer agents are intelligent components that can:
- Execute automated tasks
- Monitor system conditions
- Respond to events
- Integrate with external services

## Agent Types

### Default Agent
Basic agent for simple task execution and monitoring.

### CI Agent
Specialized agent for continuous integration tasks.

### Deployment Agent
Handles deployment and release management.

### Monitoring Agent
Collects and analyzes system metrics.

## AI Agent Deployment Flow

Nexlayer supports direct integration with AI agents for deployment. The flow is simple:

```txt
🤖 AI Agent Flow: Claude / GPT / Cursor → GET /schema → POST /validate → POST /startUserDeployment → Live!

GET /schema  
POST /validate  
POST /startUserDeployment  

✔ yourapp.nexlayer.ai is live!  
```

### Example AI Agent Integration

Here's a Python example of how to integrate with Nexlayer using an AI agent:

```python
import requests

with open("nexlayer.yaml", "rb") as f:
    res = requests.post(
        "https://app.nexlayer.io/startUserDeployment",
        headers={"Content-Type": "text/x-yaml"},
        data=f
    )

print(res.json())
```

### Example Prompts for AI Agents

Here are some ready-to-use prompts you can feed to your AI assistant or agent:

#### Cursor
> "Cursor, take the `nexlayer.yaml` in my current workspace and deploy it to Nexlayer by POSTing it to `https://app.nexlayer.io/startUserDeployment`. Show me the returned URL."

#### Windsurf
> "Windsurf, please send a POST request with `Content-Type: text/x-yaml` and body from `nexlayer.yaml` to `https://app.nexlayer.io/startUserDeployment`, then display the JSON response."

#### GitHub Copilot (in VS Code)
> "GitHub Copilot, add a VS Code task in `.vscode/tasks.json` named **Deploy to Nexlayer** that runs:
> ```bash
> curl -X POST https://app.nexlayer.io/startUserDeployment \
>   -H \"Content-Type: text/x-yaml\" \
>   --data-binary @nexlayer.yaml
> ```
> and then prints me the deployment URL."

#### Claude Code
> "Claude, generate a Node.js (or Python) script that reads `nexlayer.yaml` from disk and deploys it by calling the Nexlayer `startUserDeployment` endpoint. Log the resulting URL to the console."

#### Warp
> "Warp, create a snippet called **nexlayer deploy** that runs:
> ```bash
> curl -X POST https://app.nexlayer.io/startUserDeployment \
>   -H \"Content-Type: text/x-yaml\" \
>   --data-binary @nexlayer.yaml
> ```
> so I can trigger it with `warp run nexlayer deploy`."

#### ChatGPT (or any generic LLM)
> "Write me a bash one-liner that posts my `nexlayer.yaml` file to Nexlayer's `startUserDeployment` endpoint and parses out the `url` field."

## Creating Agents

### Using CLI

```bash
# Create a new agent
nexlayer agent create my-agent

# Configure the agent
nexlayer agent config my-agent

# Start the agent
nexlayer agent start my-agent
```

### Using Web UI

1. Navigate to Agents section
2. Click "New Agent"
3. Select agent type
4. Configure settings
5. Click "Create"

## Agent Configuration

### Basic Configuration

```yaml
name: my-agent
type: default
config:
  enabled: true
  schedule: "*/5 * * * *"  # Run every 5 minutes
  timeout: 300  # 5 minutes
  retries: 3
```

### Advanced Configuration

```yaml
name: my-agent
type: default
config:
  enabled: true
  schedule: "*/5 * * * *"
  timeout: 300
  retries: 3
  resources:
    cpu: 1
    memory: 512Mi
  environment:
    NODE_ENV: production
    API_KEY: ${API_KEY}
  hooks:
    pre-execute: scripts/pre-execute.sh
    post-execute: scripts/post-execute.sh
  monitoring:
    enabled: true
    metrics:
      - cpu
      - memory
      - disk
```

## Agent Lifecycle

1. **Creation**
   - Define agent properties
   - Set initial configuration
   - Configure resources

2. **Configuration**
   - Set up schedules
   - Define tasks
   - Configure environment
   - Set up monitoring

3. **Execution**
   - Start agent
   - Monitor execution
   - Handle errors
   - Collect metrics

4. **Maintenance**
   - Update configuration
   - Scale resources
   - Monitor performance
   - Troubleshoot issues

## Task Definition

### Basic Task

```yaml
tasks:
  - name: check-system
    command: nexlayer check
    schedule: "*/15 * * * *"
    timeout: 60
```

### Complex Task

```yaml
tasks:
  - name: deploy-application
    steps:
      - name: build
        command: make build
        timeout: 300
      - name: test
        command: make test
        timeout: 600
      - name: deploy
        command: make deploy
        timeout: 900
    dependencies:
      - build
      - test
    retries: 3
    timeout: 1800
```

## Monitoring and Metrics

### Available Metrics

- CPU usage
- Memory consumption
- Disk I/O
- Network traffic
- Task execution time
- Success/failure rates

### Setting Up Monitoring

```yaml
monitoring:
  enabled: true
  interval: 60
  metrics:
    - cpu
    - memory
    - disk
  alerts:
    - name: high-cpu
      condition: cpu > 80
      action: notify
```

## Error Handling

### Retry Configuration

```yaml
retry:
  attempts: 3
  delay: 5
  max-delay: 60
  backoff: exponential
```

### Error Actions

```yaml
error-handling:
  on-failure:
    - action: notify
      channel: slack
    - action: rollback
      steps: [deploy]
  on-timeout:
    - action: kill
    - action: notify
```

## Security

### Authentication

```yaml
security:
  auth:
    type: token
    token: ${AGENT_TOKEN}
  tls:
    enabled: true
    cert: /path/to/cert
    key: /path/to/key
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

1. **Resource Management**
   - Set appropriate resource limits
   - Monitor resource usage
   - Scale resources as needed

2. **Error Handling**
   - Implement proper retry logic
   - Set up error notifications
   - Log errors appropriately

3. **Security**
   - Use secure authentication
   - Implement role-based access
   - Encrypt sensitive data

4. **Monitoring**
   - Set up comprehensive monitoring
   - Configure alerts
   - Track performance metrics

## Troubleshooting

### Common Issues

1. **Agent Not Starting**
   - Check configuration
   - Verify resources
   - Review logs

2. **Task Failures**
   - Check dependencies
   - Verify permissions
   - Review error logs

3. **Performance Issues**
   - Monitor resource usage
   - Check task schedules
   - Review configuration

## Examples

### Basic Monitoring Agent

```yaml
name: monitor-agent
type: monitoring
config:
  schedule: "*/5 * * * *"
  tasks:
    - name: check-system
      command: nexlayer check
      timeout: 60
  monitoring:
    enabled: true
    metrics:
      - cpu
      - memory
```

### CI Agent

```yaml
name: ci-agent
type: ci
config:
  tasks:
    - name: build-and-test
      steps:
        - name: build
          command: make build
        - name: test
          command: make test
  environment:
    GO_VERSION: 1.16
    NODE_VERSION: 14
```

## Support

For additional help:
- Check the [FAQ](../get-started/faq.md)
- Review [Examples](examples.md)
- Open GitHub issues
- Join community discussions 