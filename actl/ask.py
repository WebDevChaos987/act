from .color import color

def ask(prompt_text, prompt_color="white"):
    """
    Asks the user for input using a colored prompt question.
    """
    # 1. Apply your color function to the question text
    styled_prompt = color(prompt_text, prompt_color)
    
    # 2. Pass that beautifully styled text directly into Python's input
    user_response = input(styled_prompt)
    
    return user_response
