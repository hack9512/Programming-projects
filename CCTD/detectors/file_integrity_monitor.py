import os
import hashlib
import time

# List of important files and directories to monitor
MONITOR_PATHS = {
    'Documents': os.path.expanduser('~/Documents/'),
    'SSH Keys': os.path.expanduser('~/.ssh/'),
    'Keychain': os.path.expanduser('~/Library/Keychains/'),
    'System Preferences (User)': os.path.expanduser('~/Library/Preferences/'),
    'System Preferences (System)': '/Library/Preferences/',
    'Safari': os.path.expanduser('~/Library/Safari/'),
    'Chrome': os.path.expanduser('~/Library/Application Support/Google/Chrome/'),
    'Firefox': os.path.expanduser('~/Library/Application Support/Firefox/'),
    'Application Data': os.path.expanduser('~/Library/Application Support/'),
    'Startup Items (User)': os.path.expanduser('~/Library/LaunchAgents/'),
    'Startup Items (System)': '/Library/LaunchDaemons/',
    'System Binaries': ['/usr/bin/', '/usr/sbin/']
}

# Dictionary to store original file hashes
file_hashes = {}

# Function to calculate the hash of a file
def calculate_file_hash(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as file:
            buffer = file.read()
            hasher.update(buffer)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

# Function to monitor file or directory integrity
def monitor_file_or_directory(path):
    if os.path.isfile(path):
        monitor_file(path)
    elif os.path.isdir(path):
        monitor_directory(path)

# Monitor a single file
def monitor_file(file_path):
    current_hash = calculate_file_hash(file_path)
    if file_path in file_hashes:
        if current_hash != file_hashes[file_path]:
            print(f"[ALERT] File changed: {file_path}")
    else:
        file_hashes[file_path] = current_hash

# Monitor a directory
def monitor_directory(dir_path):
    for root, _, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            monitor_file(file_path)

# Main monitoring function
def monitor_paths():
    while True:
        for label, path in MONITOR_PATHS.items():
            print(f"Monitoring {label}: {path}")
            if isinstance(path, list):  # Handle system binaries
                for sub_path in path:
                    monitor_file_or_directory(sub_path)
            else:
                monitor_file_or_directory(path)
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    print("Starting file integrity monitoring...")
    monitor_paths()
