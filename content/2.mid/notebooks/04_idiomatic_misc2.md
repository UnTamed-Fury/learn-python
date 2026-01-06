# Idiomatic Python - miscellaneous part 2

## String concatenation

```python
names = ("John", "Lisa", "Terminator", "Python")
```

<font color='red'>Don't do this.</font>

```python
semicolon_separated = names[0]
for name in names[1:]:
    semicolon_separated += ";" + name
print(semicolon_separated)
```

### <font color='green'>Use `join` instead!</font>

```python
semicolon_separated = ";".join(names)
print(semicolon_separated)
```

## `or` in assignments
The return value of `a or b`:
* `a` if `a` is truthy
* `b` otherwise

You can take advantage of this e.g. while writing variable assignments.

```python
a = 0
b = None
c = "John Doe"
```

<font color='red'>Instead of doing something like this:</font>

```python
my_variable = "default value"
if a:
    my_variable = a
elif b:
    my_variable = b
elif c:
    my_variable = c
print(my_variable)
```

### <font color='green'>Prefer doing this:</font>

```python
my_variable = a or b or c or "default value"
print(my_variable)
```

## `try` - `except` - `else`

<font color='red'>Don't use the following technique for checking if there was exceptions during execution of some block of code.</font>

```python
exception_occured = False
try:
    # here would be the logic of your master piece

    bad_calculation = 1 / 0

except ValueError as e:
    print(f"Oh boi, some value error: {e}")
    exception_occured = True
except Exception as e:
    print(f"Oh boi, something bad happened: {e}")
    exception_occured = True

if not exception_occured:
    print("All went well!")
```

### <font color='green'>Use this instead!</font>

```python
try:
    # here would be the logic of your master piece

    bad_calculation = 1 / 0

except ValueError as e:
    print(f"Oh boi, some keyerror: {e}")
except Exception as e:
    print(f"Oh boi, something bad happened: {e}")
else:
    print("All went well!")
```

## `try` - `finally`
For scenarios where you want to do something always, even when there are exceptions.

<font color='red'>Don't do it like this</font>

```python
def magical_calculation():
    try:
        # here would be the logic of your master piece
        result = 1 / 0
    except ZeroDivisionError:
        print("This could be something important that should be done every time")
        return 0
    except Exception:
        print("This could be something important that should be done every time")
        return None

    print("This could be something important that should be done every time")
    return result


print(f"return value: {magical_calculation()}")
```

### <font color='green'>This is better fit for the purpose!</font>

```python
def magical_calculation():
    try:
        # here would be the logic of your master piece
        result = 1 / 0
    except ZeroDivisionError:
        return 0
    except Exception:
        return None
    finally:
        print("This could be something important that should be done every time")
    return result


print(f"return value: {magical_calculation()}")
```

**Note**: You can also have `try`-`except`-`else`-`finally` structure. In cases where exception is not raised inside `try`, `else` will be executed before `finally`. If there is an expection, `else` block is not executed.

## Use context managers when possible
One use case example is file I/O.

<font color='red'>Don't play with files like this.</font>

```python
try:
    some_file = open("tmp.txt", "w")
    print(f"the file is now open: {not some_file.closed}")

    # here would be some logic

finally:
    some_file.close()
    print(f"now it's closed: {some_file.closed}")
```

### <font color='green'>Use context manager instead!</font>

```python
with open("tmp.txt", "w") as some_file:
    print(f"the file is now open: {not some_file.closed}")

    # here would be some logic

print(f"now it's closed: {some_file.closed}")
```

### <font color='green'>It's also easy to implement one yourself.</font>

```python
from contextlib import contextmanager


@contextmanager
def my_context():
    print("Entering to my context")
    yield
    print("Exiting my context")


def do_stuff():
    with my_context():
        print("Doing stuff")

    print("Doing some stuff outside my context")


do_stuff()
```

## `min()` & `max()`

```python
secret_data = (1, 2, 5, 99, 8, -9)
```

<font color='red'>No need to bake it yourself.</font>

```python
max_value = 0
for val in secret_data:
    if val > max_value:
        max_value = val
print(max_value)
```

### <font color='green'>Use builtin functionality instead!</font>

```python
max_value = max(secret_data)
print(max_value)
```

## `contextlib.suppress` - ignoring exceptions 

<font color='red'>If there's a potential exception that is ok, don't handle it like this.</font>

```python
value = 0
try:
    value = 1 / 0  # just for demonstrating purposes
except ZeroDivisionError:
    pass

print(value)
```

### <font color='green'>Do it like this instead!</font>

```python
from contextlib import suppress

value = 0
with suppress(ZeroDivisionError):
    value = 1 / 0  # just for demonstrating purposes

print(value)
```

## Properties instead of getter/setter methods

<font color='red'>Instead of doing something like this.</font>

```python
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def set_full_name(self, full_name):
        parts = full_name.split()
        if len(parts) != 2:
            raise ValueError("Sorry, too difficult name")

        self.first_name, self.last_name = parts


p = Person("John", "Doe")
print(p.get_full_name())
p.set_full_name("Lisa Doe")
print(p.get_full_name())
```

### <font color='green'>Prefer properties!</font>

```python
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, name):
        parts = name.split()
        if len(parts) != 2:
            raise ValueError("Sorry, too difficult name")

        self.first_name, self.last_name = parts


p = Person("John", "Doe")
print(p.full_name)
p.full_name = "Lisa Doe"
print(p.full_name)
```

