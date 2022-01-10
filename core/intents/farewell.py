from datetime import datetime

from core import venom
from core.modules.output_mod import output


def goodbye():
    hour = datetime.now().hour
    master = venom.cfg["va.master"]

    if 4 >= hour > 18:
        output(f"Good night {master}. Have a nice sleep!")
    else:
        output(f"Bye {master}. Have a nice day!")
