import math
from pyaudio import PyAudio
from time import sleep
import thread

class Beep():
  BITRATE = 16000 #number of frames per second/frameset.
  is_active = True

  # https://de.wikipedia.org/wiki/H%C3%B6rton
  def start(self, frequency = 425):
    thread.start_new_thread(self.__start, (frequency, ))

  def __start(self, frequency):
    p = PyAudio()
    stream = p.open(
      format=p.get_format_from_width(1),
      channels=1,
      rate=self.BITRATE,
      output=True,
    )
    self.is_active = True
    x = 0
    while self.is_active:
      stream.write(chr(int(math.sin(x / ((self.BITRATE / frequency) / (2 * math.pi))) * 127 + 128)))
      x += 1

    stream.stop_stream()
    stream.close()
    p.terminate()

  def stop(self):
    self.is_active = False

  def play(self, duration, frequency = 425):
    self.start(frequency)
    sleep(duration / 1000.0)
    self.stop()
