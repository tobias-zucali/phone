from time import sleep, time
from gpiozero import Button, DigitalOutputDevice, PWMOutputDevice
from signal import pause
from threading import Timer


# settings
DIAL_TIMEOUT = 1.5

# config
DIAL_CYCLE = 8
DIAL_SIGNAL = 7
HOOK = 13
BUTTON_LOW = 19
BUTTON_HIGH = 26
BELL_1A = 27
BELL_2A = 22
BLINK = 21

# TODO: wrap whole dial stuff in own class(?) to start/stop and set callback
dial_cycle = Button(DIAL_CYCLE)
dial_signal = Button(DIAL_SIGNAL)

signal_count = None
timeout = None
numbers = []

def handle_dial_timeout():
  global numbers
  sequence = ''.join(map(str, numbers))
  print(sequence)
  print("Number Sequence: %s" % (sequence))
  # ring_the_bell_often(int(sequence), 10)
  numbers = []

  global hook
  # hook.when_pressed = lamda x: start_ringing(int(sequence))
  hook.when_pressed = start_ringing
  hook.when_released = stop_ringing

def start_dial_timeout():
  global timeout
  stop_dial_timeout()
  timeout = Timer(DIAL_TIMEOUT, handle_dial_timeout)
  timeout.start()

def stop_dial_timeout():
  global timeout
  if timeout:
    timeout.cancel()

def dial_cycle_pressed():
  global signal_count
  signal_count = None
  stop_dial_timeout()
dial_cycle.when_pressed = dial_cycle_pressed

def dial_signal_pressed():
  global signal_count
  if signal_count:
    signal_count = signal_count + 1
  else:
    signal_count = 1
dial_signal.when_pressed = dial_signal_pressed

def dial_cycle_released():
  global signal_count
  start_dial_timeout()
  if signal_count:
    numbers.append(signal_count%10)
dial_cycle.when_released = dial_cycle_released


# TODO: wrap whole button stuff
button_low = Button(BUTTON_LOW)
button_high = Button(BUTTON_HIGH)

def button_low_pressed():
  print("button pressed (low)")
button_low.when_pressed = button_low_pressed

def button_high_pressed():
  print("button pressed (high)")
button_high.when_pressed = button_high_pressed


# TODO: wrap whole hook stuff
hook = Button(HOOK)

def hook_pressed():
  print("pick up")
hook.when_pressed = hook_pressed

def hook_released():
  print("hang up")
hook.when_released = hook_released


# TODO: wrap bell stuff
bell_1a = DigitalOutputDevice(BELL_1A)
bell_2a = DigitalOutputDevice(BELL_2A)

turn_the_other_direction = False
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

is_ringing = False
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
