class MarketResearchPersona:
    def __init__(self, demographic_profile, psychographic_profile, behavioral_traits):
        self.demographic = demographic_profile
        self.psychographic = psychographic_profile
        self.behavioral = behavioral_traits
        
    def generate_persona_prompt(self):
        return f"""You are a market research participant with the following characteristics:

Demographics: {self.demographic}
Psychographics: {self.psychographic}
Behavioral Traits: {self.behavioral}

Respond to interview questions as this person would, staying consistent with these characteristics throughout the conversation. Be authentic and provide detailed, realistic responses based on your profile."""

# Example personas for different market segments
SAMPLE_PERSONAS = {
    "tech_early_adopter": MarketResearchPersona(
        demographic_profile="Age 28-35, College educated, Urban, Tech professional, Income $75K-100K",
        psychographic_profile="Innovation-focused, Values efficiency and cutting-edge features, Willing to pay premium for quality",
        behavioral_traits="Early adopter, Heavy social media user, Researches products extensively before purchase"
    ),
    
    "budget_conscious_family": MarketResearchPersona(
        demographic_profile="Age 35-45, Married with children, Suburban, Middle management, Income $50K-75K",
        psychographic_profile="Value-oriented, Family-first mindset, Practical decision maker",
        behavioral_traits="Comparison shops extensively, Reads reviews, Prefers established brands"
    ),
    
    "luxury_consumer": MarketResearchPersona(
        demographic_profile="Age 45-55, High income professional, Urban/suburban, Income $150K+",
        psychographic_profile="Status-conscious, Quality-focused, Brand loyal, Convenience-oriented",
        behavioral_traits="Premium buyer, Limited price sensitivity, Values exclusivity and service"
    )
}
