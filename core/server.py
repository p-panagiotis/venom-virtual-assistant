import sys

from core import venom

if __name__ == "__main__":
    try:
        venom.run()
    except KeyboardInterrupt:
        sys.exit(0)
