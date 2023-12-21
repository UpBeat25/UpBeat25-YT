import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import requests
import pyaudio
import wave
import time
import webbrowser
import os

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location():
    ip_info = subprocess.check_output("curl ipinfo.io", shell=True, text=True).strip()
    location_info = subprocess.check_output("curl ipinfo.io/loc", shell=True, text=True).strip()
    return ip_info, location_info

def record_audio(file_path, duration=3):
    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

    frames = []

    current_time = time.time()
    end_time = time.time() + duration
    print("Recording Started!")
    while current_time <= end_time:
        data = stream.read(1024)
        frames.append(data)
        current_time = time.time()

    print("Recording Stopped!")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(file_path, "wb") as help_audio:
        help_audio.setnchannels(1)
        help_audio.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        help_audio.setframerate(44100)
        help_audio.writeframes(b''.join(frames))

def send_email(sender, password, receiver, subject, body, attachment_path):
    message = MIMEMultipart()
    message["From"] = sender
    message['To'] = receiver
    message['Subject'] = subject

    plain_text = MIMEText(body, _subtype='plain', _charset='UTF-8')
    message.attach(plain_text)

    with open(attachment_path, 'rb') as attachment:
        obj = MIMEBase('application', 'octet-stream')
        obj.set_payload(attachment.read())
        encoders.encode_base64(obj)
        obj.add_header('Content-Disposition', f"attachment; filename={os.path.basename(attachment_path)}")
        message.attach(obj)

    with smtplib.SMTP('smtp-mail.outlook.com', 587) as email_session:
        email_session.starttls()
        email_session.login(sender, password)
        email_session.sendmail(sender, receiver, message.as_string())

if __name__ == "__main__":
    guardian_email = str(input("Enter Guardian Email (put your email address):> "))

    # Record audio
    audio_file = "help.wav"
    record_audio(audio_file)

    # Get location
    ip_info, loc = get_location()
    link = f"https://www.google.com/maps/dir/{loc}"
    webbrowser.open(link)
    body = f'SOS! exact location \n {link}'

    # Send email
    send_email("guardianvoice576@outlook.com", 'dummyaccount_password124', guardian_email, "Help! `Test Account` is in trouble.", body, audio_file)
    print("Location sent!")
