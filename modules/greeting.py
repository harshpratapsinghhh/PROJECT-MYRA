from datetime import datetime

def get_greeting(name="Harsh"):
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        return f"Good Morning, {name}!"
    elif 12 <= current_hour < 18:
        return f"Good Afternoon, {name}!"
    elif 18 <= current_hour < 22:
        return f"Good Evening, {name}!"
    else:
        return f"It's late night soo jayo"