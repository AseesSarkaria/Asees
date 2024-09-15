# Outline

# The Inspiration: 
https://www.reddit.com/r/SQL/comments/g4ct1l/comment/fnx11mc/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

## Other Inspirations
1. https://github.com/jcoffland/wotd-game
2. https://github.com/ibrosen/MerriamWebsterScraper
3. https://youtu.be/PUkgK7TI0x0?si=7mcwRfeXFqyKO5LA
4. https://youtu.be/Acojo0G9kD0?si=jsZqpqx9iBwg0gf5
5. https://youtu.be/PUkgK7TI0x0?si=7mcwRfeXFqyKO5LA

## Limitation
Merriam Webster api has a limit of 1k calls per day and only allows one word per call: https://www.dictionaryapi.com/products/json

## Set Up
1. Get list of all words from https://github.com/dwyl/english-words?tab=readme-ov-file
2. Get word frequencies:
   a. https://github.com/first20hours/google-10000-english/blob/master/README.md
   b. https://www.vocabulary.com/lists/52473
   c. https://www.wordfrequency.info/samples.asp
4. Use frequency to determine order of api call of that word and store the info for that word

# DevOps
1. remote connections to database: https://blog.devart.com/configure-postgresql-to-allow-remote-connection.html

# Design

## Python ELT
1. Pull words from api using word_list into all_words
2. Add column to all_words of whether its data has been loaded into database or not (boolean)
3. Create job to run at the end of each day to load the next 1k words from API, minus however many calls have already been made
   a. Create a counter for api calls
   b. Airflow is probably overkill. Might be simpler to use windows task scheduler. BUT - Resume Driven Development XD
      1. https://stackoverflow.com/questions/50671270/how-to-use-airflow-for-orchestrating-simple-pandas-etl-python-scripts
4. Handle (exclude?) variants (varitons of words, e.g. alt spellings, different parts of speech)

## Postgres
1. Transactions to ensure integrity of loaded data and creation of master table
2. Create master table. Source of truth data. 
3. Use master to create downstream tables for different types of analytic queries

Relevant functions and notes: 
1. string_to_array(some_string, NULL) will expand the letters ARRAY column
2. Indexes on ARRARY columns in postgres: https://stackoverflow.com/questions/4058731/can-postgresql-index-array-columns
3. Analytics engine for postgres: https://github.com/paradedb/pg_analytics


# Analytics

## Ideas
1. Queries for all of these special types of words: https://theweek.com/articles/464433/palindromes-anagrams-9-other-names-alphabetical-antics
   a. Isogram - A word in which no letter of the alphabet occurs more than once
   b. Pangram - A phrase or sentence containing all 26 letters of the alphabet
   c. Palindrome - A word, sentence, or longer written work that reads the same backwards
   d. Semordnilap - A word or name that spells a different word backwards (notice what semordnilap spells backwards)
   e. Kangaroo word- This refers to a word carrying another word within it (without transposing any letters)
   f. Anagram - A word or phrase formed by rearranging the letters of another word or phrase
   g. Aptagram - A word that has a meaning that is relevant to the original word that was anagrammed
   h. Antigram - The opposite of an aptigram, these words or phrases form antonyms when rearranged
   i. Homonym: words with same sounds and same spellings but with different meanings
   j. Homograph: words with same spellings but with different meanings
   k. Homophone: words with same sounds but with different meanings
   l. Rhyme: a repetition of identical or similar sounds in two or more different words
   m. Alliteration: matching consonants sounds at the beginning of words
   n. Assonance: matching vowel sounds
   o. Consonance: matching consonant sounds
   p. Blanagram: rearranging the letters of a word or phrase and substituting one single letter to produce a new word or phrase
   q. Letter bank: using the letters from a certain word or phrase as many times as wanted to produce a new word or phrase
2. Word games, e.g. Scrabble, game pigeon word games, etc
   a. https://www.freescrabbledictionary.com/english-word-list/
   b. make it online too
3. OCR type stuff
4. If you type a wrong word, the api will return closely matching words. add functionality to handle this
   a. Could handle this through some ML model
