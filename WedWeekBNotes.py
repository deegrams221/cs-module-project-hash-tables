# indexing

# given a list of records, be able to quickly report everyone in a particular category

records = [
    ("Corey", "iOS"),
    ("Tyler", "DS"),
    ("Anika", "DS"),
    ("Jenna", "web"),
    ("Leighton", "web"),
    ("Nico", "web"),
    ("Nico", "BIRTHDAY"),
    ("Carl", "web"),
    ("Michael", "iOS"),
]

# iOS_folks = []
# web_folks = []
# for record in records:
#     if record[1] == 'iOS':
#         iOS_folks.append(record[0])
#     elif record[1] == 'web':


# return [student for student in records if student[1] == "web"]


def build_index(records):
    index = {}


# {"web": ["Jenna", "Leighton"]}

# loop over our records
for record in records:
    name, track = record
    ## key is track
    # if key isn't in dictionary, add it
    if track not in index:
        index[track] = []

# index[track].append(name)

# value: list of names
# return index

index = build_index(records)

for track in index:
    print(track)

print(index["web"])
print(index["iOS"])


# How to handle updated records?
# Update index directly, as each record or batch of records
# Or loop over the records every once in awhile, and handle deduplication

# Project Euler
# Primes can't be divided by another number
# Primes are atoms of other numbers
# 21: 3 * 7
# 42: 2 * 3 * 7

# 113

# 10398471039847109384710983 * 1309871093871093874109384 --> 242458242420482704874298379487398274098524

# Why DJB2 5681 and 33?? No one really knows.


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# transposition


## We can use to transform data, like a substitution cipher

### Like a Caesar cypher!

## Make a table, mapping every letter to another letter
## given a string, build a new string by looking up each letter in our transposition table

import datetime
import hashlib
import random
import string
import urllib.request

encode_table = {}

for i in range(26):
    letter = string.ascii_uppercase[i]
    other_letter = string.ascii_uppercase[i - 13]

    encode_table[letter] = other_letter

def encode(s):
    s = s.upper()

    new_string = ""
    for letter in s:
        if letter.isspace():
            new_string += letter
        else:
            new_string += encode_table[letter]
    return new_string
print(encode("hello everyone"))


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# web_client_cache

# Build a "client" that will cache a URL

## First request: go out to the internet, get the web page
## Second request: return from cache

# How to implement using a hash table?
## What are our keys?   URL!
## What are our values?   web page data!


cache = {}
url = "https://www.google.com"

class CacheEntry:
    def __init__(self, data):
        self.data = data
        self.time_fetched = datetime.datetime.now().timestamp()

def fetch_web_page(url):
### given a url, check if it's in the cache
    stale_data = True
    if url in cache:
        time_now = datetime.datetime.now().timestamp()
        print("Getting from cache")
        cache_entry = cache[url]

        if time_now - cache_entry.time_fetched < 10:
            page = cache_entry.data
            stale_data = False

    elif stale_data:
        print("getting from the internetz")
### otherwise, send out a request to get the web page
        response = urllib.request.urlopen(url)
        data = response.read()
        response.close()

#### and put the result in our cache
        cache_entry = CacheEntry(data)
        cache[url] = cache_entry
        page = cache[url].data

    return page

page = fetch_web_page(url)
print(page)

also_page = fetch_web_page(url)

# One issue: memory usage, lots of URLs will fill memory up
## If the page isn't requested in awhile, delete
## LRU cache
## Use time to delete really old data

# What if the page changes?
## Store time, and if data is stale, re-fetch


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# birthday_paradox


def hash_function(random_key):
    return int(hashlib.sha256(f'{random_key}'.encode()).hexdigest(), 16)

def how_many_before_collision(number_of_buckets):
# make random keys
    tried = set()
    number_tries = 0

    while True:
    # hash them, and modulo them
        random_key = random.random()
        hashed_key = hash_function(random_key) % number_of_buckets

    # keep track of the hashed keys somehow
        if hashed_key not in tried:
            tried.add(hashed_key)
            number_tries += 1
    # stop when we get a collision
        else:
            break

    return number_tries

# test out increasing our array size
print(how_many_before_collision(4))
print(how_many_before_collision(8))
print(how_many_before_collision(16))
print(how_many_before_collision(256))
print(how_many_before_collision(1024))
print(how_many_before_collision(2084))
