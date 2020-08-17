#ejemplo extraer datos de un table dentro de un html y exportarlos a un archivo csv, con beautifulsoup y pandas. 

import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://es.wikipedia.org/wiki/Pandemia_de_enfermedad_por_coronavirus_de_2020_en_Argentina').read().decode()
soup = BeautifulSoup(html,'lxml')

tables = soup.find('table',{'class':'wikitable sortable col2der col3der col4der col5der col6der col7der'}).tbody

rows = tables.find_all('tr')

columns = [v.text.replace('\n', '') for v in rows[0].find_all('th') ]

df = pd.DataFrame(columns=columns)

for i in range(1,len(rows)-1):
  tds = rows[i].find_all('td')
  len (tds)
  if True:
    values = [tds[0].text.replace('\n', ''), tds[1].text.replace('\n', '').replace('\xa0', '').replace('\u200b', '').replace('[n 3]',''), tds[2].text.replace('\n', '').replace('\xa0', ''), tds[3].text.replace('\n', ''), tds[4].text.replace('\n', ''), tds[5].text.replace('\n', ''), tds[6].text.replace('\n', '').replace('\xa0', '') ]
  else:
    values = [td.text for td in tds]

  df = df.append(pd.Series(values, index= columns), ignore_index=True)
  df.to_csv('c19ar.csv', index=False)
  
from google.colab import files
files.download('c19ar.csv') 
