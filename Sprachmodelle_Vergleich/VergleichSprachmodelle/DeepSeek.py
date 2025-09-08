import pandas as pd
import requests
import json
import re

# Datensatz
df = pd.read_csv("2024-12-31-prices.csv")

# LLM-Konfiguration
url = "https://f2ki-h100-1.f2.htw-berlin.de:11435/api/chat"
model = "deepseek-r1:8b"

fragen = [
    "Was ist der Maximalwert in Spalte 'e5'?",
    "Wie viele Spalten in 'dieselchange' haben den Wert 1?",
    "Beschreibe kurz die wichtigsten Merkmale in dem Datensatz.",
    "Bitte gib mir für die folgenden Aufgaben den entsprechenden Python-Code, damit sie gelöst werden können. Ausgabe der ersten 20 Zeilen.",
    "Bitte gib mir für die folgenden Aufgaben den entsprechenden Python-Code, damit sie gelöst werden können. Erstellen eines Boxplots für die Spalte 'e10'."
]
kontext = ("Ich bin Datenanalystin in einem Unternehmen und möchte mehr über meine "
           "Daten erfahren. Im Folgenden stelle ich die Daten zur Verfügung und stelle "
           "anschließend Fragen dazu. Beantworte die Fragen bitte so konkret wie "
           "möglich und gehe dabei auf die bereitgestellten Daten ein. Denke dir "
           "keine weiteren Inhalte aus.")

# Fragen und Kontext werden von dem Modell verarbeitet und beantwortet
# Input: Fragen (List), Kontext, Modell, HTW-URL
# Output: Antwort (Modellantwort - unbearbeitet), Code (Antwort des Modells, gekürzt auf die Codefragmente)
def get_antwort(frage, kontext, model, url):
    print(f" Frage: {frage}")
    prompt = f""" {kontext}{frage}"""
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    response = requests.post(url, json=payload, verify=True)
    # Fehleridentifizierung
    if response.status_code != 200:
        print(f"Fehler vom Server: {response.status_code}")
        print(response.text)
        return "Fehler", ""

    antwort_json = response.json()

    # Fehlerprüfung
    if "message" not in antwort_json:
        print(json.dumps(antwort_json, indent=2))
        return "Ungültige API-Antwort", ""

    antwort = antwort_json["message"]["content"]

    code = antwort[11:].strip("`")
    code = code[:-1]
    return antwort, code

def get_code(antwort):
    match = re.search(r"```(?:python)?(.*?)```", antwort, re.DOTALL)
    if match:
        code = match.group(1).strip()
        text = antwort[:match.start()].strip()
    else:
        code = ""
        text = antwort.strip()
    return text, code

# Ausgabe der Antworten je Frage
for frage in fragen:
    antwort, code = get_antwort(frage, kontext, model, url)
    print(f" Antwort: {antwort}")
    text, code = get_code(antwort)
    try:
        print(exec(code))
    except Exception as e:
        print("Fehler beim Ausführen des Codes:")
        print(e)


