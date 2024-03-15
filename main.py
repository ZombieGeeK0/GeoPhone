# ------------------------------------- Librerías ---------------------------------- # 
import os, opencage, phonenumbers, json, requests, random, time, sys
from opencage.geocoder import OpenCageGeocode
from phonenumbers import geocoder
from googlesearch import search
from colorama import Fore, Back

# ------------------------------------- Colores ---------------------------------- # color.RED
class color:
  RED = Fore.RED + Back.RESET
  RESET = Fore.RESET + Back.RESET

# ------------------------------------- Logo ---------------------------------- # 
def logo():
  os.system('clear')
  title = '''
╔═╗┌─┐┌─┐╔═╗┬ ┬┌─┐┌┐┌┌─┐
║ ╦├┤ │ │╠═╝├─┤│ ││││├┤ 
╚═╝└─┘└─┘╩  ┴ ┴└─┘┘└┘└─┘
'''
  print(color.RED + title + '\n')

# ------------------------------------- Configuración Json ---------------------------------- # 
with open('config.json', 'r') as configuracion:
  configuracion_dat = json.load(configuracion)

# ------------------------------------- Función principal ---------------------------------- # 
def main():
  os.system('clear')
  logo()
  # ------------------------------------- Dominios ---------------------------------- # 
  dom = ["com","com.tw","co.in","be","de","co.uk","co.ma","dz","ru","ca"]
  numero = input(f'{color.RED}[+] Ingresa un numero telefonico: ')
  ip = input(f'{color.RED}[+] Ingresa una IP: ')
  time.sleep(2)
  # ------------------------------------- NumVerify ---------------------------------- # 
  api = f"https://api.apilayer.com/number_verification/validate?number={numero}"
  try:
    key = configuracion_dat['Numverifykey']
    apikey = {
      "apikey": key,
    }
    payload = {}
    lol = requests.request("GET", api, headers=apikey, data = payload).json()
    
    if lol['valid'] == False:
       print(f'{color.RED}\n[!] El numero no es valido')
       sys.exit()
      
    else:
      print(f'{color.RED}\n[+] Numero: ', lol['number'])
      print(f'{color.RED}[+] Codigo del pais: ', lol['country_code'])
      print(f'{color.RED}[+] Nombre del pais: ', lol['country_name'])
      print(f'{color.RED}[+] Ubicacion: ', lol['location'])
      print(f'{color.RED}[+] Transportador: ', lol['carrier'])
      
  except KeyError:
     print(f'{color.RED}\n[+] Ha ocurrido un error')
    
  # ------------------------------------- Opencage ---------------------------------- # 
  geo = OpenCageGeocode(configuracion_dat['OpencageKey'])
  phone = phonenumbers.parse(numero)
  location = geocoder.description_for_number(phone, 'en')
  query = str(location)
  results = geo.geocode(query)
  lat = results[0]['geometry']['lat']
  lng = results[0]['geometry']['lng']
  # ------------------------------------- Phonenumber ---------------------------------- # 
  print(f'\n[+] Municipio: {location}')
  print(f'[+] Latitud: {lat}')
  print(f'[+] Longitud: {lng}')
  # ------------------------------------- Dorking ---------------------------------- # 
  print('\n[+] Realizando busqueda con dorking...')
  time.sleep(2)
  tld = random.choice(dom)
  command = f'intext:{numero}'
  command2 = f"site:@ filetype:PDF intext:{numero}"
  command3 = f"site:facebook.com intext:{numero}"
  command4 = f"site:twitter.com intext:{numero}"
  command5 = f"site:instagram.com intext:{numero}"
  # ------------------------------------- Resultados ---------------------------------- # 
  for j in search(command, tld, num=10, stop=10, pause=2):
    print(f'{color.RED}\n[+]Resultados encontrados: {j}')
  print('{color.RED}\n[+] Buscando número telefonico en archivos pdf...')

  for i in search(command2, tld, num=10, stop=10, pause=2):
    print(f'{color.RED}\n[+]Resultados encontrados: {i}')
  print('{color.RED}\n[+] Buscando numero telefonico en redes sociales..')

  for a in search(command3, tld, num=10, stop=10, pause=2):
    print(f'{color.RED}\n[+]Resultados encontrados: {a}')
    
  for b in search(command4, tld, num=10, stop=10, pause=2):
    print(f'{color.RED}\n[+]Resultados encontrados: {b}')
    
  for c in search(command5, tld, num=10, stop=10, pause=2):
    print(f'{color.RED}\n[+]Resultados encontrados: {c}')

  # ------------------------------------- GeoIP ---------------------------------- # 
  datos = {
    "considerIp": f"{ip}"
  }

  url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=YOUR_API_KEY'
  response = requests.post(url, json=datos) 

  print('\n{color.RED}[+] Latitud: ' + str(response.json()['location']['lat']))
  print('\n{color.RED}[+] Longitud: ' + str(response.json()['location']['lng']))
  print('\n{color.RED}[+] Precisión: ' + str(response.json()['accuracy']))
    
# ------------------------------------- Ejecución ---------------------------------- # 
main()
