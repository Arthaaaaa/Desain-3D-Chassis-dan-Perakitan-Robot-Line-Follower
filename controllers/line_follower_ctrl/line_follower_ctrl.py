"""Line Follower Controller (PD Control halus untuk 2 Sensor IR)."""

from controller import Robot

TIME_STEP = 16
BASE_SPEED = 4.5
MAX_SPEED = 6.8
KP = 0.015
KD = 0.011
THRESHOLD = 880.0


def clamp(val, low, high):
    return max(low, min(high, val))


def main():
    robot = Robot()

    left_motor = robot.getDevice("left_motor")
    right_motor = robot.getDevice("right_motor")
    left_motor.setPosition(float("inf"))
    right_motor.setPosition(float("inf"))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    ir_left = robot.getDevice("ir_left")
    ir_right = robot.getDevice("ir_right")
    ir_left.enable(TIME_STEP)
    ir_right.enable(TIME_STEP)

    prev_error = 0.0
    last_turn = 0  # -1 = kiri, 1 = kanan

    while robot.step(TIME_STEP) != -1:
        val_left = ir_left.getValue()
        val_right = ir_right.getValue()

        # Kedua sensor di atas hitam (garis melintang/tikungan sangat tajam)
        if val_left < THRESHOLD and val_right < THRESHOLD:
            if last_turn <= 0:
                left_speed, right_speed = -0.5, BASE_SPEED
            else:
                left_speed, right_speed = BASE_SPEED, -0.5
        else:
            # Error positif -> kanan menyentuh hitam -> belok kanan
            # Error negatif -> kiri menyentuh hitam -> belok kiri
            error = val_left - val_right
            derivative = error - prev_error
            correction = KP * error + KD * derivative
            prev_error = error

            if error < -30:
                last_turn = -1
            elif error > 30:
                last_turn = 1

            left_speed = clamp(BASE_SPEED + correction, -1.5, MAX_SPEED)
            right_speed = clamp(BASE_SPEED - correction, -1.5, MAX_SPEED)

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)


if __name__ == "__main__":
    main()
