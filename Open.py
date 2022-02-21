#def main():
#    open("D:/Archivos/LAUNCH X/OnBoarding/mars.jpg")

#if __name__ == '__main__':
#    main()

#try:
#     open('config.txt')
#except FileNotFoundError:
#     print("Couldn't find the config.txt file!")

#Uso de err como variable que almacena el error completo
#try:
#    open("mars.jpg")
#except FileNotFoundError as err:
#    print("got a problem trying to read the file:", err)

#Uso de err.no para detectar el tipo de error de acuerdo a uan excepción general para excepciones particualres
try:
     open("config.txt")
except OSError as err:
     if err.errno == 2:
         print("Couldn't find the config.txt file!")
     elif err.errno == 13:
         print("Found config.txt but couldn't read it") #Tengo la carpeta creada
