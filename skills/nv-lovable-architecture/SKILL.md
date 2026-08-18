---
name: nv-lovable-architecture
description: Bereitet bestehende Architekturvorgaben für Lovable auf. Verwende diesen Skill immer, wenn der User Lovable Project Knowledge oder Workspace Knowledge aus `docs/architecture.md` erstellen, aktualisieren, aufteilen, synchronisieren oder für Lovable vorbereiten möchte. Der Skill schreibt ausschließlich `docs/lovable-project-knowledge.md` und `docs/lovable-workspace-knowledge.md`, ohne neue Architekturregeln zu erfinden.
context: fork
metadata:
  author: nanoverse
  version: "1.0.0"
---

# NV Lovable Architecture

## Zweck

Überführe vorhandene Architekturvorgaben in zwei direkt in Lovable einsetzbare Knowledge-Texte:

- `docs/lovable-project-knowledge.md`
- `docs/lovable-workspace-knowledge.md`

Die Dateien sind eine **Aufteilung und Lovable-taugliche Verdichtung** der bestehenden Vorgaben. Sie sind keine Gelegenheit, Architektur neu zu entwerfen, zusätzliche Regeln zu recherchieren oder fehlende Informationen zu erraten.

## Auslöser

Verwende diesen Skill bei Bitten wie:

- „Bereite die Architektur für Lovable Knowledge auf."
- „Erstelle oder aktualisiere Project Knowledge und Workspace Knowledge für Lovable."
- „Teile unsere `architecture.md` für Lovable auf."
- „Synchronisiere die Lovable-Instruktionen mit der Architektur."

Verwende ihn nicht für allgemeine Architekturarbeit, neue Guidelines oder das Erstellen eines Lovable Skills. Dafür muss der User ausdrücklich nach einem separaten Artefakt fragen.

## Verbindliche Quellen und Grenzen

1. Lies bei **jeder** Ausführung zuerst die aktuelle offizielle Lovable-Dokumentation:
   `https://docs.lovable.dev/features/knowledge`
2. Ermittle daraus erneut die aktuelle Trennung zwischen Workspace Knowledge und Project Knowledge. Verlasse dich nicht auf eine in diesem Skill eingebettete Momentaufnahme.
3. Verwende danach standardmäßig ausschließlich `docs/architecture.md` als inhaltliche Quelle.
4. Lies weder den Anwendungscode noch weitere Projektdokumentation, um Lücken zu schließen oder zusätzliche Regeln abzuleiten.
5. Erfinde keine Regeln, Technologien, Nutzergruppen, Tabellen, Sicherheitsanforderungen oder Architekturentscheidungen.
6. Schreibe ausschließlich in diese beiden Zieldateien:
   - `docs/lovable-project-knowledge.md`
   - `docs/lovable-workspace-knowledge.md`
7. Verändere `docs/architecture.md` nicht.

## Fehlende oder unzureichende Quelle

Prüfe, ob `docs/architecture.md` existiert, bevor du Inhalte erstellst.

- Falls die Datei fehlt, frage:  
  **„`docs/architecture.md` existiert nicht. Welche vorhandene Datei soll ich als alleinige Grundlage für die Lovable-Knowledge-Dateien verwenden?“**
- Lies erst die vom User benannte Datei und verwende danach nur diese als Quelle.
- Falls die Quelle nicht erkennen lässt, ob eine Regel projekt- oder workspaceweit gilt, frage gezielt nach dieser Zuordnung.
- Falls die Quelle für eine Lovable-Kategorie keine Inhalte liefert, lasse diese Kategorie weg. Ergänze keine Platzhalterregeln.
- Falls die offizielle Lovable-Seite nicht abrufbar ist, halte an und bitte den User um einen erneuten Versuch oder einen aktuellen Auszug der Dokumentation. Verwende keine veraltete, angenommene Produktlogik.

## Aktuelle Lovable-Aufteilung prüfen

Nutze die offizielle Seite als Quelle der Wahrheit. Prüfe insbesondere:

- Welche Inhalte Lovable aktuell für Workspace Knowledge empfiehlt.
- Welche Inhalte Lovable aktuell für Project Knowledge empfiehlt.
- Aktuelle Zeichenlimits und sonstige relevante Einschränkungen.

Zum Zeitpunkt der Skill-Erstellung beschreibt Lovable typischerweise:

- **Workspace Knowledge** als gemeinsame Regeln für alle Projekte eines Workspace, etwa Coding Style, Benennung, bevorzugte Libraries, wiederkehrende Architekturpatterns, Tests, Qualität und Dinge, die Lovable vermeiden soll.
- **Project Knowledge** als Kontext für ein konkretes Projekt, etwa Projektzweck, Datenmodell, projektspezifische Architekturentscheidungen, Domänenbegriffe, Constraints, Design, Referenzen sowie Sicherheits- oder Compliance-Vorgaben.

Diese Zusammenfassung ist nur ein Orientierungswert. Die bei der Ausführung gelesene offizielle Dokumentation hat immer Vorrang.

## Transformationsablauf

### 1. Quelle extrahieren

- Lies die Architekturquelle vollständig.
- Extrahiere ausschließlich explizite Regeln, Entscheidungen, Verbote, Ausnahmen und Fakten.
- Erhalte die Bedeutung von harten Regeln wie „niemals“, „ausschließlich“ und „nur“ unverändert.
- Behandle Codebeispiele nur als Beleg für eine Regel. Übernimm sie nur, wenn sie für Lovable notwendig und innerhalb des Zeichenlimits sinnvoll sind.

### 2. Regeln klassifizieren

Ordne jede extrahierte Information genau einer der folgenden Gruppen zu.

**Workspace Knowledge**

Ordne hier nur Regeln ein, die ohne Bezug auf eine konkrete Projektstruktur oder Fachdomäne grundsätzlich für mehrere Projekte desselben Workspace gelten könnten, beispielsweise:

- TypeScript- und Benennungsregeln
- allgemeine Komponenten-, Formular- und Stylingkonventionen
- allgemeine Test- und Fehlerbehandlungsanforderungen
- Regeln zu Comments, technischen Schulden und Secrets
- wiederkehrende Qualitäts- oder Performance-Prinzipien

**Project Knowledge**

Ordne hier alles ein, das dieses konkrete Projekt beschreibt oder dessen konkrete Architektur voraussetzt, beispielsweise:

- konkrete Pfade wie `src/services/**`, `src/api/**`, `supabase/functions/**`
- konkrete Bibliotheken, vorhandene Layouts, Routen oder Datenzugriffsschichten
- Mandantenmodell, RLS, Edge Functions und `verifyJwt()`
- projektbezogene Branches, Deployment- und Secret-Konventionen
- Chat-spezifische Regeln, `MessagePart[]`, `parts_json`
- konkrete Integrationsausnahmen wie Jira Data Center über VPN und Browser-Extension

Wenn eine Regel theoretisch allgemein klingt, aber konkrete Projektpfade, Domänen oder Implementierungen nennt, gehört sie in Project Knowledge.

### 3. Lovable-tauglich formulieren

- Schreibe auf Deutsch, sofern die Quelle keine andere Sprache vorgibt.
- Formuliere kurze, eindeutige Anweisungen in Imperativform.
- Bewahre die Aussage jeder Quellregel. Vereinfache nur Sprache und Struktur, nicht die fachliche Bedeutung.
- Gruppiere Regeln unter knappen Überschriften.
- Entferne Wiederholungen nur, wenn dabei keine Einschränkung oder Ausnahme verloren geht.
- Übernimm keine Begründungen, Beispiele oder Implementierungsdetails, die keine handlungsrelevante Lovable-Anweisung enthalten.
- Formuliere keine neuen „Best Practices“, keine Empfehlungen aus eigener Erfahrung und keine Mutmaßungen über Lovable.

## Zieldateien

Erstelle oder überschreibe nach erfolgreicher Klassifikation beide Dateien.

### `docs/lovable-workspace-knowledge.md`

Struktur:

```md
# Lovable Workspace Knowledge

> Aus `docs/architecture.md` abgeleitete, workspaceweit wiederverwendbare Regeln.

## [Thema]

- [Knappe, explizit aus der Quelle abgeleitete Regel]
```

- Nimm nur Regeln auf, die gemäß aktueller Lovable-Dokumentation für Workspace Knowledge geeignet sind.
- Nenne weder konkrete Projektpfade noch projektinterne Sonderfälle.
- Falls die Quelle keine workspaceweit wiederverwendbaren Regeln enthält, schreibe nur den Titel und einen knappen Hinweis, dass die Quelle keine ableitbaren Workspace-Regeln enthält.

### `docs/lovable-project-knowledge.md`

Struktur:

```md
# Lovable Project Knowledge

> Aus `docs/architecture.md` abgeleitete, projektspezifische Vorgaben.

## [Thema]

- [Knappe, explizit aus der Quelle abgeleitete Regel oder Projektfakt]
```

- Nimm projektspezifische Architektur, Datenzugriff, Sicherheitsgrenzen, Integrationsausnahmen und Domänenregeln auf, sofern sie in der Quelle stehen.
- Erfinde keine Projektübersicht, Personas, Datenbanktabellen oder Referenzen, wenn die Quelle diese nicht ausdrücklich enthält.

## Zeichenlimit und Vollständigkeit

- Prüfe vor dem Schreiben die aktuell dokumentierten Zeichenlimits für beide Lovable-Felder.
- Halte jede Zieldatei innerhalb des jeweiligen Limits.
- Kürze zuerst Wiederholungen und nicht handlungsrelevante Begründungen.
- Streiche niemals eine harte Sicherheits-, Datenzugriffs- oder Architekturregel, nur um prägnanter zu wirken.
- Falls die vollständige, verlustfreie Aufteilung nicht in die aktuellen Limits passt, schreibe keine unvollständigen Dateien. Erkläre dem User, welche Quellabschnitte nicht verlustfrei untergebracht werden können, und frage nach einer Priorisierung.

## Abschluss

Berichte nach dem Schreiben knapp:

1. welche Quelle verwendet wurde,
2. dass die aktuelle Lovable-Dokumentation geprüft wurde,
3. welche Dateien geschrieben wurden,
4. die Zeichenzahl jeder Zieldatei im Verhältnis zum aktuell gültigen Limit,
5. dass keine neuen Architekturentscheidungen erfunden wurden.

Nenne offene Zuordnungs- oder Inhaltsfragen ausdrücklich, statt sie selbst zu entscheiden.
