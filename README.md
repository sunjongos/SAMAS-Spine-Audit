# 🏥 SAMAS: Spine Audit Multi-Agent System

> **온톨로지 기반 척추수술 보험심사 삭감 방어 자동화 시스템**

SAMAS(Spine Audit Multi-Agent System)는 대한민국 척추수술 보험심사의 복잡한 고시 기준과 임상 데이터를 결합하여, 삭감 리스크를 사전에 차단하고 최적화된 소견서를 생성하는 차세대 AI 시스템입니다.

## 🌟 Key Features

- **Multi-Agent Orchestration:** 연구, 추론, 작문, 검증 에이전트가 협업하여 무결점 보고서 생성.
- **Knowledge-Based RAG:** 2026년 최신 요양급여 책자(1,400p+)를 핀포인트로 파싱하여 실시간 고시 근거 제시.
- **Ontology Reasoning:** 증상(VAS, MMT)-영상(MRI)-고시코드 간의 해부학적 일치성(Clinical Correlation) 자동 검증.
- **Harness Evaluator:** 작성된 소견서를 독립적으로 비판하여 삭감 리스크 점수 산출.
- **Visual Evidence:** Mermaid.js 기반의 지식 그래프(Knowledge Graph) 시각화 제공.

## 🛠️ System Architecture

1.  **NLM Specialist Agent:** 방대한 PDF 지침서에서 필요한 규정만 추출.
2.  **Ontology Reasoner Agent:** RDF/Turtle 기반 온톨로지 모델로 의학적 당위성 추론.
3.  **Defense Writer Agent:** 2026년 HIRA 심사 트렌드를 반영한 전문가용 소견서 작성.
4.  **Harness Auditor:** 삭감 가능성을 3단계로 자가 검증.

## 🚀 Quick Start

### 1. Requirements
- Python 3.10+
- `pypdf`, `rdflib`

### 2. Build Database
방대한 요양급여 책자에서 척추 관련 데이터만 추출하여 로컬 DB를 구축합니다.
```bash
python build_spine_db.py
```

### 3. Run Analysis
환자의 EMR 데이터와 수술 코드를 입력하여 분석 보고서를 생성합니다.
```bash
python samas_orchestrator.py
```

## 📊 Output Example (HTML)
본 시스템은 최종 산출물로 시각화된 그래프가 포함된 프리미엄 HTML 보고서를 생성합니다.

---
**Developed by Director Luca & Antigravity (NDB AI Strategy Group)**
