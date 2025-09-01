ADR 001: System Architecture
Title: System Architecture for the Multi-Agent Marketing System

Date: 2025-09-01

Status: Accepted

Context
We need to design a robust and scalable architecture for a multi-agent marketing system. The system must support collaboration between multiple specialized agents, handle real-time data, and be capable of learning and adapting over time. The architecture should be modular to allow for future expansion and maintenance.

Decision
We have decided to adopt a service-oriented architecture (SOA) with a centralized API gateway. Each agent (Triage, Engagement, Optimization) is implemented as a distinct class, representing a logical service. A FastAPI application serves as the single entry point (API Gateway), routing requests to the appropriate agent. This approach offers a good balance between modularity and simplicity for this specific implementation.

API Gateway: main.py using FastAPI. It handles all incoming HTTP requests, validates data, and orchestrates agent handoffs.

Logical Services: LeadTriageAgent, EngagementAgent, CampaignOptimizationAgent classes. They are instantiated once and live for the duration of the application lifecycle.

Shared Core: The core module contains shared components like AdaptiveMemory and the MCPClient, ensuring consistent functionality across agents.

Consequences
Positive:

The system is highly modular and easy to understand.

Development is simplified as all code runs in a single process.

Agent handoffs are direct method calls, which are fast and reliable.

Easy to debug and test locally.

Negative:

The system is a monolith, so all components scale together. For a 10x load increase, we will need to run multiple instances of the entire application behind a load balancer.

A failure in one component could potentially impact the entire application.