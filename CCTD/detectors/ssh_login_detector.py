import os
import re
import time

# Define the log file to monitor (macOS uses system.log for SSH events)
log_file_path = "/var/log/system.log"

# Define a pattern to detect user processes (SSHD session start)
# We match against 'USER_PROCESS' entries in the log.
ssh_session_pattern = re.compile(r"sshd-session: (\S+) .* USER_PROCESS:")

# Store detected SSH login attempts in this file
output_file = "ssh_sessions.log"

# Function to monitor log file and detect SSH session events
def detect_ssh_sessions():
    with open(log_file_path, 'r') as log_file:
        # Seek to the end of the file to read only new log entries
        log_file.seek(0, os.SEEK_END)

        while True:
            line = log_file.readline()
            if not line:
                # No new line, wait for a while and then check again
                time.sleep(1)
                continue

            # Look for SSH session patterns
            match = ssh_session_pattern.search(line)
            if match:
                user = match.group(1)
                log_ssh_session(user)

# Function to log detected SSH sessions
def log_ssh_session(user):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    alert_message = f"[{timestamp}] SSH session started for user '{user}'"
    
    print(alert_message)  # Output to console for real-time monitoring
    
    # Append to a log file
    with open(output_file, 'a') as output:
        output.write(alert_message + '\n')

if __name__ == "__main__":
    try:
        print(f"Monitoring {log_file_path} for SSH session events...")
        detect_ssh_sessions()
    except KeyboardInterrupt:
        print("Stopping the monitoring script.")
    except FileNotFoundError:
        print(f"Log file not found: {log_file_path}")
    except PermissionError:
        print(f"Permission denied. Please run the script with proper privileges to access {log_file_path}.")
