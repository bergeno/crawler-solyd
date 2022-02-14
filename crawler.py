import requests;

from bs4 import BeautifulSoup;

URL_AUTO = "https://django-anuncios.solyd.com.br/automoveis/";


def buscar(url):
    try:
        response = requests.get(url);
        
        if response.status_code == 200:
            return response.text;
        else:
            print("Erro ao fazer requisição.");
    except Exception as error:
        print("Erro ao fazer requisição. ({})" .format(error));
    
def parsing(resposta_html):
    try:
        html = BeautifulSoup(resposta_html, 'html.parser');
        return html;
    except Exception as error:
        print("Something went wrong. ({})".format(error));

def encontrarCards(responseText):
    resposta = buscar(responseText);
    
    if resposta:
        html = parsing(resposta);
        links = html.find_all("a", class_="card");
        urls = [];
        for link in links:
            urls.append(link['href']);
            
        return urls;
    
    
print(encontrarCards(URL_AUTO));
    
# resposta = buscar(URL_AUTO);

# if resposta:
#     html = parsing(resposta);
#     links = html.find_all("a", class_="card");
#     for link in links:
#         print(link['href']);