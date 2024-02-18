import time
import Adafruit_BBIO.GPIO as GPIO

# Define the GPIO pin number
button_pin = "P2_2"  # GPIO pin 59

def button_callback(channel):
    print("Button pressed")

# Set up GPIO pin as input with pull-up resistor enabled
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Add event detection for button press
GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)

try:
    print("Press the button (connected to GPIO pin {}) to test.".format(button_pin))
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Clean up GPIO settings
    GPIO.cleanup()
    print("\nTesting complete.")

