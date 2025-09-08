import pandas as pd
import requests
import json
import re

# LLM-Konfiguration
url = "https://f2ki-h100-1.f2.htw-berlin.de:11435/api/chat"
model = "llama3.1:8b"

# Basis-Prompt
prompt_intro = (
    "Du bist ein Experte für Datenwissenschaft und überprüfst einen "
    "Bericht zur explorativen Datenanalyse für eine wissenschaftliche Publikation. "
    "Deine Aufgabe ist es, übergeordnete Einblicke zu liefern, Datenqualitätsprobleme "
    "zu bewerten und Richtungen für die weitere Analyse vorzuschlagen. "
    "Hier ist die Zusammenfassung aus dem ydata-profiling-Bericht für einen Patientendatensatz:"
)

# JSON-Datei laden
with open("eda_report.json", "r", encoding="utf-8") as file:
    report_data = json.load(file)

# Optional: JSON lesbarer formatieren (wenn du es als Text einfügst)
report_text = json.dumps(report_data, indent=2)

# Funktion zur Kommunikation mit dem Modell
def get_antwort(prompt_text, model, url):
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt_text}
        ],
        "stream": False
    }

    response = requests.post(url, json=payload, verify=True)

    if response.status_code != 200:
        print(f"Fehler vom Server: {response.status_code}")
        print(response.text)
        return "Fehler"

    antwort_json = response.json()
    if "message" not in antwort_json:
        print(json.dumps(antwort_json, indent=2))
        return "Ungültige API-Antwort"

    return antwort_json["message"]["content"]

# Prompt und JSON zusammenfügen
voller_prompt = f"{prompt_intro}\n\n{report_text}"

# Anfrage senden
antwort = get_antwort(voller_prompt, model, url)
print("Antwort:")
print(antwort)
