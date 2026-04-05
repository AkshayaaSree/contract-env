tasks = [
    {
        "type": "clause_classification",
        "contract": """This Agreement shall terminate immediately upon written notice if either party materially breaches any obligation and fails to cure such breach within 30 days.""",
        "expected": {
            "label": "termination"
        }
    },
    {
        "type": "risk_detection",
        "contract": """The vendor shall not be liable for any indirect, incidental, or consequential damages, including loss of profits, even if advised of the possibility of such damages. The client assumes all risks.""",
        "expected": {
            "risk_keywords": ["liable", "no liability", "one-sided", "all risks"],
            "severity": "high"
        }
    },
    {
        "type": "contract_improvement",
        "contract": """The vendor shall not be liable for any damages under this agreement.""",
        "expected": {
            "must_include": ["limit", "cap", "reasonable"],
            "goal": "reduce risk"
        }
    }
]