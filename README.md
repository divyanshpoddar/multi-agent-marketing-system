# 🤖 AI-Driven Multi-Agent Marketing System  

This project implements an advanced **AI-driven, marketing-focused multi-agent system** for **Purple Merit’s client**.  
The system is designed to optimize **lead management**, **campaign execution**, and **customer engagement** through the collaboration of three specialized agents:  

- 🧑‍💼 **Lead Triage Agent** → Classifies and prioritizes incoming leads  
- 💬 **Engagement Agent** → Manages customer interactions and engagement  
- 📈 **Campaign Optimization Agent** → Optimizes marketing campaigns for better performance  

---

## 📂 File Structure  

multi-agent-marketing-system/
│── main.py
│── requirements.txt
│── agents/
│ ├── init.py
│ ├── lead_triage_agent.py
│ ├── engagement_agent.py
│ └── campaign_optimization_agent.py
│── memory/
│ ├── init.py
│ └── persistent_memory.py
│── protocols/
│ ├── init.py
│ └── handoff_protocols.py

---

## ⚙️ Technical Requirements  

- 🔒 **MCP Server/Client** → For secure data access  
- 🔗 **JSON-RPC 2.0** → For inter-agent communication  
- 📝 **Agent Handoff Protocols** → To preserve context during agent transitions  
- 🧠 **Persistent Agent Memory** → For adaptive learning and personalization  

---

## 🚀 Setup Instructions  

### 1️⃣ Create a virtual environment  
```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate.bat      # On Windows
```
###2️⃣ Install dependencies
```bash
pip install "fastapi[all]" "python-jsonrpc-server"
```
###▶️ Running the System
```bash
From the root directory multi-agent-marketing-system/, run:
uvicorn main:app --reload
```
🌐 Server: http://127.0.0.1:8000

📘 API Docs: http://127.0.0.1:8000/docs

##✅ Features
-🤝 Multi-Agent Collaboration for marketing workflows
-📊 Real-Time Campaign Optimization
-🔄 Seamless Agent Handoffs with context preservation
-🧩 Scalable Architecture with modular design
