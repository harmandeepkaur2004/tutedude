import math

num = float(input("\033[95mEnter a number:\033[0m "))

sqrt_value = math.sqrt(num)
log_value = math.log(num)
sine_value = math.sin(num)

print(f"\n\033[95mSquare root:\033[0m {sqrt_value}")
print(f"\033[95mLogarithm:\033[0m {log_value}")
print(f"\033[95mSine:\033[0m {sine_value}")
