from core.adaptive_memory import AdaptiveMemory
from core.mcp_server_client import MCPClient

class CampaignOptimizationAgent:
    """Monitors campaign performance and adapts strategies."""

    def __init__(self, mcp_client: MCPClient):
        """
        Initializes the agent.

        Args:
            mcp_client: The client for secure data access.
        """
        self.memory = AdaptiveMemory(agent_name="campaign_optimization")
        self.mcp_client = mcp_client

    def analyze_and_suggest(self, campaign_id: str) -> list[str]:
        """Analyzes campaign performance and suggests optimizations."""
        
        # Use the MCP client to get the campaign's full data
        campaign_data = self.mcp_client.get_campaign_data(campaign_id)
        if not campaign_data:
            return ["Campaign data not found."]

        suggestions = []
        ctr = campaign_data.get("click_through_rate", 0)
        conversion_rate = campaign_data.get("conversion_rate", 0)

        # Basic rule-based analysis
        if ctr < 0.02: # Click-through rate is less than 2%
            suggestions.append("Low CTR: Consider revising ad copy or targeting.")
        
        if conversion_rate < 0.05: # Conversion rate is less than 5%
            suggestions.append("Low Conversion Rate: Review landing page experience.")

        if not suggestions:
            suggestions.append("Campaign is performing within expected parameters.")

        print(f"[CampaignOptimizationAgent] Analysis for {campaign_id}: {suggestions}")
        return suggestions