# Outline

## Limitation
Merriam Webster api has a limit of 1k calls per day and only allows one word per call

## Outline
1. Get list of all words from https://github.com/dwyl/english-words?tab=readme-ov-file
2. Get word frequency list from https://www.wordfrequency.info/samples.asp
3. Use frequency to determine order of api call of that word and store the info for that word

# Design

## Python ETL
1. Modify stack overflow script to pull words from api using total word list
2. Have word list have column of whether it is inserted or not
3. Create job to run at the end of each day to load the next 1k words from API, minus however many calls have already been made
  a. create counter for api calls
4. Handle (exclude?) variants

## Postgres
1. all_words table with all words and autoincrement primary key
2. "word" table for each word's info from api associated. Foriegn key to all_words primary key (this won't work for analyis. will need structs or other datatypes)
