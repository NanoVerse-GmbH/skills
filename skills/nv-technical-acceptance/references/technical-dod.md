# NanoVerse Definition of Done – Technisch

Diese Referenz ist die für den Skill maßgebliche, eigenständige Fassung der
technischen Definition of Done. Sie prüft technische Ergebnisse und Verträge,
nicht die konkrete Modul- oder Frameworkstruktur. Prüfe nur anwendbare Kriterien
und begründe Nichtanwendbarkeit konkret.

## A · Automatisierte Qualitätsgates

Der Stand ist reproduzierbar und technisch konsistent.

- `npm run lint` läuft fehlerfrei.
- `npm run typecheck` zeigt keine TypeScript-Fehler.
- `npm run build` baut ohne Fehler.
- Weitere für die Änderung relevante Qualitätschecks sind ausgeführt.

## B · Angemessene technische Verifikation

Das Verhalten ist entsprechend seines Risikos nachgewiesen.

- `npm run test` läuft vollständig grün.
- Neues oder geändertes Verhalten besitzt angemessene Tests.
- Eingabe-, Validierungs-, Fehler-, Rand- und Kompatibilitätsfälle sind geprüft.
- Fehlerbehebungen besitzen einen Regressionstest.
- Tests prüfen beobachtbares Verhalten oder Verträge statt Implementierungsdetails.
- Erforderliche manuelle, Integrations- oder End-to-End-Prüfungen sind dokumentiert.

## C · Technische Integration & Systemverträge

Betroffene Systeme verarbeiten Daten und Zustände über ihre Grenzen hinweg
konsistent.

- Schnittstellen, Datenmodelle und Zustandsübergänge sind vollständig nachgezogen.
- Die vorgesehene Plattform- oder Transportmöglichkeit funktioniert in unterstützten Betriebsmodellen.
- Daten bleiben zwischen Client, Backend, Persistenz und externen Systemen konsistent.
- Kompatibilität ist erhalten oder Migration bzw. Rückfallpfad dokumentiert.
- Feature-spezifische technische Risiken und Abhängigkeiten sind adressiert.

## D · Datensicherheit & Zugriffskontrolle

Datenzugriffe entsprechen Sensitivität und Berechtigungsmodell.

- Ausschließlich fachlich berechtigte Akteure erhalten Zugriff.
- Neue persistierte Daten besitzen eine angemessene RLS- und Berechtigungsstrategie.
- Kontext wie Tenant, Nutzer, Rolle, Gruppe oder andere berechtigte Beziehungen wird berücksichtigt.
- Schema- und Berechtigungsänderungen sind versioniert und sicher ausrollbar.
- Sensitive Daten, Zugangsdaten und personenbezogene Inhalte werden nicht ungeschützt offengelegt oder weitergegeben.

## E · Robuster Runtime-Betrieb

Backend-, Edge- und Integrationsfunktionen verhalten sich in ihren vorgesehenen
Laufzeitbedingungen vorhersehbar.

- Erforderliche Konfiguration, Authentifizierung und Netzwerkanbindung sind betriebsbereit.
- Erwartete Aufrufe und Browser-/Client-Szenarien erhalten zuverlässige Antworten.
- Doppelte Schreibaufrufe erzeugen keine widersprüchlichen Zustände oder Seiteneffekte.
- Antworten, Statuscodes und Timeouts sind eindeutig und konsistent.
- Betriebsgrenzen, Abhängigkeiten und Degradationsfälle sind erkennbar dokumentiert.

## F · Fehlerverhalten & Wiederherstellung

Fehler lassen das System sicher, verständlich und konsistent.

- Fehler führen nicht zu unvollständigen, verlorenen oder widersprüchlichen Daten.
- Nutzer erhalten verständliche, nicht-sensitive und handlungsorientierte Meldungen.
- Wiederholbare Fehler besitzen einen angemessenen Retry- oder Wiederherstellungsweg.
- Betrieb und Analyse erhalten ausreichend Kontext ohne Offenlegung sensibler Daten.
- Externe oder ungültige Daten führen zu kontrollierter Degradation.

## G · Chat- und Aktionsverträge

Gilt für Chat-, Karten- und Integrationsaktionsänderungen.

- Strukturierte Nachrichten-, Karten- und Aktionsrepräsentationen bleiben Source of Truth.
- Neue Karten, Aktionen und Zustände sind modelliert, validiert, gespeichert und dargestellt.
- Seiteneffekte sind transparent und bei Bedarf bestätigt.
- Die Anwendung zeigt nach Aktionen frischen, konsistenten Zustand und vermeidet Duplikate.
- Bestehende Unterhaltungen, Karten und Aktionen bleiben kompatibel oder werden kontrolliert migriert.

## H · Prompt-, Kontext- & LLM-Qualität

Gilt für KI-Verhalten, Prompting und Kontextaufbau.

- Kontextquellen und Modi sind klar identifizierbar und kombinierbar.
- Debug- und Betriebsinformationen zeigen wirksame Modi, Quellen und Entscheidungswege.
- LLM- und externe Antworten werden validiert und bei Fehlern kontrolliert behandelt.
- Kontextumfang, Priorisierung und Token-Budget sind geprüft.
- Verhaltensregeln und Schutzmechanismen besitzen passende Tests oder Evals.

## I · Kontrollierte Einführung & Konfiguration

Aktivierung, Beobachtung und Rücknahme entsprechen dem Risiko.

- Aktivierungs-, Rollout- oder Rückfallstrategie ist angemessen.
- Sichere Defaults und Berechtigungen verhindern unbeabsichtigte Nutzung.
- Grenzwerte, Budgets, Timeouts und Konfigurationen sind zentral nachvollziehbar.
- Konfigurationsänderungen sind auf Nutzer, Daten und Integrationen geprüft.

## J · Parität & Schnittstellenkompatibilität

Gilt für gemeinsame Verträge zwischen Clients, Backend oder externen Systemen.

- Alle Beteiligten verarbeiten die neue Semantik konsistent.
- Vertragsänderungen besitzen Tests, Integrationsprüfungen oder gleichwertige Nachweise.
- Vorhandene technische Dokumentation und Spezifikationen sind aktualisiert.
- Inkompatible Änderungen besitzen Versions-, Migrations- oder Rückfallpfad.

## K · Modell-, Tenant- & Skill-Policy

Gilt für KI-Modelle, Skills und tenant-spezifische Fähigkeiten.

- Verhalten entspricht Produkt- und Plattform-Policies.
- Berechtigung, Sichtbarkeit und Lebenszyklus sind für betroffene Gruppen korrekt.
- Änderungen wirken schichtübergreifend konsistent und nachvollziehbar.
- Nicht unterstützte, unautorisierte oder veraltete Varianten werden sicher behandelt.

## L · Evals & Telemetrie

Technisch relevante Verhaltensänderungen sind risikogerecht messbar und
diagnostizierbar.

- Aussagekräftige Evals, Qualitätsmessungen oder gleichwertige Nachweise existieren.
- Fehlerklassen, Abhängigkeiten und technische Zustände sind sichtbar.
- Traces, Logs oder Metriken erlauben Diagnose ohne Preisgabe sensibler Daten.
- Schutzmechanismen und Degradationspfade sind beobachtbar und regressionsgeschützt.

## M · Dependencies, Performance & Auslieferbarkeit

Die Änderung ist mit Build- und Releaseprozess vereinbar und belastet das
Produkt nicht unverhältnismäßig.

- Abhängigkeiten und Lockfile sind synchron; Installation ist reproduzierbar.
- Neue Abhängigkeiten sind erforderlich, gepflegt und risikogerecht bewertet.
- Performance-, Speicher- und Bundle-Auswirkungen sind geprüft.
- Große oder selten benötigte Funktionen belasten den Standardpfad nicht unverhältnismäßig.

## N · Sprache & Lokalisierung (technisch)

Gilt für nutzer- oder systemseitige Textausgaben.

- Ausgaben verwenden die für Nutzer und Kontext vorgesehene Sprache.
- Texte, Platzhalter und Fehlerrückmeldungen sind in unterstützten Lokalisierungen konsistent.
- Fallbacks erzeugen keine widersprüchliche Sprache und offenbaren keine internen Details.

## O · Jira Data Center & VPN-Kompatibilität

Gilt für Jira-Data-Center-Integrationen.

- Unterstützte Zugriffsmodelle funktionieren, einschließlich VPN-/Browser-Extension-Szenarien.
- Verbindungsabbrüche, Timeouts und eingeschränkte Erreichbarkeit werden kontrolliert behandelt.
- Die Lösung setzt keinen nicht unterstützten Direktzugriff auf Kundeninfrastruktur voraus.
- Sicherheits- und Berechtigungsgrenzen des Kunden-Netzwerks werden respektiert.
