from machine import Pin
import utime

# Create an object 'led' linked to GPIO 28 [cite: 1365-1368, 1380]
# Note: Onboard LED for Pico W is usually accessed differently, 
# but this tests external LED hardware on Pin 34 (GPIO 28)[cite: 1366].
led = Pin(28, Pin.OUT)
led.low() # Ensure it starts off [cite: 1369, 1381]

print("Starting Blink Test...")

while True:
    led.toggle() # Toggle LED on and off [cite: 1373, 1383]
    print("Toggle") # Feedback to Shell [cite: 1374, 1384]
    utime.sleep(1) # Wait for 1 second [cite: 1375, 1385]
