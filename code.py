from machine import Pin, ADC
import time

motor_fr_in1 = Pin(12, Pin.OUT)
motor_fr_in2 = Pin(13, Pin.OUT)
motor_fl_in1 = Pin(14, Pin.OUT)
motor_fl_in2 = Pin(15, Pin.OUT)

right_ir = ADC(26)
left_ir = ADC(27)

=== Parameters ===,
LINE_THRESHOLD = 20000
PULSE_TIME = 0.03

def move_forward():
    motor_fr_in1.high()
    motor_fr_in2.low()
    motor_fl_in1.high()
    motor_fl_in2.low()
    time.sleep(PULSE_TIME)
    stop()

def move_backward():
    motor_fr_in1.low()
    motor_fr_in2.high()
    motor_fl_in1.low()
    motor_fl_in2.high()
    time.sleep(PULSE_TIME)
    stop()

def turn_right():
    motor_fr_in1.low()
    motor_fr_in2.high()
    motor_fl_in1.high()
    motor_fl_in2.low()
    time.sleep(PULSE_TIME)
    stop()

def turn_left():
    motor_fr_in1.high()
    motor_fr_in2.low()
    motor_fl_in1.low()
    motor_fl_in2.high()
    time.sleep(PULSE_TIME)
    stop()

def stop():
    motor_fr_in1.low()
    motor_fr_in2.low()
    motor_fl_in1.low()
    motor_fl_in2.low()

print("Starting Line Follower...")
while True:
    right_val = right_ir.read_u16()
    left_val = left_ir.read_u16()

    print(f"Left: {left_val} | Right: {right_val}")

    right_on_line = right_val < LINE_THRESHOLD
    left_on_line = left_val < LINE_THRESHOLD

    if left_on_line and right_on_line:
        move_forward()
    elif left_on_line and not right_on_line:
        turn_right()
    elif right_on_line and not left_on_line:
        turn_left()
    else:
        stop()
