class PID:
    def __init__(self, kp, ki, kd):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, setpoint, measured, dt):
        error = setpoint - measured
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative


if __name__ == "__main__":
    pid = PID(kp=1.2, ki=0.1, kd=0.5)
    target_altitude = 10.0  # meters
    altitude = 0.0
    velocity = 0.0
    dt = 0.1

    for step in range(100):
        thrust = pid.update(target_altitude, altitude, dt)
        velocity += (thrust - 9.81 * 0.1) * dt  # simple toy physics
        altitude += velocity * dt
        if step % 10 == 0:
            print(f"t={step * dt:4.1f}s  altitude={altitude:6.2f} m")