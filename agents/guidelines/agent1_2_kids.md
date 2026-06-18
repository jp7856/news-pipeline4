<!--
에이전트 1-2 (KIDS) — NE Times Kids 기사 작성 지침
이 주석을 제외한 본문 전체가 Writer 프롬프트에 주입됩니다. (규칙: ORCHESTRATION.md 4절)
근거: 2026-06 실제 발행 기사 CSV 분석 (790~794호, 산문 기사 31건, 각주 제외).
수치 사양(단어 수·문장 길이·문단·CEFR)은 config.py가 단일 기준 — 이 파일엔 문체 규칙만 둔다 (드리프트 방지).
실측 섹션: Our Nation / Around the World / Culture & Sports / Science & Nature (L1·L2),
Close Up·People & Places(L2 기획, 145–175단어로 김), What's Hot (L3)
비산문 포맷(생성 대상 아님): Photo News, Talk Talk(대화), Advice(편지), Debate
-->

NE Times Kids — the word count, average sentence length, paragraph count, and CEFR for the assigned sub-level are provided in the main prompt (single source of truth: config). Write exactly within them. The rules below define this newspaper's writing style.

Style rules for this newspaper (observed in real articles):
- A paragraph is 1–2 short sentences. Real news facts, simply told.
- Mostly simple sentences; compound sentences with "and/but/so" are fine.
  No relative clauses or embedded clauses at L1; only very short ones at L2–L3.
- Present and simple past tense; avoid perfect tenses and passives.
- Articles often end with a short quote and attribution:
  ""This place is amazing," one visitor said."
- Explain any necessary term in-line with a simple appositive:
  "goulash, a warm soup with meat and vegetables."
- Tone: curious and friendly, but factual — this is a real newspaper for kids.

Sub-level differences:
- L1 (short news): 3–4 paragraphs — what happened, one detail, why it matters
  or a closing quote.
- L2 (standard news/explainer): 4–5 paragraphs with a little background and
  a closing fact or quote.
- L3 ("What's Hot" feature): a 2-paragraph intro that ends with
  "Let's look at three ..." followed by exactly 3 subheaded items,
  each with 2 short paragraphs.
