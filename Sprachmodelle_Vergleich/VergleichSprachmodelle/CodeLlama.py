import pandas as pd
import requests
import json
import re

# Datensatz
df = pd.read_csv("2024-12-31-prices.csv")

# LLM-Konfiguration
url = "https://f2ki-h100-1.f2.htw-berlin.de:11435/api/chat"
model = "codellama:7b"

fragen = [
    "Was ist der Maximalwert in Spalte 'e5'?",
    "Wie viele Spalten in 'dieselchange' haben den Wert 1?",
    "Beschreibe kurz die wichtigsten Merkmale in dem Datensatz.",
    "Bitte gib mir für die folgenden Aufgaben den entsprechenden Python-Code, damit sie gelöst werden können. Ausgabe der ersten 20 Zeilen.",
    "Bitte gib mir für die folgenden Aufgaben den entsprechenden Python-Code, damit sie gelöst werden können. Erstellen eines Boxplots für die Spalte 'e10'."
]
kontext = f"""Ich bin Datenanalystin in einem Unternehmen und möchte mehr über meine Daten erfahren. 
Die Pandas DataFrame heißt 'df'. Bitte gib mir nur den reinen Python-Code (ohne Erklärungen, ohne 
Kommentare, ohne Markdown-Formatierung), um folgende Frage zu beantworten – mit print-Ausgabe, falls nötig: """

# Funktion: Fragen und Kontext werden von dem Modell verarbeitet und beantwortet
# Input: Fragen (List), Kontext, Modell, HTW-URL
# Output: Antwort (Modellantwort - unbearbeitet), Code (Antwort des Modells, gekürzt auf die Codefragmente)
# Quellen: https://requests.readthedocs.io/en/latest/user/quickstart, https://docs.python.org/3/library/json.html
def get_antwort(frage, kontext, model, url):
    print(f"Frage: {frage}")
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
    return antwort

# Funktion: Extrahieren des Codes aus der Antwort
# Input: Antwort
# Output: Code
# Quellen: https://docs.python.org/3/library/re.htmld
def get_code(antwort):
    match = re.search(r"```(?:python)?(.*?)```", antwort, re.DOTALL)
    if match:
        code = match.group(1).strip()
    else:
        code = antwort
    return code

# Funktion: Ausgabe des Codes
# Input: Code
# Output: Code-Ausgabe in der Konsole
# Quellen: https://docs.python.org/3/library/functions.html
def run_code(code):
    code = format_multiline_prints_for_eval(code)
    try:
        result = eval(code)
        if result is not None:
            print("Eval:")
            print(result)
    except Exception:
        try:
            print("Exec:")
            exec(code)
        except Exception as e:
            print("Fehler beim Ausführen des Codes:")
            print(e)

# Funktion: Formattieren des Codes, bei mehrzeiliger Ausgabe (Sonst Zeilenumbruch, der nicht ausgeführt werden kann)
# Input: Code
# Output: Code
# Quellen: https://docs.python.org/3/library/stdtypes.html
def format_multiline_prints_for_eval(code):
    lines = code.strip().splitlines()
    lines = [line.strip() for line in lines if line.strip()]
    if all(line.startswith("print(") for line in lines):
        return ", ".join(lines)
    return code

# Ausgabe der Antworten je Frage
for frage in fragen:
    antwort = get_antwort(frage, kontext, model, url)
    print(f"Antwort: {antwort}")
    code = get_code(antwort)
    run_code(code)