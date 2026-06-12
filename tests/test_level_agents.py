"""에이전트 1-1 ~ 1-5 분리 검증 — 라우팅·지침 로딩·프롬프트 주입."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from models import Level
from config import LEVEL_CONFIG
from agents.level_agents import AGENT1_BY_LEVEL, create_agent1
from agents.content_producer import ContentProducerAgent, GUIDELINES_DIR
from agents.sub_agents.writer import WriterAgent
from agents.translator import _LEVEL_STYLE

# 1) 5개 레벨 모두 라우팅 등록 + LEVEL_CONFIG/번역 스타일 존재
assert len(AGENT1_BY_LEVEL) == 5
for lv in Level:
    assert lv in AGENT1_BY_LEVEL, f"{lv} 라우팅 누락"
    assert lv.value in LEVEL_CONFIG, f"{lv.value} LEVEL_CONFIG 누락"
    assert lv.value in _LEVEL_STYLE, f"{lv.value} 번역 스타일 누락"
print("routing OK")

# 2) 에이전트 라벨·지침 파일 매핑
expected = {
    Level.KINDER: ("Agent1-1 KINDER", "agent1_1_kinder.md"),
    Level.KIDS: ("Agent1-2 KIDS", "agent1_2_kids.md"),
    Level.JUNIOR: ("Agent1-3 JUNIOR", "agent1_3_junior.md"),
    Level.TIMES: ("Agent1-4 TIMES", "agent1_4_times.md"),
    Level.JUNIOR_M: ("Agent1-5 JUNIOR M", "agent1_5_junior_m.md"),
}
for lv, (label, fname) in expected.items():
    cls = AGENT1_BY_LEVEL[lv]
    assert cls.AGENT_LABEL == label, (cls.AGENT_LABEL, label)
    assert cls.GUIDELINE_FILE == fname
    assert (GUIDELINES_DIR / fname).exists(), f"{fname} 파일 없음"
print("labels & files OK")

# 3) 지침 로딩 — 주석만 있는 placeholder는 빈 문자열(주입 안 함)
agent = create_agent1(Level.JUNIOR)
assert agent.AGENT_LABEL == "Agent1-3 JUNIOR"
assert agent._guidelines == "", f"placeholder인데 지침이 로드됨: {agent._guidelines[:80]!r}"
print("placeholder skip OK")

# 4) 지침 본문이 있으면 로드되고 주석은 제거됨
test_md = GUIDELINES_DIR / "_test_tmp.md"
test_md.write_text("<!-- 메모: 주입 금지 -->\n제목은 항상 의문문으로.\n", encoding="utf-8")
try:
    class _TmpAgent(ContentProducerAgent):
        GUIDELINE_FILE = "_test_tmp.md"
    tmp = _TmpAgent.__new__(_TmpAgent)
    tmp._log = lambda m: None
    loaded = tmp._load_guidelines()
    assert loaded == "제목은 항상 의문문으로.", repr(loaded)
finally:
    test_md.unlink()
print("guideline load OK")

# 5) Writer 프롬프트 주입 헬퍼
cfg = LEVEL_CONFIG["junior"]
assert WriterAgent._guideline_hint("", cfg) == ""
hint = WriterAgent._guideline_hint("제목은 의문문", cfg)
assert "NE Times Junior" in hint and "제목은 의문문" in hint
print("prompt injection OK")

print("ALL TESTS PASSED")
