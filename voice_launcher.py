import speech_recognition as sr
import webbrowser

apps = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "facebook": "https://www.facebook.com",
    "twitter": "https://twitter.com",
    "instagram": "https://www.instagram.com",
    "whatsapp": "https://www.whatsapp.com",
    "amazon": "https://www.amazon.com",
    "gmail": "https://mail.google.com",
    "reddit": "https://www.reddit.com",
    "linkedin": "https://www.linkedin.com",
    "netflix": "https://www.netflix.com",
    "openai": "https://www.openai.com",
    "chatgpt": "https://chat.openai.com",
    "stackoverflow": "https://stackoverflow.com",
    "spotify": "https://www.spotify.com",
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

    # Search command
    if command.startswith("search for "):
        query = command.replace("search for ", "", 1)
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return

    # Normalize spoken command
    cleaned = command.replace("open ", "").replace("go to ", "").replace("launch ", "").replace("start ", "").replace(" ", "")

    for key in apps:
        if key in cleaned or is_subsequence(key, cleaned):
            webbrowser.open(apps[key])
            return

    # Default fallback to search
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
        print(f"❌ Could not request results; {e}")

if __name__ == "__main__":
    while True:
        listen()
