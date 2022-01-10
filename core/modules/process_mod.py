import random
import re

from core.intents.bot import get_bot_name, get_bot_marital_status, get_bot_hate, get_bot_love
from core.intents.datetime import get_time, get_date, get_day
from core.intents.farewell import goodbye
from core.intents.jokes import get_joke


def process(query):
    query = query.lower()

    if "your name" in query:
        return get_bot_name()

    elif "you single" in query:
        return get_bot_marital_status()

    elif "you hate" in query:
        return get_bot_hate()

    elif "you love" in query:
        return get_bot_love()

    elif "joke" in query:
        return get_joke()

    elif "time" in query:
        return get_time()

    elif "date" in query:
        return get_date()

    elif re.search(r"\bday\b", query):
        return get_day()

    elif any(i in query for i in ["bye", "see you", "offline"]):
        goodbye()
        quit()

    else:
        return random.choice([
            "Sorry, I can't understand you.",
            "Sorry, I didn't catch that. Could you please repeat?",
            "Not sure I understand."
        ])
