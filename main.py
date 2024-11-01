# Import necessary modules
import logging                     # For logging application events and errors
from monitor import SystemMonitor   # Import SystemMonitor class from the monitor module
from alarm import AlarmManager      # Import AlarmManager class from the alarm module

# Function to set up and configure the logger
def setup_logger():
    # Configure logging settings
    logging.basicConfig(
        filename='system_monitor.log',              # Specify the log file name
        level=logging.INFO,                         # Set log level to INFO to capture all info and above logs
        format='%(asctime)s - %(levelname)s - %(message)s'  # Define log format to include time, level, and message
    )
    return logging.getLogger()  # Return the configured logger instance

# Define the main menu function for user interaction with the monitoring application
def main_menu():
    # Initialize the SystemMonitor and AlarmManager instances
    monitor = SystemMonitor()
    alarm_manager = AlarmManager()

    # Main loop for user menu, runs continuously until the user chooses to exit
    while True:
        # Display the main menu options to the user
        print("\nSystem Monitoring Application")
        print("1. Start Monitoring")
        print("2. List Active Monitoring")
        print("3. Configure Alarms")
        print("4. View Alarms")
        print("5. Start Monitoring Mode")
        print("6. Remove Alarm")
        print("7. Exit")

        # Get user input for their menu choice
        choice = input("Enter your choice: ")

        # Handle user's menu choice with conditional statements
        if choice == "1":
            monitor.start_monitoring()  # Start monitoring system resources
        elif choice == "2":
            monitor.list_active_monitoring()  # List all currently active monitoring tasks
        elif choice == "3":
            alarm_manager.create_alarm()  # Allow user to configure a new alarm
        elif choice == "4":
            alarm_manager.view_alarms()  # Display all configured alarms
        elif choice == "5":
            monitor.start_monitoring_mode(alarm_manager)  # Begin monitoring with alarms enabled
        elif choice == "6":
            alarm_manager.remove_alarm()  # Remove an existing alarm
        elif choice == "7":
            # Exit the loop and end the application
            print("Exiting the application...")
            break
        else:
            # Handle invalid menu input
            print("Invalid choice. Please enter a valid option.")

# Entry point for the script execution
if __name__ == "__main__":
    # Initialize and configure the logger
    logger = setup_logger()
    logger.info("System Monitoring Application Started")  # Log the application start event
    
    # Run the main menu and handle any unexpected errors
    try:
        main_menu()  # Start the main menu loop
    except Exception as e:
        # Log any exceptions that occur, and display a message to the user
        logger.error(f"Application crashed: {e}")
        print("An error occurred. Check the log for more details.")
