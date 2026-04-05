# Contract Review OpenEnv

## Overview
This environment simulates real-world legal contract review workflows. Agents must classify clauses, detect risks, and propose safer alternatives.

## Tasks
- Clause Classification (Easy)
- Risk Detection (Medium)
- Contract Improvement (Hard)

## Action Space
Agent provides textual analysis or suggestions.

## Observation Space
- Contract text
- Task type
- Instructions
- Previous actions

## Reward Design
- Partial credit via keyword matching
- Bonus for detailed reasoning
- Penalties for vague or repeated answers
- Completion bonus

## Setup
```bash
pip install -r requirements.txt
uvicorn server:app --host 0.0.0.0 --port 7860