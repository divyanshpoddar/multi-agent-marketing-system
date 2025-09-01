import json
import os
from pathlib import Path

# In a real system, this would be a graph database like Neo4j.
# For this simulation, we use JSON files to represent persistent memory.
MEMORY_DIR = Path("agent_memory")

class AdaptiveMemory:
    """
    A sophisticated memory architecture for agents to learn and adapt.
    This implementation simulates short-term, long-term, episodic, and semantic memory.
    """
    def __init__(self, agent_name: str):
        """
        Initializes the memory system for a specific agent.

        Args:
            agent_name (str): The name of the agent this memory belongs to.
                              This ensures each agent has its own memory file.
        """
        self.agent_name = agent_name
        self.memory_file = MEMORY_DIR / f"{self.agent_name}_memory.json"
        self._short_term_memory = {}  # In-memory dictionary for current context
        self._long_term_memory = self._load_memory()  # Persistent JSON file

        # Ensure the memory directory exists
        MEMORY_DIR.mkdir(exist_ok=True)

    def _load_memory(self) -> dict:
        """Loads the agent's long-term memory from its file."""
        if self.memory_file.exists():
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        return {"customer_history": {}, "episodic": {}, "semantic": {}}

    def _save_memory(self):
        """Saves the current state of long-term memory to the file."""
        with open(self.memory_file, 'w') as f:
            json.dump(self._long_term_memory, f, indent=4)

    def add_episodic_memory(self, problem_context: str, successful_solution: str):
        """Adds a new successful problem-resolution pattern."""
        self._long_term_memory["episodic"][problem_context] = successful_solution
        self._save_memory()

    def add_semantic_memory(self, concept: str, relationship: str, value: any):
        """Adds a fact or relationship to the knowledge graph."""
        if concept not in self._long_term_memory["semantic"]:
            self._long_term_memory["semantic"][concept] = {}
        self._long_term_memory["semantic"][concept][relationship] = value
        self._save_memory()