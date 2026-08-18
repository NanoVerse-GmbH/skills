# NanoVerse Definition of Done – Fachlich

Diese Referenz ist die für den Skill maßgebliche, eigenständige Fassung der
fachlichen Definition of Done. Prüfe nur die Kriterien, die auf den tatsächlichen
Featureumfang zutreffen. Begründe jede Nichtanwendbarkeit.

## A · Anforderungen vollständig erfüllt (DoR-Reifegrad)

Das Ticket ist fachlich umgesetzt, nicht lediglich technisch implementiert.

- Alle Akzeptanzkriterien sind manuell oder automatisch verifiziert.
- Alle definierten Nutzerabläufe funktionieren end-to-end.
- Fehlerzustände und Edge Cases sind fachlich abgedeckt.
- Das Verhalten ist in den im Ticket beschriebenen Szenarien konsistent.
- Abweichungen vom beschriebenen Verhalten sind dokumentiert und mit dem Product Owner abgestimmt.

## B · Jira-Ticket ist aktuell

Das Ticket bildet den tatsächlichen Lieferstand nachvollziehbar ab.

- Status entspricht dem vorgesehenen Abschluss- oder Review-Status.
- Planabweichungen sind in Beschreibung oder ACs aktualisiert.
- Sub-Tasks sind abgeschlossen oder als nicht benötigt begründet.
- Relevante Pull Requests oder Branches sind verlinkt.
- Neu entdeckte Lücken sind als neue Tickets erfasst.

## C · Fachliches Dokument aktualisiert

Nutzer- und fachrelevantes Wissen ist im Repository auffindbar.

- Feature-Dokumentation in `docs/functional/` angelegt oder aktualisiert.
- Sie beschreibt Ziel, Nutzergruppen, Regeln und relevante Abläufe.
- Bestehende Dokumentation ist auf Aktualität geprüft und bereinigt.
- Screenshots oder Ablaufdiagramme zeigen den tatsächlichen Stand, sofern sie für das Feature sinnvoll sind.

## D · Glossar aktualisiert

Produktbegriffe werden eindeutig und durchgängig verwendet.

- Neue fachliche Begriffe in Ticket oder UI sind im Confluence-Glossar (Kapitel 12) ergänzt.
- Veränderte Begriffe sind angepasst.
- Abkürzungen und Produktnamen sind korrekt eingetragen.
- Ticket, UI und Dokumentation verwenden dieselbe Terminologie.

## E · Hilfebereich / In-App-Hilfe

Nicht selbsterklärende Funktionen unterstützen Anwender beim Einstieg.

- Betroffene Hilfe-Inhalte sind aktuell.
- Neue, nicht selbsterklärende Funktionen besitzen einen Hilfe-Eintrag.
- `src/lib/helpKnowledgeIndex.ts` ist angepasst, sofern dort ein Eintrag besteht oder benötigt wird.
- Hilfe-Texte sind verständlich und deutschsprachig.

## F · Fachliche Releasenotes

Sichtbare Produktänderungen sind für Anwender verständlich beschrieben.

- `CHANGELOG.md` enthält einen nutzerfreundlichen Eintrag in der passenden Kategorie.
- `src/lib/releaseNotes.ts` enthält sichtbare, nutzerrelevante Highlights.
- Sprache ist Deutsch und für Nicht-Entwickler verständlich.
- Interne technische Umbauten und Dependency-Details fehlen.
- Der Nutzen für Anwender steht im Mittelpunkt.

## G · Sprache & Texte

Alle neuen nutzersichtbaren Inhalte sind verständlich und produktkonsistent.

- Texte, Buttons, Labels und Beschriftungen sind Deutsch.
- Fehlermeldungen sind handlungsorientiert und frei von technischen Details.
- Tooltips, Platzhalter und Hilfen sind vorhanden, wo sie Orientierung schaffen.
- Keine unbeabsichtigten englischen UI-Reste sind sichtbar.
- Neue Texte verwenden die bestehende Produktterminologie.

## H · Handover-Dokument vorhanden

Dieses Kriterium gilt für komplexe oder stakeholder-relevante Features. Kleine
Bugfixes können es begründet als nicht anwendbar markieren, wenn Ticket- und
Feature-Dokumentation ausreichen.

- Handover in `docs/handovers/` angelegt oder aktualisiert.
- Es beschreibt Umfang, Zweck, Einschränkungen und offene Punkte.
- Bei demo-relevanten Features ist ein Demo-Leitfaden aktualisiert.
- Bekannte Bugs und offene Punkte sind sichtbar dokumentiert.
