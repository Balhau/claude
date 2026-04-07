# MCP Gateway

This project contains an MCP (Model Context Protocol) gateway that aggregates multiple backend MCP servers and exposes them as a single SSE-based endpoint. It also includes an example backend server (`names`) that generates random names.

## Project Structure

```
mcp/
├── docker-compose.yml       # Orchestrates the full stack
├── gateway/
│   ├── server.py            # Gateway server — aggregates backends over SSE
│   ├── backends.json        # Default backend configuration
│   ├── requirements.txt
│   └── Dockerfile
└── names/
    ├── server.py            # Example backend — generates random names (stdio)
    ├── requirements.txt
    └── Dockerfile
```

### How It Works

```
Claude / MCP Client
       │  SSE (HTTP)
       ▼
  Gateway (:8080)
       │  stdio
       ├──▶ names/server.py
       └──▶ (other backends...)
```

The gateway connects to each backend on startup, collects their tools, and exposes two meta-tools to clients:

| Tool | Description |
|---|---|
| `list_tools` | Lists all tools registered from all backends |
| `gateway_call` | Calls any backend tool by name with JSON arguments |

---

## Build & Run

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) 20.10+
- [Docker Compose](https://docs.docker.com/compose/) v2+

### Option 1 — Docker Compose (recommended)

Build and start the gateway with the bundled `names` backend:

```bash
cd mcp
docker compose up --build
```

The gateway will be available at `http://localhost:8080`.

To run in the background:

```bash
docker compose up --build -d
```

To stop:

```bash
docker compose down
```

### Option 2 — Build the image manually

```bash
cd mcp
docker build -f gateway/Dockerfile -t mcp-gateway .
docker run --rm -p 8080:8080 mcp-gateway
```

---

## Backend Configuration

Backends are configured via `gateway/backends.json`:

```json
[
  {
    "name": "names",
    "command": "python",
    "args": ["/servers/names/server.py"]
  }
]
```

Each entry spawns a backend MCP server as a stdio subprocess. Fields:

| Field | Required | Description |
|---|---|---|
| `name` | no | Display name used in logs |
| `command` | yes | Executable to run |
| `args` | no | Command-line arguments |
| `env` | no | Extra environment variables (key/value object) |

### Override at Runtime

You can skip `backends.json` entirely and pass the configuration as an environment variable:

```bash
docker run --rm -p 8080:8080 \
  -e BACKENDS_CONFIG='[{"name":"names","command":"python","args":["/servers/names/server.py"]}]' \
  mcp-gateway
```

Or in `docker-compose.yml`:

```yaml
environment:
  BACKENDS_CONFIG: '[{"name":"names","command":"python","args":["/servers/names/server.py"]}]'
```

---

## Integrating with Claude

### Claude Code (CLI)

Add the gateway to your MCP configuration file (`~/.claude/claude_desktop_config.json` or project-level `.mcp.json`):

```json
{
  "mcpServers": {
    "gateway": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

Then restart Claude Code. The gateway tools will appear alongside your other MCP tools.

### Claude Desktop

Open **Settings → Developer → Edit Config** and add:

```json
{
  "mcpServers": {
    "gateway": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

Save and restart the app.

---

## Usage Examples

Once connected, you can interact with the gateway directly in Claude.

### List all available tools

```
What tools are available through the gateway?
```

Claude will call `list_tools` and return something like:

```
- get_name
```

### Generate a random name

```
Use the gateway to generate a random name.
```

Claude will call `gateway_call` with `tool_name = "get_name"` and return:

```
Rachel Thompson
```

### Call a tool with arguments

If a backend tool accepts parameters, pass them as a JSON string in the `arguments` field:

```
Call the gateway tool "greet" with arguments {"language": "es"}.
```

Claude will invoke:

```json
{
  "tool_name": "greet",
  "arguments": "{\"language\": \"es\"}"
}
```

---

## Adding a New Backend

1. Create your backend server under `mcp/<your-server>/server.py` using `FastMCP` with `transport="stdio"`.
2. Add it to `gateway/backends.json`:
   ```json
   {
     "name": "your-server",
     "command": "python",
     "args": ["/servers/your-server/server.py"]
   }
   ```
3. In `gateway/Dockerfile`, copy the server into the image:
   ```dockerfile
   COPY ../your-server/requirements.txt /tmp/your-server-requirements.txt
   RUN pip install --no-cache-dir -r /tmp/your-server-requirements.txt
   COPY ../your-server/server.py /servers/your-server/server.py
   ```
4. Rebuild: `docker compose up --build`
