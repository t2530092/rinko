import requests

def fetch_data():
    url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
    response = requests.get(url)
    return response.json()


def main():
    web_datas = fetch_data()
    web_datas = web_datas[0]
    for timeSerie in web_datas["timeSeries"]:
        for area in timeSerie["areas"]:
            name = ""
            weathers = ""
            for key in area.keys():
                if key == "area":
                    name = area[key]["name"]
                elif key == "weathers":
                    weathers = area[key]
            if weathers != "":
                print(f"{name}    {weathers}")
    return

if __name__ == "__main__":
    main()
    