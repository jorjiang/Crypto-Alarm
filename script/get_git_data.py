import re
import urllib.request as ur
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm


def get_git():
    quote_page = 'https://www.cryptomiso.com/'
    
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'
    page = ur.urlopen(ur.Request(quote_page, data=None, headers={'User-Agent': user_agent}))
    
    
    
    soup = BeautifulSoup(page, 'html.parser')
    
    tags = soup.find_all('div', attrs={'class': 'card-body'})
    
   
    date = pd.date_range(end = pd.datetime.today(), periods = 52, freq = '7D', normalize = True).tolist()
    date = pd.to_datetime(date)
    coin_name = []
    data = []
    for tg in tqdm(tags[:-1]):
        axis_max = float(str(tg.contents).split('</text><text')[0].split('">')[-1])
        coin_name.append(str(tg.contents[1]).split('href="#')[1].split('"')[0])
        try:                     
            data_string = str(tg.contents[5]).split('path d=')[1][2:].split('"><')[0]
        except:
            data_string = str(tg.contents[3]).split('path d=')[1][2:].split('"><')[0]
    
        string = re.findall('M[^M]*Z', data_string)
        string = list(map(lambda x: (float(x.split(',')[1].split(' ')[0]) - float(x.split(',')[-1][:-2]))*1.11265*axis_max/242, string))
        data.append(string)                      
    
    df = pd.DataFrame(data).transpose()
    df.columns = coin_name
    df.index = date
    df = df.resample('1D').interpolate()
    return df
