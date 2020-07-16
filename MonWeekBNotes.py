# fibonacci

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# Recursive functions require:
# base case
# move toward the base case
# function has to call itself
import math


def slow_fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


cache = {}


def fibonacci(n):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return cache[n]

# Use a cache!
# Memoizing
# dynamic programming


print(fibonacci(8))
print(fibonacci(9))
print(fibonacci(15))
print(fibonacci(25))
print(fibonacci(45))
print(fibonacci(1000))
print(len(cache))

# clearly, this has linear time complexity


def tiny_recurse(n):
    if n <= 1:
        return n

    return n + tiny_recurse(n - 1)


# # # # # # # # # # # # # # # # # # # # #
# lookup_tables
lookup_table = {}


def inverse_root(n):
    return 1 / math.sqrt(n)


def populate_lookup_table():

    for i in range(1, 1000):
        lookup_table[i] = inverse_root(i)


populate_lookup_table()

print(lookup_table[25])
print(lookup_table[932])
# precomputing
# lazily computing


# # # # # # # # # # # # # # # # # # # # #
# sorting
# Is order in a hash table guaranteed?
my_list = []
my_list.append(3)
my_list.append(2)
my_list.append(1)

my_dict = {}

my_dict['key1'] = 1
my_dict['key2'] = 2
my_dict['key3'] = 3
my_dict['key4'] = 4

# {'key2', 'key4', 'key3': 3, 'key1'}

# Why not?
# Hash function scrambles keys to unpredictable indices


# goal: sort dictionary keys

d = {
    "foo": 1,
    "bar": 99,
    "qux": 42,
}

# Can't sort a dictionary, especially not hash tables in general
# But we could sort a list based on it!

for pair in d.items():
    print(pair)

dict_list = list(d.items())

dict_list.sort()

# or sorted(dict_list) - return a new list, not mutate the old list in place

# How could we sort reverse alphabetical? aka, descending
dict_list.sort(reverse=True)

# how to sort by value, not by key?
# (x, y) => x + 1
dict_list.sort(key=lambda pair: pair[1])

# sort descending by value, using Python's lambda functions
dict_list.sort(key=lambda pair: pair[1], reverse=True)


# # # # # # # # # # # # # # # # # # # # #
# letter_count
# write a function that takes a string
# and return each letter, along with how many times it occurs in the string
def letter_count(s):
    # create a dictionary
    counts = {}

    # iterate through the string
    for character in s:
        # ensure character is a letter
        if character.isalpha():
            # if the character is in the dictionary, increment its count
            if character in counts:
                counts[character] += 1

        # if not, add it, with value 1
            else:
                counts[character] = 1
    # return the dictionary
    return counts


# Stage 2:
# Print them all, but start with the key that occurs most often in our string
# Also: accept only letters, and ensure they are lowercased
def print_sorted_letter_count(s):

    letters = letter_count(s)

    letters_list = list(letters.items())

    letters_list.sort(key=lambda pair: pair[1], reverse=True)

    for pair in letters_list:
        print(f'Letter: {pair[0]}, count: {pair[1]}')


print_sorted_letter_count('Hello!')
print_sorted_letter_count('The quick brown fox jumps over the lazy dog')
