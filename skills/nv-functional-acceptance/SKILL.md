---
name: nv-functional-acceptance
description: >
  Führt die NanoVerse-fachliche Abnahme eines implementierten Features anhand der
  eingebetteten funktionalen Definition of Done durch und erstellt eine formale
  Übergabe für die technische Abnahme. Verwende diesen Skill immer, wenn jemand
  eine fachliche Abnahme, Produktabnahme, Feature-Abnahme, fachlichen DoD-Check,
  UAT oder eine Übergabe von fachlicher zu technischer Prüfung verlangt – auch
  bei Formulierungen wie "fachlich done?", "ACs abnehmen", "Feature prüfen" oder
  "an die technische Abnahme übergeben". Dieser Skill bewertet ausdrücklich
  keine technische Qualität und ersetzt keine technische Abnahme.
metadata:
  author: NanoVerse
  version: "1.0.0"
---

# NanoVerse – Fachliche Abnahme

## Zweck und Abgrenzung

Prüfe, ob ein Feature aus Sicht von Produkt, Nutzerinnen und Nutzern sowie dem
Jira-Auftrag fachlich fertig ist. Die Entscheidung bezieht sich ausschließlich
auf die Kriterien in [references/functional-dod.md](references/functional-dod.md).
Diese Referenz ist Teil des Skills; fordere keine externe DoD-Datei an.

Die technische Abnahme ist ein getrennter Arbeitsschritt einer anderen Rolle.
Prüfe oder bewerte daher nicht Architektur, Codequalität, Tests, Build,
Security, Performance oder technische Integrationen. Halte technische Risiken
oder Beobachtungen nur als Übergabehinweis fest, ohne daraus ein fachliches
Urteil abzuleiten.

## Benötigter Kontext

Sammle aus dem Ticket, dem verfügbaren Arbeitsstand und den vorhandenen
Artefakten mindestens:

- Ticket- oder Feature-ID und fachliches Ziel,
- Akzeptanzkriterien, Nutzergruppen und relevante Nutzerabläufe,
- nachprüfbare Evidenz (z. B. Demo, Screenshots, Testprotokoll, Dokumentation),
- bekannte Abweichungen, Einschränkungen und offene Punkte.

Fehlt entscheidende Evidenz, markiere den Punkt als **blockiert** statt ihn zu
erraten. Ein Kriterium darf nur dann als **nicht anwendbar** gelten, wenn die
Begründung konkret auf den Featureumfang eingeht.

## Ablauf

1. Lies die eingebettete funktionale DoD-Referenz vollständig.
2. Ordne jedes Kriterium A–H dem Feature als `erfüllt`, `offen`, `blockiert` oder
   `nicht anwendbar` zu. Notiere für jeden Status Evidenz bzw. Begründung.
3. Prüfe die ACs und fachlich beschriebenen Fehler- und Randfälle aus Nutzer- und
   Produktperspektive. Eine rein technische Fehlermeldung genügt nicht als
   fachliche Abdeckung.
4. Prüfe die geforderten Fachartefakte risikobasiert: Jira-Aktualität,
   Feature-Dokumentation, Glossar, Hilfe, Releasenotes, Texte und Handover.
5. Entscheide:
   - **PASS**: alle anwendbaren Kriterien sind erfüllt;
   - **FAIL**: mindestens ein anwendbares Kriterium ist offen oder nicht erfüllt;
   - **BLOCKIERT**: die Entscheidung scheitert an fehlender Evidenz oder einer
     externen Abhängigkeit.
6. Erstelle die formale technische Übergabe anhand von
   [templates/technical-handover.md](templates/technical-handover.md).

## Ergebnisregeln

- Lies vor dem Schreiben sowohl die DoD-Referenz als auch das Template.
- Kopiere die Überschriften, Tabellenstruktur und die acht Kriterien A–H aus
  `templates/technical-handover.md` unverändert in das Ergebnis. Benenne sie
  nicht um, teile sie nicht auf und ersetze sie nicht durch eigene Kategorien.
  Das fest definierte Schema macht die Übergabe für die technische Rolle
  vergleichbar und weiterverarbeitbar.
- Verweise auf konkrete Artefakte und Tickets statt pauschal „geprüft“ zu
  schreiben.
- Dokumentiere Abweichungen offen; eine unvollständige fachliche Abnahme darf
  nicht als PASS erscheinen.
- Eine PASS-Übergabe bedeutet nur „fachlich abgenommen“. Sie ist weder eine
  technische Freigabe noch ein Deploy- oder Releaseentscheid.

## Pflegevertrag

`references/functional-dod.md` ist die ausführbare, eingebettete Fassung der
funktionalen DoD. Ändert sich `dod-functional.md`, aktualisiere in derselben
Änderung diese Referenz und prüfe das Template sowie die Evals auf Konsistenz.
