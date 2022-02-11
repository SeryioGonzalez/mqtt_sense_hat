import sys
import time
from sense_hat import SenseHat

message_to_display = sys.argv[1]

sense = SenseHat()
sense.show_message(message_to_display)

