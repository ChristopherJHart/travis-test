import sys
import requests


def make_request():
    return requests.get("https://google.com")

def main():
    print("Hello world!")
    for x in range(0, 10):
        print(f"{x} -> {x * x}")
    make_request()
    print("All done!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
