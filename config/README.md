# Configuration

This directory contains project configuration files.

Sensitive information such as API keys, passwords, tokens, and private credentials must never be committed to this repository.
## Current Module

### settings.py

Contains the initial application configuration.

Current settings include:

- Application name
- Application version
- Environment
- Debug mode

## Configuration Principle

Application configuration should be separated from application logic.

## Security

Never store the following directly in source code:

- API keys
- Passwords
- Access tokens
- Private keys
- Authentication secrets

Sensitive configuration should use environment variables or a secure secret-management system.

## Future Configuration

The configuration system may later include:

- AI model settings
- Voice settings
- Database settings
- Device settings
- Security settings
- Logging settings
- Feature flags
