# Import the logging module to enable logging functionality
import logging

# Function to set up and configure the logger
def setup_logger(log_file):
    # Configure basic settings for logging
    logging.basicConfig(
        filename=log_file,               # Set the file where logs will be saved
        level=logging.INFO,               # Set the logging level to INFO (only logs INFO and higher levels)
        format='%(asctime)s - %(levelname)s - %(message)s',  # Format for log messages: timestamp, level, and message
    )
    # Return the configured logger instance
    return logging.getLogger()
