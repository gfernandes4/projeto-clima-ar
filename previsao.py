import requests

api_key = ":)"  # Substitua pela sua chave de API

def get_coordinates(city, state, country, api_key):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        location_data = response.json()
        if location_data:
            lat = location_data[0]['lat']
            lon = location_data[0]['lon']
            return lat, lon
        else:
            print("Nenhuma localização encontrada!")
            return None, None
    else:
        print("Erro ao acessar a API de Geocoding:", response.status_code)
        return None, None

def get_weather(lat, lon, city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        weather = response.json()
        print(f"Temperatura em {city}: {weather['main']['temp']} Celsius")
    else:
        print("Erro ao acessar a API de clima:", response.status_code)


def air_pollution(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        pollution = response.json()
        aqi = pollution['list'][0]['main']['aqi']
        print(f"Indice de Qualidade do Ar: {aqi}")
        if aqi == 1:
            print("Qualidade do ar: Otima")
        elif aqi == 2:
            print("Qualidade do ar: Boa")
        elif aqi == 3:
            print("Qualidade do ar: Moderada")
        elif aqi == 4:
            print("Qualidade do ar: Ruim")
        elif aqi == 5:
            print("Qualidade do ar: Muito ruim")
    else:
        print("Erro ao acessar a API de clima:", response.status_code)
        
# Entrada de dados
print("Informe a cidade:")
city = input()
print("Informe o estado (Ex: SP, RJ, MS, MT):")
state = input()  # Abreviação do estado
print("Informe o pais (Ex: BR, EUA, UK):")
country = input()  # Código do país

# Obter coordenadas e depois a previsão do tempo
lat, lon = get_coordinates(city, state, country, api_key)
# Se a lat e lon != Nome, mostra os graus e a 
if lat is not None and lon is not None:
    get_weather(lat, lon, city, api_key)
    air_pollution(lat, lon, api_key)
