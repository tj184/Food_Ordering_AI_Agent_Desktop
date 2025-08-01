# platform_navigation.py

import webbrowser

def navigate_to_platform(pizza, platform):
    platform = platform.lower().strip()

    if "domino" in platform:
        print(f"Opening Domino's website to order {pizza}...")
        webbrowser.open("https://www.dominos.co.in/")
    
    elif "pizza hut" in platform or "pizzahut" in platform:
        print(f"Opening Pizza Hut website to order {pizza}...")
        webbrowser.open("https://www.pizzahut.co.in/")
    
    else:
        print(f"Platform '{platform}' not supported yet. Cannot order '{pizza}'.")
