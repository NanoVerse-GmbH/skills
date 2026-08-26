# Definition of Done – Technisch

Dieses Dokument beschreibt die technischen Ergebnisse, die ein Feature vor seinem Abschluss erreichen muss. Es richtet sich an Entwickler und KI-Agenten und ergänzt Architektur-Guidelines: Diese DoD prüft **ob** das technische Ergebnis verlässlich erreicht ist, nicht **wie** einzelne Klassen, Module oder Framework-Patterns umgesetzt werden. Ein Feature ist technisch „done", wenn alle zutreffenden Kriterien erfüllt sind.

Die Checklisten sind ein Mindestumfang, keine abschließende Liste. Für jedes Feature müssen zusätzlich dessen spezifische technische Risiken, Abhängigkeiten und Auswirkungen beurteilt und bei Bedarf abgesichert werden.

---

## A · Automatisierte Qualitätsgates

Der auslieferbare Stand ist technisch konsistent und kann reproduzierbar gebaut werden. Statische Analyse, Typprüfung und Build sind die erste Schranke; sie ersetzen keine fachlich-technische Prüfung der weiteren Kriterien.

- [ ] `npm run lint` läuft fehlerfrei
- [ ] `npm run typecheck` zeigt keine TypeScript-Fehler
- [ ] `npm run build` baut ohne Fehler
- [ ] Alle für die Änderung relevanten zusätzlichen Qualitätschecks sind ausgeführt

---

## B · Angemessene technische Verifikation

Das geänderte Verhalten ist durch eine zum Risiko passende Mischung aus automatisierten Tests und, falls nötig, manuellen oder Integrationsprüfungen abgesichert. Die Teststrategie deckt nicht nur den erwarteten Ablauf, sondern auch relevante Fehler-, Rand- und Kompatibilitätsszenarien ab.

- [ ] `npm run test` läuft vollständig grün
- [ ] Neues oder geändertes Verhalten ist durch angemessene Tests abgesichert
- [ ] Relevante Eingabe-, Validierungs-, Fehler- und Randfälle sind geprüft
- [ ] Bei Fehlerbehebungen verhindert mindestens ein Regressionstest die Wiederkehr des ursprünglichen Problems
- [ ] Tests prüfen beobachtbares Verhalten oder Verträge, nicht nur Implementierungsdetails
- [ ] Erforderliche manuelle, Integrations- oder End-to-End-Prüfungen sind durchgeführt und dokumentiert

---

## C · Technische Integration & Systemverträge

Das Feature ist in alle betroffenen technischen Systeme vollständig integriert. Schnittstellen, Datenflüsse und Zustände verhalten sich über ihre Grenzen hinweg konsistent; vorhandene Funktionen werden nicht unbemerkt beschädigt.

- [ ] Alle betroffenen technischen Schnittstellen, Datenmodelle und Zustandsübergänge sind vollständig nachgezogen
- [ ] Das Feature nutzt die für seine Integration vorgesehene Plattform- oder Transportmöglichkeit und funktioniert in den unterstützten Betriebsmodellen
- [ ] Daten bleiben beim Übergang zwischen Client, Backend, Persistenz und externen Systemen vollständig und konsistent
- [ ] Änderungen sind mit bestehenden Daten, Clients und abhängigen Features kompatibel oder haben einen dokumentierten Migrations- bzw. Rückfallpfad
- [ ] Feature-spezifische technische Risiken und Abhängigkeiten sind geprüft und adressiert

---

## D · Datensicherheit & Zugriffskontrolle

Das Feature schützt Daten entsprechend ihrer Sensitivität und ihrem tatsächlichen Berechtigungsmodell. Zugriffskontrolle wird nicht anhand eines starren Musters, sondern passend zu Tenant-, Nutzer-, Rollen- oder Gruppenbeziehungen umgesetzt und geprüft.

- [ ] Neue oder geänderte Datenzugriffe erlauben ausschließlich die fachlich berechtigten Akteure
- [ ] Neue persistierte Daten sind durch eine sinnvolle Row-Level-Security- und Berechtigungsstrategie geschützt
- [ ] Zugriffskontrollen berücksichtigen den tatsächlichen Kontext der Daten, z.B. Tenant, Nutzer, Rolle, Gruppe oder eine andere berechtigte Beziehung
- [ ] Schema- und Berechtigungsänderungen sind nachvollziehbar versioniert und sicher ausrollbar
- [ ] Keine sensiblen Daten, Zugangsdaten oder personenbezogenen Inhalte werden ungeschützt ausgegeben, protokolliert oder an unberechtigte Systeme weitergegeben

---

## E · Robuster Runtime-Betrieb

Neue oder geänderte Backend-, Edge- oder Integrationsfunktionen sind unter den vorgesehenen Laufzeitbedingungen zuverlässig betreibbar. Konfiguration, Wiederholungen, Antworten und Störungen verhalten sich vorhersehbar, ohne Datenverlust oder doppelte Seiteneffekte.

- [ ] Die Funktion ist mit der erforderlichen Konfiguration, Authentifizierung und Netzwerkanbindung betriebsbereit
- [ ] Erwartete Aufrufe und Browser-/Client-Szenarien werden zuverlässig beantwortet
- [ ] Wiederholte oder doppelte Schreibaufrufe erzeugen keinen widersprüchlichen Zustand und keine doppelten Seiteneffekte
- [ ] Technische Antworten, Statuscodes und Timeouts sind für aufrufende Systeme eindeutig und konsistent
- [ ] Unvermeidbare Betriebsgrenzen, Abhängigkeiten oder Degradationsfälle sind erkennbar und dokumentiert

---

## F · Fehlerverhalten & Wiederherstellung

Bei Fehlern bleibt das System sicher, verständlich und in einem konsistenten Zustand. Nutzer und aufrufende Systeme erhalten eine angemessene Rückmeldung und können, wenn sinnvoll, den Vorgang kontrolliert wiederholen.

- [ ] Fehler führen nicht zu unvollständigen, verlorenen oder widersprüchlichen Daten
- [ ] Nutzer erhalten verständliche, nicht-sensitive und handlungsorientierte Fehlermeldungen
- [ ] Wiederholbare Fehler bieten einen angemessenen Wiederherstellungs- oder Retry-Weg
- [ ] Fehler werden für Betrieb und Analyse mit ausreichendem Kontext sichtbar, ohne sensible Daten offenzulegen
- [ ] Externe oder ungültige Daten führen zu kontrollierter Degradation statt zu undefiniertem Verhalten

---

## G · Chat- und Aktionsverträge

Dieses Kriterium gilt für Änderungen am Chat, an Karten oder an Integrationsaktionen. Nachrichten, Aktionen und Nutzerentscheidungen bleiben strukturiert, nachvollziehbar und über Backend, Persistenz sowie UI hinweg konsistent.

- [ ] Die kanonische strukturierte Repräsentation von Nachrichten, Karten und Aktionen bleibt die Source of Truth
- [ ] Neue oder geänderte Karten, Aktionen und Zustände sind in allen beteiligten Schichten vollständig modelliert, validiert, gespeichert und dargestellt
- [ ] Änderungen mit Seiteneffekten sind für Nutzer transparent und erfordern dort eine Bestätigung, wo dies fachlich oder sicherheitlich nötig ist
- [ ] Nach einer Aktion zeigt die Anwendung den aktuellen, konsistenten Zustand; veraltete Daten und doppelte Aktionen werden vermieden
- [ ] Bestehende Unterhaltungen, Karten und Aktionen bleiben kompatibel oder werden kontrolliert migriert

---

## H · Prompt-, Kontext- & LLM-Qualität

Dieses Kriterium gilt für Änderungen an KI-Verhalten, Prompting oder Kontextaufbau. Neue Einflüsse auf eine Antwort sind nachvollziehbar, budgetiert, validiert und im Betrieb beobachtbar.

- [ ] Neue Kontextquellen oder Modi sind als klar identifizierbare, kombinierbare Bestandteile der Prompt- und Kontextverarbeitung integriert
- [ ] Debug- und Betriebsinformationen machen sichtbar, welche Modi, Kontextquellen oder Entscheidungswege wirksam waren
- [ ] LLM- und externe Antworten werden vor ihrer Verwendung validiert und bei Fehlern kontrolliert behandelt
- [ ] Kontextumfang, Priorisierung und Token-Budget sind für das neue Verhalten geprüft
- [ ] Neue Verhaltensregeln, Schutzmechanismen und Qualitätsanforderungen sind durch passende Tests oder Evals abgesichert

---

## I · Kontrollierte Einführung & Konfiguration

Das Feature kann entsprechend seinem Risiko kontrolliert aktiviert, beobachtet, angepasst und bei Problemen zurückgenommen werden. Konfigurationen und Grenzwerte sind nachvollziehbar, konsistent und nicht an versteckten Stellen im Code verteilt.

- [ ] Für das Feature existiert eine dem Risiko angemessene Aktivierungs-, Rollout- oder Rückfallstrategie
- [ ] Sichere Defaults und Berechtigungen verhindern eine unbeabsichtigte Aktivierung oder Nutzung
- [ ] Veränderliche Grenzwerte, Budgets, Timeouts und Konfigurationen sind zentral nachvollziehbar gepflegt
- [ ] Auswirkungen einer Konfigurationsänderung auf bestehende Nutzer, Daten und Integrationen sind geprüft

---

## J · Parität & Schnittstellenkompatibilität

Dieses Kriterium gilt, wenn mehrere Clients, Backend-Komponenten oder externe Systeme einen gemeinsamen Vertrag teilen. Der Vertrag bleibt beidseitig konsistent, versionierbar und durch geeignete Nachweise abgesichert.

- [ ] Alle Beteiligten eines gemeinsamen Vertrags verarbeiten die neue oder geänderte Semantik konsistent
- [ ] Vertragsänderungen sind durch Tests, Integrationsprüfungen oder gleichwertige Nachweise abgesichert
- [ ] Dokumentation und technische Spezifikationen gemeinsamer Verträge sind aktualisiert, sofern sie existieren
- [ ] Inkompatible Änderungen haben einen abgestimmten Versions-, Migrations- oder Rückfallpfad

---

## K · Modell-, Tenant- & Skill-Policy

Dieses Kriterium gilt für KI-Modelle, Skills und tenant-spezifische Fähigkeiten. Auswahl, Verfügbarkeit und Berechtigung folgen den geltenden Plattformregeln und verhalten sich für Nutzer wie für Betreiber transparent.

- [ ] Modell-, Skill- und Tenant-spezifisches Verhalten entspricht den gültigen Produkt- und Plattform-Policies
- [ ] Berechtigung, Sichtbarkeit und Lebenszyklus neuer Fähigkeiten sind für die betroffenen Nutzergruppen korrekt
- [ ] Änderungen sind über alle beteiligten Schichten konsistent und nachvollziehbar wirksam
- [ ] Nicht unterstützte, nicht autorisierte oder veraltete Varianten werden sicher verhindert oder kontrolliert behandelt

---

## L · Evals & Telemetrie

Neue technisch relevante Verhaltensänderungen sind messbar und im Betrieb nachvollziehbar. Die Tiefe der Evaluation und Telemetrie entspricht dem Risiko, insbesondere bei KI-, Integrations- und Schreibvorgängen.

- [ ] Für relevante neue Verhaltensweisen existieren aussagekräftige Evals, Qualitätsmessungen oder gleichwertige Nachweise
- [ ] Fehlerklassen, relevante Abhängigkeiten und technische Zustände sind im Betrieb sichtbar
- [ ] Traces, Logs oder Metriken erlauben die Diagnose von Fehlverhalten ohne sensible Daten preiszugeben
- [ ] Schutzmechanismen und Degradationspfade sind beobachtbar und gegen Regressionen abgesichert

---

## M · Dependencies, Performance & Auslieferbarkeit

Die Änderung verschlechtert die Auslieferbarkeit und Nutzbarkeit des Produkts nicht unverhältnismäßig. Neue Abhängigkeiten, Ressourcenverbrauch und Ladeverhalten sind begründet, überprüft und mit dem bestehenden Build- und Releaseprozess vereinbar.

- [ ] Abhängigkeiten und Lockfile sind synchron; der reproduzierbare Installationsprozess funktioniert
- [ ] Neue Abhängigkeiten sind erforderlich, gepflegt und verursachen keine vermeidbaren Sicherheits-, Lizenz- oder Wartungsrisiken
- [ ] Performance-, Speicher- und Bundle-Auswirkungen sind für die betroffenen Nutzungsszenarien geprüft
- [ ] Große oder selten benötigte Funktionalität belastet den Standardpfad nicht unverhältnismäßig

---

## N · Sprache & Lokalisierung (technisch)

Dieses Kriterium gilt für Änderungen mit nutzer- oder systemseitigen Textausgaben. Sprache, Terminologie und Lokalisierung bleiben für die unterstützten Kontexte konsistent, auch in Fehler- und Degradationsfällen.

- [ ] Neue oder geänderte Ausgaben verwenden die für Nutzer und Kontext vorgesehene Sprache
- [ ] Texte, Platzhalter und Fehlerrückmeldungen bleiben bei allen unterstützten Lokalisierungen konsistent und verständlich
- [ ] Technische Fallbacks führen nicht zu widersprüchlicher Sprache oder unbeabsichtigter Preisgabe interner Details

---

## O · Jira Data Center & VPN-Kompatibilität

Dieses Kriterium gilt für Funktionen, die Jira Data Center integrieren. Sie müssen im unterstützten Kunden-Netzwerkmodell funktionieren – einschließlich Umgebungen, in denen Jira Data Center nur über eine VPN-gestützte Browser-Extension erreichbar ist.

- [ ] Die Funktion funktioniert in allen unterstützten Zugriffsmodellen für Jira Data Center, einschließlich VPN-/Extension-Szenarien
- [ ] Verbindungsabbrüche, Timeouts und eingeschränkte Erreichbarkeit werden verständlich erkannt und kontrolliert behandelt
- [ ] Das Feature setzt keinen nicht unterstützten Direktzugriff auf Kundeninfrastruktur voraus
- [ ] Sicherheits- und Berechtigungsgrenzen des Kunden-Netzwerks werden respektiert
