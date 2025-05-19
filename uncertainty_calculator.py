import sys
import math

def sol():
    length = tuple(map(float, input().split()))
    wavelength = tuple(map(float, input().split()))
    n = int(input())

    for _ in range(n):
        t, x1, x2 = map(float, input().split())
        a = (t * wavelength[0] * length[0]) / x1
        b = a * (wavelength[1] / wavelength[0] + length[1] / length[0] + x2 / x1)
        print(f"{a:.2e} {b:.2e}")
    print()

def main():
    t = int(input())
    for _ in range(t):
        sol()

if __name__ == "__main__":
    main()
