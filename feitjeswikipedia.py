import requests
from datetime import datetime

def get_wikipedia_page_wikitext():
    # Basis URL voor de Wikipedia API
    url = "https://en.wikipedia.org/w/api.php"

    # Huidige datum ophalen
    now = datetime.now()
    
    # Engelstalige naam van de maand ophalen
    month_name = now.strftime("%B")
    
    # Dag van de maand ophalen (zonder voorloopnul)
    day = now.day
    
    # Datum in het gewenste formaat samenstellen
    formatted_date = f"{month_name}_{day}"
    
    # Parameters voor de API-aanroep
    params = {
        "action": "parse",
        "page": formatted_date,
        "prop": "wikitext",
        "format": "json"
    }
    
    # Voer de API-aanroep uit
    response = requests.get(url, params=params)
    
    # Controleer of de aanroep succesvol was
    if response.status_code == 200:
        data = response.json()
        # Haal de wikitext op uit de response
        wikitext = data.get("parse", {}).get("wikitext", {}).get("*", "")
        return wikitext
    else:
        return None

wikitext = get_wikipedia_page_wikitext

if wikitext:
    print(wikitext)
else:
    print("Er is een fout opgetreden bij het ophalen van de wikitext.")