import requests
import json 

hakusana = input("Anna hakusana: ")

pyynto = "https://api.tvmaze.com/search/shows?q=" + hakusana
vastaus = requests.get(pyynto).json()
print(vastaus)
