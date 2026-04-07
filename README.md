# claude

A workspace for exploring Claude Code capabilities, MCP (Model Context Protocol) server development, and AI-assisted data analysis.

## What's Here

### `mcp/` — MCP Gateway & Backend Servers

A local MCP gateway that aggregates multiple backend MCP servers and exposes them as a single SSE endpoint, making it easy to connect custom tools to Claude Code or Claude Desktop.

- **Gateway** (`mcp/gateway/`) — Python server built with FastMCP that proxies tool calls to backend stdio servers
- **Names backend** (`mcp/names/`) — Example backend that generates random full names
- Orchestrated via Docker Compose; gateway listens on `http://localhost:8080`

See [`mcp/README.md`](mcp/README.md) for full setup and usage instructions.

### `docs/` — EU EV Adoption Analysis

Research and forecasting documents on EU electric vehicle adoption trends:

- `docs/evs_adoption.md` — EU27 BEV registration data and analysis (2016–2025)
- `docs/ev_forecast_2030.md` — EV adoption forecast through 2030
- `docs/sources/` — Individual data source references (ACEA, EAFO, EEA, T&E, etc.)

### `.claude/commands/` — Custom Claude Code Skills

Project-level slash commands for maintaining the EV analysis docs:

| Command | Purpose |
|---|---|
| `/cite-check` | Verify factual claims against source data |
| `/add-source` | Add a new data source |
| `/fetch-ev-data` | Fetch latest EU EV registration data |
| `/forecast-update` | Refresh the 2030 forecast against latest actuals |
| `/refresh-analysis` | Re-read all sources and update analysis |
