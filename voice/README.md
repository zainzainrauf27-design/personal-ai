# Voice System

The Voice System allows the user to communicate with the Personal AI through speech.

## Responsibilities

- Capture microphone input
- Detect speech
- Convert speech to text
- Send commands to the AI Core
- Convert AI responses to speech
- Manage listening state
- Manage processing state
- Manage speaking state

## Voice Flow

Microphone
→ Speech Recognition
→ Text
→ AI Core
→ Response
→ Text-to-Speech
→ Speaker

## Future Capabilities

- Wake-word detection
- Continuous conversation
- Voice interruption
- Multiple language support
- Voice settings
- Voice activity detection
- Noise handling
- Configurable speech rate
- Configurable voice

## Security

Microphone access must require appropriate device permission.

The system should clearly indicate when it is actively listening.
## Current Module

### voice_system.py

Contains the initial `VoiceSystem` class.

Current responsibilities:

- Maintain listening state
- Start listening state
- Stop listening state
- Provide the interface for future speech processing

## Future Voice Pipeline

Microphone
→ Speech Detection
→ Speech-to-Text
→ AI Core
→ Response
→ Text-to-Speech
→ Speaker

## Future Capabilities

The Voice System may later support:

- Wake word
- Continuous conversation
- Multiple languages
- Voice activity detection
- Noise handling
- Interruptible responses
- Configurable voice settings
