Deployment Runbook
This runbook provides step-by-step instructions for deploying, configuring, and maintaining the multi-agent marketing system in a production environment.

1. Prerequisites
A Linux-based server (e.g., Ubuntu 22.04).

Python 3.8+ and pip installed.

A process manager like systemd or supervisor.

A reverse proxy like Nginx or Caddy.

Access to a production database and other marketing tools (the MCP would connect to these).

2. Deployment Steps
Clone the Repository:

git clone <your-repo-url> /var/www/multi-agent-system
cd /var/www/multi-agent-system

Create Virtual Environment:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
# (Create a requirements.txt with: fastapi, uvicorn, python-jsonrpc-server)

Configure Environment Variables:
Create a .env file to store secrets. The application would need to be modified to load this file (e.g., using python-dotenv).

DATABASE_URL="your-production-db-url"
MARKETING_API_KEY="your-api-key"

Set up Process Manager (systemd):
Create a service file at /etc/systemd/system/marketing-agent.service:

[Unit]
Description=Multi-Agent Marketing System
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/multi-agent-system
ExecStart=/var/www/multi-agent-system/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target

Enable and start the service:

sudo systemctl enable marketing-agent
sudo systemctl start marketing-agent

Configure Reverse Proxy (Nginx):
Set up Nginx to proxy requests to the Uvicorn server. This provides an additional layer for security, caching, and load balancing.

4. Validation and Monitoring
Health Check: Access the root endpoint (/) to confirm the service is running.

Logging: Ensure systemd journal or a dedicated logging service is capturing application output.

Monitoring: Use tools like Prometheus and Grafana to monitor API latency, error rates (4xx, 5xx), and server resource utilization.