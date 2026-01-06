# Efficient use of `pytest` fixtures

Required boilerplate for using `pytest` inside notebooks.

```python
# Let's make sure pytest and ipytest packages are installed
# ipytest is required for running pytest inside Jupyter notebooks
import sys

!{sys.executable} -m pip install pytest
!{sys.executable} -m pip install ipytest

# These are needed for running pytest inside Jupyter notebooks
import ipytest

ipytest.autoconfig()

import pytest
```

## Parametrizing fixtures
Similarly as you can parametrize test functions with `pytest.mark.parametrize`, you can parametrize fixtures:

```python
PATHS = ["/foo/bar.txt", "/bar/baz.txt"]


@pytest.fixture(params=PATHS)
def executable(request):
    return request.param
```

```python
%%ipytest -s

def test_something_with_executable(executable):
    print(executable)
```

## [`pytest.mark.usefixtures`](https://docs.pytest.org/en/latest/fixture.html#usefixtures)
[`pytest.mark.usefixtures`](https://docs.pytest.org/en/latest/fixture.html#usefixtures) is useful especially when you want to use some fixture in a set of tests but you don't need the return value of the fixture.

```python
%%ipytest -s


@pytest.fixture
def my_fixture():
    print("\nmy_fixture is used")
  

@pytest.fixture
def other_fixture():
    return "FOO"


@pytest.mark.usefixtures('my_fixture')
class TestMyStuff:
    def test_somestuff(self):
        pass
    
    def test_some_other_stuff(self, other_fixture):
        print(f'here we use also other_fixture which returns: {other_fixture}')
```

## `pytest` [built-in fixtures](https://docs.pytest.org/en/latest/builtin.html#pytest-api-and-builtin-fixtures)
Here are a couple of examples of the useful built-in fixtures, you can view all available fixtures by running `pytest --fixtures`.

### [`monkeypatch`](https://docs.pytest.org/en/latest/reference.html#_pytest.monkeypatch.MonkeyPatch)
Built-in [`monkeypatch`](https://docs.pytest.org/en/latest/reference.html#_pytest.monkeypatch.MonkeyPatch) fixture lets you e.g. set environment variables and set/delete attributes of objects. The use cases are similar as with patching/mocking with `unittest.mock.patch`/`unittest.mock.MagicMock` which are part of the Python Standard Library.

**Monkeypatching environment variables:**

```python
import os


def get_env_var_or_none(var_name):
    return os.environ.get(var_name, None)
```

```python
%%ipytest -s

def test_get_env_var_or_none_with_valid_env_var(monkeypatch):
    monkeypatch.setenv('MY_ENV_VAR', 'secret')
    res = get_env_var_or_none('MY_ENV_VAR')
    assert res == 'secret'
    
def test_get_env_var_or_none_with_missing_env_var():
    res = get_env_var_or_none('NOT_EXISTING')
    assert res is None
```

**Monkeypatching attributes:**

```python
class SomeClass:
    some_value = "some value"

    @staticmethod
    def tell_the_truth():
        print("This is the original truth")
```

```python
def fake_truth():
    print("This is modified truth")


@pytest.fixture
def fake_some_class(monkeypatch):
    monkeypatch.setattr("__main__.SomeClass.some_value", "fake value")
    monkeypatch.setattr("__main__.SomeClass.tell_the_truth", fake_truth)
```

```python
%%ipytest -s

def test_some_class(fake_some_class):
    print(SomeClass.some_value)
    SomeClass.tell_the_truth()
```

### [`tmpdir`](https://docs.pytest.org/en/latest/tmpdir.html#the-tmpdir-fixture)
[`tmpdir`](https://docs.pytest.org/en/latest/tmpdir.html#the-tmpdir-fixture) fixture provides functionality for creating temporary files and directories.

```python
def word_count_of_txt_file(file_path):
    with open(file_path) as f:
        content = f.read()
        return len(content.split())
```

```python
%%ipytest -s

def test_word_count(tmpdir):
    test_file = tmpdir.join('test.txt')
    test_file.write('This is example content of seven words')
    res = word_count_of_txt_file(str(test_file)) # str returns the path
    assert res == 7
```

## Fixture scope

```python
@pytest.fixture(scope="function")
def func_fixture():
    print("\nfunc")


@pytest.fixture(scope="module")
def module_fixture():
    print("\nmodule")


@pytest.fixture(scope="session")
def session_fixture():
    print("\nsession")
```

```python
%%ipytest -s

def test_something(func_fixture, module_fixture, session_fixture):
    pass

def test_something_else(func_fixture, module_fixture, session_fixture):
    pass
```

## Setup-teardown behaviour

```python
@pytest.fixture
def some_fixture():
    print("some_fixture is run now")
    yield "some magical value"
    print("\nthis will be run after test execution, you can do e.g. some clean up here")
```

```python
%%ipytest -s

def test_something(some_fixture):
    print('running test_something')
    assert some_fixture == 'some magical value'
    print('test ends here')
```

## Using fixtures automatically

```python
@pytest.fixture(autouse=True)
def my_fixture():
    print("\nusing my_fixture")
```

```python
%%ipytest -s

def test_1():
    pass
    
def test_2():
    pass
```

