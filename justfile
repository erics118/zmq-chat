# List all recipes
default:
    @just --list --unsorted

# Install dependencies
install:
    pip install -e .

# Run the primary node
primary +ip:
    python3 src/main.py --primary {{ip}}

# Run secondary node
secondary +ip:
    python3 src/main.py --secondary {{ip}}
