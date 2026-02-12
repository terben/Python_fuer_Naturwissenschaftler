# Setup von Anaconda und VS Code für wissenschaftliches Programmieren

### Was wir in diesem Video machen

Wir setzen von Grund auf ein vollständiges Python-System für wissenschaftliches Programmieren auf:

* Python Distribution Anaconda installieren
* Codeeditor VS Code installieren
* nötige Extensions für VS Code installieren
* Das gesamte Setup testen

Ich gehe speziell auf die Besonderheiten bei der Installation unter Windows ein.

### Empfehlung für Windows-Nutzer

Falls Sie Anaconda und VS Code für Ihre wissenschaftlichen Projekte nutzen möchten, ist es empfehlenswert, Ihr System zunächst auf bereits bestehende Python-Installationen zu überprüfen. Mehrere parallele Python-Versionen können insbesondere unter Windows zu Problemen führen. Um allen Problemen von Anfang an aus dem Weg zu gehen, ist die beste Lösung, bereits vorhandene Installationen an dieser Stelle zu entfernen.

Ein erster Hinweis auf eine bestehende Python-Installation ist die Suche nach `idle` im Windows-Suchfeld. Falls hier Treffer erscheinen, ist sehr wahrscheinlich bereits eine andere Python-Version vorhanden.

### Anaconda installieren

Anaconda enthält sowohl Python als auch alle Bibliotheken, um schnell mit wissenschaftlichen Projekten loszulegen. Es ist zudem sehr nützlich zur Verwaltung mehrerer Python-Umgebungen und Abhängigkeiten.

![](https://www.google.com/s2/favicons?sz=64&domain_url=https%3A%2F%2Fwww.anaconda.com)[https://www.anaconda.com/download/success](https://www.anaconda.com/download/success)

Installieren Sie am einfachsten die `komplette Anaconda Distribution`, um sich nicht gleich zu Anfang mit dem Thema *Python-Umgebungen* auseinandersetzen zu müssen.

**Tipp für Windows-Nutzer:**
Bei der Installation von Anaconda kann die Checkbox *Add Anaconda3 to my PATH environment variable* gesetzt werden, auch wenn häufig davon abgeraten wird. Dies vereinfacht später die Nutzung von Python und Conda in VS Code. Wenn sich außer Anaconda weitere Python-Installationen auf dem System befinden, kann genau diese Einstellungen aber zu Konflikten führen (siehe oben).

### VS Code installieren

Visual Studio Code ist ein plattformübergreifender Code-Editor, der sich sehr gut für wissenschaftliches Programmieren, Datenanalyse und Python-basierte Workflows eignet. Er ist kostenlos und auf Linux, macOS und Windows verfügbar.

![](https://www.google.com/s2/favicons?sz=64&domain_url=https%3A%2F%2Fcode.visualstudio.com)[https://code.visualstudio.com](https://code.visualstudio.com)

Die Installation kann mit den vorgeschlagenen Standardeinstellungen durchgeführt werden.

### Extensions unter VS Code installieren

VS Code kommt in der Standardinstallation nur mit begrenztem Funktionsumfang. Unterstützungen für Programmiersprachen und viele andere Erweiterungen werden über sogenannte *Extensions* realisiert.

Um mit Python loszulegen, benötigen Sie anfangs diese zwei Extensions:

- [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

- [Jupyter Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

Installation einer Extension in VS Code:
1. Extensions View mit `Ctrl+Shift+X` öffnen
2. Namen der Erweiterung suchen
3. **Installieren** anklicken

**Hinweise:**
1. Manchmal bekommt man sehr viele Suchtreffer, wenn man nach dem Namen (z.B. `Python`) sucht. Hier ist meist die Extension mit den meisten Downloads diejenige, die man haben möchte
2. Nach der Installation benötigen einige Erweiterungen möglicherweise zusätzliche Einrichtung oder einen Neustart von VS Code, damit sie ordnungsgemäß funktionieren.

### Das Setup testen

- Laden Sie die Materialien dieses Videos von [GitHub](https://github.com/terben/Python_fuer_Naturwissenschaftler) herunter.
- Öffnen Sie in VS Code über `File → Open Folder` das Verzeichnis `Video_02_Python_Setup` innerhalb der Materialien.
- Beim ersten Öffnen des Ordners erscheint in VS Code möglicherweise eine Sicherheitsabfrage (*Trust author*). Da es sich um die Materialien dieses Videos handelt und die Dateien lokal auf Ihrem Rechner liegen, können Sie diese Abfrage bedenkenlos bestätigen.
- Öffnen Sie über den File-Explorer (links in VS Code) das Notebook `VSCode_notebook.ipynb` und führen Sie die einzelnen Zellen aus. Sie können innerhalb von VS Code wie gewohnt mit Jupyter-Notebooks arbeiten.
- Abhängig von Ihrem System kann VS Code beim Öffnen des Notebooks oder einer Python-Datei nach der zu verwendenden Python-Umgebung fragen. Diese Abfrage erscheint nur, wenn mehrere Python-Umgebungen vorhanden sind. Falls eine Auswahl angezeigt wird, wählen Sie die entsprechende Anaconda-Umgebung aus (z.B. die *base*-Umgebung). Ist nur eine Umgebung vorhanden, erfolgt die Auswahl automatisch.
- Öffnen Sie anschließend das Python-Skript `VSCode_skript.py`. Starten Sie das Skript, indem Sie auf das ▶-Symbol (**Run Python File**) oben rechts im Editor klicken. Im unteren Bereich von VS Code öffnet sich ein Terminal, in dem die Ausgabe des Skripts angezeigt wird.

Nach diesem Setup können Sie Python-Skripte und Jupyter-Notebooks in VS Code mit Anaconda-Umgebungen ausführen und direkt mit der Programmierung loslegen.
