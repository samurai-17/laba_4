import requests

headers = {"accept": "application/json", "X-API-KEY": "6FEB804-GSJ4P3F-H8Q997J-WQPQMEK"}


# def get_describe(name):
#     url = f"https://api.kinopoisk.dev/v1.4/movie/search?query={name}"
#     a = requests.get(url, headers=headers).json()
#     return(a["docs"][0]["description"], a["docs"][0]["rating"]["kp"])
#
#
# print(get_describe("Волк с Уолл-стрит"))


# def get_actor(name):
#     url = f"https://api.kinopoisk.dev/v1.4/person/search?query={name}"
#     a = requests.get(url, headers=headers).json()
#     idd = a["docs"][0]["id"]
#     new_url = f"https://api.kinopoisk.dev/v1.4/person/awards?personId={idd}"
#     a = requests.get(new_url, headers=headers).json()
#     return a["docs"][0]["nomination"]
#
# print(get_actor("Леонардо ДиКаприо"))


def get_film(name):
    url = f"https://api.kinopoisk.dev/v1.4/movie/search?query={name}"
    a = requests.get(url, headers=headers).json()["docs"][0]["id"]
    return f"https://www.kinopoisk.ru/film/{a}/"

print(get_film("Во все тяжкие"))