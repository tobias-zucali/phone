import os

def speak(message, locale='de'):
  print("speech: '%s' (%s)" % (message, locale))
  os.system("espeak -v%s '%s'" % (locale, message))
