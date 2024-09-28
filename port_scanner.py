import socket
import sys
import argparse
from os import path


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="ingresa la url sin http")
parse = parser.parse_args()



def main():
    if parse.target:
        if path.exists('puertos.txt'):
            with open('puertos.txt', 'r') as wordlist:
                puertos = wordlist.read().splitlines()
            if not puertos:
                print("no hay")
            for puerto in puertos:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                res = s.connect_ex((parse.target, int(puerto)))
                if res == 0:
                    print(f"El puerto {puerto} Esta abiertyo y vulnerable")
                s.close()

if __name__ == "__main__":
    try:
        main()
    except  KeyboardInterrupt:
        sys.exit()