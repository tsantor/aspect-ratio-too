set shell := ["bash", "-cu"]
# set shell := ["powershell.exe", "-NoLogo", "-Command"]

# List all available recipes
default:
  @just --list

# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------

python_version := "3.13.1"
aws_profile := "xstudios"
s3_bucket := "xstudios-pypi"
cov_fail_under := "44"

# Dynamic variables (evaluated at runtime - DO NOT EDIT)
package_name := `uv run python -c "import tomllib; n=tomllib.load(open('pyproject.toml','rb'))['project']['name']; print(n.replace('-', '_'))"`
wheel_name := `basename $(ls dist/*.whl 2>/dev/null | head -n 1) 2>/dev/null || echo ""`
package_url := "https://" + s3_bucket + ".s3.amazonaws.com/" + wheel_name

# Show variable values
[group('help')]
show-vars:
  @echo "Python Version: {{python_version}}"
  @echo "AWS Profile: {{aws_profile}}"
  @echo "S3 Bucket: {{s3_bucket}}"
  @echo "Coverage Fail Under: {{cov_fail_under}}"
  @echo "Package Name: {{package_name}}"
  @echo "Wheel Name: {{wheel_name}}"
  @echo "Package URL: {{package_url}}"

# DO NOT EDIT BELOW THIS LINE - auto-generated from template
# -----------------------------------------------------------------------------
# Environment
# -----------------------------------------------------------------------------

# Create virtual environment (uses `uv`)
[group('environment')]
env:
  uv venv --python {{python_version}}

# Remove virtual environment
[group('environment')]
env-remove:
  rm -rf .venv/

# Recreate environment from scratch
[group('environment')]
env-recreate: env-remove env pip-install-editable

# -----------------------------------------------------------------------------
# Pip
# -----------------------------------------------------------------------------

# Install in editable mode
[group('uv')]
pip-install-editable:
  uv sync --all-groups
  uv pip install -e .

# Add dev dependencies
[group('uv')]
uv-add-dev-dependencies:
  uv add twine hatch xapp-tools ruff pre-commit --group dev

# Add test dependencies
[group('uv')]
uv-add-test-dependencies:
  uv add pytest-cov pytest-mock pytest-asyncio coverage --group test

# Run pip list
[group('uv')]
pip-list:
  uv pip list

# Run pip tree
[group('pip')]
pip-tree:
  uv pip tree

# Sync dependencies from lock file
[group('uv')]
uv-sync:
  uv sync

# Sync dependencies [production, dev, test]
[group('uv')]
uv-install-dev:
  uv sync --no-default-groups --group test --group dev

# Match lock file to current dependencies in pyproject.toml
[group('uv')]
uv-lock:
  uv lock

# Upgrade dependencies and update lock file
[group('uv')]
uv-lock-upgrade:
  uv lock --upgrade

# Check if lock file is up to date
[group('uv')]
uv-lock-check:
  uv lock --check

# -----------------------------------------------------------------------------
# Testing
# -----------------------------------------------------------------------------

# Run tests
[group('testing')]
pytest:
  uv run pytest -vx --cov={{package_name}} --cov-report=html

# Run tests in verbose mode
[group('testing')]
pytest-verbose:
  uv run pytest -vvs --cov={{package_name}} --cov-report=html

# Run tests with coverage
[group('testing')]
coverage:
  uv run pytest -q --cov={{package_name}} --cov-report=term --cov-report=html

# Run tests with coverage in verbose mode
[group('testing')]
coverage-verbose:
  uv run pytest -vs --cov={{package_name}} --cov-report=term --cov-report=html

# Run tests with coverage and skip covered
[group('testing')]
coverage-skip:
  uv run pytest -vs --cov={{package_name}} --cov-report=term:skip-covered --cov-report=html

# Run tests with coverage threshold gate
[group('testing')]
pytest-cov-gate:
  uv run pytest -q --cov={{package_name}} --cov-report=term --cov-fail-under={{cov_fail_under}}

# Open coverage report
[group('testing')]
open-coverage:
  open htmlcov/index.html

# Run tox
[group('testing')]
tox:
  uv run tox

# -----------------------------------------------------------------------------
# Linting
# -----------------------------------------------------------------------------

# Run ruff format
[group('linting')]
ruff-format:
  uv run ruff format

# Run ruff check
[group('linting')]
ruff-check:
  uv run ruff check

# Run ruff check with autofix
[group('linting')]
ruff-check-fix:
  uv run ruff check --fix

# Run ruff clean
[group('linting')]
ruff-clean:
  uv run ruff clean

# -----------------------------------------------------------------------------
# Workflow
# -----------------------------------------------------------------------------

# Run fast local quality checks
[group('workflow')]
check: uv-lock-check ruff-check pytest-cov-gate

# Apply automatic fixes and re-run checks
[group('workflow')]
fix: ruff-format ruff-check-fix check

# Mirror CI/release gate locally
[group('workflow')]
ci: release-check

# Show toolchain and environment diagnostics
[group('workflow')]
doctor:
  uv --version
  uv run python --version
  uv pip list --strict
  uv lock --check

# Show outdated dependencies across all groups
[group('workflow')]
outdated:
  uv tree --outdated --all-groups

# -----------------------------------------------------------------------------
# Cleanup
# -----------------------------------------------------------------------------

# Remove build artifacts
[group('cleanup')]
clean-build:
  rm -fr build/ dist/ .eggs/
  find . -name '*.egg-info' -o -name '*.egg' -exec rm -fr {} +

# Remove python file artifacts
[group('cleanup')]
clean-pyc:
  find . \( -name '*.pyc' -o -name '*.pyo' -o -name '*~' -o -name '__pycache__' \) -exec rm -fr {} +

# Remove all build and python artifacts
[group('cleanup')]
clean: clean-build clean-pyc

# Clear pytest cache
[group('cleanup')]
clean-pytest-cache:
  rm -rf .pytest_cache

# Clear ruff cache
[group('cleanup')]
clean-ruff-cache:
  rm -rf .ruff_cache

# Clear tox cache
[group('cleanup')]
clean-tox-cache:
  rm -rf .tox

# Clear coverage cache
[group('cleanup')]
clean-coverage:
  rm .coverage
  rm -rf htmlcov

# Clear pytest, ruff, tox, and coverage caches
[group('cleanup')]
clean-tests: clean-pytest-cache clean-ruff-cache clean-tox-cache clean-coverage

# Full cleanup
[group('cleanup')]
clean-all: clean clean-tests

# -----------------------------------------------------------------------------
# Miscellaneous
# -----------------------------------------------------------------------------

# Show src directory tree
[group('misc')]
tree:
  tree src -I '__pycache__'

# Show full directory tree
[group('misc')]
tree-root:
  tree -I '.claude|.tmp|.coverage|htmlcov|dist|build|.eggs|*.egg-info|__pycache__|.pytest_cache|.ruff_cache|.tox|.vscode|node_modules|*.csv'

# ----------------------------------------------------------------------------
# Deploy
# -----------------------------------------------------------------------------

# Build source and wheel package
[group('deploy')]
dist: clean
  uv run hatch build

# Show package metadata
[group('deploy')]
metadata:
  uv run hatch project metadata

# Run full release quality gates
[group('deploy')]
release-check: ruff-check pytest-cov-gate twine-check

# Upload package to pypi test
[group('deploy')]
twine-upload-test: dist
  uv run twine upload dist/* -r pypitest

# Package and upload a release
[group('deploy')]
twine-upload: dist
  uv run twine upload dist/*

# Twine check
[group('deploy')]
twine-check: dist
  uv run twine check dist/*

# Fix twine issues
[group('deploy')]
twine-fix:
  uv pip install -U twine pkginfo

# -----------------------------------------------------------------------------
# X Studios S3 PyPi
# -----------------------------------------------------------------------------

# Push distro to S3 bucket
[group('s3')]
push-to-s3:
  aws s3 sync --profile={{aws_profile}} --acl public-read ./dist/ s3://{{s3_bucket}}/ \
    --exclude "*" --include "*.whl"
  echo "{{package_url}}"

# DO NOT EDIT ABOVE THIS LINE UNLESS YOU KNOW WHAT YOU'RE DOING
# -----------------------------------------------------------------------------
# Project Specific
# -----------------------------------------------------------------------------

user := "pi"
host := "192.168.1.48"
remote_dir := "/home/pi/Sandbox/Python/my-pypi-packages/{{package_name}}"

# Sync files to Raspberry Pi
[group('project')]
rsync-to-pi:
  rsync -avz . {{user}}@{{host}}:{{remote_dir}} --delete \
    --exclude=".DS_Store" --exclude='.git' --exclude='.venv' \
    --exclude=".coverage" --exclude='htmlcov' --exclude='__pycache__' \
    --exclude='.pytest_cache' --exclude='.ruff_cache' --exclude='.tox' \
    --exclude='.vscode' --exclude='node_modules' --exclude='dist' \
    --exclude='*.egg-info' --exclude=".tmp"
