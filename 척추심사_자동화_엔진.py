import os
import json

class SpineReviewOntologyEngine:
    """
    온톨로지 기반 척추수술 보험심사 및 소견서 자동 생성 엔진
    """
    def __init__(self):
        # 온톨로지 규칙 정의 (Knowledge Base)
        self.ontology_rules = {
            "N1493": {
                "name": "추간판절제술",
                "essential": ["vas", "motor", "mri_root_compression", "conservative_tx"],
                "critical_check": "하지 방사통 기록 필수",
                "template_path": "템플릿/N1493_템플릿.md"
            },
            "N1499": {
                "name": "요추후궁절제술",
                "essential": ["vas", "claudication", "mri_stenosis", "functional_limit"],
                "critical_check": "보행 파행(Claudication) 및 보행 가능 거리 필수",
                "template_path": "템플릿/N1499_템플릿.md"
            },
            "N2470": {
                "name": "TLIF 유합술",
                "essential": ["vas", "instability", "longterm_conservative_tx", "recent_conservative_tx"],
                "critical_check": "최근 1년 3개월 이상의 보존적 치료 기록 필수",
                "template_path": "템플릿/N2470_템플릿.md"
            },
            "자46": {
                "name": "척추고정술",
                "essential": ["instability_radiology", "flexion_extension_xray"],
                "critical_check": "동적 X-ray상 시상면 전위 4mm 이상 확인 필수",
                "template_path": "템플릿/자46_템플릿.md"
            }
        }

    def analyze_clinical_data(self, data):
        """
        입력된 임상 데이터를 온톨로지 규칙과 대조하여 분석
        """
        code = data.get("surgery_code")
        if code not in self.ontology_rules:
            return {"status": "error", "message": f"정의되지 않은 수술코드입니다: {code}"}

        rules = self.ontology_rules[code]
        missing_items = []
        findings = data.get("findings", {})

        # 필수 항목 체크
        for item in rules["essential"]:
            if item not in findings or not findings[item]:
                missing_items.append(item)

        # 삭감 방어 논리 생성
        defense_logic = f"본 환자는 {rules['name']}({code})의 급여 기준을 충족함. "
        if not missing_items:
            defense_logic += "모든 필수 임상 및 영상학적 지표가 문서화되어 있어 삭감 방어력이 높음."
        else:
            defense_logic += f"주의: 현재 기록상 {', '.join(missing_items)} 항목이 누락되어 보완이 필요함."

        return {
            "code": code,
            "rules": rules,
            "missing_items": missing_items,
            "defense_logic": defense_logic,
            "data": data,
            "mermaid_graph": self.generate_mermaid(code, rules, missing_items)
        }

    def generate_mermaid(self, code, rules, missing_items):
        """
        분석 결과를 Mermaid 지식 그래프 코드로 변환
        """
        mermaid = "graph LR\n"
        mermaid += f"    Patient[환자 사례] --> |수술코드| {code}[{rules['name']}]\n"
        
        for item in rules["essential"]:
            status = "Verified" if item not in missing_items else "Missing"
            color = "green" if status == "Verified" else "red"
            mermaid += f"    {code} --> |Required| {item}[{item}]\n"
            mermaid += f"    {item} -.-> |{status}| {item}_stat(({status}))\n"
        
        mermaid += f"    {code} --> |Review| Standard[2025 HIRA 기준]\n"
        return mermaid

    def generate_draft(self, analysis):
        """
        분석 결과를 바탕으로 소견서 초안 생성
        """
        if "status" in analysis and analysis["status"] == "error":
            return analysis["message"]

        # 실제로는 템플릿 파일을 읽어서 변수를 치환하는 로직이 들어감
        draft = f"--- 척추수술 보험심사 소견서 (Draft) ---\n"
        draft += f"수술코드: {analysis['code']} ({analysis['rules']['name']})\n"
        draft += f"삭감 방어 논리: {analysis['defense_logic']}\n\n"
        
        if analysis['missing_items']:
            draft += "[⚠️ 추가 기재 필요 항목]\n"
            for item in analysis['missing_items']:
                draft += f"- {item}: 의무기록 재검토 후 구체적 수치(VAS/Grade 등) 보완 필요\n"
        
        draft += "\n[소견서 본문 요약]\n"
        findings = analysis['data'].get('findings', {})
        draft += f"- 임상증상: {findings.get('symptoms', '기록 없음')}\n"
        draft += f"- 영상학적 근거: {findings.get('imaging', '기록 없음')}\n"
        draft += f"- 보존적 치료: {findings.get('conservative_detail', '기록 없음')}\n"
        
        draft += "\n[2. 근거 온톨로지 지식 그래프]\n"
        draft += "```mermaid\n"
        draft += analysis.get('mermaid_graph', '')
        draft += "```\n"
        
        return draft

# --- 실행 예시 ---
if __name__ == "__main__":
    engine = SpineReviewOntologyEngine()

    # 예시 데이터: TLIF 수술인데 보존치료 기간이 누락된 경우
    mock_patient_data = {
        "surgery_code": "N2470",
        "findings": {
            "vas": "8/10",
            "instability": "L4/5 Spondylolisthesis confirmed",
            "symptoms": "양하지 방사통 및 요통 심함",
            "imaging": "MRI상 L4/5 severe stenosis 동반",
            # "longterm_conservative_tx": None, # 누락됨
            "conservative_detail": "신경차단술 2회 시행함"
        }
    }

    result = engine.analyze_clinical_data(mock_patient_data)
    print(engine.generate_draft(result))
