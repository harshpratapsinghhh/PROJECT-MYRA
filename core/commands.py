from difflib import get_close_matches

def my_command(command):
    known_commands = {
        "hello": "Hello Boss! how are you?",
        "myra": "Haan ji!",
        "oyeee myra": "Haan ji haan!",
        "how are you": "Fine boss, waiting for your command.",
        "your work": "I work as your personal AI assistant.",
        "kaise ho": "Ekdam badhiya.",
        "mera name batyo": "Harsh Pratap Singh.",
        "tum kiski paglu ho": "Main Harsh ki paglu hoon.",
        "are you real": "I am as real as your imagination.",
        "what is your name": "My name is MYRA. Multimodal Yielding Responsive Assistant.",
        "what is ai": "AI means Artificial Intelligence.",
        "who is prime minister of india": "Narendra Modi is the Prime Minister of India.",
        "i am hungry": "Boss, you should eat something light and healthy.",
        "nice": "Thank you"
    }

    if command in known_commands:
        return known_commands[command]

    close_match = get_close_matches(command, known_commands.keys(), n=1, cutoff=0.6)
    if close_match:
        return known_commands[close_match[0]]

    return None
