import sys
import time


# Standard Text
def print2(impFromDoom):
    for c in impFromDoom:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

# Editor Webb
def print3(impFromDoom):
    for c in impFromDoom:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    print()
