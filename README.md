# Dagster Vide Coding Cursor Setup

This project contains Dagster components for data engineering workflows, including Sling replication and CSV ingestion capabilities.

## Development Setup

### Prerequisites

- Python 3.11 or higher
- UV package manager (`pip install uv`)

### Setting up the Development Environment

1. **Create and activate a virtual environment using UV**:

```bash
# Create a new virtual environment
uv venv

# Activate the virtual environment
# On Unix/macOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

2. **Install dependencies using UV**:

```bash
# Install the project and development dependencies
uv pip install ".[dev]"
```

This will install:
- All core dependencies from `pyproject.toml`
- Development dependencies (testing, linting, etc.)
- The project in editable mode

### Clone Dagster Repository

After setting up your environment, you'll need to clone the Dagster repository for reference and development:

1. **Run the clone utility**:

```bash
# From the project root
python utils/clone_dagster.py
```

This will:
- Create a `context/dagster` directory
- Clone the latest version of Dagster into this directory
- The directory is gitignored, so it won't be tracked in version control

2. **Verify the clone**:

```bash
# Check that the repository was cloned successfully
ls context/dagster
```

You should see the Dagster repository contents in the `context/dagster` directory.

Note: The cloned repository is used for:
- Reference implementation
- Development guidance
- Documentation access
- Component patterns and examples

### To Install Repomix and Generate MCP Server

[Source](https://repomix.com/)


1. **Prerequisites**:
- Node.js installed (Download from [nodejs.org](https://nodejs.org))
- npm (comes with Node.js)

2. **Install Repomix globally**:
```bash
npm install -g repomix
```

3. **Verify installation**:
```bash
repomix --version
```

4. **MCP Server**:
Navigate to the dagster folder and then start the MCP server with 
```bash
repomix --mcp
```

5. Update Cursor Settings

Edit the cline_mcp_settings.json file:

```json
{
  "mcpServers": {
    "repomix": {
      "command": "npx",
      "args": [
        "-y",
        "repomix",
        "--mcp"
      ]
    }
  }
}
```

In Cursor, add a new MCP server from Cursor Settings > MCP > + Add new global MCP server

