
import time
import logging
from sqlalchemy import create_engine
import slack

token1 = "xoxp-628857889554-634024900689-658515126419-bdad1fff4c384c3b7b9e4b7839fad7a1"
token2 = "xoxb-628857889554-671766097511-3oFink2LyCtAQ6mxEnU8tS4v"

client = slack.WebClient(token=token2)

pg = create_engine('postgres://postgres@postgresdb:5432')

while True:
    logging.critical("\n\nTop Scoring Sentiment:\n")
    q = pg.execute("SELECT text FROM tweets ORDER BY sentiment DESC LIMIT 1")
    msg = str(list(q))
    logging.critical(msg + "\n\n\n")
    client.chat_postMessage(channel='#zufällig', text=f"Here is another Tweet: {msg}")

    time.sleep(30)
