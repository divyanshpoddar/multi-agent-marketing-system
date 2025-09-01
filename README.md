AI-Driven Multi-Agent Marketing System
This project implements an advanced AI-driven, marketing-focused multi-agent system for Purple Merit's client. The system is designed to optimize lead management, campaign execution, and customer engagement through the collaboration of three specialized agents: the Lead Triage Agent, the Engagement Agent, and the Campaign Optimization Agent.

File Structure
(The file structure you created)

Technical Requirements
MCP Server/Client: For secure data access.

JSON-RPC 2.0: For inter-agent communication.

Agent Handoff Protocols: To preserve context.

Persistent Agent Memory: For adaptive learning.

Setup Instructions
Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install "fastapi[all]" "python-jsonrpc-server"

Running the System
To start the FastAPI server, run the following command from the root multi-agent-marketing-system/ directory:

uvicorn main:app --reload

The server will be running at http://127.0.0.1:8000. You can access the interactive API documentation at http://127.0.0.1:8000/docs.