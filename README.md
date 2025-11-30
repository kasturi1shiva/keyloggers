Basic Keylogger (Python) — Educational Use Only

This project is a simple Python keylogger created strictly for learning and educational purposes.
It demonstrates how keyboard events can be captured using Python’s pynput library and how logs can be stored and optionally emailed using SMTP.

⚠️ Disclaimer:
This project is intended ONLY for personal learning, research, and cybersecurity education.
Do NOT use this code for any unauthorized monitoring or malicious activity.
The author is not responsible for any misuse.

✨ Features

Captures all keystrokes entered on the keyboard

Stores logs in a keylogger.txt file

Sends logged keystrokes to an email via Gmail SMTP

Stops logging when the ESC key is pressed

Works in the background while you type

📌 Requirements

Install required Python modules:

pip install pynput


The following modules come pre-installed with Python:

smtplib

ssl

⚙️ How It Works

The program listens for keyboard events using pynput

Every key pressed is written to a local file

When the logger stops (ESC pressed), the contents of the file are appended to an email message

The script sends the keystroke log to the configured email

Gmail SMTP is used for sending emails, so 2FA must be disabled, or an app password must be used.

▶️ How to Run

Run the script from your terminal:

python keylogger.py


Press ESC anytime to stop the keylogger.

📝 Configuration

Edit the following fields in the script:

sender_mail = "your_email@gmail.com"
receiver_mail = "your_email@gmail.com"
password = "your_password"


You may use the same email for both sending and receiving.

📁 File Output

All keystrokes will be saved to:

keylogger.txt


This includes characters, enter, tab, backspace events, and special keys.

🛡️ Ethical Use Notice

This project is meant only for:

Security research

Understanding how keylogging works

Personal learning

Classroom or controlled-lab environments

Do not use this software to monitor anyone without clear permission.

📜 License

This project is open-source and free to use for educational purposes under the MIT License.
