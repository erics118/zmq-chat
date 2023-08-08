# List all recipes
default:
    @just --list --unsorted

# Install dependencies
install:
    pip install -e .

# Run node A
a:
    python3 src/nodeA.py

# Run node B
b:
    python3 src/nodeB.py


