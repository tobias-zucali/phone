# -*- coding: utf-8 -*-
from signal import pause
from time import sleep

from record import record_to_file, play_from_file
from speak import speak
from beep import Beep


RECEIVER_GPIO = 13
FLASH_BUTTON_LOW_GPIO = 19
FLASH_BUTTON_HIGH_GPIO = 26
DIAL_CYCLE_GPIO = 8
DIAL_SIGNAL_GPIO = 7
BELL_1_GPIO = 27
BELL_2_GPIO = 22
BLINK_GPIO = 21

def main():
  record_some_words()
  pause()


def record_some_words():
  sleep(2)
  speak("Bitte sprechen Sie nach dem Piepston")
  beep = Beep()
  beep.play(1000)

  record_to_file('demo.wav')

  speak("Danke! Sie haben folgende Nachricht aufgenommen:")
  play_from_file('demo.wav')

  speak("... und noch einmal:")
  play_from_file('demo.wav')

if __name__ == "__main__":
  # execute only if run as a script
  main()
