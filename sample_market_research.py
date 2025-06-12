import sys
import os
from datetime import datetime

# Add the reverie backend to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'reverie', 'backend_server'))

from interview_simulator import MarketResearchInterviewer

# Define your research questions
PRODUCT_CONCEPT_QUESTIONS = [
    "Can you tell me about your typical morning routine and what products you use?",
    "What factors are most important to you when choosing products in this category?",
    "How do you typically discover new products in this category?",
    "What would make you switch from your current brand to a new one?",
    "If I showed you a product with innovative features, what would be your initial reaction?",
    "What concerns, if any, would you have about trying a completely new product?",
    "How much research do you typically do before making a purchase decision?",
    "Where would you expect to find and purchase products like this?",
    "Who else influences your purchase decisions in this category?",
    "What would convince you that a new product is worth trying?"
]

# Technology Product Research
TECH_PRODUCT_QUESTIONS = [
    "How do you typically discover new technology products?",
    "What features matter most when choosing tech devices?",
    "How important is brand reputation in your tech purchases?",
    "What's your experience with early adoption vs waiting for reviews?",
    "How do you evaluate the value proposition of new tech products?",
    "What role do online reviews play in your tech purchasing decisions?"
]

# Food & Beverage Research
FOOD_BEVERAGE_QUESTIONS = [
    "Describe your typical grocery shopping process.",
    "What influences your food purchasing decisions?",
    "How do you discover new food products or brands?",
    "What role does health information play in your choices?",
    "How important are ingredients lists when making food purchases?",
    "What factors make you willing to pay more for food products?"
]

# Service Experience Research
SERVICE_QUESTIONS = [
    "What makes a great customer service experience?",
    "How do you typically research service providers?",
    "What factors determine if you'll recommend a service?",
    "Describe a recent positive service interaction.",
    "How do you handle service disappointments or complaints?",
    "What communication channels do you prefer for service interactions?"
]

# Brand Perception Research
BRAND_PERCEPTION_QUESTIONS = [
    "What comes to mind when you hear about [brand name]?",
    "How would you describe this brand's personality?",
    "What sets this brand apart from its competitors?",
    "How does this brand's pricing compare to others in the category?",
    "Would you recommend this brand to friends or family? Why?",
    "What would improve your perception of this brand?"
]

# Question Templates for Common Research Scenarios
QUESTION_TEMPLATES = {
    "brand_awareness": [
        "What brands come to mind when you think of [category]?",
        "How did you first hear about [brand]?",
        "What's your overall impression of [brand]?",
        "How does [brand] compare to competitors?",
        "What words would you use to describe [brand]?"
    ],
    "purchase_journey": [
        "Walk me through your last purchase in this category.",
        "What triggered your need for this product/service?",
        "Where did you research before buying?",
        "What factors influenced your final decision?",
        "How satisfied were you with the purchase process?"
    ],
    "user_experience": [
        "Describe your typical interaction with [product/service].",
        "What works well in your current experience?",
        "What frustrations do you encounter?",
        "How could the experience be improved?",
        "How often do you use this product/service?"
    ],
    "pricing_sensitivity": [
        "How important is price in your decision-making process?",
        "What price range would you consider reasonable for this product?",
        "What would justify paying a premium price?",
        "How do you typically compare prices before purchasing?",
        "What payment methods do you prefer?"
    ]
}

def select_research_topic():
    """Interactive topic selection for market research"""
    
    topic_options = {
        "1": ("Product Concept Testing", PRODUCT_CONCEPT_QUESTIONS),
        "2": ("Technology Products", TECH_PRODUCT_QUESTIONS),
        "3": ("Food & Beverage", FOOD_BEVERAGE_QUESTIONS),
        "4": ("Service Experience", SERVICE_QUESTIONS),
        "5": ("Brand Perception", BRAND_PERCEPTION_QUESTIONS),
        "6": ("Question Templates", None),
        "7": ("Custom Questions", None)
    }
    
    print("\n=== Select Research Topic ===")
    for key, (name, _) in topic_options.items():
        print(f"{key}. {name}")
    
    while True:
        choice = input("\nEnter your choice (1-7): ").strip()
        if choice in topic_options:
            topic_name, questions = topic_options[choice]
            
            if choice == "6":
                questions = load_question_template()
                topic_name = "Template-Based Research"
            elif choice == "7":
                questions = create_custom_questions()
                topic_name = "Custom Research"
            
            return topic_name, questions
        else:
            print("Invalid choice. Please select 1-7.")

def load_question_template():
    """Load predefined question templates"""
    
    print("\n=== Available Question Templates ===")
    for i, (key, questions) in enumerate(QUESTION_TEMPLATES.items(), 1):
        print(f"{i}. {key.replace('_', ' ').title()} ({len(questions)} questions)")
    
    print(f"{len(QUESTION_TEMPLATES) + 1}. Skip template selection")
    
    while True:
        try:
            choice = input(f"\nSelect template (1-{len(QUESTION_TEMPLATES) + 1}): ").strip()
            choice_num = int(choice)
            
            if choice_num == len(QUESTION_TEMPLATES) + 1:
                return create_custom_questions()
            elif 1 <= choice_num <= len(QUESTION_TEMPLATES):
                template_keys = list(QUESTION_TEMPLATES.keys())
                selected_key = template_keys[choice_num - 1]
                return QUESTION_TEMPLATES[selected_key].copy()
            else:
                print(f"Please enter a number between 1 and {len(QUESTION_TEMPLATES) + 1}")
        except ValueError:
            print("Please enter a valid number.")

def create_custom_questions():
    """Allow users to input custom research questions"""
    questions = []
    print("\n=== Create Custom Questions ===")
    print("Enter your questions one by one (press Enter on empty line to finish):")
    
    while True:
        question = input(f"Question {len(questions) + 1}: ").strip()
        if not question:
            if len(questions) == 0:
                print("Please enter at least one question.")
                continue
            break
        questions.append(question)
        
        if len(questions) >= 15:
            print("Maximum 15 questions reached.")
            break
    
    print(f"\n{len(questions)} questions created successfully!")
    return questions

def review_questions(questions):
    """Display questions for review and ask if user wants to edit"""
    
    print(f"\n=== Review Questions ({len(questions)} total) ===")
    for i, question in enumerate(questions, 1):
        print(f"{i:2d}. {question}")
    
    while True:
        choice = input("\nWould you like to edit these questions? (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def edit_questions(questions):
    """Allow users to edit, add, or remove questions"""
    
    while True:
        print(f"\n=== Edit Questions ({len(questions)} total) ===")
        for i, question in enumerate(questions, 1):
            print(f"{i:2d}. {question}")
        
        print("\nOptions:")
        print("e [number] - Edit question")
        print("a - Add new question")
        print("d [number] - Delete question")
        print("r - Reorder questions")
        print("f - Finished editing")
        
        action = input("\nChoose action: ").strip().lower()
        
        if action == 'f':
            break
        elif action == 'a':
            new_question = input("Enter new question: ").strip()
            if new_question:
                questions.append(new_question)
                print("Question added!")
        elif action == 'r':
            questions = reorder_questions(questions)
        elif action.startswith('e '):
            try:
                index = int(action.split()[1]) - 1
                if 0 <= index < len(questions):
                    print(f"Current: {questions[index]}")
                    new_text = input("Enter new text: ").strip()
                    if new_text:
                        questions[index] = new_text
                        print("Question updated!")
                else:
                    print("Invalid question number.")
            except (IndexError, ValueError):
                print("Invalid format. Use 'e [number]'")
        elif action.startswith('d '):
            try:
                index = int(action.split()[1]) - 1
                if 0 <= index < len(questions):
                    removed = questions.pop(index)
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid question number.")
            except (IndexError, ValueError):
                print("Invalid format. Use 'd [number]'")
        else:
            print("Invalid action.")
    
    return questions

def reorder_questions(questions):
    """Allow users to reorder questions"""
    print("\n=== Reorder Questions ===")
    print("Enter new order as comma-separated numbers (e.g., 3,1,4,2):")
    
    for i, question in enumerate(questions, 1):
        print(f"{i}. {question}")
    
    try:
        order_input = input("\nNew order: ").strip()
        new_order = [int(x.strip()) - 1 for x in order_input.split(',')]
        
        if len(new_order) != len(questions) or any(i < 0 or i >= len(questions) for i in new_order):
            print("Invalid order. Please use all question numbers exactly once.")
            return questions
        
        reordered_questions = [questions[i] for i in new_order]
        print("Questions reordered successfully!")
        return reordered_questions
        
    except (ValueError, IndexError):
        print("Invalid format. Questions not reordered.")
        return questions

def select_personas():
    """Allow users to select which personas to interview"""
    
    available_personas = {
        "1": "tech_early_adopter",
        "2": "budget_conscious_family", 
        "3": "luxury_consumer"
    }
    
    persona_descriptions = {
        "tech_early_adopter": "Tech-savvy professional, early adopter, values innovation",
        "budget_conscious_family": "Family-oriented, value-conscious, practical decision maker",
        "luxury_consumer": "High-income professional, quality-focused, brand loyal"
    }
    
    print("\n=== Select Personas to Interview ===")
    for key, persona_id in available_personas.items():
        description = persona_descriptions[persona_id]
        print(f"{key}. {persona_id.replace('_', ' ').title()} - {description}")
    
    print("4. All personas")
    
    while True:
        choice = input("\nEnter choice (1-4, or comma-separated for multiple): ").strip()
        
        if choice == "4":
            return list(available_personas.values())
        
        try:
            if ',' in choice:
                choices = [x.strip() for x in choice.split(',')]
                selected_personas = []
                for c in choices:
                    if c in available_personas:
                        selected_personas.append(available_personas[c])
                    else:
                        raise ValueError(f"Invalid choice: {c}")
                return selected_personas
            else:
                if choice in available_personas:
                    return [available_personas[choice]]
                else:
                    raise ValueError(f"Invalid choice: {choice}")
        except ValueError as e:
            print(f"Error: {e}. Please enter valid choices (1-4).")

def run_market_research_simulation():
    """Run a complete market research simulation with topic selection"""
    
    print("=" * 70)
    print("MARKET RESEARCH INTERVIEW SIMULATION")
    print("Using Stanford Generative Agents with Local Phi-3.5 Model")
    print("=" * 70)
    
    # Select research topic
    topic_name, questions = select_research_topic()
    
    if not questions:
        print("No questions selected. Exiting.")
        return
    
    # Review questions before proceeding
    if review_questions(questions):
        questions = edit_questions(questions)
    
    # Select personas to interview
    selected_personas = select_personas()
    
    print(f"\n{'='*70}")
    print(f"RESEARCH TOPIC: {topic_name}")
    print(f"TOTAL QUESTIONS: {len(questions)}")
    print(f"PERSONAS TO INTERVIEW: {len(selected_personas)}")
    print(f"{'='*70}")
    
    # Confirm before starting
    confirm = input("\nProceed with interviews? (y/n): ").lower().strip()
    if confirm not in ['y', 'yes']:
        print("Interview cancelled.")
        return
    
    all_results = {}
    
    for persona_type in selected_personas:
        print(f"\n{'='*70}")
        print(f"INTERVIEWING: {persona_type.replace('_', ' ').title()}")
        print(f"{'='*70}")
        
        try:
            # Create interviewer instance
            interviewer = MarketResearchInterviewer(
                persona_type=persona_type,
                research_topic=topic_name
            )
            
            # Conduct interview
            results = interviewer.conduct_full_interview(questions)
            
            # Save results
            filepath = interviewer.save_interview()
            all_results[persona_type] = {
                "results": results,
                "filepath": filepath
            }
            
            print(f"\nInterview completed and saved to: {filepath}")
            
        except Exception as e:
            print(f"Error interviewing {persona_type}: {e}")
            continue
        
        # Optional pause between interviews
        if len(selected_personas) > 1:
            input("\nPress Enter to continue to next interview...")
    
    print(f"\n{'='*70}")
    print("SIMULATION COMPLETE")
    print(f"{'='*70}")
    print(f"Total interviews conducted: {len(all_results)}")
    print("Results saved in the 'interview_results' directory")
    
    # Generate summary
    generate_interview_summary(all_results, topic_name)
    
    return all_results

def generate_interview_summary(results, topic_name):
    """Generate a brief summary of interview results"""
    
    if not results:
        return
    
    print(f"\n=== INTERVIEW SUMMARY: {topic_name} ===")
    
    for persona_type, data in results.items():
        conversation_history = data.get("results", {})
        total_questions = len(conversation_history)
        
        print(f"\n{persona_type.replace('_', ' ').title()}:")
        print(f"  - Questions answered: {total_questions}")
        print(f"  - Results file: {os.path.basename(data['filepath'])}")
    
    print(f"\nAll interview data is available in the 'interview_results' directory.")
    print("You can analyze the JSON files or use the analyze_interviews.py script for detailed analysis.")

def run_quick_test():
    """Run a quick test with one persona and fewer questions"""
    
    print("=== QUICK TEST MODE ===")
    print("Testing with Tech Early Adopter persona and 3 sample questions")
    
    test_questions = [
        "What's your favorite type of product to buy?",
        "How do you make purchasing decisions?",
        "What influences your brand choices?"
    ]
    
    try:
        interviewer = MarketResearchInterviewer(
            persona_type="tech_early_adopter",
            research_topic="Quick Test"
        )
        
        results = interviewer.conduct_full_interview(test_questions)
        filepath = interviewer.save_interview()
        
        print(f"\nTest completed successfully!")
        print(f"Results saved to: {filepath}")
        
        return results
        
    except Exception as e:
        print(f"Test failed with error: {e}")
        return None

def show_help():
    """Display help information"""
    
    print("\n=== HELP ===")
    print("Usage:")
    print("  python sample_market_research.py        - Run full interactive simulation")
    print("  python sample_market_research.py test   - Run quick test")
    print("  python sample_market_research.py help   - Show this help")
    print("\nFeatures:")
    print("  - Multiple research topic categories")
    print("  - Customizable question sets")
    print("  - Question templates for common scenarios") 
    print("  - Interactive question editing")
    print("  - Multiple AI persona interviews")
    print("  - Automatic result saving and analysis")
    print("\nOutput:")
    print("  - Individual JSON files for each interview")
    print("  - Saved in 'interview_results' directory")
    print("  - Compatible with analyze_interviews.py script")

if __name__ == "__main__":
    # Choose what to run based on command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            run_quick_test()
        elif sys.argv[1] == "help":
            show_help()
        else:
            print(f"Unknown option: {sys.argv[1]}")
            print("Use 'test', 'help', or no argument for full simulation")
    else:
        run_market_research_simulation()
