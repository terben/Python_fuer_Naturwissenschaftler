## Von Anfang an professionell arbeiten
## (Python‑Skripte mit Notebook‑Komfort in VS Code)

### Warum wir zu Recht mit Jupyter Notebooks starten
Jupyter Notebooks sind großartig für:
- Interaktives Lernen und schnelles Ausprobieren
- Direkte Visualisierung von Ergebnissen
- Nachvollziehbare Dokumentation (inkl. LaTeX)

→ Perfekt für den Einstieg in Python, für die Lehre und für Dokumentationen.

### Aber: Wissenschaft braucht mehr
In den Naturwissenschaften arbeiten wir mit:
- **Versionskontrolle (Git)**
- Reproduzierbaren Simulationen und Parameterstudien
- Automatisierter Datenauswertung und Pipelines
- Integration in größere Projekte

→ Dafür sind sauber strukturierte Python‑Skripte oft nachhaltiger – Notebooks stoßen hier an Grenzen.

### Praxis: Ihr Workflow in VS Code (Notebook‑Komfort im Skript)
- Skript in Zellen strukturieren: Abschnitte/Zellen mit „# %%“ anlegen.
- Zellen oder einzelne Code-Zeilen/Blöcke interaktiv ausführen: Shift+Enter → Ausgabe im Jupyter Interactive Window.
- Variablen und Plots prüfen: Interactive Window/Variables‑Ansicht nutzen; Kernel bei Bedarf neu starten (Strg+Shift+P → „Jupyter: Restart“).
- Große Daten inspizieren: Data Wrangler öffnen (z. B. per Befehl „Data Wrangler: Launch“ oder Kontextmenü „Open in Data Wrangler“) und DataFrames komfortabel durchsuchen.

### Setup und Einstellungen
- VS‑Code‑Erweiterungen „Data Wrangler“ und „Rainbow CSV“.
- VS-Code-Einstellung „Jupyter › Interactive Window › Text Editor: Execute Selection“ aktivieren, damit Shift+Enter stets ins Interactive Window sendet. Am schnellsten via Nutzereinstellungen (JSON):

   Strg+Shift+P → „Open User Settings (JSON)“, dann ergänzen:
   ```json
   {
     "jupyter.interactiveWindow.textEditor.executeSelection": true,
   }
   ```

### Entscheidungshilfe auf einen Blick
- Notebook: Anfängliche Datenexploration und Visualisierung, Lehre.
- Skript: Reproduzierbare Pipelines, Batch‑Runs, Versionierung.

**Meine Empfehlung:** VS Code (#%%)-Modus: Von Anfang an Skripte mit Notebook‑Komfort entwickeln!
