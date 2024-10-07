# Cybersecurity Control Testing Device

This repository contains a **Cybersecurity Control Testing Device** project, designed to monitor critical system files, detect unauthorized changes, and observe key security-related events on a macOS system. The project includes monitoring SSH session activities, file integrity checks, and other important system configurations for security purposes.

## Objective

The objective of this project is to create a set of cybersecurity detection scripts that continuously monitor key files, directories, and system activities for integrity and security. By providing real-time detection of unauthorized access and modifications, the project aims to enhance system security for personal and **professional macOS** users.

## Features

The project is divided into three major components, each focusing on a specific area of cybersecurity monitoring:

### 1. SSH Session Monitoring

The **SSH session monitoring** feature is responsible for tracking SSH login events on macOS by reading system logs from `/var/log/system.log`. It detects when an SSH session starts and logs relevant details, such as the username and timestamp.

#### Key Points:
- **Log Source**: `/var/log/system.log`
- **Detected Events**: SSH session starts (`USER_PROCESS`)
- **Logging**: All detected sessions are logged to `ssh_sessions.log`

#### File: `ssh_login_detector.py`
This file contains the logic to monitor SSH session activity. It continuously scans the system log for any SSH session initiation and outputs the session details both to the console and the log file.

2. File Integrity Monitoring

The File Integrity Monitoring feature ensures that critical system files and directories are not tampered with. It uses hashing (SHA-256) to create a digital fingerprint of each monitored file and continuously checks for any changes. If a file is modified, the system will raise an alert.

Key Points:

	•	Files/Directories Monitored:
	•	~/Documents/
	•	~/.ssh/
	•	~/Library/Keychains/
	•	/Library/Preferences/
	•	/usr/bin/ and /usr/sbin/ (System binaries)
	•	Method: SHA-256 hashing for file integrity checks.
	•	Alerts: Detects unauthorized modifications to monitored files and directories.

File: file_integrity_monitor.py

![Screenshot 2024-10-07 at 06 37 22](https://github.com/user-attachments/assets/f54bbd6b-e0d3-4f82-8514-cbe143dbb799)

3. Network Intrusion Detection (ARP Monitoring)

The Network Intrusion Detection feature uses the Python library scapy to sniff ARP packets on the local network. It looks for suspicious activities like ARP spoofing, which can indicate man-in-the-middle (MITM) attacks.

Key Points:

	•	Detection Method: ARP packet sniffing using scapy.
	•	Detected Events: ARP requests and responses.
	•	Use Case: Detects potential ARP spoofing attacks and alerts the user.

File: network_monitor.py

![Screenshot 2024-10-07 at 06 40 24](https://github.com/user-attachments/assets/d77052b5-a858-401c-9ecc-37530b84170e)


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



