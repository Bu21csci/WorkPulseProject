import time
import psutil
import requests
from pynput import mouse, keyboard

SERVER_URL = "http://localhost:5000/upload"  # Your Flask backend endpoint

idle_threshold = 60  # 60 seconds = 1 minute
last_input_time = time.time()

# Reset timer on user activity
def reset_timer(event=None):
    global last_input_time
    last_input_time = time.time()

# Set up listeners for mouse and keyboard
mouse.Listener(on_move=reset_timer, on_click=reset_timer).start()
keyboard.Listener(on_press=reset_timer).start()

while True:
    idle_time = time.time() - last_input_time

    # Get active app names (top 5)
    active_apps = []
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name']:
                active_apps.append(proc.info['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Prepare data
    payload = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "idle_time": idle_time,
        "active_apps": list(set(active_apps))[:5]
    }

    try:
        # Send data to Flask backend
        response = requests.post(SERVER_URL, json=payload)
        print(f"[✓] Data sent: {payload}")
    except Exception as e:
        print("[!] Failed to send data:", e)

    time.sleep(60)  # Repeat evpython activity_tracker.pyery 60 seconds
