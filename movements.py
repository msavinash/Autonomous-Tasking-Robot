import wiringpi as wp
import time
wp.wiringPiSetupGpio()

# Constants
rpm = 45
time_period = 0.020 # in seconds


def motor(x,y,e):			# function to initialize motor pins
	wp.pinMode(x,1)
	wp.pinMode(y,1)
	wp.pinMode(e,1)
	return (x,y,e)


def servo(pin):             # function to initialize servo motor pins
	wp.pinMode(pin,1)
	return pin


def move(dir, dist):         # function to move 'dist' in the 'dir' direction
	global pins
	x=pins[0][0],pins[1][0]
	y=pins[0][1],pins[1][1]
	e=pins[0][2],pins[1][2]

	time = (dist*60)/(rpm*3.142*7.4)
	if dir=='b':
		wp.digitalWrite(x[0],0)
		wp.digitalWrite(y[0],1)
		wp.digitalWrite(x[1],0)
		wp.digitalWrite(y[1],1)
	else:
		wp.digitalWrite(x[0],1)
		wp.digitalWrite(y[0],0)
		wp.digitalWrite(x[1],1)
		wp.digitalWrite(y[1],0)

	wp.digitalWrite(e[0],1)
	wp.digitalWrite(e[1],1)
	wp.delay(int(time*1000))
	wp.digitalWrite(e[0],0)
	wp.digitalWrite(e[1],0)


def turn(dir,thetha):       # function to turn 'theta' degrees in 'dir' direction
	global pins
	x=pins[0][0],pins[1][0]
	y=pins[0][1],pins[1][1]
	e=pins[0][2],pins[1][2]
	time = (19.2*thetha)/(rpm*6*7.4)
	if dir=='r':
		wp.digitalWrite(x[0],0)
		wp.digitalWrite(y[0],1)
		wp.digitalWrite(x[1],1)
		wp.digitalWrite(y[1],0)
	else:
		wp.digitalWrite(x[0],1)
		wp.digitalWrite(y[0],0)
		wp.digitalWrite(x[1],0)
		wp.digitalWrite(y[1],1)
	wp.digitalWrite(e[0],1)
	wp.digitalWrite(e[1],1)
	wp.delay(int(time*1000))
	wp.digitalWrite(e[0],0)
	wp.digitalWrite(e[1],0)


def gate(ball_captured):    # function to open or close gate based on 'ball_captured'
	if (ball_captured % 2) == 0:
		pwm(3)
		print("Ball Captured")
	else:
		pwm(11)
		print("Scored a goal")
	move('b',8)
	turn('r',180)


def pwm(duty_cycle):        # function to replicate softPwm
	global time_period, pins
	on_time = time_period * duty_cycle / 100
	off_time = time_period - on_time
	for i in range(20):
		wp.digitalWrite(pins[2],1)
		time.sleep(on_time)
		wp.digitalWrite(pins[2],0)
		time.sleep(off_time)

pins = (motor(22, 27, 17), motor(19, 13, 26), servo(4))
pwm(11)
