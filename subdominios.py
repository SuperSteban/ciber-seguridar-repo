'''
    Programa para encontrar los subdominios de un sitio
    Explicar que hace este script
    Desarrollado por Jorge Esteban corral Santillan
'''
import requests
from os import path
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='indica el dominio de la victima')
parse = parser.parse_args()

def main():
    if parse.target:
        if path.exists('subdominios.txt'):
            with open('subdominios.txt', 'r') as wordlist:
                wordlist = wordlist.read().splitlines()  # Split by lines

            for subdominio in wordlist:
                url = "http://" + subdominio + "." + parse.target
                print(url)

                try:
                    requests.get(url)
                except requests.ConnectionError: pass
                else:
                    print("Se encontro un subdominio: "+url)
        else:
            print("No se encontró el archivo que contiene los subdominios a buscar")
    else:
        print("No se ha indicado un dominio objetivo")

if __name__ == "__main__" :
    try:
        main()
    except  KeyboardInterrupt:
        sys.exit()

