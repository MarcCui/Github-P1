#Bloc02 ->Python Github_Practica01.py  V03

# Importar la llibreria math i la constant PI Alumn@ 26
# L'alumn@ 26 ens explicarà què és la llibreria math i perquè la fem servir
# La llibrería math proporciona accés a les funcions matemàtiques definides per l'estàndard C. L'utilitzem per fer les funcions matemàtiques bàsiques.

import math
PI = math.pi  

# Àrees i perímetres
# Els números es corresponen amb el número que he assignat a cada figura de la taula
# Els números també es corresponen amb els de l'alumn@ que ha de fer el programa i enviar-lo
# El número de l'alumnat es correspon amb el seu número de llista

def quadrat(): # 1 (figura 1 alumn@ 1 i així fins al 25    print("Càlcul de l'àrea i del perímetre d'un quadrat ")
    

def triangle(): # 2 Pau A
    

def rectangle(): # 3
    

def paralellogram(): # 4
    

def rombe(): # 5
    


def estel(): # 6 Biel B.

     
def trapezi(): # 7 Mariona B

def cercle(): # 8 Eric.C

def poligon(): # 9 PolC
    

def corona(): # 10 Judit C
    
def sector(): # 11 Marc C 
    print("Càlcul de l'àrea i del perímetre d'un sector circular ")
    angle = float(input("Angle en graus = "))
    R = float(input("radi = "))
    area = PI * pow(R,2) * angle/360
    perimetre = 2 * PI * R * (1-(angle/360))
    return area, perimetre

    

# Àrees i volums

def cub(): # 12
   

def cilindre(): # 13
    

def ortoedre(): # 14
    

def prisma_recte(): # 15
    

def con(): # 16
   

def tronc_con(): # 17
   

def esfera(): # 18
    

def piramide(): # 19
                  
def tetraedre_regular(): # 20
   

def octaedre_regular(): # 21
    
def tronc_piramide(): # 22 Irina M
 
def casquet_esferic(): # 23 Pere M.
    
def fus_falcaEsferica(): # 24
    
    
def segment_esferic(): # 25 Eduardo Otoni
    

# Els alumnes 27 i 28 buscaran les taules a treballar i comprobaran resultats d'execució
# Programa principal  Alumn@ 27

print(" Menú -- Mides en unitat donada ")
print("================================")
print("")
print("1. ")
print("2. ")
print("3. ")
print("4. ")
print("5. ")
print("6. ")
print("7. ")
print("8. ")
print("9. ")
print("10. ")
print("11. ")
print("")
print("12. L'àrea i el volum d'un cub ") # Alumne 28
print("13. L'àrea i el volum d'un cilindre ")
print("14. L'àrea i el volum d'un ortoedre ")
print("15. L'àrea i el volum d'un prisma recte ")
print("16. L'àrea i el volum d'un con ")
print("17. L'àrea i el volum d'un tronc de con ")
print("18. L'àrea i el volum d'una esfera ")
print("19. L'àrea i el volum d'una piràmide ")
print("20. L'àrea i el volum d'un tetraedre regular ")
print("21. L'àrea i el volum d'un octaedre regular ")
print("22. L'àrea i el volum d'un tronc de piràmide ")
print("23. L'àrea i el volum d'un casquet esfèric ")
print("24. L'àrea i el volum d'un fus -falca esfèrica- ")
print("25. L'àrea i el volum d'una zona o segment esfèric ")
print("")
print("==============================================")

menu = int(input("escull un element del menú: "))

# Àrees i perímetres  Alumn@ 29 jan.r

if menu == 1 :
    area, perimetre = quadrat()
    print("L'àrea és ", area)
    print("El perímetre és ", perimetre)
    
elif menu == 2 :
    area, perimetre = triangle()
    print("L'àres és ", area)
    print("El perímetre és ", perimetre)
    
elif menu == 3 :
    area, perimetre = rectangle()
    print("L'àrea és ", area)
    print("El perímetre és ", perimetre)
    
elif menu == 4 : # 30 Anaís S.
    area, perimetre = paralellogram()
    print("L'àrea és ", area)
    print("El perímetre és ", perimetre)
    
elif menu == 5 :
    area, perimetre = rombe()
    print("L'àrea és ", area)
    print("El perímetre és ",perimetre)
    
elif menu == 6 :
    area, perimetre = estel()
    print("L'àrea és ", area)
    print("El perímetre és ",perimetre)
    
elif menu == 7 :  
     area, perimetre = trapezi()
    print("L'àrea és ", area)
    print("El perímetre és ", perimetre)
    
elif menu == 8 : # Alumn@ 31
    
    
elif menu == 9 :
    

   
elif menu == 10 :
    
    
elif menu == 11 :
    

# Àrees i volums Alumn@ 32 JanS

elif menu == 12 :
    area, volum = cub()
    print("L'àrea és ",area)
    print("El volum és ",volum)
    
elif menu == 13 :
    area, volum = cilindre()
    print("L'àrea és ",area)
    print("El volum és ",volum)
    
elif menu == 14 :
    area, volum = ortoedre()
    print("L'àrea és ",area)
    print("El volum és ",volum)
elif menu == 15 :
    area, volum = prisma_recte()
    print("L'àrea és ",area)
    print("El volum és ",volum)
elif menu == 16 : # Alumn@ 33
    
elif menu == 17 :
    
elif menu == 18 :
    
elif menu == 19 :
    
elif menu == 20 :
    
elif menu == 21 : # Alumn@ 34
    
elif menu == 22 :
    
elif menu == 23 :
    
elif menu == 24 :
    
elif menu == 25 :
    

# Git commands Alumn@ 35

# git clone [https:// --- adreça de l'enllaç del codi que us poso tot seguit
# https://github.com/EscolaIndustrial-Programacio/Github_Practica01.git

# El git clone nomes s'ha de fer UNA VEGADA!!!, ja teniu les carpetes al PC

# Si voleu, per tornar a començar, esborreu la carpeta Github_Practica01 sencera...
# ... botó dreta -> Actualizar i torneu a fer un git clone a:

# https://github.com/EscolaIndustrial-Programacio/Github_Practica01.git

# Ara us heu de posar dins la carpeta Github_Practica01, on teniu els arxius
# Seguiu amb la llista de gits que ve tot seguit

# git pull (recuperar l'estat actual del programa, tal i com es troba al remot)
# Afegiu la vostra part del programa
# On hi ha el comentari amb el vostre número, poseu per exemple 36 JosepMariaB
# Configuració de correu (vosaltres amb el vostre correu)
# git config -- user.email "elvostreusuari@escolaindustrial.org"
# git config -- user.name "nom d'usuari de l'alumn@", el de l'Escola 


# git status ( si heu fet modificacions, us marcarà en vermell)
# git add . -> afegeix tots els arxius. Deixa l'espai abans del punt
# git status (ja surten les modificacins en verd)
# git commit -m "Nom+inicialcognom + Numero [el vostre]-> "Exemple JosepMariaB Num 36"
# git status
# git push -> pujar al repositori

# Us demanarà un codi:
# Usuari: EscolaIndustrial
# Contrasenya: GithubEscolaIndustrial
# També us pot demanar un codi que us donarà just abans
# git status

# cada alumn@ vetllarà perquè la seva part de codi funcioi


""" Prèviament cada alumn@ haurà programat algunes de les figures
primer amb programació estructurada i després amb programació modular.

Cada alumn@ comprobarà la part de codi que envia des del seu ordinador local
"""