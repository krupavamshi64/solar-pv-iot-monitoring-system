import network
import utime

# Network credentials
SSID = 'YOUR_WIFI_NAME'
PASSWORD = 'YOUR_WIFI_PASSWORD'

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    
    print("Connecting to WiFi...")
    # Wait for connection with a timeout
    max_wait = 10
    while max_wait > 0:
        if wlan.isconnected():
            break
        max_wait -= 1
        print('Waiting for connection...')
        utime.sleep(1)

    if wlan.isconnected():
        print('Connected successfully!')
        print('IP Address:', wlan.ifconfig()[0])
    else:
        print('Connection failed. Check credentials or signal.')

connect()
