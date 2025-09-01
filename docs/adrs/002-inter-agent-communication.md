ADR 002: Inter-Agent Communication and Handoff
Title: Inter-Agent Communication Protocol and Context Handoff

Date: 2025-09-01

Status: Accepted

Context
The multi-agent system requires a reliable and efficient method for agents to collaborate, particularly for handing off a lead from one stage to the next (e.g., from Triage to Engagement). This handoff must preserve the conversational and campaign context.

Decision
We will use a Direct Method Call pattern for inter-agent communication within our single-process application. The API gateway (main.py) will act as the orchestrator.

Communication Protocol: For internal communication (agent-to-agent), we will use direct Python method calls. This is the most efficient method within a monolithic architecture.

External Communication: All external interactions with the system will happen via the JSON-based RESTful API defined in main.py.

Secure Data Access: For accessing sensitive marketing data (e.g., lead details), agents will use the Model Context Protocol (MCP), implemented via a JSON-RPC client-server pattern (mcp_server_client.py). This simulates a secure, dedicated data access layer.

Handoff Protocol: Context will be passed as a Python dictionary during method calls. This dictionary will contain all necessary information, such as the lead ID, the triage category, and any other relevant metadata.

Example Handoff Flow:

/triage endpoint in main.py calls lead_triage_agent.triage_lead().

The agent returns the category (e.g., "Campaign Qualified").

main.py checks the category and, if applicable, calls engagement_agent.engage_lead(), passing the lead_id and a context dictionary.

Consequences
Positive:

Extremely fast and low-overhead communication.

Simple to implement and debug.

Transactional consistency is easier to manage within a single process.

Negative:

This pattern is tightly coupled. If the system were to be broken into microservices, this communication would need to be replaced with network calls (e.g., HTTP requests or a message bus), and the handoff protocol would require serialization.