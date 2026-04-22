from machine import Pin, ADC
import utime

# Hardware Setup [cite: 461-465]
# Voltage Sensor on ADC0 (GPIO 26)
voltage_adc = ADC(Pin(26))
# Current Sensor on ADC1 (GPIO 27)
current_adc = ADC(Pin(27))
# Temperature Sensor (LM35/LM34) on ADC2 (GPIO 28) [cite: 466]
temp_adc = ADC(Pin(28))

# Constants for conversion
# 16-bit ADC max value is 65535, max voltage is 3.3V [cite: 400, 460]
ADC_CONVERSION_FACTOR = 3.3 / 65535

def read_sensors():
    # Read raw values
    v_raw = voltage_adc.read_u16()
    i_raw = current_adc.read_u16()
    t_raw = temp_adc.read_u16()

    # Convert to actual values (Scales depend on your specific sensor modules)
    voltage = v_raw * ADC_CONVERSION_FACTOR * 5  # Assuming a 1:5 voltage divider
    current = i_raw * ADC_CONVERSION_FACTOR      # Amps
    
    # Power Calculation [cite: 1399, 1447]
    power = voltage * current
    
    # Temperature Calculation (LM35 scale: 10mV per degree Celsius) [cite: 947, 1023]
    temp_c = (t_raw * ADC_CONVERSION_FACTOR) * 100 

    return voltage, current, power, temp_c

print("Starting Solar PV Monitoring System...")

while True:
    v, i, p, t = read_sensors()
    
    # Display results for monitoring [cite: 1404-1407, 1450-1453]
    print("-" * 30)
    print("Voltage: {:.2f} V".format(v))
    print("Current: {:.4f} A".format(i))
    print("Power:   {:.2f} W".format(p))
    print("Temp:    {:.2f} C".format(t))
    
    # Logic for IoT Updates (Send to Blynk or ThingSpeak here) [cite: 106, 1401]
    
    utime.sleep(2) # Update every 2 seconds
