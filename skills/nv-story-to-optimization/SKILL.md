---
name: nv-story-to-optimization
description: >
  Führe diesen Skill aus, wenn der Benutzer eine bereits implementierte User Story reviewen,
  Oberflächenoptimierungen durchführen oder Verbesserungen nach der Implementierung umsetzen möchte.
  Auslöser sind Phrasen wie "Story reviewen", "Oberfläche optimieren", "Verbesserungen umsetzen",
  "Story challengen", "Findings implementieren", "ich habe Feedback zur Oberfläche" oder wenn
  der Benutzer eine Story die bereits "In Review" ist weiter verbessern möchte.
  Auch bei "/story-done" oder "ich bin fertig mit den Optimierungen" den Abschluss-Workflow starten.
  Dieser Skill greift NACH story-to-impl-plan: Epic → Story auswählen (Status: In Review) →
  Branch wechseln → Feedback-Interview → Optimierungen umsetzen → /story-done → Jira-Kommentar ergänzen.
compatibility:
  tools:
    - Atlassian MCP (Jira)
    - bash / git
    - python3
---

# Surface Test Workflow

Dieser Skill greift **nach der Implementierung** — wenn eine Story bereits "In Review" ist und
du Oberflächen- oder UX-Optimierungen durchführen möchtest. Er ergänzt den bestehenden
Jira-Kommentar aus `story-to-impl-plan` mit den Optimierungen.

## Konfiguration

Beim ersten Aufruf folgendes erfragen, falls nicht bereits bekannt:

```
JIRA_PROJECT_KEY  – z.B. "PROJ" (ohne Bindestrich, wird automatisch ergänzt)
PARALLEL_MODE     – Arbeitest du an mehreren Stories gleichzeitig? (ja/nein)
WORKTREE_ROOT     – Nur bei PARALLEL_MODE=ja: Pfad für Worktrees, z.B. ~/worktrees
```

Einmal ermittelte Werte für die gesamte Session merken und nicht erneut fragen.

**PARALLEL_MODE** bestimmt das Branch-Verhalten in Phase 3:
- `nein` → einfacher `git checkout` im Hauptrepo
- `ja`   → eigener Worktree-Ordner pro Story unter `WORKTREE_ROOT`

---

## Workflow-Übersicht

```
1. Epic laden & Stories auflisten (bevorzugt Status: In Review)
2. User Story auswählen
3. Branch wechseln (kein neuer Branch — existiert bereits)
4. Feedback-Interview führen
5. Optimierungen durchführen (Findings mitschreiben)
6. /story-done → Jira-Kommentar ergänzen
```

---

## Phase 1 – Epic laden

1. Jira-Epic anhand des übergebenen Keys laden (z.B. `PROJ-100`).
2. Alle Child-Issues (User Stories) des Epics abrufen.
3. Übersichtlich auflisten — Stories mit Status **In Review** zuerst:

```
Epic: PROJ-100 – [Titel]

User Stories:
  [1] PROJ-101 – [Titel]  (In Review)   ← bereit für Optimierung
  [2] PROJ-102 – [Titel]  (In Progress)
  ~~[3] PROJ-103 – [Titel]  (Done)~~
```

4. Benutzer fragen: "Welche Story möchtest du reviewen und optimieren?"

> Bevorzugt Stories mit Status **In Review** anbieten.
> Stories mit Status **Done** grau/durchgestrichen anzeigen.

---

## Phase 2 – Story auswählen & Details anzeigen

1. Gewählte Story vollständig laden (Titel, Beschreibung, Akzeptanzkriterien).
2. Story-Details kompakt zusammenfassen und anzeigen.
3. Prüfen ob `tasks/IMPL_<STORYKEY>.md` im Repo existiert — falls ja, kurz erwähnen:
   `ℹ️ Implementierungsplan gefunden: tasks/IMPL_<STORYKEY>.md`

---

## Phase 3 – Branch wechseln

Der Branch existiert bereits (wurde von `story-to-impl-plan` angelegt).
**Kein neuer Branch wird erstellt.** Nur wechseln.

Branch suchen:
```bash
python3 scripts/branch_manager.py find PROJ-101
```

### Modus A – PARALLEL_MODE=nein

```bash
git checkout feature/PROJ-101-story-titel
```

### Modus B – PARALLEL_MODE=ja

```bash
cd ~/worktrees/PROJ-101-story-titel
```

### Branch nicht gefunden

```
Ich konnte keinen Branch für PROJ-101 finden.
Wurde die Implementierung bereits mit story-to-impl-plan gestartet?
→ Falls ja: Branch-Name manuell eingeben
→ Falls nein: Zuerst story-to-impl-plan ausführen
```

### Sicherheitsprüfung (immer)

```bash
python3 scripts/branch_manager.py status
```

Session-Tracker initialisieren:
```bash
python3 scripts/session_tracker.py init PROJ-101
```

---

## Phase 4 – Feedback-Interview

Strukturiertes Interview, um alle Findings zu erfassen. In zwei Schritten:

### Schritt A – Gezielte Fragen

Stelle diese Fragen nacheinander oder als Block:

```
1. Welche Bereiche der Oberfläche hast du getestet?
2. Was hat nicht wie erwartet funktioniert? (Verhalten vs. Erwartung)
3. Gibt es visuelle/UI-Probleme (Layout, Abstände, Farben)?
4. Gibt es funktionale Fehler (falsche Daten, fehlende Aktionen)?
5. Gibt es Performance- oder Ladezeitprobleme?
```

### Schritt B – Freie Ergänzungen

```
Hast du noch weitere Beobachtungen, die du beschreiben möchtest?
```

### Findings-Zusammenfassung

Vor der Implementierung alle gesammelten Findings strukturiert zusammenfassen und bestätigen lassen:

```
Ich habe folgende Findings erfasst:

[F1] UI: Button "Speichern" reagiert nicht beim ersten Klick
[F2] Funktional: Filterwert wird nach Reload nicht beibehalten
[F3] Layout: Tabelle überläuft auf mobiler Ansicht

Soll ich mit der Implementierung beginnen?
```

Findings in Session speichern:
```bash
python3 scripts/session_tracker.py add-decision "Findings bestätigt: F1, F2, F3"
```

---

## Phase 5 – Optimierungen umsetzen

1. Sicherstellen dass CWD im richtigen Verzeichnis liegt und der richtige Branch aktiv ist.
2. Findings der Reihe nach abarbeiten.
3. Für jedes Finding:
   - Relevante Dateien identifizieren
   - Änderung implementieren
   - Kurz bestätigen: `✓ [F1] behoben in src/components/SaveButton.tsx`
   - Finding + Datei in Session mitschreiben:
     ```bash
     python3 scripts/session_tracker.py add-change "[F1] Event-Listener-Fix" "src/components/SaveButton.tsx"
     ```
4. Wichtige Architektur- oder Designentscheidungen sofort loggen:
   ```bash
   python3 scripts/session_tracker.py add-decision "localStorage gewählt statt SessionStorage wegen Tab-übergreifender Persistenz"
   ```
5. Nach allen Findings: kurze Gesamtübersicht der Änderungen ausgeben.

**Wann eine Entscheidung geloggt werden soll:**
- Du wählst zwischen mehreren Lösungsansätzen
- Der Benutzer gibt eine explizite Richtung vor
- Eine Anforderung war unklar und wurde geklärt

---

## Phase 6 – Abschluss (/story-done)

Wird ausgelöst durch: `/story-done` oder "Ich bin fertig mit den Optimierungen" o.ä.

### Schritt 1: Session-Daten und geänderte Dateien laden

```bash
python3 scripts/session_tracker.py summary
python3 scripts/branch_manager.py changed-files main
```

### Schritt 2: Jira-Kommentar ergänzen

**Nicht** den Status ändern — die Story bleibt "In Review".
Einen **neuen Kommentar** hinzufügen der die Optimierungen dokumentiert (via `addCommentToJiraIssue`):

```
## Oberflächenoptimierungen

**Story:** PROJ-101 – [Titel]
**Branch:** feature/PROJ-101-story-titel
**Datum:** [aktuelles Datum]

### Gefundene Probleme & Lösungen

- **[F1] Button "Speichern" reagiert nicht beim ersten Klick**
  → Event-Listener-Initialisierung in `SaveButton.tsx` korrigiert

- **[F2] Filterwert wird nach Reload nicht beibehalten**
  → Filter-State wird jetzt in localStorage persistiert

### Wichtige Entscheidungen

- **localStorage vs. SessionStorage:** localStorage gewählt wegen Tab-übergreifender Persistenz

### Geänderte Dateien

- `src/components/SaveButton.tsx`
- `src/hooks/useFilterPersistence.ts`

### Zusammenfassung

[2-3 Sätze: Was wurde optimiert und warum.]
```

### Schritt 3: Abschlussmeldung + Session zurücksetzen

```
✓ Jira-Kommentar mit Optimierungen ergänzt
✓ Branch: feature/PROJ-101-story-titel
ℹ️ Story-Status bleibt "In Review"

Nicht vergessen: git add / commit / push liegt bei dir.
```

```bash
python3 scripts/session_tracker.py reset
```

---

## Fehlerbehandlung

| Situation | Verhalten |
|---|---|
| Epic nicht gefunden | Fehlermeldung + nach korrektem Key fragen |
| Branch nicht gefunden | Hinweis: zuerst story-to-impl-plan ausführen |
| Story nicht "In Review" | Hinweis anzeigen, aber trotzdem fortfahren wenn User möchte |
| Jira-Transition schlägt fehl | Fehlermeldung anzeigen, manuellen Hinweis geben |
| Keine Änderungen nach Optimierung | Kommentar trotzdem erstellen, "Keine Codeänderungen" vermerken |

---

## Wichtige Hinweise

- Dieser Skill greift **nach** `story-to-impl-plan` — der Branch existiert bereits.
- **Nie** einen neuen Branch erstellen — immer auf den bestehenden Feature-Branch wechseln.
- **Nie** den Jira-Status ändern — Story bleibt "In Review", nur Kommentar ergänzen.
- **Nie** automatisch committen, stagen oder pushen — das bleibt dem Benutzer überlassen.
- Jira-Statusübergänge nur mit validen Transition-IDs ausführen (vorher `getTransitionsForJiraIssue` aufrufen).
- `JIRA_PROJECT_KEY`, `PARALLEL_MODE` und `WORKTREE_ROOT` einmal merken, nicht wiederholt fragen.
- Findings und Entscheidungen **kontinuierlich** mitschreiben — nicht erst am Ende rekonstruieren.
