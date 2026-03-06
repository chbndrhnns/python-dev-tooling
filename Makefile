.PHONY: install lint format check test ci

# Install all deps (including dev) with uv
install:
	uv sync --all-extras

# Lint with ruff
lint:
	uv run ruff check src/ tests/

# Auto-fix lint issues
fix:
	uv run ruff check --fix src/ tests/

# Format code
format:
	uv run ruff format src/ tests/

# Check formatting without modifying files
format-check:
	uv run ruff format --check src/ tests/

# Run tests
test:
	uv run pytest

# Full CI-style check (no auto-fix)
ci: lint format-check test
