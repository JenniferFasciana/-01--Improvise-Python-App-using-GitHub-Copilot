# Jennifer's Python API

A small FastAPI application with a welcome endpoint and an endpoint that accepts text and returns its MD5 checksum.

## Dependencies

- FastAPI
- Uvicorn
- pytest
- httpx

## Installation

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install fastapi uvicorn pytest httpx
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Start the application

From the project directory, run:

```bash
uvicorn main:app --reload
```

The API will be available at <http://127.0.0.1:8000>. Open <http://127.0.0.1:8000/docs> for the interactive API documentation.

## Generate a checksum

Send a `POST` request to `/generate/` with a JSON body containing a string field named `text`:

```bash
curl -X POST http://127.0.0.1:8000/generate/ \
  -H "Content-Type: application/json" \
  -d '{"text": "hello"}'
```

The response contains the text's MD5 checksum:

```json
{"checksum": "5d41402abc4b2a76b9719d911017c592"}
```

## Run the tests

With the virtual environment active, run:

```bash
pytest
```
