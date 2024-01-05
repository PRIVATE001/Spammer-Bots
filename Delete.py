import os
try:
 import pyfiglet
except:
 os.system("pip install pyfiglet")
try:
 import requests
except:
 os.system("pip install requests")

try:
 import os
except:
 os.system("pip install os")

logo = ('''\033[2;32m
___
_   \   \_  _/_ |  / /    |  /  __/
  /_/ /_  /_/ /  /  | / /  /| |_  /    /
_  /_  _, _// /   |/ / _  _ |  /   _  /_
/_/     /_/ |_| /_/  _/  /_/  |_/_/    /___/
''')
print(logo)
h = '-'
print('Spam Bots :- @T62RS ')        
print ('')   
token = input('\033[1;31m  Enter Yout Token :- ')
ID = input('\033[2;34m Enter ID : ')
Msg = input('\033[2;35mMessage :- ')
print('\033[2;35mSpam Run ..........')
while True:  
   tlg = requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={Msg}''')