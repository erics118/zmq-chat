# List all recipes
default:
    @just --list --unsorted

# Install dependencies
install:
    pip install -e .

# Run the primary node
primary:
    python3 src/main.py --primary

# Run secondary node
secondary +code:
    python3 src/main.py --secondary --code {{code}}
