from pandasai.llm.base import LLM
import requests

class HTWOllamaLLM(LLM):
    def __init__(self, model: str = "mistral:latest"):
        self.model = model
        self.api_url = "https://f2ki-h100-1.f2.htw-berlin.de:11435/api/chat"

    def call(self, instruction: str, context: dict = None) -> str:
        messages = [{"role": "user", "content": instruction}]
        return self.chat(messages)

    def chat(self, messages: list[dict]) -> str:
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False
        }
        response = requests.post(self.api_url, json=payload, verify=True)
        return response.json()["message"]["content"]

    @property
    def type(self) -> str:
        return "ollama-htw"


import pandas as pd
from pandasai import SmartDataframe

# CSV laden
df_31122024 = pd.read_csv("../VergleichSprachmodelle/2024-12-31-prices.csv")
print(df_31122024.head())

# HTW Ollama LLM verwenden
llm = HTWOllamaLLM(model="mistral:latest")
df = SmartDataframe(df_31122024, config={"llm": llm})

# Konversation mit dem Modell
print(df.chat("Ich bin Datenanalystin in einem Unternehmen und möchte mehr über meine Daten erfahren. Im Folgenden stelle ich die Daten zur Verfügung und stelle anschließend Fragen dazu. Beantworte die Fragen bitte so konkret wie möglich und gehe dabei auf die bereitgestellten Daten ein. Denke dir keine weiteren Inhalte aus."))
print(df.chat("Was ist der Maximalwert in Spalte 'e5'?"))
print(df.chat("Beschreibe kurz die wichtigsten Merkmale in dem Datensatz."))
print(df.chat("Bitte gib mir für die folgenden Aufgaben den entsprechenden Python-Code, damit sie gelöst werden können: Ausgabe der ersten 20 Zeilen., Erstellen eines Boxplots für die Spalte 'e10'."))
