# Tilli Prompts

Shared prompt templates and Pydantic schemas for SEAL and Prompt-Eval-Tool projects.

## Installation

### Option 1: Install as editable package (for local development)

```bash
cd tilli-prompts
pip install -e .
```

### Option 2: Install from Git (for production)

```bash
pip install git+https://github.com/yourorg/tilli-prompts.git
```

### Option 3: Install from local path (for development)

```bash
pip install -e /path/to/tilli-prompts
```

## Usage

```python
from tilli_prompts import InterventionPrompt, CurriculumPrompt
from tilli_prompts.schemas import InterventionPlan, CurriculumResponse

# Generate intervention prompt
prompt_data = {
    "class_id": "CLASS_5A_2024",
    "num_students": 25,
    "deficient_area": "EMT2",
    "emt1_avg": 65.0,
    "emt2_avg": 58.0,
    "emt3_avg": 72.0,
    "emt4_avg": 63.0,
}
prompt = InterventionPrompt.get_prompt("gemini", prompt_data)

# Generate curriculum prompt
curriculum_data = {
    "grade_level": "2",
    "skill_areas": ["emotional_awareness", "emotional_regulation"],
    "score": 65.5,
}
curriculum_prompt = CurriculumPrompt.get_prompt("gemini", curriculum_data)
```

## Structure

```
tilli-prompts/
├── tilli_prompts/
│   ├── prompts/
│   │   ├── intervention.py
│   │   └── curriculum.py
│   └── schemas/
│       ├── base.py
│       └── curriculum.py
├── pyproject.toml
└── README.md
```

## Integration with SEAL and Prompt-Eval-Tool

Both repositories can import from this shared package:

**SEAL:**
```python
from tilli_prompts import InterventionPrompt, InterventionPlan
```

**Prompt-Eval-Tool:**
```python
from tilli_prompts import InterventionPrompt, CurriculumPrompt
```

## Development

```bash
# Install in development mode
pip install -e .

# Run tests
pytest

# Format code
black .
```

