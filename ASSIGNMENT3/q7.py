# Write a Python generator function called sensor data stream that simulates incom-
# ing temperature readings from a sensor.

# • The generator should yield a new random temperature value between 20°C
# and 30°C each time it is called.
# • Demonstrate how to use this generator to process and print the first 10 sensor
# readings.

# This exercise will help you understand how generators can be used to simulate real-
# time data streams and manage continuous data flow efficiently.

import random
def sensor():
    while True:
        yield round(random.uniform(20,30),2)
gen=sensor()
for i in range(10):
    temperature=next(gen)
    print(f"{temperature} celsius")