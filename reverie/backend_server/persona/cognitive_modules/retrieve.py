from utils import safe_generate, llm

def generate_poig_score(personas, event_description, test_input=None):
    """Generate importance score for memories"""
    if test_input:
        return 5
    
    prompt = f"""On the scale of 1 to 10, where 1 is purely mundane (e.g., brushing teeth, making bed) and 10 is extremely poignant (e.g., a break up, college acceptance), rate the likely poignancy of the following piece of memory.

Memory: {event_description}

Rating (1-10):"""
    
    response = safe_generate(prompt, max_tokens=50, temperature=0.3)
    return llm.extract_rating(response)
