import random

from core import venom


def get_bot_name():
    return f"My name is {venom.cfg['va.name']}"


def get_bot_marital_status():
    return random.choice(["I'm in a relationship with wifi", "No, I'm in love with wifi"])


def get_bot_hate():
    return "I hate when people are calling me a machine"


def get_bot_love():
    return random.choice([
        "I love to chat with machines like you",
        "I love talking to those who love to hear me, those who are connected with me, I talk to them.",
        "I love you"
    ])
