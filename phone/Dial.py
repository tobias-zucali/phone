from gpiozero import Button
from threading import Timer


class Dial:
  def __init__(self, port_cycle, port_signal):
    self.__button_cycle = Button(port_cycle)
    self.__button_cycle.when_pressed = self.__dial_cycle_pressed
    self.__button_cycle.when_released = self.__dial_cycle_released

    self.__button_signal = Button(port_signal)
    self.__button_signal.when_pressed = self.__dial_signal_pressed

    self.__signal_count = None
    self.__timeout = None
    self.__numbers = []
  
  DIAL_TIMEOUT = 1.5

  def when_number_dialled(self, callback):
    self.__when_number_dialled_callback = callback

  def __handle_dial_timeout(self):
    sequence = ''.join(map(str, self.__numbers))
    print(sequence)
    print("Number Sequence: %s" % (sequence))
    
    if self.__when_number_dialled_callback:
      self.__when_number_dialled_callback(self.__numbers, sequence)

    self.__numbers = []

  def __start_dial_timeout(self):
    self.__stop_dial_timeout()
    self.__timeout = Timer(self.DIAL_TIMEOUT, self.__handle_dial_timeout)
    self.__timeout.start()

  def __stop_dial_timeout(self):
    if self.__timeout:
      self.__timeout.cancel()

  def __dial_cycle_pressed(self):
    self.__signal_count = None
    self.__stop_dial_timeout()

  def __dial_signal_pressed(self):
    if self.__signal_count:
      self.__signal_count = self.__signal_count + 1
    else:
      self.__signal_count = 1

  def __dial_cycle_released(self):
    self.__start_dial_timeout()
    if self.__signal_count:
      self.__numbers.append(self.__signal_count%10)
