# NanoGiants AI Skills Library

Zentrale Skill-Library der Organisation. Hier leben wiederverwendbare Skills für AI-Coding-Assistenten (opencode, Claude, Cursor, etc.) – kuratiert, versioniert und für das gesamte Team zugänglich.

## Was ist ein Skill?

Ein Skill ist eine Markdown-Datei (`SKILL.md`), die einem AI-Assistenten domänenspezifische Anweisungen, Workflows und Kontext gibt. Skills werden lokal in ein Projekt eingespielt und vom Assistenten bei passenden Aufgaben automatisch geladen.

Jeder Skill kann zusätzlich mitbringen:
- **`scripts/`** – ausführbare Hilfsskripte (Node.js, Bash, etc.)
- **`evals/`** – Eval-Konfigurationen zum Testen des Skills
- **`rules/`** – ausgelagerte Regelwerke, die `SKILL.md` referenziert

---

## Skills verwenden

### Einen Skill installieren

Einzelnen Skill per `git sparse-checkout` holen (empfohlen – holt nur den gewünschten Ordner):

```bash
# Temporäres Verzeichnis anlegen
git clone --no-checkout --depth=1 git@github.com:NanoVerse-GmbH/skills.git /tmp/nanoverse-skills
cd /tmp/nanoverse-skills

# Nur den gewünschten Skill auschecken
git sparse-checkout init --cone
git sparse-checkout set skills/<skill-name>
git checkout

# Skill ins Projekt kopieren
cp -r skills/<skill-name> /pfad/zu/deinem/projekt/.opencode/skills/
```

Alternativ einfach den Ordner `skills/<skill-name>/` aus diesem Repo manuell in dein Projekt kopieren:

```
dein-projekt/
└── .opencode/
    └── skills/
        └── <skill-name>/
            ├── SKILL.md
            └── scripts/   # falls vorhanden
```

### Einen Skill aktivieren

Nach dem Kopieren muss der Skill in der opencode-Konfiguration registriert werden. Der genaue Pfad hängt vom verwendeten AI-Tool ab – in der Regel reicht es, die `SKILL.md` im Skills-Verzeichnis des Projekts zu haben.

---

## Skills beisteuern

### Neuen Skill anlegen

```
skills/
└── dein-skill-name/       # kebab-case
    ├── SKILL.md            # Pflicht
    ├── scripts/            # Optional: Hilfsskripte
    ├── evals/              # Optional: Eval-Configs
    ├── rules/              # Optional: ausgelagerte Regeln
    └── LICENSE.txt         # Optional
```

**Naming:** Skill-Verzeichnisse immer in `kebab-case`.

### SKILL.md Aufbau

Jede `SKILL.md` beginnt mit einem YAML-Frontmatter-Block:

```yaml
---
name: dein-skill-name
description: >
  Einzeiliger oder mehrzeiliger Text, der beschreibt wann dieser Skill
  ausgelöst werden soll. Dieser Text wird vom AI-Assistenten genutzt,
  um den Skill automatisch zu erkennen und zu laden. Trigger-Phrasen
  (deutsch + englisch) hier mit aufführen.
license: MIT
metadata:
  author: dein-name
  version: '1.0.0'
---
```

Danach folgt der eigentliche Skill-Inhalt in Markdown: Anweisungen, Workflows, Beispiele, Referenzen.

#### Frontmatter-Felder

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| `name` | ✅ | Eindeutiger Bezeichner, muss dem Verzeichnisnamen entsprechen |
| `description` | ✅ | Wann soll der Skill ausgelöst werden? Je konkreter, desto besser |
| `license` | – | Lizenz (z.B. `MIT`) |
| `metadata.author` | – | Ersteller des Skills |
| `metadata.version` | – | Semver-Version |

### Was macht einen guten Skill aus?

- **Klare `description`**: Der Assistent entscheidet anhand der Description, ob der Skill relevant ist. Konkrete Trigger-Phrasen (auch umgangssprachlich, deutsch + englisch) erhöhen die Trefferquote erheblich.
- **Fokus**: Ein Skill löst genau ein Problem. Lieber zwei kleine als einen großen.
- **Reproduzierbar**: Der Skill sollte deterministisch sein – gleicher Input, gleicher Output.
- **Eigenständig**: Keine Abhängigkeiten zu anderen Skills voraussetzen, die nicht im Repo liegen.
- **Getestet**: Wenn möglich, `evals/` mitliefern.

### Skill einreichen

1. Feature-Branch anlegen: `git checkout -b skill/dein-skill-name`
2. Skill unter `skills/dein-skill-name/` anlegen
3. Lokal testen (manuell oder per Evals)
4. Pull Request gegen `master` öffnen
5. Review durch ein Teammitglied
6. Nach Approval: Merge

---

## Vorhandene Skills

Alle Skills folgen dem Workflow: **Idea → Epic → Stories → Testplan → Implementierung → Optimierung**

| Skill | Verzeichnis | Beschreibung |
|-------|-------------|-------------|
| **nv-idea-to-epic** | `skills/nv-idea-to-epic/` | Interviewt Schritt für Schritt und erstellt daraus ein vollständiges, AI-natives Epic-Dokument – mit Problem Statement, KPIs, Scope, Happy Path, technischem Rahmen, Edge Cases und Story-Slicing-Hinweis. Legt das Epic anschließend in Jira an. |
| **nv-epic-to-user-stories** | `skills/nv-epic-to-user-stories/` | Leitet aus einem bestehenden Jira-Epic vollständige User Stories mit Akzeptanzkriterien (Given/When/Then) ab. Erkennt bestehende Stories, entscheidet ob neu erstellen, aktualisieren oder aufteilen – inklusive Challenger Review und Qualitätsscore. |
| **nv-create-testplans** | `skills/nv-create-testplans/` | Erzeugt aus einer fertigen User Story eine deterministische, automatisierbare Testfall-Suite (Unit, Integration, E2E, Security, Performance u.a.) – mit Risk Classification, Coverage Map, Challenger Review und direkter Anlage als Tasks in Jira. |
| **nv-story-to-implementation** | `skills/nv-story-to-implementation/` | Erstellt aus einer fertigen User Story einen vollständigen, AI-nativen Implementierungsplan mit Work Breakdown, Traceability auf ACs und TCs, Feature Flag- und Rollback-Strategy. Legt den Plan als `tasks/IMPL_<STORYKEY>.md` im Repo ab und synchronisiert ihn als Tasks in Jira. |
| **nv-story-to-optimization** | `skills/nv-story-to-optimization/` | Greift nach der Implementierung: führt ein strukturiertes Feedback-Interview durch, setzt Oberflächen- und UX-Optimierungen um und dokumentiert Findings + Entscheidungen als Jira-Kommentar. Ergänzt den `story-to-implementation`-Workflow. |
| **nv-skill-installer** | `skills/nv-skill-installer/` | Installiert und aktualisiert NanoGiants AI Skills vom privaten GitHub-Repo `NanoVerse-GmbH/skills` auf die lokale Maschine. Unterstützt opencode und Claude Code, global und project-local, mit automatischer Umgebungserkennung, Auth-Check und Update-Detection. |
| **nv-skill-updater** | `skills/nv-skill-updater/` | Pusht einen lokal installierten NanoGiants Skill zurück ins private GitHub-Repo `NanoVerse-GmbH/skills`. Unterstützt neue Skill-Beiträge und Updates bestehender Skills – mit Diff-Vorschau, automatischer README-Aktualisierung bei neuen Skills und Auth-Check. |
| **nv-functional-acceptance** | `skills/nv-functional-acceptance/` | Führt die NanoVerse-fachliche Abnahme anhand der eingebetteten funktionalen Definition of Done durch und erstellt eine formale Übergabe für die technische Abnahme. |
| **nv-technical-acceptance** | `skills/nv-technical-acceptance/` | Führt die NanoVerse-technische Abnahme anhand der eingebetteten technischen Definition of Done durch und liefert eine klare PASS-, FAIL- oder BLOCKIERT-Entscheidung mit Evidenz. |
| **nv-lovable-architecture** | `skills/nv-lovable-architecture/` | Bereitet bestehende Architekturvorgaben für Lovable auf und teilt sie in Project Knowledge sowie Workspace Knowledge auf, ohne neue Architekturregeln zu erfinden. |

---

## Verzeichnisstruktur

```
skills/
├── skills/                  # Alle Skills
│   └── <skill-name>/
│       ├── SKILL.md         # Skill-Definition (Pflicht)
│       ├── scripts/         # Hilfsskripte (optional)
│       ├── evals/           # Eval-Configs (optional)
│       └── rules/           # Ausgelagerte Regeln (optional)
└── README.md
```
