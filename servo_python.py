import time
import wiringpi
 
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
delay_period = 0.08
 
while True:
        for pulse in range(250, 50, -5):
                wiringpi.pwmWrite(17, pulse)
                time.sleep(delay_period)
        for pulse in range(250, 50, -5):
                wiringpi.pwmWrite(18, pulse)
                time.sleep(delay_period)
