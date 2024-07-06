#!/bin/sh
# Run pytest
pytest --cov=openciv --cov-report=xml

# Check the exit status of pytest
if [ $? -ne 0 ]; then
    echo "pytest failed, commit aborted."
    exit 1
fi

git add coverage.xml
semantic-release changelog
git add CHANGELOG.md

# Function to fix trailing whitespace
fix_trailing_whitespace() {
    find . -type f \( -name "*.py" -o -name "*.md" \) -exec sed -i 's/[[:space:]]\+$//' {} +
}

# Function to ensure files end with a newline
ensure_newline_at_eof() {
    find . -type f \( -name "*.py" -o -name "*.md" \) -exec sed -i -e '$a\' {} +
}

# Function to format Python files using Ruff
format_python_files() {
    if command -v ruff &> /dev/null; then
        ruff check . --fix
    else
        echo "Ruff is not installed. Please install it with 'pip install ruff'."
        exit 1
    fi
}

# Function to lint Markdown files using pymarkdown
lint_markdown_files() {
    if command -v pymarkdownlnt &> /dev/null; then
        pymarkdown scan .
    else
        echo "pymarkdown is not installed. Please install it with 'pip install pymarkdown'."
        exit 1
    fi
}

fix_markdown_files() {
    pymarkdownlnt fix .
}

print() {
    echo "Running $1..."
}
# Run the functions
fix_trailing_whitespace
format_python_files
fix_markdown_files
ensure_newline_at_eof
lint_markdown_files


# Add any fixes to the commit
git add .

if git rev-parse --verify HEAD >/dev/null 2>&1
then
        against=HEAD
else
        # Initial commit: diff against an empty tree object
        against=$(git hash-object -t tree /dev/null)
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --type=bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

exec git diff-index --check --cached $against --
# Exit successfully
exit 0