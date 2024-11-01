# Import necessary modules
import psutil  # For accessing system information (CPU, memory, and disk usage)
import time    # For adding delays in monitoring processes

# Define the SystemMonitor class to handle monitoring system resources
class SystemMonitor:
    
    # Initialize the SystemMonitor instance
    def __init__(self):
        self.monitoring_active = False  # Flag to track if monitoring is active

    # Start monitoring process
    def start_monitoring(self):
        # Display message and activate monitoring
        print("Starting monitoring of CPU, Memory, and Disk usage.")
        self.monitoring_active = True
        # Simulate the start of monitoring with a delay
        time.sleep(2)

    # List current CPU, memory, and disk usage if monitoring is active
    def list_active_monitoring(self):
        # Check if monitoring is active
        if not self.monitoring_active:
            print("No active monitoring.")  # Notify if monitoring is not active
        else:
            # Get and display CPU usage
            print("CPU Usage: {:.2f}%".format(psutil.cpu_percent()))
            
            # Get memory information and display usage
            memory_info = psutil.virtual_memory()
            print(f"Memory Usage: {memory_info.percent}% ({memory_info.used / (1024 ** 3):.2f} GB used out of {memory_info.total / (1024 ** 3):.2f} GB)")
            
            # Get disk information and display usage
            disk_info = psutil.disk_usage('/')
            print(f"Disk Usage: {disk_info.percent}% ({disk_info.used / (1024 ** 3):.2f} GB used out of {disk_info.total / (1024 ** 3):.2f} GB)")

    # Start continuous monitoring with alarm checks
    def start_monitoring_mode(self, alarm_manager):
        # Display message and start monitoring loop
        print("Monitoring mode started. Press any key to return to main menu.")
        try:
            # Continuous loop to check system usage
            while True:
                print("Monitoring in progress...")
                
                # Get current CPU, memory, and disk usage
                cpu_usage = psutil.cpu_percent()
                memory_info = psutil.virtual_memory()
                disk_info = psutil.disk_usage('/')

                # Check if any alarms are triggered based on usage levels
                if alarm_manager.check_alarms(cpu_usage, memory_info.percent, disk_info.percent):
                    print("***WARNING: An alarm has been triggered!***")  # Notify if alarm triggered

                # Delay to prevent constant checking
                time.sleep(2)

        # Handle keyboard interrupt to exit monitoring mode gracefully
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")
