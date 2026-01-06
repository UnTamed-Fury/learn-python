# Idiomatic dictionaries

## `get` - default value of a non existing key while accessing
Especially handy if you're unsure about the presence of a key.

```python
my_dict = {"a": 1, "b": 2, "c": 3}
```

<font color='red'>Don't do it like this.</font>

```python
if "g" in my_dict:
    value = my_dict["g"]
else:
    value = "some default value"
print(value)
```

<font color='red'>Or like this.</font>

```python
try:
    value = my_dict["g"]
except KeyError:
    value = "some default value"
print(value)
```

### <font color='green'>Do it like this!</font>

```python
value = my_dict.get("g", "some default value")
print(value)
```

Note that if you don't provide the default value for `get`, the return value will be `None` if the key is not present in the dictionary

```python
value = my_dict.get("g")
print(value is None)
```

## `setdefault` - same as `get` but also sets the value if not present

<font color='red'>Don't do it like this.</font>

```python
my_dict = {"a": 1, "b": 2, "c": 3}

key = "g"
if key in my_dict:
    value = my_dict[key]
else:
    value = "some default value"
    my_dict[key] = value

print(value)
print(my_dict)
```

### <font color='green'>Let's do it like this!</font>

```python
my_dict = {"a": 1, "b": 2, "c": 3}

key = "g"
value = my_dict.setdefault(key, "some default value")

print(value)
print(my_dict)
```

## Comprehensions
Let's say we have a collection of numbers and we want to store those as a dictionary where the number is key and it's square is the value.

```python
numbers = (1, 5, 10)
```

<font color='red'>Don't do it like this.</font>

```python
squares = {}
for num in numbers:
    squares[num] = num**2
print(squares)
```

### <font color='green'>Do it like this!</font>

```python
squares = {num: num**2 for num in numbers}
print(squares)
```

### Another example

```python
keys = ("a", "b", "c")
values = [True, 100, "John Doe"]
```

<font color='red'>Don't do it like this.</font>

```python
my_dict = {}
for idx, key in enumerate(keys):
    my_dict[key] = values[idx]
print(my_dict)
```

### <font color='green'>Do it like this!</font>

```python
my_dict = {k: v for k, v in zip(keys, values)}
print(my_dict)

# Or even like this:
my_dict2 = dict(zip(keys, values))

assert my_dict2 == my_dict
```

## Looping

```python
my_dict = {"age": 83, "is gangster": True, "name": "John Doe"}
```

<font color='red'>Don't do it like this.</font>

```python
for key in my_dict:
    val = my_dict[key]
    print(f"key: {key:15s} value: {val}")
```

### <font color='green'>Do it like this!</font>

```python
for key, val in my_dict.items():
    print(f"key: {key:15s} value: {val}")
```

