# SCOUT

SCOUT V1 monorepo: Python 3.12 / FastAPI backend, PostgreSQL 16, and a reserved
Next.js / TypeScript frontend directory.

## Local setup

Prerequisites: Docker Engine or Docker Desktop with Docker Compose v2. `make` is
optional; equivalent commands are shown below.

1. Clone this repository and enter its directory.
2. Copy `.env.example` to `.env` (`cp .env.example .env`). Values are local-only
   placeholders; use URL-safe database credentials. Keep `.env` out of Git.
3. Run `make up` (or `docker compose up --build --wait`). The API waits for a
   healthy database. A plain `docker compose up` also builds and starts both services.
4. Open http://localhost:8000/ (returns `{"name":"SCOUT"}`) or
   http://localhost:8000/docs. Check container health with `docker compose ps`.
5. Run `make test` and `make lint` using the container commands below.
6. Run `make down` (`docker compose down`) when finished. Database data remains
   in the named volume. `docker compose down --volumes` deletes local database data.

| Task | Command without Make |
| --- | --- |
| Up | `docker compose up --build --wait` |
| Down | `docker compose down` |
| Test | `docker compose run --build --rm api python -m pytest -p no:cacheprovider` |
| Lint | `docker compose run --build --rm --no-deps api ruff check --no-cache .` |

The image includes development tools and runs as a non-root user. Rebuild after
code changes. PostgreSQL is accessible only within the Compose network. The API
binds to localhost; change `API_PORT` in `.env` if port 8000 is occupied. Database
initialization variables apply only when the database volume is empty.

## Layout and configuration

- `backend/scout/`: app factory, minimal root route, Pydantic Settings configuration.
- `backend/tests/`: deterministic FastAPI TestClient smoke test.
- `frontend/`: placeholder for SCOUT-011.
- `docs/`: project documentation and safety invariants.

Pydantic Settings reads `APP_NAME` and required `DATABASE_URL` from environment
variables or `.env` in the process working directory. Compose constructs its URL
using the database settings and service hostname `db`; the example standalone URL
is for a separately available local database. Database connections, models,
migrations, and the health endpoint arrive in later issues. The container health
probe currently requests `/` and does not test database connectivity.

For Python-only development with Python 3.12, create and activate a virtual
environment, then run `pip install -e './backend[dev]'`. From `backend/`, run
`pytest` and `ruff check .`. The smoke test supplies its own configuration and
requires no database. Running the server from the repository root uses `.env`:
`uvicorn scout.main:app --reload`.

Never fabricate candidate data: missing values remain NULL and are flagged.
No application may be submitted without explicit human approval.
