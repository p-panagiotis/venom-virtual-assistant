import logging

from core import venom
from core.modules.speak_mod import speak

logger = logging.getLogger(__name__)


def output(o):
    logger.info(f"{venom.cfg['va.name']}: {o}")
    speak(o)
