import sys
import requests


def main():
    print("Hello world!")
    for x in range(0, 10):
        print(f"{x} -> {x * x}")
    print("All done!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
