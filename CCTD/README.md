# Cybersecurity Control Testing Device

This repository contains a **Cybersecurity Control Testing Device** project, designed to monitor critical system files, detect unauthorized changes, and observe key security-related events on a macOS system. The project includes monitoring SSH session activities, file integrity checks, and other important system configurations for security purposes.

## Objective

The objective of this project is to create a set of cybersecurity detection scripts that continuously monitor key files, directories, and system activities for integrity and security. By providing real-time detection of unauthorized access and modifications, the project aims to enhance system security for personal and professional macOS users.

## Project Structure

The project is organized as follows:

```bash
cybersecurity_project/
├── detectors/                          # Contains individual detection scripts
│   ├── __init__.py                     # Initializes the detectors package
│   ├── ssh_login_detector.py           # Monitors SSH session activities on macOS
│   ├── network_monitor.py              # Detects network intrusions (ARP monitoring)
│   ├── file_integrity_monitor.py       # Monitors integrity of critical system files
├── main.py                             # Main entry point to run the device and orchestrate detection
├── README.md                           # Project description, objectives, and usage
└── ssh_sessions.log                    # Logs of detected SSH sessions
