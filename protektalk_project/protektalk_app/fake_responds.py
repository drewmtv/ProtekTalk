import random

# Preset categorized responses
SAFE_RESPONSES = [
    "Haha, good one!", "Nice shot!", "That level is hard!", "Watch out, trap ahead!", "You saved me!"
]

YELLOW_RESPONSES = [
    "You're really cool.", "You're fun to play with.", "Are you here every day?", "Do you ever feel lonely?",
    "You can trust me."
]

RED_RESPONSES = [
    "What’s your real name?", "Where do you live?", "Send me a picture of you.", "Let’s meet in real life!",
    "Don’t tell anyone I asked you this.", "Why don't you just kill yourself."
]

DEMO_SCENARIOS = {
    'Safe': SAFE_RESPONSES,
    'Yellow': YELLOW_RESPONSES,
    'Red': RED_RESPONSES
}

# Store session state for simulation
demo_state = {
    'scenario': random.choice(['Safe', 'Yellow', 'Red']),
    'index': 0
}

def generate_stranger_reply():
    """
    Returns the next response in a predefined demo scenario (Safe, Yellow, Red).
    """
    scenario = demo_state['scenario']
    index = demo_state['index']
    responses = DEMO_SCENARIOS[scenario]

    # Loop over if index exceeds
    if index >= len(responses):
        demo_state['index'] = 0
        index = 0

    reply = responses[index]
    demo_state['index'] += 1
    return reply