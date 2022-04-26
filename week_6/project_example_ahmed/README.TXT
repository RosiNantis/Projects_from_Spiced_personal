
Sample Docker data pipeline

- Reads tweets from Twitter (using part of the Tweego code).
- pushes raw tweets to MongoDB
- ETL process picks a random tweet and runs vader sentiment on it.
  Stores the tweet + sentiment in Postgres DB
- Sink process prints the highest scoring tweet (could be replaced by Slack bot)

Usage
-----

docker-compose build
docker-compose up

If you run it for the first time, the Postgres DB may lag behind, in which case half of the pipeline fails. Stop and Start everything again.
