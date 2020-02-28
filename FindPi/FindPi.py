# -- Description ----------------------------------------------------------------------------- #
# Given a function , that returns two random values between 0..1 , calculate the value of Pi
# Credits to YT channel Joma Tech
# -------------------------------------------------------------------------------------------- #
import random


def near_pi(number):
    number_points_in_circle = 0
    number_points_in_total = 0

    for _ in range(number):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if (x**2 + y**2) <= 1:
            number_points_in_circle += 1

        number_points_in_total += 1

    return 4 * number_points_in_circle/number_points_in_total


while(True):
    precision = int(input("How precise ?"))
    print(near_pi(precision))