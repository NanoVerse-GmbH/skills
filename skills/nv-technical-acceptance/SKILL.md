---
name: nv-technical-acceptance
description: >
  Führt die NanoVerse-technische Abnahme eines Features anhand der eingebetteten
  technischen Definition of Done durch und liefert eine klare PASS-, FAIL- oder
  BLOCKIERT-Entscheidung mit Evidenz. Verwende diesen Skill immer bei technischer
  Abnahme, technischem DoD-Check, Freigabeprüfung, Engineering Sign-off,
  Qualitätsnachweis, Übergabe an Entwicklung oder wenn ein Feature technisch
  fertig geprüft werden soll. Eine vorhandene fachliche Übergabe dient nur als
  Kontext; dieser Skill wiederholt oder bewertet nie die fachliche Abnahme.
metadata:
  author: NanoVerse
  version: "1.1.0"
---

# NanoVerse – Technische Abnahme

## Zweck und Abgrenzung

Prüfe, ob ein Feature technisch verlässlich integriert, betreibbar, sicher und
nachweisbar ist. Die technische Entscheidung bezieht sich ausschließlich auf
die Kriterien in [references/technical-dod.md](references/technical-dod.md).
Diese Referenz ist Teil des Skills; fordere keine externe DoD-Datei an.

Eine vorhandene fachliche Übergabe darf Scope, akzeptierte Abweichungen,
fachliche Evidenz und bekannte Risiken liefern. Übernimm jedoch keine
fachliche Entscheidung und wiederhole weder AC-Abnahme noch Texte-, Hilfe-,
Releasenotes- oder Glossarprüfung. Die Trennung schützt eine unabhängige,
qualifizierte technische Freigabe.

## Evidenz und Ausgabesicherheit

Sammle mindestens:

- Ticket- oder Feature-ID, technischen Scope und betroffene Systeme,
- optional die fachliche Übergabe,
- Änderungen, Tests, Build-/Qualitätsnachweise und relevante Laufzeit- oder
  Integrationsnachweise,
- Konfigurationen, Abhängigkeiten, Daten- und Sicherheitsauswirkungen,
- bekannte technische Risiken, Einschränkungen und offene Punkte.

- Ein Kriterium ist nur erfüllt mit konkreter, aktueller Evidenz: ausgeführter
  Befehl mit Ergebnis, geprüfter Diff oder Codepfad, Test-/Eval-Protokoll,
  Integrationsprüfung, Laufzeitnachweis oder nachvollziehbares Artefakt.
  Angaben im Prompt sind keine Evidenz.
- Fehlt entscheidende Evidenz oder ist eine relevante externe Abhängigkeit nicht
  erreichbar, entscheide **BLOCKIERT**, nicht aufgrund einer Vermutung.
- Ein Kriterium ist nur **nicht anwendbar**, wenn es mit Bezug zum technischen
  Scope begründet wird.
- Gib das Ergebnis standardmäßig als formatierte Chat-Antwort aus. Schreibe
  keine Datei, keinen Jira-Kommentar und ändere kein Ticket ohne ausdrückliche
  Nutzeranweisung beziehungsweise Bestätigung.

## Ablauf

1. Lies die eingebettete technische DoD-Referenz vollständig.
2. Lies eine vorhandene fachliche Übergabe nur als Kontext. Übernimm daraus
   ausdrücklich keine fachliche Bewertung.
3. Lege für A–O eine Relevanzmatrix an. Prüfe jedes relevante Kriterium als
   `erfüllt`, `offen` oder `blockiert`; verwende `nicht anwendbar` ausschließlich
   mit konkreter Scope-Begründung. Halte Evidenz oder den fehlenden Nachweis fest.
4. Führe passende Qualitätsgates und risikoangemessene technische Nachweise aus
   oder bewerte vorhandene Nachweise. Die in der Referenz genannten Befehle sind
   Standardnachweise; ergänze feature-spezifische Prüfungen, wenn das Risiko es
   verlangt.
5. Prüfe zusätzlich zu den Checklisten feature-spezifische technische Risiken,
   Abhängigkeiten und Auswirkungen. Prüfe insbesondere die für den Scope
   zutreffenden Daten-, Sicherheits-, Runtime-, Fehler-, Kompatibilitäts-,
   Abhängigkeits- und Rollout-Auswirkungen.
6. Entscheide:
   - **PASS**: alle anwendbaren Kriterien sind erfüllt;
   - **FAIL**: mindestens ein anwendbares Kriterium ist nicht erfüllt;
   - **BLOCKIERT**: die Entscheidung ist wegen fehlender Evidenz oder externer
     Abhängigkeiten nicht belastbar.
7. Gib das Ergebnis exakt nach
   [templates/technical-acceptance-result.md](templates/technical-acceptance-result.md)
   aus.

## Challenger Review und Entscheidung

- Lies vor dem Schreiben sowohl die DoD-Referenz als auch das Template.
- Kopiere die Überschriften, Nachweis-Tabelle und die fünfzehn Kriterien A–O
  aus `templates/technical-acceptance-result.md` unverändert in das Ergebnis.
  Benenne Kriterien nicht um, fasse sie nicht zu eigenen Kategorien zusammen
  und ordne sie nicht neu. Das feste Schema macht technische Entscheidungen
  über Features hinweg vergleichbar und auditierbar.
- Dokumentiere Befehle mit Ergebnis sowie Integrations- und Laufzeitnachweise
  mit konkreten Artefakten.
- Unterscheide eindeutig zwischen Befund, Risiko, Blocker und Empfehlung.
- Vermerke Abweichungen oder Restrestrisiken offen; PASS verlangt keinen
  fehlerfreien Idealzustand, aber eine explizit akzeptierte und kontrollierte
  Risikolage.
- Triff keinen fachlichen PASS/FAIL-Entscheid. Wenn die funktionale Übergabe
  fehlt, prüfe den technischen Scope trotzdem und vermerke den fehlenden Kontext.

Prüfe vor jeder PASS-Entscheidung, ob jede erfüllte Bewertung eine konkrete
Evidenz besitzt und ob die scope-relevanten Risiken abgefangen sind. Setze
unbelegte `erfüllt`-Werte auf `blockiert` zurück.

Ein fehlender erfolgreicher Quality Gate, fehlende angemessene Testevidenz,
unbelegte Sicherheits- oder Zugriffskontrollen, ungesicherte Datenintegrität
oder eine unbelegte relevante System-/Vertragsänderung ist ein Hard-Fail für
PASS. Bei fehlender Evidenz ist **BLOCKIERT** die korrekte Entscheidung; bei
nachgewiesen nicht erfülltem Kriterium ist die Entscheidung **FAIL**.

## Pflegevertrag

`references/technical-dod.md` ist die ausführbare, eingebettete Fassung der
technischen DoD. Ändert sich `dod-technical.md`, aktualisiere in derselben
Änderung diese Referenz und prüfe Template sowie Evals auf Konsistenz.
