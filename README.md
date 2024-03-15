# GeoPhone

`[+]` Este es un programa en `Python` para geolocalizar `números de teléfono.`

`[+]` Está probado en `Kali Linux,` y la nueva versión incorporará un ejecutable para `Windows.`

`[+]` Fuente `utilizada:` [Calvin S](https://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=GeoPhone).

<hr>

| Sistema operativo  | Soporte |
| ------------- | ------------- |
| Linux (Debian)  | ✅ |
| Windows  | :x: |
| Android | :x: |
| MacOS | :x: |
| Apple IOS | :x: |

<hr>

## 🔴 CONFIGURACIÓN 🔴

`[+]` Obtención de las `APIKeys:`

- Registrarse en [Numverify](https://numverify.com/) y en [OpenCageData](https://opencagedata.com/).
- Obtener las APIKeys.
- Escribirlas en orden correspondiente en el archivo [config.json](https://github.com/ZombieGeeK0/GeoPhone/blob/main/config.json).

<hr>

`[+]` Instalación en `Linux (Debian):`

`[+]` Ejecutar el siguiente `comando:`

    sudo apt update -y && sudo apt upgrade -y && git clone https://github.com/ZombieGeeK0/GeoPhone && cd GeoPhone && chmod +x install.sh && chmod 777 install.sh && sudo bash install.sh

<hr>

## 🏁 FUNCIONAMIENTO 🏁

`[+]` Se importan las `librerías:`

```python
import os, opencage, phonenumbers, json, requests, random, time, sys
from opencage.geocoder import OpenCageGeocode
from phonenumbers import geocoder
from googlesearch import search
from colorama import Fore, Back
```

`[+]` Se definen los `dominios:`

```python
dom = ["com","com.tw","co.in","be","de","co.uk","co.ma","dz","ru","ca"]
```

`[+]` Hacemos el setup de `OpenCage:`

```python
geo = OpenCageGeocode(configuracion_dat['OpencageKey'])
phone = phonenumbers.parse(numero)
location = geocoder.description_for_number(phone, 'en')
query = str(location)
results = geo.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
```

## 🥇 CREDITS 🥇

- [ZombieGeek0](https://www.github.com/ZombieGeek0): El proyecto [GeoPhone](https://www.github.com/ZombieGeek0/GeoPhone).
- [Euronymou5](https://www.github.com/Euronymou5): Por el proyecto [Dark-Hydro](https://www.github.com/Euronymou5/Dark-Hydro).

<hr>

PONER IMAGEN

<hr>

`[ 📬 ]` Contacta conmigo a través de `Discord` mandando una invitación a `qwfkr.`

    qwfkr
`[ 📬 ]` Si lo prefieres, mándame un correo a `3xpl017.contact@proton.me.`

    3xpl017.contact@proton.me.
