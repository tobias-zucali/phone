from gpiozero import PWMOutputDevice


class Blink:
  def __init__(self, port):
    self.blink = PWMOutputDevice(port, initial_value=0, frequency=1000)
  
  def set(self, value):
    self.blink.value = value

  def on(self):
    self.blink.on()

  def off(self):
    self.blink.off()

  def pulse(self, n):
    self.blink.pulse(n)
