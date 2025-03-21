import pyaudio
import socket

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Connect to the audio server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5001))  # Replace SERVER_IP with actual server IP

# Initialize audio player
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

print("Receiving Audio Stream...")
while True:
    data = client_socket.recv(CHUNK)
    stream.write(data)
