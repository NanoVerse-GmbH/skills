# Fachliche Abnahme & technische Übergabe – {{ticket_key}} {{feature_title}}

## Abnahmeentscheidung

- **Status:** {{PASS | FAIL | BLOCKIERT}}
- **Abgenommen durch:** {{name_or_role}}
- **Datum:** {{date}}
- **Scope:** {{feature_scope}}

## Fachliche Evidenz

- **Ticket / Epic:** {{jira_link}}
- **AC- und Flow-Nachweise:** {{evidence_links_or_summary}}
- **Feature-Dokumentation:** {{functional_documentation_link_or_not_applicable}}
- **Weitere Artefakte:** {{screenshots_demo_or_other_links}}

## Kriterienbewertung

| Kriterium | Status | Evidenz oder Begründung |
|---|---|---|
| A · Anforderungen vollständig erfüllt | {{status}} | {{evidence_or_reason}} |
| B · Jira-Ticket aktuell | {{status}} | {{evidence_or_reason}} |
| C · Fachliches Dokument | {{status}} | {{evidence_or_reason}} |
| D · Glossar | {{status}} | {{evidence_or_reason}} |
| E · In-App-Hilfe | {{status}} | {{evidence_or_reason}} |
| F · Fachliche Releasenotes | {{status}} | {{evidence_or_reason}} |
| G · Sprache & Texte | {{status}} | {{evidence_or_reason}} |
| H · Handover-Dokument | {{status}} | {{evidence_or_reason}} |

Zulässige Kriterienstatus: `erfüllt`, `offen`, `blockiert`, `nicht anwendbar`.
Für `nicht anwendbar` ist eine konkrete Begründung erforderlich.

## Bekannte Einschränkungen und offene Punkte

{{known_limitations_and_open_points}}

## Übergabe an die technische Abnahme

Die fachliche Entscheidung bewertet keine technische Qualität. Die technische
Abnahme soll die folgenden Hinweise als Kontext verwenden, ohne die fachliche
Abnahme erneut durchzuführen:

- **Fachlich akzeptierte Abweichungen:** {{accepted_deviations}}
- **Technische Beobachtungen ohne fachliches Urteil:** {{technical_observations}}
- **Abhängigkeiten / benötigte Zugänge:** {{dependencies_and_access}}
- **Zu prüfende technische Risiken:** {{technical_risks}}

## Abschluss

{{decision_rationale}}
