from math import log, fabs
from time import sleep


def infinite_power(base, exponent):
    for x in [base for x in range(exponent-1)]:
        base *= x
    return base


def infinite_log(argument, base=10):
    return log(fabs(argument), fabs(base))


def infinite_division(dividend, divisor):
    quotient, remainder = "", 0
    dividend_B, divisor_B = False, False

    if dividend < 0:
        dividend = int(fabs(dividend))
        dividend_B = True

    if divisor < 0:
        divisor = int(fabs(divisor))
        divisor_B = True

    for digit in str(dividend):
        num = remainder * 10 + int(digit)
        q, r = divmod(num, divisor)
        quotient += str(q)
        remainder = r
    quotient = quotient.lstrip("0")

    if (dividend_B and not divisor_B) or (divisor_B and not dividend_B):
        quotient = f"-{quotient}"

    return (int(quotient), remainder)


def preloader(Character, time=0.5):
    for sleep_number in range(3):
        print(Character)
        sleep(time)


def input_math(explanation, mode="f"):
    while True:
        entry = input(explanation)
        if mode == "f":
            try:
                number = int(entry)
                return number
            except:
                print("Error! Please enter numbers.")
        elif mode == "b":
            if entry != "":
                try:
                    number = int(entry)
                    return number
                except:
                    print("Error! Please enter numbers or blank.")
            else:
                return None
        else:
            sample = mode.split("/")
            if entry in sample:
                return entry
            else:
                print(f"Error! Please enter", *sample)
