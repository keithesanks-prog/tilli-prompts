## Starting SEAL and Prompt Eval

### 1. SEAL API (`/home/keith/seal`)
- `cd /home/keith/seal`
- `source venv/bin/activate`
- `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
- Verify: `curl http://localhost:8000/health`

### 2. Prompt Eval Tool (`/home/keith/prompt-eval-tool`)
- `cd /home/keith/prompt-eval-tool`
- `source .venv/bin/activate`
- `streamlit run app.py --server.port 8501`
- In the Streamlit sidebar, enable “Use SEAL API for generation” and set the SEAL URL to `http://localhost:8000`

