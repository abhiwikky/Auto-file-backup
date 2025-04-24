# 🗂️ Auto File Backup System

A lightweight and customizable Python script to automatically back up specified files and directories to a backup location at scheduled intervals using Cron (Linux).

---

## 🚀 Features

- 📁 Backup multiple files and directories
- 🕒 Scheduled automatic backups using Cron
- 🧾 Logging of backup status and errors
- 🧩 Easily configurable source and destination paths

---


## 🧑‍💻 Setup

### 1. Clone or Download the Script

### Configure the Script
Open auto_backup.py and modify:

SOURCE_PATHS = [
    "/path/to/your/folder",
    "/path/to/your/file.txt"
]

BACKUP_ROOT = "/path/to/your/backup/directory"


### ⏰ Schedule with Cron (Linux)
Open your crontab:

crontab -e
Add this line to run the script daily at 6 PM:

0 18 * * * /usr/bin/python3 /path/to/auto_backup.py.

📂 Example Folder Structure
Copy
Edit
Backups/
├── backup_2025-04-24_18-00-00/
│   ├── important_folder/
│   └── notes.txt
└── backup_log.txt


👨‍💻 Author
Created by Abhijith S
📧 connect.abhijiths@gmail.com



