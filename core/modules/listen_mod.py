import logging

import speech_recognition as sr

from core import venom

logger = logging.getLogger(__name__)
r = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        logger.info("Listening...")
        r.pause_threshold = venom.cfg["va.pause_threshold"]
        audio = r.listen(source)

    query = ""

    try:
        logger.info("Recognizing...")
        query = r.recognize_google(audio, language="en-US")
        logger.info(f"Master: {query}")
    except:
        pass

    return query
