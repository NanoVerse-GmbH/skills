# Definition of Done – Fachlich

Dieses Dokument beschreibt alle fachlichen Kriterien, die erfüllt sein müssen, bevor ein Feature als fertig gilt. Es richtet sich an Product Owner, Fachexperten und KI-Agenten, die nach Abschluss einer Implementierung prüfen, ob das Feature aus Nutzer- und Produktperspektive vollständig ist. Ein Feature ist fachlich „done“, wenn **alle** zutreffenden Kriterien dieser Liste abgehakt sind. Bei Chat-relevanten Features, neuen Integrationen, Kartentypen oder Workflows ist zusätzlich ein passender Testfall in `docs/test-catalog-chat.md` zu ergänzen oder zu aktualisieren.

### Ausgabeformat des DoD-Prüfergebnisses

Das DoD-Prüfergebnis wird standardmäßig als formatierte Chat-Antwort ausgegeben. Eine Markdown-Datei in `docs/functional/` oder `docs/handovers/` wird nur auf ausdrücklichen Nutzerwunsch erstellt. Ein Jira-Kommentar wird nur nach expliziter Bestätigung geschrieben, weil er ein externes System verändert.

Jede Bewertung benötigt konkrete Evidenz aus dem aktuellen Stand, etwa aus geänderten Dateien, einer Funktionsprüfung oder einem direkten Jira- beziehungsweise Confluence-Abruf. Eine bloße Angabe im Prompt ist keine Evidenz. Fehlt der Nachweis, bleibt das Kriterium offen.

---

## A · Anforderungen vollständig erfüllt (DoR-Reifegrad)

Das Herzstück jeder Fertigstellung: Die im Ticket beschriebenen Anforderungen sind in der Implementierung vollständig umgesetzt. „Vollständig“ bedeutet, dass alle Akzeptanzkriterien erfüllt sind – nicht nur die einfachen, sondern auch Randfälle und Fehlersituationen.

- [ ] Alle Akzeptanzkriterien (ACs) aus dem Jira-Ticket sind erfüllt und manuell oder automatisch verifiziert
- [ ] Alle definierten User-Flows funktionieren end-to-end (Happy Path vollständig)
- [ ] Fehlerzustände und Edge Cases sind fachlich abgedeckt (nicht nur technisch behandelt)
- [ ] Das Feature verhält sich konsistent in allen relevanten Szenarien, die im Ticket beschrieben sind
- [ ] Abweichungen vom ursprünglich beschriebenen Verhalten sind explizit dokumentiert und mit dem Product Owner abgestimmt

**Evidenz**: Ordne jedem Akzeptanzkriterium eine geänderte Datei, einen überprüften Nutzerablauf oder einen dokumentierten Nachweis zu. Ist kein Nachweis für ein Akzeptanzkriterium vorhanden, bleibt dieses Kriterium offen.

---

## B · Jira-Ticket ist aktuell

Das Ticket spiegelt den tatsächlichen Stand der Implementierung wider. Veraltete Tickets führen zu Missverständnissen beim nächsten Sprint-Review und bei der Übergabe.

- [ ] Ticket-Status ist auf den definierten Abschlussstatus gesetzt (z.B. „Done“ / „In Review“)
- [ ] Bei Abweichungen vom ursprünglichen Plan: Ticket-Beschreibung oder ACs aktualisiert
- [ ] Alle Sub-Tasks sind abgeschlossen oder explizit als „nicht benötigt“ markiert (mit Begründung)
- [ ] Verlinkungen zu relevanten Pull Requests / Branches sind eingetragen
- [ ] Fehlende Anforderungen oder nachträglich entdeckte Lücken sind als neue Tickets erfasst

**Evidenz**: Lies das Jira-Ticket direkt und prüfe Status, Sub-Tasks sowie verlinkte Pull Requests oder Branches. Angaben aus dem Prompt ersetzen keinen Abruf aus Jira.

---

## C · Fachliches Dokument aktualisiert

Neue Features ohne Dokumentation sind Features, die niemand richtig nutzen kann. Alle Änderungen, die ein Nutzer oder ein anderes Teammitglied verstehen muss, brauchen ein Dokumentations-Update.

- [ ] Fachliche Feature-Dokumentation in `docs/functional/` angelegt oder aktualisiert (Struktur und Namensschema: `docs/README.md`)
- [ ] Dokument beschreibt fachliches Ziel, betroffene Nutzergruppen, Regeln und relevante Nutzerabläufe
- [ ] Bestehende Dokumentation auf Aktualität geprüft – veraltete Beschreibungen angepasst oder entfernt
- [ ] Screenshots oder Ablaufdiagramme sind aktuell und zeigen den tatsächlichen Zustand des Features

**Evidenz**: Prüfe in `docs/functional/`, ob eine Datei nach dem in `docs/README.md` definierten Namensschema vorhanden ist. Gleiche Ziel, Nutzergruppen, Regeln, Abläufe sowie Screenshots oder Diagramme mit dem aktuellen Feature ab.

---

## D · Glossar aktualisiert

Neue Features bringen oft neue Begriffe mit. Wenn ein Begriff im Ticket oder in der UI verwendet wird, den es vorher nicht gab, gehört er ins Glossar – damit alle dasselbe meinen.

- [ ] Neue fachliche Begriffe, die im Feature oder in der UI auftauchen, sind im Confluence-Glossar (Kapitel 12) ergänzt
- [ ] Bestehende Begriffe, deren Bedeutung sich durch das Feature verändert hat, sind angepasst
- [ ] Abkürzungen und Produktnamen (z.B. neue Integrationsnamen) sind korrekt eingetragen
- [ ] Konsistenz-Check: gleiche Begriffe werden im Ticket, in der UI und in der Doku identisch verwendet

**Evidenz**: Prüfe das Confluence-Glossar in Kapitel 12 sowie Ticket, UI und fachliche Dokumentation auf identische Begriffe und Schreibweisen. Abweichende oder nicht dokumentierte neue Fachbegriffe lassen das Kriterium offen.

---

## E · Hilfebereich / In-App-Hilfe

Nutzer, die eine neue Funktion zum ersten Mal sehen, brauchen Orientierung. Der In-App-Hilfebereich muss mit dem Feature Schritt halten.

- [ ] Betroffene Hilfe-Inhalte in der App sind auf dem aktuellen Stand
- [ ] Neue Features, die nicht selbsterklärend sind, haben einen Hilfe-Eintrag
- [ ] `src/lib/helpKnowledgeIndex.ts` ist aktualisiert, sofern das Feature dort einen Eintrag hat oder braucht
- [ ] Hilfe-Texte sind auf Deutsch und in verständlicher Sprache (kein technisches Kauderwelsch)

**Evidenz**: Prüfe die betroffenen Artikel in `src/data/helpArticles.ts` beziehungsweise `src/data/helpArticles.json`. Wenn für das Feature ein Index-Eintrag erforderlich ist, prüfe zusätzlich `src/lib/helpKnowledgeIndex.ts` auf einen konsistenten Verweis.

---

## F · Fachliche Releasenotes

Releasenotes erklären Nutzern, was sich geändert hat – in ihrer Sprache, nicht in der Sprache der Entwickler. Technische Refactorings tauchen hier nicht auf.

- [ ] `CHANGELOG.md` enthält einen nutzerfreundlichen Eintrag für das Feature (Abschnitt „Hinzugefügt“ / „Geändert“ / „Behoben“)
- [ ] `src/lib/releaseNotes.ts` ist um nutzerrelevante Highlights ergänzt (nur sichtbare Änderungen). Ein Versionssprung in `package.json` erfolgt ausschließlich auf explizite Nutzeranweisung.
- [ ] Sprache: Deutsch, verständlich für Nicht-Entwickler
- [ ] Technische Details (Refactoring, interne Umbauten, Dependency-Updates) gehören nicht in die fachlichen Releasenotes
- [ ] Der Changelog-Eintrag beschreibt den Nutzen für den Anwender – nicht die technische Lösung

**Evidenz**: Prüfe `CHANGELOG.md` und `src/lib/releaseNotes.ts` im aktuellen Diff. Einträge müssen den Nutzen für Anwender beschreiben und dürfen keine rein technischen Implementierungsdetails enthalten.

---

## G · Sprache & Texte

Alle nutzersichtbaren Texte sind korrekt auf Deutsch, konsistent mit dem restlichen Produkt und fehlerfrei formuliert. Englische Restflecken in der UI sind ein Qualitätsmangel.

- [ ] Alle neuen UI-Texte, Buttons, Labels und Beschriftungen sind auf Deutsch
- [ ] Fehlermeldungen sind nutzerfreundlich formuliert – kein Stack-Trace, kein technischer Fachjargon
- [ ] Tooltips, Platzhalter und Hilfstexte sind vorhanden, wo sie nützlich sind
- [ ] Keine englischen Texte in der Benutzeroberfläche (außer explizit als Fachbegriff erwünscht, z.B. „Jira“, „Confluence“)
- [ ] Konsistenz-Check: neue Texte verwenden dieselbe Terminologie wie der Rest der App

**Evidenz**: Prüfe die geänderten Oberflächen auf Buttons, Labels, Fehlermeldungen, Tooltips und Platzhalter. Englische UI-Texte, die keine bewusst verwendeten Fachbegriffe sind, lassen das Kriterium offen.

---

## H · Handover-Dokument vorhanden

Ein Handover-Dokument sichert das Wissen über das Feature. Es ist für das Team, nicht für den Endnutzer – damit beim nächsten Sprint-Review, bei einer Demo oder bei einem Entwicklerwechsel niemand von vorne anfangen muss.

*Dieses Kriterium gilt bei komplexen oder stakeholder-relevanten Features. Bei kleineren Bugfixes kann es entfallen, wenn B und C ausreichend sind.*

- [ ] Handover-Dokument in `docs/handovers/` angelegt oder aktualisiert (Struktur und Namensschema: `docs/README.md`)
- [ ] Enthält: Was wurde gebaut, warum, und welche Einschränkungen / offenen Punkte es gibt
- [ ] Bei Demo-relevanten Features: Demo-Leitfaden in `docs/` aktualisiert
- [ ] Bekannte Bugs oder noch offene Punkte sind explizit aufgeführt (nicht versteckt)

**Evidenz**: Prüfe bei komplexen oder stakeholder-relevanten Features in `docs/handovers/`, ob ein Handover nach dem in `docs/README.md` definierten Namensschema vorhanden ist und Umfang, fachlicher Zweck, Einschränkungen sowie offene Punkte abdeckt.
