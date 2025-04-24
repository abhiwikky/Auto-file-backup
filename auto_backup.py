import os
import shutil
import datetime
import logging

# Configuration
SOURCE_PATHS = [
    "/home/yourusername/Documents/important_folder",
    "/home/yourusername/Desktop/notes.txt"
]
BACKUP_ROOT = "/home/yourusername/Backups"

# Setup logging
LOG_FILE = os.path.join(BACKUP_ROOT, "backup_log.txt")
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

def backup():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = os.path.join(BACKUP_ROOT, f"backup_{timestamp}")
    
    try:
        os.makedirs(backup_folder, exist_ok=True)
        for path in SOURCE_PATHS:
            if os.path.exists(path):
                if os.path.isdir(path):
                    shutil.copytree(path, os.path.join(backup_folder, os.path.basename(path)))
                else:
                    shutil.copy2(path, backup_folder)
            else:
                logging.warning(f"Path not found: {path}")
        logging.info(f"Backup completed successfully at {backup_folder}")
    except Exception as e:
        logging.error(f"Backup failed: {e}")

if __name__ == "__main__":
    backup()
