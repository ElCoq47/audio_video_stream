import pyaudio
import socket

CHUNK = 1024  # Audio buffer size
FORMAT = pyaudio.paInt16  # 16-bit format
CHANNELS = 1  # Mono audio
RATE = 44100  # Sample rate

# Create a socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 5001))
server_socket.listen(1)
print("Waiting for connection...")
conn, addr = server_socket.accept()
print(f"Connected to {addr}")

# Initialize audio stream
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("Streaming Audio...")
while True:
    data = stream.read(CHUNK)
    conn.sendall(data)
