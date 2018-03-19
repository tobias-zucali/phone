# TODO: how to do a 'beep.start()' and 'beep.stop()'?
# Think I have to switch to pygame to be able to do that?

# # pygame minimal example: https://gist.github.com/nekozing/5774628
# import pygame, numpy, pygame.sndarray

# sampleRate = 44100
# # 44.1kHz, 16-bit signed, mono
# pygame.mixer.pre_init(sampleRate, -16, 1) 
# pygame.init()
# # 4096 : the peak ; volume ; loudness
# # 440 : the frequency in hz
# # ?not so sure? if astype int16 not specified sound will get very noisy, because we have defined it as 16 bit mixer at mixer.pre_init()
# # ( probably due to int overflow resulting in non continuous sound data)
# arr = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * 440 * x / sampleRate) for x in range(0, sampleRate)]).astype(numpy.int16)
# sound = pygame.sndarray.make_sound(arr)
# # ?not so sure? -1 means loop unlimited times
# sound.play(-1)
# pygame.time.delay(1000)
# sound.stop()

import math
from pyaudio import PyAudio

def beep():
  # See http://en.wikipedia.org/wiki/Bit_rate#Audio
  BITRATE = 16000 #number of frames per second/frameset.

  # https://de.wikipedia.org/wiki/H%C3%B6rton
  FREQUENCY = 425 #Hz
  LENGTH = 1.2232 #seconds to play sound

  NUMBEROFFRAMES = int(BITRATE * LENGTH)
  RESTFRAMES = NUMBEROFFRAMES % BITRATE
  WAVEDATA = ''    

  for x in xrange(NUMBEROFFRAMES):
    WAVEDATA += chr(int(math.sin(x / ((BITRATE / FREQUENCY) / (2*math.pi))) * 127 + 128))    

  #fill remainder of frameset with silence
  for x in xrange(RESTFRAMES): 
    WAVEDATA += chr(128)

  p = PyAudio()
  stream = p.open(
    format=p.get_format_from_width(1),
    channels=1,
    rate=BITRATE,
    output=True,
  )
  stream.write(WAVEDATA)
  stream.stop_stream()
  stream.close()
  p.terminate()
