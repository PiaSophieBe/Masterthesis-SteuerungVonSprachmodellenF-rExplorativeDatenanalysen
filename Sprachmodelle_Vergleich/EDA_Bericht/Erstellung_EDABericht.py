import pandas as pd
from ydata_profiling import ProfileReport

# Datensatz
df = pd.read_csv("df_PreiseStationen2.csv")

# Erstellen des Profiling-Objekts im minimalen Modus für bessere Performance
profile = ProfileReport(
    df,
    title="Explorative Datenanalyse für wissenschaftliche Arbeit",
    minimal=True
)

# Speichern des Berichts in zwei Formaten:
# 1. HTML für die visuelle Analyse durch den Forscher
profile.to_file("eda_report.html")

# 2. JSON für die programmatische Verarbeitung durch das LLM
profile.to_file("eda_report.json")

print("EDA-Bericht erfolgreich als 'eda_report.html' und 'eda_report.json' gespeichert.")