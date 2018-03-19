# Not done yet:
``` python
from time import sleep, time
from gpiozero import Button, DigitalOutputDevice, PWMOutputDevice
from threading import Timer
from signal import pause


turn_the_other_direction = False
is_ringing = False

def init_phone():
  # config
  BELL_1A = 27
  BELL_2A = 22
  BLINK = 21

  # TODO: wrap bell stuff
  bell_1a = DigitalOutputDevice(BELL_1A)
  bell_2a = DigitalOutputDevice(BELL_2A)

  def ring_the_bell(speed):
    global turn_the_other_direction
    if turn_the_other_direction:
      bell_1a.on()
      bell_2a.off()
    else:
      bell_1a.off()
      bell_2a.on()

    turn_the_other_direction = not turn_the_other_direction
    sleep(speed / 1000.0)

  def ring_the_bell_often(speed, count):
    current_count = 0
    while current_count < count:
      ring_the_bell(speed)
      current_count += 1

  def start_ringing(speed = 100):
    print("start_ringing")
    global is_ringing
    is_ringing = True
    while is_ringing:
      ring_the_bell(speed)
  hook.when_pressed = start_ringing

  def stop_ringing():
    print("stop_ringing")
    global is_ringing
    is_ringing = False
    
  # TODO: how to do a "start ringing" and "stop ringing" function?
  ring_the_bell_often(50, 2)

  blink = PWMOutputDevice(BLINK, initial_value=0, frequency=500)
  blink.pulse(n = 2)
  # blink.value = 0

  pause()
```

# Wissenswertes
- [Hörton](https://de.wikipedia.org/wiki/H%C3%B6rton)
- [Rückfragetaste](https://de.wikipedia.org/wiki/R%C3%BCckfragetaste)
- [Anleitung Kohlemikrophon](http://www.instructables.com/id/Balanced-Microphone-From-An-Old-Telephone/) ([Bauteil](https://www.conrad.at/de/miniatur-uebertrager-impedanz-670-primaerspannung-155-v-inhalt-1-st-739679.html))