#FONCTIONS
# verifierIntegriteMasque(masque) ==> Vérifie l'intégralité du masque entré (true / false en sortie)
# verifierIntegriteIP(ip) ==> Vérifie l'intégrité de l'ip entré (true / false en sortie)
# getNotationCIDR(masque) ==> Donne la notation format "/24" d'un masque (int en sortie)
# getNormalMask(masqueCIDR) ==> Donne la notation classique d'un masque via une entrée "/24" (string en sortie)
# transformationEnVecteur(ip) ==> A utiliser en début de chaque script avec l'entrée des données, permets de vérifié l'intégrité générale
# des informations (ip ou masque). Renvoie False si les données sont incohérantes ou un vecteur des informations transformées.


import re 
import ipaddress

def verifierIntegriteMasque(masque):
    masqueValide = True

    if(int(masque[0])==0):
        masqueValide = False
        return masqueValide

    for octet in masque:
        if (int(octet)>255 or int(octet) <0):
            masqueValide = False
            return masqueValide
        
    x = range(1,4)
    for n in x:
        if(int(masque[n])>int(masque[n-1])):
            masqueValide = False
    return masqueValide


def getNotationCIDR(masque):

    compteur = 0

    masqueDivise = masque.split()

    for octet in masqueDivise:
        octetBinare = bin(int(octet))[2:]
        
        for bit in octetBinare:
            if(bit == '1'):
                compteur = compteur +1

    
    return compteur    


def getNormalMask(masqueCIDR):
    if(masqueCIDR<0 or masqueCIDR>32):
        return False
    masque = "0.0.0.0/"+str(masqueCIDR)
    masqueNormal = ipaddress.ip_network(masque,strict = False)
    resultat = str(masqueNormal.with_netmask).replace("0.0.0.0/","")
    return(resultat)


def verifierIntegriteIP(adresseIP):
    IPValide = True

    for octet in adresseIP:
        if (int(octet)>255 or int(octet) <0):
            IPValide = False
            return IPValide

    return IPValide


def transformationEnVecteur(ip):
    ipSplite = ip.split()

    if(len(ipSplite)!=4):
        return False

    for octet in ipSplite:
        if (re.search('[a-zA-Z_]',octet)):
            return False

    return ipSplite

def TrouverAdresseSousReseau(ip,masque):
    resultat = ['0', '0', '0', '0']
    x = range(0,4)
    for n in x:
        resultat[n] = int(ip[n]) & int(masque[n])
    return resultat

def TrouverAdresseBroadcastClassfull(ip):
    indiceMasque = 0
    ip[0] = int(ip[0])
    if(ip[0]==127 or ip[0]==0 or ip[0] >223):
        indiceMasque=0
    elif(ip[0]>=0 and ip[0]<=127):
        indiceMasque=1
    elif(ip[0]>=128 and ip[0]<=191):
        indiceMasque=2
    elif(ip[0]>=192 and ip[0]<=223):
        indiceMasque=3
    ipReseau = ['255', '255', '255', '255']
    x = range(0,indiceMasque)
    for n in x:
        ipReseau[n] = str(ip[n])
    return ipReseau

def trouverAdresseReseau(ip):
    indiceMasque = 0
    ip[0] = int(ip[0])
    if(ip[0]==127 or ip[0]==0 or ip[0] >223):
        return("IP reservée ou de classe D ou E")
    elif(ip[0]>=0 and ip[0]<=127):
        indiceMasque=1
    elif(ip[0]>=128 and ip[0]<=191):
        indiceMasque=2
    elif(ip[0]>=192 and ip[0]<=223):
        indiceMasque=3
    ipReseau = ['0', '0', '0', '0']
    x = range(0,indiceMasque)
    for n in x:
        ipReseau[n] = str(ip[n])
    return ipReseau