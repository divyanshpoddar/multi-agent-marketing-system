from core.adaptive_memory import AdaptiveMemory
from core.mcp_server_client import MCPClient

class EngagementAgent:
    """Manages personalized outreach and lead nurturing."""

    def __init__(self, mcp_client: MCPClient):
        """
        Initializes the agent.

        Args:
            mcp_client: The client for secure data access.
        """
        self.memory = AdaptiveMemory(agent_name="engagement")
        self.mcp_client = mcp_client

    def handle_lead(self, lead_id: str, context: dict):
        """
        Handles an incoming lead, typically handed off from the Triage Agent.
        This is a simplified example of sending a personalized email.
        """
        # Use the MCP client to get the lead's full data
        lead_data = self.mcp_client.get_lead_data(lead_id)
        if not lead_data:
            print(f"[EngagementAgent] ERROR: Could not find data for lead {lead_id}.")
            return

        email = lead_data.get("email")
        name = lead_data.get("name")
        category = context.get("category", "General")

        # Simulate sending a personalized email
        print(f"[EngagementAgent] Sending personalized '{category}' email to {name} at {email}.")
        
        # Remember this successful interaction
        self.memory.add_semantic_memory(
            concept=f"lead_{lead_id}",
            relationship="engagement_status",
            value="contacted"
        )