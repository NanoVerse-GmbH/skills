# Technische Abnahme – {{ticket_key}} {{feature_title}}

## Abnahmeentscheidung

- **Status:** {{PASS | FAIL | BLOCKIERT}}
- **Abgenommen durch:** {{name_or_role}}
- **Datum:** {{date}}
- **Technischer Scope:** {{technical_scope}}
- **Fachliche Übergabe:** {{link_or_not_provided}} (nur Kontext, nicht erneut bewertet)

## Ausgeführte Nachweise

| Nachweis | Ergebnis | Artefakt / Details |
|---|---|---|
| `npm run lint` | {{pass_fail_blocked_na}} | {{output_or_reason}} |
| `npm run typecheck` | {{pass_fail_blocked_na}} | {{output_or_reason}} |
| `npm run test` | {{pass_fail_blocked_na}} | {{output_or_reason}} |
| `npm run build` | {{pass_fail_blocked_na}} | {{output_or_reason}} |
| Weitere risikobasierte Prüfungen | {{pass_fail_blocked_na}} | {{output_or_reason}} |

## Kriterienbewertung

| Kriterium | Status | Evidenz oder Begründung |
|---|---|---|
| A · Automatisierte Qualitätsgates | {{status}} | {{evidence_or_reason}} |
| B · Technische Verifikation | {{status}} | {{evidence_or_reason}} |
| C · Integration & Systemverträge | {{status}} | {{evidence_or_reason}} |
| D · Datensicherheit & Zugriff | {{status}} | {{evidence_or_reason}} |
| E · Runtime-Betrieb | {{status}} | {{evidence_or_reason}} |
| F · Fehlerverhalten & Recovery | {{status}} | {{evidence_or_reason}} |
| G · Chat- und Aktionsverträge | {{status}} | {{evidence_or_reason}} |
| H · Prompt, Kontext & LLM | {{status}} | {{evidence_or_reason}} |
| I · Rollout & Konfiguration | {{status}} | {{evidence_or_reason}} |
| J · Parität & Kompatibilität | {{status}} | {{evidence_or_reason}} |
| K · Modell-, Tenant- & Skill-Policy | {{status}} | {{evidence_or_reason}} |
| L · Evals & Telemetrie | {{status}} | {{evidence_or_reason}} |
| M · Dependencies & Performance | {{status}} | {{evidence_or_reason}} |
| N · Lokalisierung | {{status}} | {{evidence_or_reason}} |
| O · Jira DC & VPN | {{status}} | {{evidence_or_reason}} |

Zulässige Kriterienstatus: `erfüllt`, `offen`, `blockiert`, `nicht anwendbar`.
`Nicht anwendbar` setzt eine konkrete Scope-Begründung voraus.

## Risiken, Abweichungen und verbleibende Blocker

### Akzeptierte Restrisiken

{{accepted_residual_risks}}

### Nicht erfüllte Kriterien / Blocker

{{remaining_blockers}}

### Empfohlene Folgearbeiten

{{recommended_follow_ups}}

## Technische Schlussfolgerung

{{decision_rationale}}
