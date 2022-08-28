import requests.exceptions
import requests
from pyfiglet import Figlet
import folium

def info_by_api(ip = ' '):
    try:
        response = requests.get( url = f"http://ip-api.com/json/{ip}").json()
        #print(response)
        data = {
            "[IP]": response.get("query"),
            "[Internet provaider]": response.get ("isp"),
            "[Country]": response.get ("country"),
            "[Name region]": response.get ("regionName"),
            "[location_lat]": response.get("lat"),
            "[location_Lon]" : response.get("lat")
        }

        for x, y in data.items():
            print(f"{x} : {y}")

        x = folium.Map(location = [response.get("lat"), response.get("lon")])
        x.save(f"{response.get('query') } _ {response.get ('regionName')} .png")

    except requests.exceptions.ConnectionError():
        print("Произошла неизвестная ошибка!")

def main():
    preview = Figlet(font = "slant")
    print(preview.renderText("IP INFORMATION"))
    ip = input("Введите айпи адрес:")

    info_by_api(ip = ip)

if __name__ == "__main__":
    main()