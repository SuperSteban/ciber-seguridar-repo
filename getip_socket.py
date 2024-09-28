'''

Primera Forma: nslookup {url}
Segunda forma: nslookup.oi 
Tercera forma mxtoolbox.com
Cuerta Forma: Scrip python

'''

import socket
import sys
import argparse

parse = argparse.ArgumentParser()
parse.add_argument("-t", "--target", help="ingresa la utl sin http")
parse = parse.parse_args()

def getIp(url):
    try:
        ip = socket.gethostbyname(url)
        print(f"La dirección ip de la {url} es: \n {ip}")
    except:
        print("no se pudo encontrar la ip")

def main():
    if parse.target:
        getIp(parse.target)
    else:
        print('Ingresa una direccion valida')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
