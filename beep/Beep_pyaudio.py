import math
from pyaudio import PyAudio
from time import sleep
from threading import Thread

class Beep(Thread):
  BITRATE = 16000 #number of frames per second/frameset.
  is_active = True

  # https://de.wikipedia.org/wiki/H%C3%B6rton
  def __init__(self, frequency = 425):
    # See http://en.wikipedia.org/wiki/Bit_rate#Audio
    # LENGTH = 0.1 #seconds to play sound
    LENGTH = 0.1 #seconds to play sound

    NUMBEROFFRAMES = int(self.BITRATE * LENGTH)
    RESTFRAMES = NUMBEROFFRAMES % self.BITRATE
    self.WAVEDATA = ''

    for x in xrange(NUMBEROFFRAMES):
      self.WAVEDATA += chr(int(math.sin(x / ((self.BITRATE / frequency) / (2 * math.pi))) * 127 + 128))

    # #fill remainder of frameset with silence
    # for x in xrange(RESTFRAMES): 
    #   self.WAVEDATA += chr(128)

  def start(self):
    p = PyAudio()
    stream = p.open(
      format=p.get_format_from_width(1),
      channels=1,
      rate=self.BITRATE,
      output=True,
    )
    self.is_active = True
    while self.is_active:
      stream.write(self.WAVEDATA)

    stream.stop_stream()
    stream.close()
    p.terminate()

  def stop(self):
    self.is_active = False

  # def play(self, duration):
  #   self.start()
  #   pygame.time.delay(duration)
  #   self.stop()

beep = Beep()
beep.start()
sleep(3)
beep.stop()