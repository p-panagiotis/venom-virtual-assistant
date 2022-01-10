from datetime import datetime

from core.modules.output_mod import output


def greet(master):
    hour = datetime.now().hour

    if 5 <= hour < 12:
        output(f"Good morning {master}")
    elif 12 <= hour < 18:
        output(f"Good afternoon {master}")
    else:
        output(f"Good evening {master}")
