<!--
에이전트 1-3 (JUNIOR) — NE Times Junior 기사 작성 지침
이 주석을 제외한 본문 전체가 Writer 프롬프트에 주입됩니다. (규칙: ORCHESTRATION.md 4절)
근거: 2026-06 실제 발행 기사 CSV 분석 (126~130호, 산문 기사 35건, 각주 제외).
수치 사양(단어 수·문장 길이·문단·CEFR)은 config.py가 단일 기준 — 이 파일엔 문체 규칙만 둔다 (드리프트 방지).
실측 섹션: National/World News, Science, Lifestyle&Culture, Sports&Entertainment (L1·L2),
Focus / People / World Tour (L3, 소제목 2개 구조)
비산문 포맷(생성 대상 아님): Photo News, Did You Know, Debate, NE You(편지·대화)
-->

NE Times Junior — the word count, average sentence length, paragraph count, and CEFR for the assigned sub-level are provided in the main prompt (single source of truth: config). Write exactly within them. The rules below define this newspaper's writing style.

Style rules for this newspaper (observed in real articles):
- Standard news register, inverted pyramid: the first paragraph states what
  happened; the final paragraph gives significance, reaction, or outlook.
- A paragraph is 2–3 sentences. Mix short and medium sentences.
- Compound and simple complex sentences are expected (because/when/if/that-clauses,
  basic relative clauses). Do not stack more than one subordinate clause.
- Tense variety is normal (present, past, present perfect); simple passives okay.
- Connectives appear naturally: However, Meanwhile, In addition, As a result.
- Quotes with attribution are common: ""Drivers say protecting young people is
  rewarding," ..." — include one when the topic allows.
- Topic-specific terms are allowed; gloss briefly in-line at first use.

Sub-level differences:
- L1 (straight news): exactly 4 paragraphs — event, background, detail,
  reaction/outlook. Keep structures on the simpler side.
- L2 (news/explainer): 4–5 paragraphs with fuller background or a step-by-step
  explanation (science topics often explain a process).
- L3 (Focus/People/World Tour feature): a 1–2 paragraph intro, then exactly
  2 subheaded sections (noun-phrase subheadings like "History of Everland",
  "Cause of the Accident"), each with 1–2 paragraphs.
