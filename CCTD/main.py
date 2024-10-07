# Import the ssh_login_detector sub-module
from detectors import ssh_login_detector
from detectors import network_monitor
from detectors import file_intergrity_monitor

# Main function to orchestrate the control tests
def main():
    print("Cybersecurity Control Testing Device is running...")

    # Call the SSH login attempt detection function
    print("Starting SSH login attempt detection...")
    ssh_login_detector.detect_ssh_sessions()

    # You can later add calls to other functions like:
    network_monitor.detect_network_intrusions()
    file_integrity_monitor.check_file_integrity('/var/log')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Shutting down the Cybersecurity Control Testing Device.")
