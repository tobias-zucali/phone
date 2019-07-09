from time import sleep
from gpiozero import DigitalOutputDevice


class Bell:
  def __init__(self, port_bell_1, port_bell_2):
    self.__bell_1 = DigitalOutputDevice(port_bell_1)
    self.__bell_2 = DigitalOutputDevice(port_bell_2)
    self.turn_the_other_direction = True
    self.is_ringing = False

  def __chime(self, duration):
    if self.turn_the_other_direction:
      self.__bell_1.on()
      self.__bell_2.off()
    else:
      self.__bell_1.off()
      self.__bell_2.on()

    self.turn_the_other_direction = not self.turn_the_other_direction
    sleep(duration / 1000.0)

  def ring_the_bell(self, speed = 100, count = -1):
    current_count = 0
    self.is_ringing = True
    while self.is_ringing:
      if count > -1:
        current_count += 1
        if current_count > count:
          break
      self.__chime(speed)

  def stop_ringing(self, ):
    self.is_ringing = False
