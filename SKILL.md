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
5.  **[Audit] Harness Evaluator:** 인터랙티브 리스크 평가 도구를 통해 최종 결과물을 검토합니다.

## 🧠 기술적 특징 (Technical Excellence)

- **Context Optimization:** 방대한 PDF 책자를 직접 컨텍스트에 넣지 않고, `nlm query`를 통해 필요한 파트만 핀포인트로 추출합니다.
- **Ontology Alignment:** 척추 수술의 상관관계(증상-영상-코드)를 기준으로 팩트 체크를 수행합니다.
- **Premium Reporting:** 원클릭 복사 및 실시간 리스크 시뮬레이션이 가능한 HTML 보고서를 생성합니다.

## 🚀 운영 지침 (Operational Protocols)

### 1단계: 책자 실시간 쿼리 (nlm CLI)
- 수술코드 확인 후 NotebookLM에 해당 코드의 최신 기준을 질의합니다.

### 2단계: 온톨로지 추론 (Ontology Engine)
- 공식 기준과 환자 데이터를 매핑하여 논리적 무결성을 검증합니다.

### 3단계: 인터랙티브 리스크 평가 및 작성
- 소견서를 작성하고 사용자가 직접 리스크를 조정할 수 있는 툴을 포함합니다.

### 4단계: 최종 리포팅 (Premium Output)
에이전트는 반드시 다음 요소가 포함된 **인터랙티브 HTML 보고서**를 생성하고 즉시 실행(`Start-Process`)해야 합니다.
1. **보험 심사 삭감 방어 소견서:** [복사하기] 버튼 포함.
2. **Harness 인터랙티브 리스크 평가 도구:** 실시간 점수 계산기 포함.
3. **근거 온톨로지 지식 그래프:** Mermaid.js 시각화.

## 📄 표준 운영 원칙 (Standard Operating Procedure)
- 모든 보고서는 `SAMAS_최종_보고서_코드_날짜.html` 형식으로 저장한다.
- 생성 즉시 대표님의 화면에 팝업으로 띄운다.
- 온톨로지 엔진은 매주 최신 고시 DB와 동기화한다.

---
**Director Luca's Promise:** "우리는 단순한 글쓰기가 아니라, 데이터와 규정의 완벽한 결합을 통한 경영 방어를 목표로 합니다."
