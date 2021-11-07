# Note

1. Install dependencies `cd` into the directory where the `pyproject.toml` is located then `poetry install`
2. Run the DB migrations via poetry `poetry run ./scripts/prestart.sh` (only required once)
3. Run the FastAPI server via poetry `poetry run ./scripts/run.sh`
4. Open http://localhost:8000/
