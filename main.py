print("Hello, ESP32!")
from machine import Pin
from utime import sleep

print("Hello Word")

ledVerde = Pin(15,Pin.OUT)
ledAmarelo = Pin(16,Pin.OUT)
ledVermelho = Pin(17,Pin.OUT)

while True:
  ledVerde.on()
  print("Led Verde ON, Ligado")
  sleep(20)
  ledVerde.off()
  print("Led Verde OFF, Desligado")
  sleep(0.5)


  ledAmarelo.on()
  print("Led Amarelo ON, Ligado")
  sleep(10)
  ledAmarelo.off()
  print("Led Amarelo OFF, Desligado")
  sleep(0.5)

  ledVermelho.on()
  print("Led Vermelho ON, Ligado")
  sleep(7)
  ledVermelho.off()
  print("Led Vermelho OFF, Desligado")
  sleep(0.5)
