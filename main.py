
import serial                           # bibliothèque gérant la communication série



def connexion():
    try : # vérification du port série
        global arduino
        arduino = serial.Serial("COM5")
        test = ""
        compteur = 0
        while test != "OK" and compteur<10:
            print("ECHEC")
            compteur = compteur+1 # vérification de la bonne connexion
            test = str(arduino.readline())[2:][:-5]
        if compteur == 10 :
            pb = False
        else :
            pb = True
    except :
        pb = False
    return(pb)


connexion_radar = connexion()

if connexion_radar:
    print("CONNECTE")
    arduino.write('1'.encode('ascii'))


    reception = str(arduino.readline())
    print(reception[2:-5])

    for i in range(180):
        reception = str(arduino.readline())
        print(reception[2:-5])




print("*********  FIN  **********")



