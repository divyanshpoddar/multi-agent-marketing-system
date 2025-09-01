Agent Interaction and Conversation Flow
This document provides a visual and analytical representation of how agents in the system interact and manage a lead handoff.

Conversation Flow Diagram
A typical automated workflow for a new lead (lead1) proceeds as follows:

Step 1: Ingestion & Triage

Trigger: An external system sends a POST request to /triage with {"lead_id": "lead1"}.

Action: The main application receives the request. It uses the MCPClient to fetch the full data for lead1.

Agent: The data is passed to the LeadTriageAgent. It analyzes the data (e.g., engagement_score: 80) and categorizes the lead as "Campaign Qualified".

Output: The agent returns the category string to main.

Step 2: Handoff & Engagement

Trigger: The main application sees the "Campaign Qualified" category.

Action: It constructs a context dictionary: {"category": "Campaign Qualified", "source": "triage"}.

Agent: It calls the EngagementAgent's engage_lead method, passing the lead_id and the context.

Output: The EngagementAgent logs the action (simulating an email being sent) and updates its memory.

Step 3: Monitoring & Optimization (Asynchronous)

Trigger: A scheduled job or manual request to the /optimize endpoint for the relevant campaign.

Action: The main application calls the CampaignOptimizationAgent.

Agent: The agent pulls performance data, analyzes it, and checks its episodic memory for similar past situations.

Output: The agent returns a set of actionable recommendations.

Agent Handoff Protocol
The handoff protocol is critical for maintaining context. It is a simple dictionary passed between agents via the orchestrator (main.py).

Key Principles:

Context Preservation: The handoff dictionary carries essential data from the previous step.

Stateless Agents: Agents themselves are stateless; all long-term information is stored and retrieved from their dedicated AdaptiveMemory instance. The context dictionary provides the necessary information for the current transaction.