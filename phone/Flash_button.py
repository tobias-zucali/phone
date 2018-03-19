from gpiozero import Button


class Flash_button:
  def __init__(self, port_half, port_full):
    self.__button_half = Button(port_half)
    self.__button_full = Button(port_full)
  
  def when_pressed_half(self, callback):
    self.__button_half.when_pressed = callback

  def when_pressed_full(self, callback):
    self.__button_full.when_pressed = callback

  def when_released_full(self, callback):
    self.__button_full.when_released = callback

  def when_released_half(self, callback):
    self.__button_half.when_released = callback
