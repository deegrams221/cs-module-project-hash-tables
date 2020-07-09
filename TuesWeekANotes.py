my_arr = ["hello", "world", "how", "are", "you"]
# O(1) with an array?
# append, pop
# look up from index
my_arr[4]

# hashing or hash function: that will give us the index of the word we're looking for
## "you" --> 4

# to make a hash of something

# take a string
# give us a number
def my_hash(s):
    return len(s)

my_hash("you") # return 3

my_alphabet = {'a': 0, 'b': 1}
def my_hash(s):
    total = 0
    for char in s:
        total += my_alphabet[char]

    return total

# ASCII: assigns letters to numbers
## ord()

# UTF-8
# how to make the output more unique
## could use a random number? but make sure we get back same index every time?

def my_hash(s):
    s_utf8 = s.encode()

    total = 0
    for c in s_utf8:
        total += c

    return total

"Fourscore and seven years ago,/nour forefathers blah blah blah"

hello_idx = my_hash("hello") #532

my_arr = [None] * 500000

hello_idx = hello_idx % len(my_arr)

my_arr[hello_idx] = "hello"

world_idx = my_hash("world")

world_idx = world_idx % len(my_arr)

my_arr[world_idx] = "world value"
# hash table, dictionary, object, hash map: array paired up with a hash function (PHP??)

# insert into hash map
key = "key"
key_idx = my_hash(key) % len(my_arr)
my_arr[key_idx] = "value"
print(my_arr)

# access the value
key_idx = my_hash(key) % len(my_arr)
print(my_arr[key_idx])


## say you have a hash function, and you have an array, and key-value to put in the array:
# Steps to put
    # 1. hash the word, get some number back from your hash function
    # 2. modulo this num with array len to find the index
    # 3. use the index to insert the word
    # Time Complexity -> constant O(1) if you ignore the len of the string

# Steps to get
    # 1. hash the key/word, get some num back from hash function
    # 2. modulo this num with the array len to find the index
    # 3. look up value at that index, return it
    # Time Complexity -> constant O(1) if you ignore the len of the string

## Why use a hash table instead of an array?? -> dynamic programming, cashing for lookup, key-value pairs, search things, store things, database entry, input a value to get something back

# Hash function ideal speeds:
## in a hash table: fast! we want to look stuff up FAST
## to hash passwords and store hashes instead of plaintext passwords: relatively SLOW

# dictionary_of_passwords

# for potential_passwords in dictionary_of_passwords:
#     pssd = my_hash(potential_passwords)
# want it SLOW in this instance, so this is more secure
# “bcrypt is an adaptive function: over time, the iteration count can be increased to make it slower, so it remains resistant to brute-force search attacks even with increasing computation power.” - wikipedia

# What is the output of a hashing function called?
    # hash, or digest

# hashlib.sha256 -> will always give a different output
## good for making private predictions and be able to prove when the predictions were made

# a good hash function like SHA265 gives a totally unique output
# can use as id aka fingerprint of a document (document == big string)

# Can you reverse the output of a hash function? Can you go from 532 --> 'Hello'?
## --> A good hash function is non-reversible!

# Example:
# hashlib.sha256('hello'.encode()).hexdigest()
# --> '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
# https://emn178.github.io/online-tools/sha256.html

