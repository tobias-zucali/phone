import pygame, numpy, pygame.sndarray

class Beep:
  def __init__(self, frequency = 425):
    sampleRate = frequency * 100
    # 44.1kHz, 16-bit signed, mono
    pygame.mixer.pre_init(sampleRate, -16, 1) 
    pygame.init()
    # 4096 : the peak ; volume ; loudness
    # 440 : the frequency in hz
    # ?not so sure? if astype int16 not specified sound will get very noisy, because we have defined it as 16 bit mixer at mixer.pre_init()
    # ( probably due to int overflow resulting in non continuous sound data)
    arr = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * 440 * x / sampleRate) for x in range(0, sampleRate)]).astype(numpy.int16)
    self.sound = pygame.sndarray.make_sound(arr)
    # ?not so sure? -1 means loop unlimited times

  def start(self):
    self.sound.play(-1)

  def stop(self):
    self.sound.stop()

  def play(self, duration):
    self.start()
    pygame.time.delay(duration)
    self.stop()
