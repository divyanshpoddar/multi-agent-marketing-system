from core.adaptive_memory import AdaptiveMemory
from core.mcp_server_client import MCPClient
from agents.engagement_agent import EngagementAgent

class LeadTriageAgent:
    """Categorizes incoming marketing leads."""
    def __init__(self, mcp_client: MCPClient, engagement_agent: EngagementAgent):
        self.memory = AdaptiveMemory(agent_name="lead_triage")
        self.mcp_client = mcp_client
        self.engagement_agent = engagement_agent # Agent to hand off to

    def classify(self, lead_data: dict) -> str:
        """Categorizes an incoming marketing lead based on score and content."""
        score = lead_data.get("engagement_score", 0)
        subject = lead_data.get("subject", "").lower()

        if score >= 70:
            category = "Campaign Qualified"
        elif score < 40: # Any lead with a score below 40 is considered cold
            category = "Cold Lead"
        elif "inquiry" in subject or "question" in subject:
            category = "General Inquiry"
        else:
            # Fallback for leads with middling scores and no specific keywords
            category = "Cold Lead"
        
        self.memory.add_episodic_memory(
            problem_context=f"lead_subject_{subject}",
            successful_solution=category
        )
        print(f"[LeadTriageAgent] Triaged lead {lead_data['id']} as '{category}'")
        return category

    def process_lead(self, lead_id: str) -> str:
        """Main entry point to process a single lead."""
        lead_data = self.mcp_client.get_lead_data(lead_id)
        if not lead_data:
            return "Lead not found"
        
        category = self.classify(lead_data)

        # Handoff Protocol: If the lead is qualified, pass it to the Engagement Agent
        if category == "Campaign Qualified":
            print("--- Handoff: Triage -> Engagement ---")
            context = {"category": category, "source": "automated_triage"}
            self.engagement_agent.handle_lead(lead_id, context)

        return category