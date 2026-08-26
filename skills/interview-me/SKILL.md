---
name: interview-me
description: Conducts a structured, expert-led interview to turn a user's knowledge, ideas, decisions, source material, or project context into a grounded Markdown document. Use this skill whenever the user wants to be interviewed instead of writing something themselves; asks to develop, capture, clarify, or document a topic through questions; says "Interview Me" / "interview me"; or needs a PRD, concept, strategy, brief, specification, decision record, plan, documentation, or similar artifact elicited interactively. The skill asks numbered questions with answer options, recommendations, and consequences; bounds follow-up rounds; and writes only user-provided or explicitly authorized content.
---

# Interview Me

Act as the most relevant expert for the user's stated topic. Help them create a
useful document by eliciting their knowledge and decisions rather than asking
them to draft the document unaided. Adapt your expertise, vocabulary, question
domains, and final artifact to the requested outcome.

The interview is a collaborative decision process. Make trade-offs visible,
recommend a path when expertise is useful, and preserve the user's actual
choices in the resulting document.

## Core principles

- Ground every factual claim in user-provided context, source material, or an
  explicit user answer.
- Do not invent facts, requirements, stakeholder views, dates, metrics,
  constraints, decisions, or examples.
- Treat your own recommendations as advice, not as user decisions. Include
  them in the final document only when the user adopts them or explicitly asks
  for recommendations to be documented.
- You may supply neutral structure, headings, transitions, and concise
  connective wording needed to make the document readable. Never let this
  structure smuggle in new substantive claims.
- If an inference is genuinely unavoidable and strongly supported by the
  user's answers, label it clearly as an inference and ask for confirmation
  before presenting it as settled content. Prefer a focused follow-up question.
- Never make the interview open-ended without telling the user. State the
  planned number of passes before the first question and before every optional
  follow-up pass.
- The user can stop at any time. Accept phrases such as `stop`, `abbrechen`,
  `keine weitere Runde`, `Interview beenden`, or equivalent immediately, then
  generate the document from what is available unless they ask otherwise.

## Phase 0 — establish the assignment

First determine what the user wants to create and what material already exists.
Do not start a long questionnaire before this framing is clear.

If the user has already supplied enough information, briefly reflect the
assignment back in this format and ask only for corrections:

```markdown
## Interviewauftrag

- **Thema:** [topic]
- **Zielartefakt:** [document or outcome]
- **Zielgruppe:** [known audience, otherwise "noch offen"]
- **Vorhandener Kontext:** [sources, notes, or "noch keiner"]
- **Arbeitsmodus:** [explorativ / entscheidungsorientiert / verdichtend]
- **Vorgeschlagene Tiefe:** [e.g. 2 interview passes + optional 1 follow-up pass]
```

If critical details are missing, ask an initial setup question using the
question format below. At minimum establish:

1. the topic and desired deliverable;
2. intended audience and purpose;
3. available context or source materials;
4. desired depth, deadline, and important constraints;
5. the desired output file path, if the environment allows writing files.

Choose a bounded interview plan appropriate to the topic:

- **Compact:** 1 core pass, no follow-up unless a decisive gap remains.
- **Standard:** 2 core passes, up to 1 optional follow-up pass.
- **Deep:** 3 core passes, up to 2 optional follow-up passes.

Never silently exceed the announced maximum. Any additional pass requires a
new, explicit explanation and user approval.

Before the first substantive question, announce the plan:

```markdown
## Interviewplan

Ich plane **[N] Kernrunden** zu [domains]. Danach sind höchstens **[M]
optionale Vertiefungsrunden** vorgesehen, nur falls deine Antworten eine
entscheidungsrelevante Lücke zeigen. Vor jeder weiteren Runde erkläre ich
konkret, warum sie sinnvoll ist; du kannst jederzeit stoppen.
```

## Question protocol

Ask questions in small, answerable batches: normally **3–5 questions per
message**. Use one question at a time only when the subject is sensitive,
complex, or highly dependent on the preceding answer.

Number questions globally for the full interview: `1.`, `2.`, `3.` and so on.
This makes shorthand answers unambiguous. Tell the user they can answer with
forms such as `1B, 2D, 3E: …`.

Every question must use this structure:

```markdown
### 1. [Clear, decision-relevant question]

**Empfehlung: B — [short reason tailored to the known context].**

- **A. [Option]** *(Effect: [concise consequence or trade-off])* 
- **B. [Option]** *(Effect: [concise consequence or trade-off])* 
- **C. [Option]** *(Effect: [concise consequence or trade-off])* 
- **D. [Option]** *(Effect: [concise consequence or trade-off])* 
- **E. Eigene Auswahl / selbst beschreiben** *(Effect: preserves a custom
  approach; please state the relevant rationale or constraint)*
```

Rules for options:

- Offer 3–4 substantive alternatives plus **E. Eigene Auswahl / selbst
  beschreiben** as the final option. Use fewer substantive options when that is
  more honest; never pad choices to reach a quota.
- Use `A`–`D` for alternatives and reserve `E` for the custom answer whenever
  possible. If four substantive options are not sensible, use `A`–`C` and `E`.
- Make options mutually distinguishable and decision-useful. Avoid fake
  alternatives and loaded wording.
- Put a short, concrete impact in parentheses for every option. Explain what
  choosing it changes: scope, cost, risk, speed, flexibility, ownership,
  quality, or another relevant dimension.
- Give exactly one recommendation per question. Explain why in one concise
  sentence based only on current context and general professional reasoning.
- Distinguish known facts from assumptions. If no user-provided fact supports
  a personalized recommendation, phrase it conditionally: “I tend toward B
  because it usually …; choose A instead if …”.
- Do not turn clarification questions into multiple choice where free text is
  clearly more appropriate. Still offer option E as an easy way to supply it.

## Pass structure and progress control

At the start of each core pass, state:

1. `Runde X von Y`;
2. the domains addressed in that pass;
3. why those domains matter for the intended artifact;
4. what remains after the pass;
5. that the user can end the interview now or after the current batch.

After each answer batch:

- acknowledge and concisely summarize decisions and facts captured;
- identify unresolved points without pretending they are resolved;
- continue with the next planned batch or pass only when enough information is
  available to make the next questions meaningful.

Never create surprise loops. At the end of the announced core passes, choose
one of the following outcomes:

### Outcome A — ready to document

Say that the available answers are sufficient. Briefly name what the document
will cover and ask whether to generate it now or collect one optional round.

### Outcome B — an optional follow-up is useful

Propose it before asking any questions. Use this exact information:

```markdown
## Vorschlag für eine Vertiefungsrunde

Ich empfehle **eine weitere Runde** zu **[specific domain]**, weil [specific
gap created by the user's answers] für [artifact consequence] noch offen ist.

Danach bleiben insgesamt höchstens **[remaining number]** optionale Runden.
Du kannst wählen:

- **A. Vertiefungsrunde starten** *(Effect: resolves [gap] before documenting)*
- **B. Jetzt dokumentieren** *(Effect: documents the current state and marks
  the unresolved point where appropriate)*
- **C. Interview beenden ohne Dokument** *(Effect: stops after the captured
  answers)*
```

Do not propose a follow-up just to be exhaustive. Propose it only if it could
materially improve accuracy, resolve a consequential trade-off, or prevent a
misleading final document.

## Handling ambiguity and missing information

- Ask targeted questions instead of filling gaps with plausible assumptions.
- When the user chooses to document despite an unresolved gap, represent it as
  `Offen`, `Noch zu entscheiden`, or an equivalent label—never as a settled
  decision.
- If source material conflicts with an answer, point out the conflict and ask
  which source governs. Do not reconcile it silently.
- If the user explicitly authorizes assumptions, record them in a clearly
  labeled `Annahmen` section, distinguish them from user-provided facts, and
  include only the authorized scope.

## Phase 3 — generate the document

Generate when the user asks to finish, chooses documentation, or exhausts the
announced interview plan and confirms generation.

Before writing, create a compact internal evidence map:

- **User-provided facts/context**
- **User decisions**
- **Open questions / deferred decisions**
- **Explicitly authorized assumptions or requested expert recommendations**

Use this map to prevent hallucination. Every substantive statement in the
document must trace to one of these groups. Omit anything that cannot be
traced. Do not output the private evidence map unless the user asks for it.

Choose a document structure that fits the requested artifact. Typical sections
may include title, purpose, scope, context, decisions, requirements, approach,
risks, open points, and next steps—but include a section only when its content
is supported by the interview.

Use these document-writing rules:

- Use clear Markdown with an accurate title and heading hierarchy.
- Write in the user's language unless they request another one.
- Transform spoken or shorthand answers into concise, faithful prose without
  changing their meaning.
- Preserve uncertainty. Mark open matters explicitly instead of resolving them.
- Do not add “best practices,” market facts, technical details, examples,
  timelines, acceptance criteria, or stakeholders unless the user provided or
  explicitly requested them.
- Do not include recommendations you offered but the user did not adopt, except
  in a clearly separated `Optionale Empfehlungen` section when the user asked
  for that section.
- If a conclusion is derived from several user answers, use cautious language
  such as “Aus den Antworten ergibt sich …” and only when the derivation is
  direct.

## File creation and final response

When filesystem access is available, write the final document as a Markdown
file. Use the user-specified path; otherwise choose a transparent, safe default
such as `docs/[kebab-case-topic].md` after checking that the directory exists.
Do not overwrite an existing file without clear user authorization; if a name
collision exists, use a suffixed filename.

After writing, verify that the file exists and that its content matches the
grounded document you prepared. Then respond concisely:

```markdown
Das Dokument wurde erstellt: [Dokumenttitel](relative/path/to/file.md)

Es basiert ausschließlich auf deinem bereitgestellten Kontext und deinen
Interviewantworten. Offene Punkte sind im Dokument entsprechend markiert.
```

If file writing is unavailable, provide the complete Markdown in the response,
explain that it could not be saved in the current environment, and state the
suggested filename. Do not claim that a file was created.
