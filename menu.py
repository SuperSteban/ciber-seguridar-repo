import os
import time

opcion = 0
while(opcion != 6):
    os.system("cls")
    print("SISTEMA PARA PRUEBAS EN SEGURIDAD INFORMATICA")
    print(r"""\
 __     ___   ___   ___      _                                  _       _                 
 \ \   / / | / _ \ / _ \    (_) ___  _ __ __ _  ___    ___  ___| |_ ___| |__   __ _ _ __  
  \ \ / /| || | | | | | |   | |/ _ \| '__/ _` |/ _ \  / _ \/ __| __/ _ \ '_ \ / _` | '_ \ 
   \ V / | || |_| | |_| |   | | (_) | | | (_| |  __/ |  __/\__ \ ||  __/ |_) | (_| | | | |
    \_/  |_(_)___(_)___/   _/ |\___/|_|  \__, |\___|  \___||___/\__\___|_.__/ \__,_|_| |_|
                          |__/           |___/                                            
""")
    print("OPCION 1 ---- Busqueda de Subdominios -----")
    print("OPCION 2 ---- Port Scanner -----")
    print("OPCION 3 ---- Banner Grabbing -----")
    print("OPCION 4 ---- Get ip SOCKET -----")
    print("OPCION 5 ---- Get Ip Command-----")
    print("OPCION 6 ---- SALIR-----")

    try:

        opcion = int(input("Selecciona Opción  "))
        if(opcion==1):
            dominio = str(input("Selecciona un Dominio OBTENER DOMINIOS www."))
            os.system(f"python subdominios.py -t {dominio}")
            time.sleep(11)
        if(opcion==2):
            command = str(input("Selecciona un dominio para Scannear PORTS www."))
            os.system(f"python port_scanner.py -t {command}")
            time.sleep(11)
        if(opcion==3):
            command = str(input("Selecciona un dominio para OBTENER Banner www."))
            port = str(input("Selecciona un puerto"))
            os.system(f"python banner_grabing.py -t {command} -p {port}")
            time.sleep(11)
        if(opcion==4):
            command = str(input("(SOCKET) Selecciona un dominio para OBTENER IP www."))
            os.system(f"python getip_socket.py -t {command}")
            time.sleep(11)
        if(opcion==5):
            command = str(input("(COMMAND)Selecciona un dominio para OBTENER IP www."))
            os.system(f"python getip_command.py -t {command}")
            time.sleep(11)
            

        print("Vale Que le vaya bien!")
    except:
        print("Favor de capturar un numero valido")