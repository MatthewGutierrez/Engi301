"""
--------------------------------------------------------------------------
Blink User 3 LED for Pocket Beagle
--------------------------------------------------------------------------
License:   
Copyright 2024 - <Matthew Gutierrez>

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Program to blink the User 3 LED that will: 
  - Use Adafruit BBIO library to blink the USR3 LED at 5 Hz
  - Repeat this indefinetly
  - Only be broken when program is terminated with Ctrl^C

--------------------------------------------------------------------------
"""

import Adafruit_BBIO.GPIO as GPIO
import time

# Name the GPIO pin as the User 3 pin
LED_PIN = "USR3"

def main():
    # Make the GPIO pin the output for the blinking
    GPIO.setup(LED_PIN, GPIO.OUT)
    
    #To make it blink at 5 Hz, have it blink at 0.1 second intervals
    try:
        while True:
            # Turn on the LED
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.1)  # Wait for 0.1 seconds
            
            # Turn off the LED
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.1)  # Wait for 0.1 seconds
    except KeyboardInterrupt:
        # Create a way to stop the blinking with Ctrl^C
        GPIO.cleanup()

if __name__ == "__main__":
    main()
    