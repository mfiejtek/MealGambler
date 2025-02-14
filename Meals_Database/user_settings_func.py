import json, sys, os



# Database path
# Prawidłowa ścieżka do bazy danych w przypadku uruchomienia z pliku .exe
if getattr(sys, 'frozen', False):  # Gdy uruchamiane z pliku exe
    BASE_DIR = os.path.dirname(sys.executable)  # Katalog, w którym znajduje się plik exe
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Katalog w przypadku uruchamiania z pliku .py
SETTINGS_PATH = os.path.join(BASE_DIR, "settings.json")  # Full database path

def load_settings():
    try:
        with open(SETTINGS_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_settings(settings):
    with open(SETTINGS_PATH, "w") as file:
        json.dump(settings, file, indent = 4)

