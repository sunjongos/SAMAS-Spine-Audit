---
name: Spine Audit Multi-Agent System (초고성능 척추 심사 멀티 에이전트 시스템)
description: NotebookLM CLI + 온톨로지 지식 그래프 + Multi-Agent Teams(Harness) 체제를 결합하여 2026년 요양급여 책자의 방대한 데이터를 실시간으로 파싱하고 삭감 제로를 달성하는 최고 지능의 보험 심사 스킬입니다.
---

# 🏥 Spine Audit Multi-Agent System (SAMAS)

본 스킬은 단일 LLM의 컨텍스트 한계(Lost in the Middle)를 극복하기 위해 **분산형 멀티 에이전트 아키텍처**를 채택했습니다. 2026년 최신 보험 심사 책자의 방대한 텍스트를 NotebookLM CLI로 정밀 타격하여 가져오고, 온톨로지 엔진으로 논리적 무결성을 검증합니다.

## 🎭 에이전트 팀 구성 (Multi-Agent Team)

1.  **[Lead] Luca Orchestrator:** 전체 공정을 지휘하고 에이전트 간 데이터를 조율합니다.
2.  **[Research] NLM Specialist:** `nlm` CLI를 통해 2026년 요양급여 책자에서 해당 수술코드의 최신 심사 지침과 고시 원문을 실시간으로 추출합니다.
3.  **[Logic] Ontology Reasoner:** 추출된 고시 원문과 환자의 EMR 데이터를 온톨로지 그래프상에서 대조하여 논리적 모순과 누락을 식별합니다.
4.  **[Tactics] Defense Writer:** 심사관의 논리를 역이용하는 '삭감 방어용 전문 용어'를 사용하여 소견서 초안을 작성하고 지식 그래프를 시각화합니다.
5.  **[Audit] Harness Evaluator:** 최종 결과물을 독립적으로 검토하여 삭감 리스크 점수를 산출하고 미비점을 보완하도록 환류(Feedback)를 보냅니다.

## 🧠 기술적 특징 (Technical Excellence)

- **Context Optimization:** 방대한 PDF 책자를 직접 컨텍스트에 넣지 않고, `nlm query`를 통해 필요한 파트만 핀포인트로 추출하여 LLM의 'Lost in the Middle' 현상을 방지합니다.
- **Ontology Alignment:** 단순 RAG를 넘어, 온톨로지에 정의된 척추 수술의 상관관계(증상-영상-코드)를 기준으로 팩트 체크를 수행합니다.
- **Harness Mode:** 생성된 소견서가 실제 심평원 기준에 부합하는지 3단계 자가 검증을 거칩니다.

## 🚀 운영 지침 (Operational Protocols)

### 1단계: 책자 실시간 쿼리 (nlm CLI)
- 수술코드가 확인되면 즉시 NotebookLM에 해당 코드의 최신 기준(보존적 치료 기간, 조기수술 사유 등)을 질의합니다.
- **Command:** `nlm notebook query <id> "N2470 수술의 최신 급여 기준과 보존적 치료 기간 요건을 책자 원문 근거로 정리해줘"`

### 2단계: 온톨로지 추론 (Ontology Engine)
- NLM 에이전트가 가져온 '공식 기준'과 '환자 데이터'를 매핑합니다.
- **핵심:** 고시 문구의 키워드가 EMR에 '구조화'되어 있는지 확인합니다.

### 3단계: 삭감 방어 소견서 작성
- `템플릿/`을 기본으로 하되, NLM에서 가져온 최신 고시 번호와 날짜를 소견서 전면에 배치하여 공신력을 높입니다.

### 4단계: 하니스(Harness) 검증
- 작성된 소견서에서 누락된 키워드가 있는지, 혹은 고시 기준과 상충되는 표현이 있는지 최종 체크합니다.

## 📂 파일 구조
- `SKILL.md`: 본 스킬 명세서
- `samas_orchestrator.py`: 멀티 에이전트 제어 엔진
- `nlm_specialist.py`: NotebookLM CLI 연동 모듈
- `harness_evaluator.py`: 삭감 리스크 검증 모듈

---
**Director Luca's Promise:** "우리는 단순한 글쓰기가 아니라, 데이터와 규정의 완벽한 결합을 통한 경영 방어를 목표로 합니다."
