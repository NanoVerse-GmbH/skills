---
name: nv-functional-acceptance
description: >
  Führt die fachliche Abnahme eines implementierten Features anhand der eingebetteten funktionalen
  Definition of Done durch. Verwende diesen Skill bei „fachliche Abnahme“, „funktionale Abnahme“,
  „fachlichen DoD prüfen“, „fachlich done?“, „ACs abnehmen“, „Feature prüfen“, „UAT“ oder vor
  Abschluss, Demo, Übergabe oder Release. Bewertet ausschließlich fachliche Vollständigkeit anhand
  konkreter Evidenz und erstellt Dateien, Jira-Kommentare oder Ticket-Änderungen nur auf ausdrückliche
  Anweisung beziehungsweise Bestätigung.
license: MIT
metadata:
  author: NanoVerse
  version: '1.1.0'
---

# NanoVerse – Fachliche Abnahme

Prüfe, ob ein Feature aus Sicht von Produkt und Nutzern fachlich fertig ist. Die maßgebliche,
eingebettete DoD steht in [references/functional-dod.md](references/functional-dod.md); lies sie
vollständig, bevor du bewertest. Die technische Abnahme ist getrennt: Architektur, Codequalität,
Build, Performance und Security sind keine eigenen fachlichen Entscheidungskriterien.

## Grundsätze

- Ein Kriterium ist nur erfüllt, wenn konkrete Evidenz vorliegt: geprüfte Datei, Funktionsprüfung,
  Demo/Testprotokoll oder direkter Jira-/Confluence-Abruf. Angaben im Prompt sind keine Evidenz.
- Fehlt ein Nachweis, markiere das Kriterium als **offen**. Ist eine externe Quelle nicht erreichbar,
  markiere es als **nicht prüfbar**; dies ist kein PASS.
- `Nicht erforderlich` ist nur mit einer konkreten, am Featureumfang begründeten Erklärung zulässig.
- Gib das Ergebnis standardmäßig als formatierte Chat-Antwort aus. Schreibe keine Datei, keinen
  Jira-Kommentar und ändere kein Ticket ohne ausdrückliche Nutzeranweisung bzw. Bestätigung.

## Phase 1: Kontext und Relevanz festlegen

1. Lade bei einem Issue Key das Jira-Ticket direkt und prüfe Titel, ACs, Status, Sub-Tasks, Links
   sowie den Epic-Kontext. Prüfe bei Branch/PR/Repository den aktuellen Diff, geänderte Dateien und
   vorhandene Artefakte. Eine Featurebeschreibung dient nur zur Eingrenzung.
2. Erfasse Feature/Story, ChangeType (`New Feature`, `Behavior Change`, `Refactor`, `Migration`,
   `Removal`), Nutzergruppen, betroffene Oberflächen oder Integrationen, Komplexität bzw.
   Stakeholder-Relevanz und alle zugänglichen Evidenzquellen.
3. Extrahiere und nummeriere belastbare ACs als `AC-1`, `AC-2`, usw. Fehlen sie, bleibt Abschnitt A
   offen; erfinde keine Anforderungen.
4. Lege für A–H eine Relevanzmatrix an:

| Bereich | Erforderlich, wenn |
|---|---|
| A Anforderungen | ACs oder fachliche Anforderungen existieren |
| B Jira | ein Jira-Ticket verfügbar oder als Abschlussartefakt erwartet wird |
| C Fachliche Doku | Nutzerverhalten, Regeln, Zielgruppen oder Abläufe neu oder geändert sind |
| D Glossar | neue/geänderte Fachbegriffe, Abkürzungen oder Integrationsnamen vorkommen |
| E In-App-Hilfe | Nutzer Orientierung brauchen oder bestehende Hilfe betroffen ist |
| F Releasenotes | sichtbarer Nutzen für Nutzer entsteht |
| G Sprache & Texte | nutzersichtbare UI-Texte oder Fehlermeldungen betroffen sind |
| H Handover | das Feature komplex oder stakeholder-/demo-relevant ist |

## Phase 2: DoD A–H evidenzbasiert prüfen

Bewerte jede anwendbare Prüffrage aus `references/functional-dod.md` mit `erfüllt`, `offen` oder
`nicht prüfbar`; bei nicht relevanten Bereichen verwende `nicht erforderlich` samt Begründung.

### A · Anforderungen vollständig erfüllt

- Ordne jedem AC mindestens eine geänderte Datei, einen geprüften Nutzerablauf oder einen anderen
  dokumentierten Nachweis zu.
- Prüfe Happy Path, fachliche Fehlerzustände und Edge Cases end-to-end aus Nutzersicht.
- Prüfe die Konsistenz aller im Ticket beschriebenen Szenarien sowie dokumentierte und mit dem PO
  abgestimmte Abweichungen.

### B · Jira-Ticket ist aktuell

Prüfe direkt Status, Planabweichungen, Sub-Tasks, PR-/Branch-Links und nachträglich angelegte
Lücken-Tickets. Ist Jira nicht abrufbar, darf B nicht als erfüllt erscheinen.

### C · Fachliche Dokumentation

Prüfe in `docs/functional/` eine Datei nach dem Namensschema aus `docs/README.md`. Sie muss Ziel,
Nutzergruppen, Regeln und Abläufe abdecken; vorhandene Screenshots oder Diagramme müssen dem
aktuellen Zustand entsprechen.

### D · Glossar

Prüfe das Confluence-Glossar in Kapitel 12 sowie Ticket, UI und Doku auf neue/geänderte Begriffe,
Abkürzungen und Integrationsnamen. Ohne Confluence-Zugriff bleibt ein relevanter Glossar-Check
nicht prüfbar.

### E · Hilfebereich / In-App-Hilfe

Prüfe betroffene Inhalte in `src/data/helpArticles.ts` oder `src/data/helpArticles.json` und, wenn
erforderlich, den konsistenten Verweis in `src/lib/helpKnowledgeIndex.ts`. Hilfe muss Deutsch und
verständlich für Nicht-Techniker sein.

### F · Fachliche Releasenotes

Prüfe `CHANGELOG.md` und `src/lib/releaseNotes.ts` im aktuellen Diff. Einträge beschreiben Nutzen
in verständlichem Deutsch und enthalten keine Refactorings, Dependency-Updates oder interne Details.
Fordere oder ändere `package.json` nur bei ausdrücklicher Nutzeranweisung.

### G · Sprache & Texte

Prüfe tatsächlich betroffene Screens und Textquellen auf deutsche, konsistente Texte,
handlungsorientierte Fehlerzustände sowie sinnvolle Tooltips, Platzhalter und Hilfen. Englische
Resttexte sind nur für bewusste Fachbegriffe wie Jira oder Confluence zulässig.

### H · Handover

Bei komplexen oder stakeholder-/demo-relevanten Features prüfe in `docs/handovers/` ein Dokument
nach `docs/README.md`, das Umfang, Zweck, Einschränkungen und offene Punkte abdeckt. Prüfe bei
Demo-Relevanz auch den Leitfaden in `docs/`. Kleine Bugfixes dürfen H nur mit konkreter Begründung
als nicht erforderlich markieren.

### Chat-Testkatalog

Bei chatrelevanten Features, neuen Integrationen, Kartentypen oder Workflows prüfe zusätzlich
`docs/test-catalog-chat.md`. Ein passender Testfall muss angelegt oder aktualisiert sein; sonst
bleibt die Abnahme offen.

## Phase 3: Challenger Review und Entscheidung

Prüfe automatisch, ob jede erfüllte Bewertung durch Evidenz gedeckt ist, ob Happy Path, relevante
Fehler-/Edge-Cases und ACs geprüft wurden und ob erforderliche Artefakte (Jira, Doku, Glossar,
Hilfe, Releasenotes, Sprache, Chat-Testkatalog, Handover) fehlen. Setze unbelegte „erfüllt“-Werte
auf offen zurück.

**Entscheidung:**

- **PASS / Bestanden:** alle anwendbaren Kriterien sind erfüllt.
- **FAIL / Nicht bestanden:** mindestens ein anwendbares Kriterium ist offen oder nicht erfüllt.
- **BLOCKIERT / Nicht prüfbar:** fehlende Evidenz oder eine externe Abhängigkeit verhindert die
  Entscheidung; dies ist kein PASS.

Ein AC ohne Evidenz, ein offener Happy Path/Edge Case, eine nicht abgestimmte Abweichung oder ein
fehlendes erforderliches Artefakt ist ein Hard-Fail für PASS.

## Standard-Ausgabeformat

```markdown
# Fachliche Abnahme: <STORY-KEY – Titel>

**Ergebnis:** Bestanden | Nicht bestanden | Nicht prüfbar
**Prüfumfang:** <ChangeType, Nutzergruppen, relevante Bereiche>
**Geprüfte Quellen:** <Jira, Branch/PR, Dateien, Funktionsprüfung, Confluence>

## Evidenz zu Akzeptanzkriterien
| AC | Ergebnis | Evidenz | Offener Nachweis |
|---|---|---|---|
| AC-1 | Erfüllt / Offen | `<Pfad>` / geprüfter Flow / Jira-Link | – / <was fehlt> |

## DoD-Check
### A · Anforderungen vollständig erfüllt
- [x] / [ ] <Kriterium> — **Evidenz:** <konkret>
...
### H · Handover-Dokument vorhanden
- [x] / [ ] <Kriterium> — **Evidenz:** <konkret>

## Challenger Review
- <Lücke oder „Keine zusätzlichen Lücken identifiziert“>

## Offene Punkte vor fachlicher Abnahme
1. <Restarbeit oder benötigte Evidenz>

## Nächster Schritt
<kleinste konkrete Folgeaktion>
```

Bei PASS bleibt die Liste offener Punkte leer. Nutze
[templates/technical-handover.md](templates/technical-handover.md) nur dann, wenn der User
ausdrücklich eine formale Übergabe-Datei verlangt.

## Optionale Folgeaktionen

| Wunsch | Aktion |
|---|---|
| „Abnahme als Datei speichern“ | Erstelle die Abnahme in `docs/functional/` oder `docs/handovers/` nach `docs/README.md`. |
| „Jira-Kommentar schreiben“ | Zeige den geplanten Kommentar und hole eine explizite Bestätigung vor dem Schreiben ein. |
| „Ticket aktualisieren“ | Beschreibe die konkreten Änderungen und hole vor jeder Ticket-Änderung eine explizite Bestätigung ein. |
