import speech_recognition as sr
import webbrowser
import os
import pyautogui

web_apps = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "facebook": "https://www.facebook.com",
    "twitter": "https://twitter.com",
    "instagram": "https://www.instagram.com",
    "whatsapp": "https://web.whatsapp.com",
    "amazon": "https://www.amazon.com",
    "gmail": "https://mail.google.com",
    "reddit": "https://www.reddit.com",
    "linkedin": "https://www.linkedin.com",
    "netflix": "https://www.netflix.com",
    "openai": "https://www.openai.com",
    "chatgpt": "https://chat.openai.com",
    "stackoverflow": "https://stackoverflow.com",
    "spotify": "https://www.spotify.com",
    "meet": "https://meet.google.com/new",
    "googlemeet": "https://meet.google.com/new"
}

desktop_apps = {
    "zoom": r"C:\Users\Amanah Mall\AppData\Roaming\Zoom\bin\Zoom.exe",
    "anydesk": r"C:\Program Files (x86)\AnyDesk\AnyDesk.exe",
    "vs code": r"C:\Users\Amanah Mall\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "vscode": r"C:\Users\Amanah Mall\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "cmd": "cmd.exe"
}

folder_shortcuts = {
    "downloads": r"C:\Users\Amanah Mall\Downloads",
    "documents": r"C:\Users\Amanah Mall\Documents",
    "desktop": r"C:\Users\Amanah Mall\Desktop",
    "pictures": r"C:\Users\Amanah Mall\Pictures",
    "music": r"C:\Users\Amanah Mall\Music",
    "videos": r"C:\Users\Amanah Mall\Videos"
}

def is_subsequence(pattern, text):
    i = j = 0
    while i < len(pattern) and j < len(text):
        if pattern[i] == text[j]:
            i += 1
        j += 1
    return i == len(pattern)

def handle_command(command):
    command = command.lower().strip()

    # FOLDER NAVIGATION
    for folder_name in folder_shortcuts:
        if folder_name in command and any(word in command for word in ["open", "go to", "navigate to"]):
            print(f"📁 Opening {folder_name}...")
            os.startfile(folder_shortcuts[folder_name])
            return

    if "developer panel" in command:
        folder_path = r"C:\Users\Amanah Mall\Desktop\Komail Meptics"
        print(f"📁 Opening folder: {folder_path}")
        os.startfile(folder_path)
        return

    # WINDOW MANAGEMENT
    if "minimize all" in command or "show desktop" in command:
        print("🗔 Minimizing all windows...")
        pyautogui.hotkey('win', 'd')
        return

    if "stack windows" in command or "snap windows up" in command:
        print("🗔 Stacking windows upward...")
        pyautogui.hotkey('win', 'up')
        return

    if "snap left" in command:
        print("🗔 Snapping window left...")
        pyautogui.hotkey('win', 'left')
        return

    if "snap right" in command:
        print("🗔 Snapping window right...")
        pyautogui.hotkey('win', 'right')
        return

    if "maximize window" in command:
        print("🗔 Maximizing window...")
        pyautogui.hotkey('win', 'up')
        return

    if "minimize window" in command:
        print("🗔 Minimizing window...")
        pyautogui.hotkey('win', 'down')
        return

    if any(phrase in command for phrase in ["start meeting", "new meeting", "google meet", "start google meet"]):
        print("🔗 Opening Google Meet...")
        webbrowser.open("https://meet.google.com/new")
        return

    if command.startswith("search for "):
        query = command.replace("search for ", "", 1)
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return

    cleaned = command.replace("open ", "").replace("go to ", "").replace("launch ", "").replace("search for", "").replace("start ", "").replace(" ", "")

    for key in desktop_apps:
        if key.replace(" ", "") in cleaned or is_subsequence(key.replace(" ", ""), cleaned):
            print(f"🖥️ Launching {key}...")
            try:
                os.startfile(desktop_apps[key])
            except FileNotFoundError:
                print(f"❌ Could not find {key}. Check the path.")
            except Exception as e:
                print(f"❌ Failed to launch {key}: {e}")
            return

    for key in web_apps:
        if key in cleaned or is_subsequence(key, cleaned):
            print(f"🔗 Opening {key}...")
            webbrowser.open(web_apps[key])
            return

    print(f"🔍 Searching for: {command}")
    webbrowser.open(f"https://www.google.com/search?q={command}")

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎤 Listening... Speak now:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"✅ Heard: {command}")
        handle_command(command)
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
    except sr.RequestError as e:
        print(f"❌ Request error: {e}")

if __name__ == "__main__":
    while True:
        listen()
