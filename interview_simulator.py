import os
import json
from datetime import datetime
from reverie.backend_server.market_research_personas import SAMPLE_PERSONAS
from reverie.backend_server.utils import safe_generate

class MarketResearchInterviewer:
    def __init__(self, persona_type, research_topic):
        self.persona_type = persona_type
        self.research_topic = research_topic
        self.persona_context = SAMPLE_PERSONAS[persona_type].generate_persona_prompt()
        self.conversation_history = []
        self.results = {}
        self.interview_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    def ask_question(self, question):
        full_prompt = f"""{self.persona_context}

Research Topic: {self.research_topic}

Previous Conversation:
{self.format_conversation_history()}

Interview Question: {question}
Participant:"""
        response = safe_generate(full_prompt)
        self.conversation_history.append({"question": question, "response": response})
        return response

    def format_conversation_history(self):
        return "\n".join([
            f"Q: {item['question']}\nA: {item['response']}" for item in self.conversation_history[-3:]
        ])

    def conduct_full_interview(self, questions):
        for idx, question in enumerate(questions, 1):
            response = self.ask_question(question)
            self.results[question] = response
        return self.results

    def save_interview(self, directory="interview_results"):
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = f"interview_{self.persona_type}_{self.interview_time}.json"
        filepath = os.path.join(directory, filename)
        with open(filepath, "w") as f:
            json.dump({
                "persona_type": self.persona_type,
                "research_topic": self.research_topic,
                "conversation_history": self.conversation_history,
                "results": self.results
            }, f, indent=2)
        return filepath
