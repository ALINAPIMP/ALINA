import requests
from bs4 import BeautifulSoup
# import pandas as pd
import csv

url = "https://www.aruodas.lt/uzsienio-objektai/"
response = requests.get(url)
if response.status_code == 200:
    # print("Puslapis pasiekiamas")
    soup = BeautifulSoup(response.content, 'html.parser')

    objektu_informacija = []

    objektai = soup.find_all('div', class_='project-list-item')

    for objektas in objektai:
        pavadinimas = objektas.find('h2', class_='project-title-full project-title').text.strip()
        plotas_ir_kaina = objektas.find('h3', class_='project-title-full project-min-values')
        if plotas_ir_kaina:
            h3_tekstas = plotas_ir_kaina.get_text(" ", strip=True)
            h3_dalys = h3_tekstas.split('|')
            plotas = None
            kaina = None

            for tekstas in h3_dalys:
                if 'Plotas' in tekstas:
                    plotas = tekstas.split(':')[1].strip().replace(' ', '')
                elif 'Kaina' in tekstas:
                    kaina = tekstas.split(':')[1].strip()
            plotas = plotas if plotas is not None else "Plotas nerastas"
            kaina = kaina if kaina is not None else "Kaina nerasta"
        else:
            plotas = "Plotas nerastas"
            kaina = "Kaina nerasta"

        objektu_informacija.append({'Pavadinimas': pavadinimas, 'Plotas': plotas, 'Kaina': kaina})

        with open('aruodas_data.csv', mode='w', newline='', encoding='utf-8') as failas:
            writer = csv.DictWriter(failas, fieldnames=objektu_informacija[0].keys())
            writer.writeheader()
            for objektas in objektu_informacija:
                writer.writerow(objektas)