from telegram.ext import Updater

from bs4 import BeautifulSoup
import requests
import time

import cx_Oracle
####################################################
############################################



###################################################
###########################################################
# BELOW CODE IS TABLE CREATION CODE , TO BE EXECUTED JUST ONCE , THAT'S WHY COMMENTED
########
###
# conn = cx_Oracle.connect('hr/hr@localhost:1521/XEPDB1')

# print(conn.version)

# #create a cursor
# cur = conn.cursor().


# sql_create = """create table score_upk(score varchar2(20))  """


# cur.execute(sql_create)
# print('table created')


########################################################################################################################

#######################################################################################################################


import cx_Oracle

conn = cx_Oracle.connect('hr/hr@localhost:1521/XEPDB1')
# create connection
url = 'https://www.cricbuzz.com/live-cricket-scores/75560/ban-vs-pak-31st-match-icc-cricket-world-cup-2023'

while True:

    conn = cx_Oracle.connect('hr/hr@localhost:1521/XEPDB1')

    time.sleep(60)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    score_card = soup.find('div', class_='cb-col cb-col-67 cb-scrs-wrp').span.text

    cur = conn.cursor()

    sql_insert = """INSERT INTO score_upk VALUES (:1)"""
    data = [(score_card)]
    cur.execute(sql_insert, data)

    conn.commit()

    cur.close()
    conn.close()

    print("Current Score Is \n ", format(score_card))
    

## ## ## ## ## ## ## ## ##              BOT CODE                  ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
    import asyncio
    from telegram import Bot
    async def send_telegram_message():
        # Replace 'YOUR_BOT_TOKEN' with your bot's token
        bot = Bot(token='YOUR_BOT_TOKEN')

        # Replace 'CHAT_ID' with the chat ID where you want to send the message
        chat_id = 'CHAT_ID'

        # Replace 'YOUR_MESSAGE' with the message you want to send
        message = score_card

        await bot.send_message(chat_id=chat_id, text=message)


    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(send_telegram_message())




