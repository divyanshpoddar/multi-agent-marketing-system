import pytest
from fastapi.testclient import TestClient

# Import the app from your main application file
from main import app

# Create a TestClient instance
client = TestClient(app)

def test_health_check():
    """Tests if the root endpoint is working."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Multi-Agent Marketing System is running. See /docs for API details."}

def test_triage_qualified_lead_and_handoff():
    """
    Tests the full workflow for a qualified lead.
    Note: We can't directly check terminal output here, but we can verify the API response
    which is the primary contract of the service.
    """
    response = client.post("/triage", json={"lead_id": "lead1"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["lead_id"] == "lead1"
    assert data["category"] == "Campaign Qualified"

def test_triage_cold_lead():
    """Tests the workflow for a cold lead where no handoff should occur."""
    response = client.post("/triage", json={"lead_id": "lead2"})
    assert response.status_code == 200
    data = response.json()
    assert data["category"] == "Cold Lead"

def test_triage_lead_not_found():
    """Tests the 404 error handling for a non-existent lead."""
    response = client.post("/triage", json={"lead_id": "lead_that_does_not_exist"})
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]

def test_optimize_campaign():
    """Tests the campaign optimization agent endpoint."""
    response = client.post("/optimize", json={"campaign_id": "summer_sale"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["recommendations"], list)
    assert len(data["recommendations"]) > 0