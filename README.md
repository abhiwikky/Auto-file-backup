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

Configure the Script
Open auto_backup.py and modify:

python
Copy
Edit
SOURCE_PATHS = [
    "/path/to/your/folder",
    "/path/to/your/file.txt"
]

BACKUP_ROOT = "/path/to/your/backup/directory"
3. Test the Script
bash
Copy
Edit
python3 auto_backup.py
Check the backup folder and backup_log.txt for results.

⏰ Schedule with Cron (Linux)
Open your crontab:

bash
Copy
Edit
crontab -e
Add this line to run the script daily at 6 PM:

bash
Copy
Edit
0 18 * * * /usr/bin/python3 /path/to/auto_backup.py
Tip: Use which python3 to find your exact Python path.

📂 Example Folder Structure
Copy
Edit
Backups/
├── backup_2025-04-24_18-00-00/
│   ├── important_folder/
│   └── notes.txt
└── backup_log.txt
📋 License
This project is licensed under the MIT License.

🤝 Contributing
Feel free to open issues or submit pull requests to enhance functionality—compression, encryption, GUI, cloud storage, etc. are welcome!

👨‍💻 Author
Created by [Your Name]
📧 your.email@example.com
🌐 [LinkedIn / GitHub / Portfolio]

yaml
Copy
Edit
