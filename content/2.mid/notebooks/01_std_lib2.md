# Goodies of the [Python Standard Library](https://docs.python.org/3/library/#the-python-standard-library)

## [`json`](https://docs.python.org/3/library/json.html#module-json) for encoding and decoding JSON
Because the web is filled with JSON nowadays and the good days of xml are gone.

```python
data = {"b": True, "a": 1, "nested": {"foo": "bar"}, "c": None, "some_list": [1, 2, 3]}
```

### Encoding

```python
import json

json_data = json.dumps(data)
print(f"type: {type(json_data)} data: {json_data}")
```

### Decoding

```python
decoded = json.loads(json_data)
print(f"type: {type(decoded)} data: {decoded}")
```

## [`unittest.mock`](https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock)
Although `pytest` is the preferred testing framework, `unittest.mock` module offers some goodies that are helpful also in pytest test cases. Mocking and patching are generally useful for "faking" some parts of the logic/state of the software under test. Common use cases are, for example, patching parts of code that interact with 3rd parties (e.g. some web services).

### [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock)

In general, [Mocks](https://en.wikipedia.org/wiki/Mock_object) are simulated objects that replace the functionality/state of a real world object in a controlled way. Thus, they are especially useful in tests for mimicing some behavior of a specific part of the implementation under test.

There is also a [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock) class in the Python Standard Library but you usually want to use [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock) which is a subclass of `Mock`. `MagicMock` provides default implementation for the most of the magic methods (e.g. `__setitem__()` and `__getitem__()`)

A potential use case could be something like this:

```python
import random


class Client:
    def __init__(self, url, username, password):
        self.url = url
        self.creds = (username, password)

    def fetch_some_data(self):
        print(
            "Here we could for example fetch data from 3rd party API and return the data."
        )
        print("Now we will just return some random number between 1-100.")
        return random.randint(1, 100)


class MyApplication:
    def __init__(self):
        self.client = Client(
            url="https://somewhere/api", username="John Doe", password="secret123?"
        )

    def do_something_fancy(self):
        data = self.client.fetch_some_data()
        return data ** (1 / 2)  # let's return a square root just for example


####################
# In the test module:

from unittest.mock import MagicMock

# Inside a test case:
app = MyApplication()
app.client = MagicMock()  # Mock the client
app.client.fetch_some_data.return_value = 4  # Set controlled behaviour
result = app.do_something_fancy()
assert result == 2
print("All good, woop woop!")
```

### [`patch`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch)
The use cases of [`patch`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch) are pretty similar to `MacigMock`. The biggest difference is that `patch` is used as a context manager or a decorator. Object to be patched is given as an argument for `patch`. In addition, you can provide additional object as a second argument (`new`) which will replace the original one. In case the `new` is omitted, `MagicMock` will be used by default.

Let's see how the example above would look like with `patch`.

```python
# In the test module:

from unittest.mock import patch

# Inside a test case:
app = MyApplication()
with patch("__main__.app.client") as patched_client:  # Patch the client
    patched_client.fetch_some_data.return_value = 4  # Set controlled behaviour
    result = app.do_something_fancy()
    assert result == 2
    print("All good, woop woop!")
```

The same but with a function decorator instead of a context manager. Note that here we are patching the whole `Client` class, not just the `client` instance variable of `app`.

```python
from unittest.mock import patch


@patch("__main__.Client")  # Patch the Client
def test_do_something_fancy(client_cls):
    client_cls().fetch_some_data.return_value = 4  # Set controlled behaviour
    app = MyApplication()
    result = app.do_something_fancy()
    assert result == 2
    print("All good, woop woop!")


test_do_something_fancy()  # This is just for the sake of example
```

## [`collections`](https://docs.python.org/3/library/collections.html#module-collections)

### [`namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple)
A great helper for creating more readable and self documenting code.

`namedtuple` is a function that returns a tuple whose fields have names and also the tuple itself has a name (just like classes and their instance variables). Potential use cases include storing data which should be immutable. If you can use Python 3.7 or newer, you may want to take a look at [`dataclasses`](https://docs.python.org/3/library/dataclasses.html#module-dataclasses) as well. 

```python
from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "is_gangster"])

# instance creation is similar to classes
john = Person("John Doe", 83, True)
lisa = Person("Lis Doe", age=77, is_gangster=False)

print(john, lisa)
print(f"Is John a gangster: {john.is_gangster}")

# tuples are immutable, thus you can't do this
# john.is_gangster = False
```

### [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter)
For counting the occurences of elements in a collection.

```python
from collections import Counter

data = [1, 2, 3, 1, 2, 4, 5, 6, 2]

counter = Counter(data)
print(f"type: {type(counter)}, counter: {counter}")

print(f"count of twos: {counter[2]}")
print(f"count of tens: {counter[10]}")  # zero for non existing

print(f"counter is a dict: {isinstance(counter, dict)}")
```

### [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict)
For cleaner code for populating dictionaries.

Let's first see how you could use a normal `dict`.

```python
data = (1, 2, 3, 4, 3, 2, 5, 6, 7)

my_dict = {}
for val in data:
    if val % 2:
        if not "odd" in my_dict:
            my_dict["odd"] = []
        my_dict["odd"].append(val)
    else:
        if not "even" in my_dict:
            my_dict["even"] = []
        my_dict["even"].append(val)

print(my_dict)
```

With `defaultdict`:

```python
from collections import defaultdict

my_dict = defaultdict(list)
for val in data:
    if val % 2:
        my_dict["odd"].append(val)
    else:
        my_dict["even"].append(val)
print(my_dict)
```

In the above example, `defaultdict` makes sure that a fresh `list` is automatically initialized as a value when a new key is added.

Here's another example with `int` as a default.

```python
my_dict = defaultdict(int)
for val in data:
    if val % 2:
        my_dict["odd_count"] += 1
    else:
        my_dict["even_count"] += 1
print(my_dict)
```

