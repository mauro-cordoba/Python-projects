def encriptar(texto):
    texto_final = ''
    for letra in texto:
        ascii = ord(letra)
        ascii += 1
        texto_final += chr(ascii)   
    return texto_final

def desencriptar(texto):
    texto_final = ''
    for letra in texto:
        ascii = ord(letra)
        ascii -= 1
        texto_final += chr(ascii)
    return texto_final

def encriptarArchivo(Ruta_Archivo):
    archivo = open(Ruta_Archivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(Ruta_Archivo, 'w')
    archivo.write(textoEncriptado)
    archivo.close()
    print('======El archivo se encripto correctamente======')


def desencriptarArchivo(Ruta_Archivo):
    archivo = open(Ruta_Archivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(Ruta_Archivo, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()
    print('======El archivo se desencripto correctamente======')

Respuesta_Usuario = input('Presione la letra "e" para encriptar un archivo o "d" para desencriptar: ')
Ruta_Archivo = input('Ingrese la ruta del arhivo: ')

if Respuesta_Usuario == 'e':
    encriptarArchivo(Ruta_Archivo)
else:
    desencriptarArchivo(Ruta_Archivo)



