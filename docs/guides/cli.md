# CLI Reference

This document provides detailed information about Nexlayer's command-line interface.

## Command Structure

Nexlayer commands follow this general structure:
```bash
nexlayer <command> [subcommand] [flags]
```

## Global Flags

- `--config string`: Path to config file (default: ~/.nexlayer/config.yaml)
- `--debug`: Enable debug mode
- `--log-level string`: Log level (debug, info, warn, error) (default: info)
- `--version`: Show version information

## Core Commands

### Configuration

```bash
nexlayer config init      # Initialize configuration
nexlayer config edit      # Edit configuration
nexlayer config validate  # Validate configuration
nexlayer config show      # Show current configuration
```

### Project Management

```bash
nexlayer init <project>   # Initialize a new project
nexlayer status          # Show project status
nexlayer list            # List project components
```

### Agent Management

```bash
nexlayer agent create <name>    # Create a new agent
nexlayer agent config <name>    # Configure an agent
nexlayer agent start <name>     # Start an agent
nexlayer agent stop <name>      # Stop an agent
nexlayer agent list            # List all agents
nexlayer agent status <name>   # Show agent status
```

### Web Interface

```bash
nexlayer web start       # Start the web interface
nexlayer web stop        # Stop the web interface
nexlayer web status      # Show web interface status
```

## Advanced Commands

### CI/CD Integration

```bash
nexlayer ci init         # Initialize CI/CD configuration
nexlayer ci validate     # Validate CI/CD configuration
nexlayer ci run          # Run CI/CD pipeline
```

### Logging and Debugging

```bash
nexlayer logs            # Show logs
nexlayer logs tail       # Tail logs
nexlayer logs clear      # Clear logs
nexlayer doctor          # Run diagnostics
```

## Command Examples

### Initialize a New Project

```bash
# Create a new project
nexlayer init my-project

# Navigate to project directory
cd my-project

# Initialize configuration
nexlayer config init

# Create and configure an agent
nexlayer agent create my-agent
nexlayer agent config my-agent

# Start the agent
nexlayer agent start my-agent
```

### Manage Configuration

```bash
# Edit configuration
nexlayer config edit

# Validate configuration
nexlayer config validate

# Show current configuration
nexlayer config show
```

### Monitor and Debug

```bash
# Check project status
nexlayer status

# View logs
nexlayer logs

# Run diagnostics
nexlayer doctor
```

## Environment Variables

- `NEXLAYER_CONFIG`: Path to config file
- `NEXLAYER_LOG_LEVEL`: Log level
- `NEXLAYER_DEBUG`: Enable debug mode

## Configuration File

The configuration file (default: `~/.nexlayer/config.yaml`) supports the following structure:

```yaml
version: "1.0"
log:
  level: info
  file: ~/.nexlayer/logs/nexlayer.log
agents:
  - name: my-agent
    type: default
    config:
      # Agent-specific configuration
web:
  port: 8080
  host: localhost
```

## Best Practices

1. Always validate configuration before making changes
2. Use version control for your configuration files
3. Keep logs for debugging purposes
4. Use the doctor command to diagnose issues
5. Follow the principle of least privilege when configuring agents

## Troubleshooting

Common issues and solutions:

1. **Command not found**
   - Verify installation
   - Check PATH environment variable
   - Reinstall if necessary

2. **Configuration errors**
   - Validate configuration file
   - Check file permissions
   - Verify YAML syntax

3. **Agent issues**
   - Check agent logs
   - Verify agent configuration
   - Restart agent if necessary

For more detailed information, see our [Examples](examples.md) or [FAQ](../get-started/faq.md). 