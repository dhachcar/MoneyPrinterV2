import os
import sys
from classes.Tts import TTS

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)

from utils import *
from config import *