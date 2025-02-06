#####################################
# Import Modules
#####################################

import json
import os
import sys
import time
import pathlib
import datetime
from collections import deque

import matplotlib.pyplot as plt

from utils.utils_logger import logger

#####################################
# Set up Paths - read from the file the producer writes
#####################################

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
DATA_FOLDER = PROJECT_ROOT.joinpath("data")
DATA_FILE = DATA_FOLDER.joinpath("project_live.json")

logger.info(f"Project root: {PROJECT_ROOT}")
logger.info(f"Data folder: {DATA_FOLDER}")
logger.info(f"Data file: {DATA_FILE}")

#####################################
# Set up data structures for tracking sentiment
#####################################

time_window = 100  # Maximum number of messages to keep in memory
timestamps = deque(maxlen=time_window)  # Stores timestamps
sentiments = deque(maxlen=time_window)  # Stores sentiment scores

#####################################
# Set up live visuals
#####################################

plt.ion()  # Turn on interactive mode for live updates
fig, ax = plt.subplots()
ax.set_xlabel("Timestamp")
ax.set_ylabel("Sentiment Score")
ax.set_ylim(-1, 1)  # Sentiment values range from -1 to 1
ax.set_title("Real-Time Sentiment Over Time - Josiah Randleman")

#####################################
# Define an update chart function for live plotting
#####################################

def update_chart():
    """Update the live chart with the latest sentiment values."""
    ax.clear()
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Sentiment Score")
    ax.set_ylim(-1, 1)
    ax.set_title("Real-Time Sentiment Over Time - Josiah Randleman")

    if timestamps:
        # Sort timestamps to ensure correct order
        sorted_data = sorted(zip(timestamps, sentiments))
        sorted_timestamps, sorted_sentiments = zip(*sorted_data)

        ax.plot(sorted_timestamps, sorted_sentiments, 'r-', lw=2)

        # Improve x-axis readability
        plt.xticks(rotation=45, ha="right")

    plt.draw()
    plt.pause(0.01)  # Pause briefly to allow for live updates

#####################################
# Process Message Function
#####################################

def process_message(message: str) -> None:
    """
    Process a single JSON message and update the sentiment chart.

    Args:
        message (str): The JSON message as a string.
    """
    try:
        logger.debug(f"Raw message: {message}")
        message_dict: dict = json.loads(message)

        logger.info(f"Processed JSON message: {message_dict}")

        # Extract sentiment and timestamp
        sentiment = float(message_dict.get("sentiment", 0))  # Default to 0 if missing
        timestamp = datetime.datetime.strptime(message_dict["timestamp"], "%Y-%m-%d %H:%M:%S")

        # Append new data to rolling window
        timestamps.append(timestamp)
        sentiments.append(sentiment)

        logger.info(f"Updated Sentiment Values: {list(sentiments)}")

        # Update the chart live
        update_chart()

    except json.JSONDecodeError:
        logger.error(f"Invalid JSON message: {message}")
    except Exception as e:
        logger.error(f"Error processing message: {e}")

#####################################
# Main Function
#####################################

def main() -> None:
    """
    Main entry point for the consumer.
    - Monitors a file for new messages and updates a live chart.
    """

    logger.info("START consumer.")

    # Verify the file exists, if not, exit early
    if not DATA_FILE.exists():
        logger.error(f"Data file {DATA_FILE} does not exist. Exiting.")
        sys.exit(1)

    try:
        # Try to open the file and read from it
        with open(DATA_FILE, "r") as file:
            file.seek(0, os.SEEK_END)
            print("Consumer is ready and waiting for new JSON messages...")

            while True:
                line = file.readline()
                if line.strip():
                    process_message(line)
                else:
                    logger.debug("No new messages. Waiting...")
                    time.sleep(0.5)
                    continue

    except KeyboardInterrupt:
        logger.info("Consumer interrupted by user.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        plt.ioff()
        plt.show()
        logger.info("Consumer closed.")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()
