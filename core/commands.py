from difflib import get_close_matches
from core.speak import speak

def my_command(command):
    known_commands = {
        "hello": "Hello Boss! how r u?.",
        "myra": "Haaann Jii!",
        "oyeee myra": "Haaann Jii Haaann!",
        "how are you": "Fine boss, waiting for your command.",
        "your work": "I work as your personal AI assistant.",
        "kaise ho": "Ekdam Badhiya.",
        "mera name batyo": "Harsh Pratap Singh.",
        "tum kiski paglu ho": "maaiin harshhpagluuu hu.",
        "are you real": "I am as real as your imagination.",
        "what is your name": "My name is MYRA. Multimodal Yielding Responsive Assistant.",
        "what is ai": "AI means Artificial Intelligence, the simulation of human intelligence in machines.",
        "who is prime minister of india": "Narendra Modi is the current Prime Minister of India.",
        "i am hungry": "Boss, you should eat something light and healthy.",
        "nice": "Thank you"
    }

    if command in known_commands:
        speak(known_commands[command])
        return True
    else:
        close_match = get_close_matches(command, known_commands.keys(), n=1, cutoff=0.6)
        if close_match:
            speak(known_commands[close_match[0]])
            return True
        return False
