# 1. Let's mock things!
Below you can see `get_wiki_article` function which is a very simple implementation for fetching an article from wikipedia. Your task is to mock it's implementation such that it's going to always return `'Python is cool!'`. However, note that you should be able to check which argument is given to `urlopen` when `get_wiki_article` is called.

**Note**: `get_content_of_url` uses [`urrlib`](https://docs.python.org/3/library/urllib.html#module-urllib), which is part of the Standard Library, for creating a HTTP request. Usually it's preferable to use [`requests`](http://docs.python-requests.org/en/master/) library (not part of the Standard Library) for such operations. Actually, `requests` uses `urllib` under the hood so it's good to know what's happening when you start using `requests` - or maybe you have already used it.

```python
from urllib.request import urlopen


def get_wiki_article(name):
    url = f"https://en.wikipedia.org/wiki/{name}"
    response = urlopen(url)
    content = str(response.read())
    return content
```

```python
# Your implementation here
```

Let's verify it works as expected.

```python
article = "Python_(programming_language)"
res = get_wiki_article(article)
assert "Guido van Rossum" not in res, "Guido is still there!"
assert res == "Python is cool!"
urlopen.assert_called_with(
    "https://en.wikipedia.org/wiki/Python_(programming_language)"
)

print("All good!")
```

# 2. The power of `collections` module

## 2.1 Creating a namedtuple
Create a namedtuple `Car` which has fields `price`, `mileage`, and `brand`. 

```python
# Your implemenation here
```

Let's test it.

```python
car1 = Car(25000, 2000, "BMW")
assert car1.price == 25000
assert car1.mileage == 2000
assert car1.brand == "BMW"
assert isinstance(car1, tuple)

# Note that indexing works also!
# This means that if you change a tuple into a namedtuple,
# the change will be backwards compatible.
assert car1[2] == "BMW"

print("All good!")
```

The power of namedtuples is their simplicity. If `Car` would have been implemented as a class, the implementation would have been notably longer. However, if you would need to be able to e.g. change the `mileage` or `price` during the lifetime of a `Car` instance, consider using `class` because `tuples` are immutable.

## 2.2 dict of dicts
Implement a `name_mapping` function which takes a collection of names as argument. 

#### The specification for `name_mapping`
* you can assume that all the elements in the names collection are strings
* if the provided names collection is empty, returns an empty dict
* returns a dictionary of dictionaries
    * outer dictionary should contain keys `vowel` and `consonant`
    * `vowel` and `consonant` keys should have dictionaries of names (keys) and their occurences (values) as values
    * names belong to either `vowel` or `consonant` based on their first letter
    * vowels are defined by the `VOWELS` constant
    * if there are only names starting with a vowel, `consonant` key should not be present in the return value (same applies vice versa)
* see the tests below for complete examples 

Tip: `defaultdict` and `Counter` may be helpful here :)

```python
VOWELS = ("a", "e", "i", "o", "u")
```

```python
def name_mapping(names):
    # Your implementation here
```

Let's verify that it works correctly!

```python
names = ("Alice", "John", "Lisa", "John", "Eric", "Waldo", "annie", "Alice", "John")
expected = {
    "consonant": {"John": 3, "Waldo": 1, "Lisa": 1},
    "vowel": {"Alice": 2, "annie": 1, "Eric": 1},
}
assert name_mapping(names) == expected
print("First ok!")

only_consonants = ("John", "Doe", "Doe")
expected2 = {"consonant": {"John": 1, "Doe": 2}}
assert name_mapping(only_consonants) == expected2
print("Second ok!")

assert name_mapping([]) == {}

print("All ok!")
```

