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


guardian_email = str(input("Enter Guardian Email (put your email address):> "))

# Audio
audio = pyaudio.PyAudio()

stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

frames = []

current_time = time.time()
end_time = time.time() + 3
print("Recording Started!")
while current_time <= end_time:
    data = stream.read(1024)
    frames.append(data)
    current_time = time.time()

print("Recording Stopped!")

stream.stop_stream()
stream.close()
audio.terminate()

help_audio = wave.open("help.wav", "wb")
help_audio.setnchannels(1)
help_audio.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
help_audio.setframerate(44100)
help_audio.writeframes(b''.join(frames))
help_audio.close()


# IP
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


# Location

def get_location():
    # Get IP information
    ip_info = subprocess.check_output("curl ipinfo.io", shell=True, text=True).strip()

    # Get location information
    location_info = subprocess.check_output("curl ipinfo.io/loc", shell=True, text=True).strip()

    return ip_info, location_info
    pass


location = get_location()
dat, loc = location
link = F"https://www.google.com/maps/dir/{loc}"
webbrowser.open(link)
body = F'SOS! exact location \n {link}'


def send(sender, password, receiver, subject):
    plain_text = MIMEText(body, _subtype='plain', _charset='UTF-8')
    message = MIMEMultipart()
    message["From"] = sender
    message['To'] = receiver
    message['Subject'] = subject
    file = "help.wav"
    attachment = open(file, 'rb')
    obj = MIMEBase('application', 'octet-stream')
    obj.set_payload(attachment.read())
    encoders.encode_base64(obj)
    obj.add_header('Content-Disposition', "attachment; filename= "+file)
    message.attach(obj)
    message.attach(plain_text)
    my_message = message.as_string()
    email_session = smtplib.SMTP('smtp-mail.outlook.com', 587)
    email_session.starttls()
    email_session.login(sender, password)
    email_session.sendmail(sender, receiver, my_message)
    email_session.quit()


send("guardianvoice576@outlook.com", 'your_password', guardian_email, F"Help! `Test Account` is in trouble.")
print("Location sent!")
