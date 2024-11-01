# Import required modules
import json   # For handling JSON data (used to save and load alarms)
import os     # For file and operating system interactions

# Define the AlarmManager class to handle creating, viewing, saving, loading, and checking alarms
class AlarmManager:
    
    # Initialize the AlarmManager instance and load existing alarms from a file
    def __init__(self):
        self.alarms = self.load_alarms()  # Load saved alarms on initialization

    # Load alarms from a JSON file (alarms.json) if it exists
    def load_alarms(self):
        try:
            # Check if the alarms file exists
            if os.path.exists('alarms.json'):
                with open('alarms.json', 'r') as file:
                    return json.load(file)  # Load and return alarms as a list of dictionaries
            return []  # Return an empty list if no alarms file exists
        except json.JSONDecodeError:
            # Handle JSON decoding errors (if the file is corrupted)
            print("Error: Alarms file is corrupted. Resetting alarms.")
            return []
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred while loading alarms: {e}")
            return []

    # Save the current list of alarms to the alarms.json file
    def save_alarms(self):
        try:
            # Write the list of alarms to alarms.json in JSON format
            with open('alarms.json', 'w') as file:
                json.dump(self.alarms, file)
        except Exception as e:
            # Handle errors that may occur during saving
            print(f"Error saving alarms: {e}")

    # Create a new alarm with user-specified type and threshold level
    def create_alarm(self):
        # Display options for the type of alarm
        print("Configure alarms:")
        print("1. CPU Usage")
        print("2. Memory Usage")
        print("3. Disk Usage")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")

        # Validate and handle user's choice
        if choice in ["1", "2", "3"]:
            alarm_type = ["CPU Usage", "Memory Usage", "Disk Usage"][int(choice) - 1]  # Map choice to alarm type
            level = input("Set alarm level (0-100): ")
            try:
                # Validate that level is an integer between 0 and 100
                level = int(level)
                if 0 <= level <= 100:
                    # Add the new alarm to the list and save it
                    self.alarms.append({'type': alarm_type, 'level': level})
                    self.save_alarms()  # Save alarms to file
                    print(f"Alarm for {alarm_type} set to {level}%.")
                else:
                    print("Invalid level. Please enter a number between 0-100.")
            except ValueError:
                # Handle invalid input if level is not an integer
                print("Invalid input. Please enter a valid integer.")
        elif choice == "4":
            # Exit if the user chooses to go back to the main menu
            return
        else:
            print("Invalid choice.")

    # Display all configured alarms to the user
    def view_alarms(self):
        if not self.alarms:
            # If no alarms are configured, notify the user
            print("No alarms configured.")
        else:
            # Display a sorted list of alarms by type
            print("Configured Alarms:")
            for alarm in sorted(self.alarms, key=lambda x: x['type']):
                print(f"{alarm['type']} Alarm: {alarm['level']}%")
        input("Press any key to return to main menu.")

    # Remove an existing alarm based on user selection
    def remove_alarm(self):
        if not self.alarms:
            # If no alarms are configured, notify the user
            print("No alarms configured.")
            return

        # List all alarms for the user to select one to remove
        print("Configured Alarms:")
        for i, alarm in enumerate(self.alarms):
            print(f"{i + 1}. {alarm['type']} Alarm: {alarm['level']}%")

        choice = input("Select an alarm to remove (enter the number): ")
        try:
            # Validate the user's choice and remove the selected alarm
            if choice.isdigit() and 1 <= int(choice) <= len(self.alarms):
                removed_alarm = self.alarms.pop(int(choice) - 1)  # Remove selected alarm
                self.save_alarms()  # Save updated list to file
                print(f"Removed {removed_alarm['type']} alarm.")
            else:
                print("Invalid selection.")
        except Exception as e:
            # Handle errors that may occur during removal
            print(f"Error removing alarm: {e}")

    # Check current system usage against alarms and notify if any threshold is exceeded
    def check_alarms(self, cpu_usage, memory_usage, disk_usage):
        # Iterate through each alarm and check if the threshold is exceeded
        for alarm in self.alarms:
            if alarm['type'] == "CPU Usage" and cpu_usage > alarm['level']:
                print(f"***WARNING: CPU usage exceeds {alarm['level']}%***")
                return True
            elif alarm['type'] == "Memory Usage" and memory_usage > alarm['level']:
                print(f"***WARNING: Memory usage exceeds {alarm['level']}%***")
                return True
            elif alarm['type'] == "Disk Usage" and disk_usage > alarm['level']:
                print(f"***WARNING: Disk usage exceeds {alarm['level']}%***")
                return True
        return False  # Return False if no alarm threshold is exceeded
