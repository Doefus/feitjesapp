import locale
from datetime import datetime
from babel.dates import format_date
from openai import OpenAI
from telegrambericht import telegramMessage
from feitjesconstants import telegram_token, chat_GPT_key, telegram_chat_id
from feitjeswikipedia import get_wikipedia_page_wikitext

def feitjes_van_de_dag_van_chat_gpt(wikitext):
    # Huidige datum naar NL format
    huidige_datum = datetime.now()
    geformatteerde_datum = format_date(huidige_datum, format='d MMMM', locale='nl')
    # print(geformatteerde_datum)

    # Initiëer de client
    client = OpenAI(api_key=chat_GPT_key)
    vraag = "Onderstaande tekst komt van Wikipedia. Geef me de 5 noemenswaardige of opvallende historische/nationale vieringen, verjaardagen of andere belangrijke gebeurtenissen op basis van deze info:\n\n" + wikitext

    # Request Chat-GPT
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": vraag,
            }
        ],
        model="gpt-4o",
    )

    response_message = chat_completion.choices[0].message.content
    # print(response_message)

    # Zet de Nederlandse dag van de week
    locale.setlocale(locale.LC_TIME, 'nl_NL.UTF-8')
    dag_van_de_week = huidige_datum.strftime('%A')

    # Maak totaalbericht
    message_totaal = 'Het is vandaag ' + dag_van_de_week + ' ' + geformatteerde_datum + ' en daarover kunnen we het volgende melden:\n\n' + response_message

    # print(message_totaal)
    return message_totaal

wikitext = get_wikipedia_page_wikitext()

feitjes_van_de_dag = feitjes_van_de_dag_van_chat_gpt(wikitext)

telegramMessage(feitjes_van_de_dag, telegram_token, telegram_chat_id)