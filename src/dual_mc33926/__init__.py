import pigpio

pi = None
# Motor speeds for this library are specified as numbers
# between -MAX_SPEED and MAX_SPEED, inclusive.
# 19.2 MHz / 2 / 480 = 20 kHz
MAX_SPEED = 480

class Motor(object):
    MAX_SPEED = _max_speed

    def __init__(self, pi, pwm_pin, dir_pin, en_pin):
        self.pi = pi
        self.pwm_pin = pwm_pin
        self.dir_pin = dir_pin
        self.en_pin = en_pin

    def enable(self):
        self.pi.write(self.en_pin, 1)

    def disable(self):
        self.pi.write(self.en_pin, 0)

    def setSpeed(self, speed):
        if speed < 0:
            speed = -speed
            dir_value = 1
        else:
            dir_value = 0

        if speed > MAX_SPEED:
            speed = MAX_SPEED

        self.pi.write(self.dir_pin, dir_value)
        self.pi.set_PWM_dutycycle(self.pwm_pin, speed)

class Motors(object):
    def __init__(self):
        self.pi = None
        self.io_init()
        self.motor1 = Motor(self.pi, 12, 24, 22)
        self.motor2 = Motor(self.pi, 13, 25, 23)

    def io_init():
      if self.pi not None:
        return
      pi = pigpio.pi()
      pi.set_mode(12, pigpio.OUTPUT)
      pi.set_mode(13, pigpio.OUTPUT)
      pi.set_PWM_range(12,MAX_SPEED)
      pi.set_PWM_range(13,MAX_SPEED)
      pi.set_PWM_frequency(12,20000)
      pi.set_PWM_frequency(13,20000)
      pi.set_mode(22, pigpio.OUTPUT)
      pi.set_mode(23, pigpio.OUTPUT)
      pi.set_mode(24, pigpio.OUTPUT)
      pi.set_mode(25, pigpio.OUTPUT)
      self.pi = pi

    def enable(self):
        self.motor1.enable()
        self.motor2.enable()

    def disable(self):
        self.motor1.disable()
        self.motor2.disable()

    def setSpeeds(self, m1_speed, m2_speed):
        self.motor1.setSpeed(m1_speed)
        self.motor2.setSpeed(m2_speed)

motors = Motors()
