from pyjokes import pyjokes


def get_joke():
    return pyjokes.get_joke(category="all")
