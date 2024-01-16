"""
This module defines the Logger class for configuring logging in the admin_metro application.
It sets up a logger with a file handler and a console handler, allowing logging to both a file
('admin_metro.log') and the console. The log messages include timestamps, log levels, and messages.
"""
import logging


class Logger:
    """Class for configuring logging in the admin_metro application."""

    def __init__(self):
        """Initialize the Logger instance."""
        # Configure logging
        self.logger = logging.getLogger("admin_metro")
        self.logger.setLevel(logging.INFO)

        # Create file handler and set formatter
        file_handler = logging.FileHandler('admin_metro.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Create console handler and set formatter
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
