from gpiozero import Button


class Receiver:
  def __init__(self, port):
    self.__button = Button(port)
  
  def when_picked_up(self, callback):
    self.__button.when_pressed = callback

  def when_put_down(self, callback):
    self.__button.when_released = callback
  