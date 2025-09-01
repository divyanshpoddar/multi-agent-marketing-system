import json
from jsonrpc.manager import JSONRPCResponseManager

class MCPServer:
    """A mock MCP server simulating a secure, internal marketing database."""
    def __init__(self):
        # Mock database of leads and campaigns
        self.db = {
            "leads": {
                "lead1": {"id": "lead1", "name": "Alice", "email": "alice@example.com", "engagement_score": 85, "subject": "Sales Inquiry"},
                "lead2": {"id": "lead2", "name": "Bob", "email": "bob@example.com", "engagement_score": 30, "subject": "Support Question"},
            },
            "campaigns": {
                "summer_sale": {"id": "summer_sale", "click_through_rate": 0.015, "conversion_rate": 0.03},
            }
        }
        # The dispatcher maps method names to the actual methods
        self.dispatcher = {
            "get_lead_data": self.get_lead_data,
            "get_campaign_data": self.get_campaign_data, 
        }

    def get_lead_data(self, lead_id: str) -> dict | None:
        print(f"[MCPServer] Received request for lead_id: {lead_id}")
        return self.db["leads"].get(lead_id)
        
    def get_campaign_data(self, campaign_id: str) -> dict | None:
        """Retrieves mock data for a given campaign."""
        print(f"[MCPServer] Received request for campaign_id: {campaign_id}")
        return self.db["campaigns"].get(campaign_id)

    def dispatch(self, request: str) -> str:
        """Handles incoming JSON-RPC requests."""
        response = JSONRPCResponseManager.handle(request, self.dispatcher)
        return response.json

class MCPClient:
    """A client to securely interact with the MCP server."""
    def __init__(self, server: MCPServer):
        self.server = server

    def _make_request(self, method: str, params: list) -> dict | None:
        """Helper to create and dispatch a JSON-RPC request."""
        request = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": 1
        }
        response_str = self.server.dispatch(json.dumps(request))
        response = json.loads(response_str)
        return response.get("result")

    def get_lead_data(self, lead_id: str) -> dict | None:
        """Public method to fetch lead data."""
        return self._make_request("get_lead_data", [lead_id])

    def get_campaign_data(self, campaign_id: str) -> dict | None:
        """Public method to fetch campaign data."""
        return self._make_request("get_campaign_data", [campaign_id])