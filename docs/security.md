# Security Policy

## Purpose

Security is a core requirement of the Personal AI project.

The system is designed to give the owner control over AI capabilities, personal data, connected devices, memory, and automation.

## Core Security Principles

- Owner-controlled access
- Least privilege
- Explicit permissions
- Secure authentication
- Protected secrets
- Privacy-first design
- Secure device connections
- Safe execution
- Transparent error reporting
- Security logging

## Sensitive Operations

Sensitive operations must not automatically execute without the required permission.

Examples include:

- Shutdown
- Restart
- File deletion
- Software installation
- Important system changes
- Sending communications
- Accessing private data
- Device control

Depending on the configured permission level, the AI may require confirmation before execution.

## Secrets

The following must never be hard-coded into source files:

- API keys
- Passwords
- Access tokens
- Private keys
- Authentication secrets

Secrets should use environment variables or appropriate secure storage.

## Personal Data

Personal information should only be stored when required and authorized.

The owner should be able to:

- View stored information
- Modify stored information
- Delete stored information
- Disable memory
- Revoke access

## Device Security

Connected devices must have explicit authorization.

Removing device authorization should immediately prevent the AI from using that device.

## Logging

Security-relevant events should be logged when appropriate.

Examples:

- Login
- Permission changes
- Device connections
- Sensitive actions
- Failed actions
- Security events

Logs must not unnecessarily expose passwords, tokens, or other secrets.

## Safe Failure

The AI must never falsely claim that an operation was completed.

If an operation fails, the system should clearly report the failure.

## Owner Control

The owner has final control over:

- Skills
- Permissions
- Memory
- Devices
- Automations
- AI configuration
- Security settings

## Security Goal

Build a powerful Personal AI without giving the AI unnecessary or uncontrolled access.
