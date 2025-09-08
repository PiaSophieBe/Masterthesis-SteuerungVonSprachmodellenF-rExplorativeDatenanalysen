# Masterthesis-SteuerungVonSprachmodellenF-rExplorativeDatenanalysen
Code zur Masterthesis: Steuerung von Sprachmodellen für explorative Datenanalysen

Dieses Repository beinhaltet den Code zu der zugehörigen Masterthesis mit dem Titel "Steuerung von Sprachmodellen für explorative Datenanalysen". Das Repository ist unterteilt in: 
- ReferenzEDA und 
- Vergleich_der_Sprachmodelle. 

## Die explorative Datenanalyse ist unterteilt in:
- Loading, dabei werden die Daten aus dem Tankerkönig Datensatz zusammengeführt. 
- UmfassendeEDA, unterteilt in der Betrachtung der einzelnen Merkmalen (einzelneMerkmale), Betrachtung aus Merkmalskombinationen (kombinationMerkmale), vertiefende Analyse (vertiefend) und entsprechenden Anpassung der Merkmale (Merkmalsanpassung). 
- Goldstandard, dient als Referenz-EDA und wird in der Thesis näher beschrieben. 

## Der Vergleich der Sprachmodelle ist unterteilt in: 
- Archiv
- EDA-Bericht: Es wird ein Analysebericht geladen, kombiniert mit einem Prompt, beides wird an ein Sprachmodell geschickt und die Antwort zurück gegeben. Es wird zudem mit ydata-profiling ein EDA-Bericht aus dem Datensatz erstellt und sowohl als HTML- als auch als JSON-Datei gespeichert.
- PandasAI: Es wird ein Datensatz geladen, mit PandasAI und verschiedenen Sprachmodellen verbunden und anschließend per Chat nach Auswertungen und passendem Python-Code abgefragt. Es wird in einem weiteren Skript eine CSV mit einem eigenen HTW-Ollama-LLM über PandasAI verbunden und per Chat nach Analysen und Python-Code abgefragt.
- VergleichSprachmodelle: Es werden für jedes betrachtete Open-Source-Sprachmodell eine CSV geladen, Fragen samt Kontext an eine Sprachmodell-API gesendet, aus den Antworten der Python-Code extrahiert und automatisch ausgeführt.

Die Daten, die in dieser Arbeit verwendet worden sind, können hier geladen werden: https://dev.azure.com/tankerkoenig/_git/tankerkoenig-data