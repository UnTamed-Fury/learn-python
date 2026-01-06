# Idiomatic loops

## Looping in general

```python
data = ["John", "Doe", "was", "here"]
```

<font color='red'>Don't do it like this. While loops are actually really rarely needed.</font>

```python
idx = 0
while idx < len(data):
    print(data[idx])
    idx += 1
```

<font color='red'>Don't do like this either.</font>

```python
for idx in range(len(data)):
    print(data[idx])
```

### <font color='green'>Do it like this!</font>

```python
for item in data:
    print(item)
```

<font color='green'>If you need the index as well, you can use enumerate.</font>

```python
for idx, val in enumerate(data):
    print(f"{idx}: {val}")
```

## Looping over a range of numbers

<font color='red'>Don't do this.</font>

```python
i = 0
while i < 6:
    print(i)
    i += 1
```

<font color='red'>Don't do this either.</font>

```python
for val in [0, 1, 2, 3, 4, 5]:
    print(val)
```

### <font color='green'>Do it like this!</font>

```python
for val in range(6):
    print(val)
```

## Reversed looping

```python
data = ["first", "to", "last", "from"]
```

<font color='red'>This is no good.</font>

```python
i = len(data) - 1
while i >= 0:
    print(data[i])
    i -= 1
```

### <font color='green'>Do it like this!</font>

```python
for item in reversed(data):
    print(item)
```

## Looping over __n__ collections simultaneously

```python
collection1 = ["a", "b", "c"]
collection2 = (10, 20, 30, 40, 50)
collection3 = ["John", "Doe", True]
```

<font color='red'>Oh boy, not like this.</font>

```python
shortest = len(collection1)
if len(collection2) < shortest:
    shortest = len(collection2)
if len(collection3) < shortest:
    shortest = len(collection3)

i = 0
while i < shortest:
    print(collection1[i], collection2[i], collection3[i])
    i += 1
```

<font color='red'>This is getting better but there's even a better way!</font>

```python
shortest = min(len(collection1), len(collection2), len(collection3))
for i in range(shortest):
    print(collection1[i], collection2[i], collection3[i])
```

### <font color='green'>Do it like this!</font>

```python
for first, second, third in zip(collection1, collection2, collection3):
    print(first, second, third)
```

<font color='green'>You can also create a dict out of two collections!</font>

```python
my_dict = dict(zip(collection1, collection2))
print(my_dict)
```

## `for - else` - Checking for a match in a collection
Let's say we want to verify a certain condition is met by at least one element in a collection. Let's consider the following relatively naive example where we want to verify that at least one item is "python" (case insensitive) in `data`. If not, we'll raise a ValueError.

```python
data = [1, 2, 3, "This", "is", "just", "a", "random", "Python", "list"]
```

<font color='red'>Don't do it like this</font>

```python
found = False
for val in data:
    if str(val).lower() == "python":
        found = True
        break
if not found:
    raise ValueError("Nope, couldn't find.")
```

### <font color='green'>Do it like this!</font>

```python
for val in data:
    if str(val).lower() == "python":
        break
else:
    raise ValueError("Nope, couldn't find.")
```

