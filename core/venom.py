import sys

from core.configs import Configuration
from core.intents import welcome
from core.logs import Logger
from core.modules.input_mod import take_input
from core.modules.listen_mod import listen
from core.modules.output_mod import output
from core.modules.process_mod import process

cfg = None


def run():
    # load virtual assistant configuration
    global cfg
    cfg = Configuration(filename=sys.argv[1] if len(sys.argv) > 1 else None)

    # initialize virtual assistant logger
    Logger().configure()

    welcome.greet(master=cfg["va.master"])

    while True:
        if cfg["va.listen"]:
            query = listen()
        else:
            query = take_input()

        o = process(query=query)
        output(o)
