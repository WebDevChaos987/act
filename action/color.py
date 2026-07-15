def color(text, color_name):
    """
    Returns text wrapped in ANSI escape codes to change its color.
    Colors available: red, green, yellow, blue, purple, cyan.
    """
    # Color dict
    codes = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
        "end": "\033[0m"  # Resets colors
    }
    
    # Grab the selected code & if no selected code revert back to default text
    selected_code = codes.get(color_name.lower(), "")
    
    # If the color exists in color dictionary, wrap the text and add the 'end' reset
    if selected_code:
        return f"{selected_code}{text}{codes['end']}"
    return text
