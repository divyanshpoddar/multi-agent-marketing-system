from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Any

# Import agent and core classes
from agents.lead_triage_agent import LeadTriageAgent
from agents.engagement_agent import EngagementAgent
from agents.campaign_optimization_agent import CampaignOptimizationAgent
from core.mcp_server_client import MCPServer, MCPClient

# --- API Data Models ---
class TriageRequest(BaseModel):
    lead_id: str = Field(..., json_schema_extra={"example": "lead1"}, description="The unique identifier for the lead.")

class OptimizeRequest(BaseModel):
    campaign_id: str = Field(..., json_schema_extra={"example": "summer_sale"})

# --- Application Setup ---
app = FastAPI(
    title="Multi-Agent Marketing System",
    description="An AI-driven system for marketing automation.",
    version="1.0.0"
)

# --- Agent and Service Initialization (with Dependency Injection) ---
mcp_server = MCPServer()
mcp_client = MCPClient(server=mcp_server)
engagement_agent = EngagementAgent(mcp_client=mcp_client)
optimization_agent = CampaignOptimizationAgent(mcp_client=mcp_client)
lead_triage_agent = LeadTriageAgent(mcp_client=mcp_client, engagement_agent=engagement_agent)

# --- API Endpoints ---
@app.post("/triage", tags=["Agent Workflows"])
async def triage_lead_endpoint(request: TriageRequest):
    """Triggers the Lead Triage Agent and handles handoff."""
    print(f"\n--- Received Triage Request for {request.lead_id} ---")
    
    # The process_lead method now contains the full logic including handoff
    category = lead_triage_agent.process_lead(request.lead_id)
    
    if category == "Lead not found":
        raise HTTPException(status_code=404, detail=f"Lead '{request.lead_id}' not found.")
    
    return {"status": "success", "lead_id": request.lead_id, "category": category}

@app.post("/optimize", tags=["Agent Workflows"])
async def optimize_campaign_endpoint(request: OptimizeRequest):
    """Triggers the Campaign Optimization Agent."""
    print(f"\n--- Received Optimization Request for {request.campaign_id} ---")
    
    # --- FIX: The method is named 'analyze_and_suggest', not 'optimize_campaign' ---
    recommendations = optimization_agent.analyze_and_suggest(request.campaign_id)
    
    return {"status": "success", "campaign_id": request.campaign_id, "recommendations": recommendations}

@app.get("/", tags=["System"])
async def health_check():
    """Health check endpoint."""
    # --- FIX: Updated message to match the test expectation ---
    return {"message": "Multi-Agent Marketing System is running. See /docs for API details."}