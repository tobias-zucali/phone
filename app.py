# -*- coding: utf-8 -*-
from signal import pause
from time import sleep

from record import record_to_file, play_from_file
from speak import speak
from beep import Beep
from phone import Bell, Blink, Dial, Flash_button, Receiver


RECEIVER_GPIO = 13
FLASH_BUTTON_LOW_GPIO = 19
FLASH_BUTTON_HIGH_GPIO = 26
DIAL_CYCLE_GPIO = 8
DIAL_SIGNAL_GPIO = 7
BELL_1_GPIO = 27
BELL_2_GPIO = 22
BLINK_GPIO = 21

def main():
  receiver = Receiver(RECEIVER_GPIO)
  receiver.when_picked_up(record_some_words)
  print("waiting for pickup")

  # # test bell
  # blink = Blink(BLINK_GPIO)
  # blink.pulse(3)

  # # test flash button
  # flash_button = Flash_button(FLASH_BUTTON_LOW_GPIO, FLASH_BUTTON_HIGH_GPIO)
  # flash_button.when_pressed_half(get_set_blink_value(blink, 0.5))
  # flash_button.when_pressed_full(get_set_blink_value(blink, 1))
  # flash_button.when_released_full(get_set_blink_value(blink, 0.5))
  # flash_button.when_released_half(get_set_blink_value(blink, 0))

  # test bell
  bell = Bell(BELL_1_GPIO, BELL_2_GPIO)
  bell.ring_the_bell(100, 2)

  # test dial
  dial = Dial(DIAL_CYCLE_GPIO, DIAL_SIGNAL_GPIO)
  dial.when_number_dialled(when_dialed)

  pause()

def get_set_blink_value(blink, value):
  def set_blink_value():
    blink.set(value)
  return set_blink_value

def record_some_words():
  sleep(2)
  speak("Bitte sprechen Sie nach dem Piepston")
  # beep = Beep()
  # beep.play(1000)

  record_to_file('demo.wav')

  speak("Danke! Sie haben folgende Nachricht aufgenommen:")
  play_from_file('demo.wav')

  speak("... und noch einmal:")
  play_from_file('demo.wav')

def when_dialed(numbers, sequence):
  speak("Sie haben %s gewählt" % ' '.join(map(str, numbers)))

if __name__ == "__main__":
  # execute only if run as a script
  main()
