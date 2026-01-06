# Best practices in development

## One virtual environment per project
<img style="float: left;" src="../img/virtualenvs.jpg">


### Why
* Isolation
* Different projects have different dependency versions
* You don't want to mess up the system Python

### Tooling
`poetry` is currently the recommended tool for dependency management but ["consider other tools such as pip when poetry does not meet your use case"](https://packaging.python.org/guides/tool-recommendations/#application-dependency-management). If `poetry` doesn't fit your use case, I recommend using `virtualenvwrapper` for managing virtual environments and `pip` for package management. On the other hand, if you're working on only a couple of projects, built-in [`venv`](https://docs.python.org/3/library/venv.html) will do just fine.
#### [`poetry`](https://python-poetry.org/docs/)
* Basically combines `pip`, `virtualenv`, and packaging facilities under single CLI
* [pyproject.toml](https://python-poetry.org/docs/pyproject/) which replaces the need for requirements.txt and requirements-dev.txt 
* poetry.lock which pins dependencies, this means deterministic builds

#### [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/)
* If you are using Windows command prompt: [`virtualenvwrapper-win`](https://pypi.org/project/virtualenvwrapper-win/)
* Like the name suggests, a wrapper around [`virtualenv`](https://pypi.org/project/virtualenv/)
* Eases the workflow for creating, deleting, and (de)activating your virtual environments

#### [`pyenv`](https://github.com/pyenv/pyenv)
* Easily change global / per project Python version 
* Also a tool for installing different Python versions (also different runtimes available, e.g. [PyPy](https://pypy.org/))
* Useful if you'll need to work with different Python versions

## Test your code
<img style="float: left;" src="../img/testing.png">

### Why
* No surprises (especially in production)
* Make sure that everything works as expected
* Make sure that old stuff works as expected after introducing new features (regression)
* Tests give you confidence while refactoring
* Good tests demonstrate the use cases of application, i.e. they also document the implementation  
* ...

### Tooling
#### [`pytest`](https://docs.pytest.org/en/latest/)
There's [`unittest`](https://docs.python.org/3/library/unittest.html) module in Python Standard Library but the go-to test runner nowadays is definitely `pytest`.

Some reasons to use `pytest`:
* [`fixtures`](https://docs.pytest.org/en/latest/fixture.html#fixture) for writing reusable testing code
* [`markers`](https://docs.pytest.org/en/latest/example/markers.html) for splitting tests to different groups (e.g. smoke, run only on CI machine, etc) or skipping tests in certain conditions
* [Automatic test discovery](https://docs.pytest.org/en/latest/goodpractices.html#test-discovery)
* [Configurability](https://docs.pytest.org/en/latest/customize.html)
* Active development of plugins, to mention a few:
    * [`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/) for coverage reporting
    * [`pytest-xdist`](https://github.com/pytest-dev/pytest-xdist) for speeding up test suit run time with parallelization
    * see [complete list](https://github.com/pytest-dev) of plugins maintained by `pytest`
* Ease of [writing own plugins](https://docs.pytest.org/en/latest/writing_plugins.html)

#### [`tox`](https://tox.readthedocs.io/en/latest/)
`tox` makes it simple to test your code against different Python interpreter/runtime and dependency versions. This is important when you're writing software which should support different Python versions, which is usually the case with library-like packages. On the other hand, if you're developing, say, a web application which will be deployed to a known target platform, testing against multiple different versions is usually not necessary. However, `tox` makes it also possible to configure, for example, linting as part of `tox` run. Thus, `tox` may simplify the development workflow significantly by wrapping multiple different operations under a single command.

## Write high quality code
<img style="float: left;" src="../img/high_quality_code.png">

### Why
* Easy to read
* Better maintainability
* Better quality == less bugs

```python
import this
```

### Tooling - code formatters
[PEP8](https://www.python.org/dev/peps/pep-0008/?) (see also ["for humans version"](https://pep8.org/)) describes the style guidelines for Python code, you should follow them. Luckily, there are awesome tools that handle this for you while you focus on writing code, not formatting it.

#### [`black`](https://black.readthedocs.io/en/stable/)
* This is the go-to formatter of the Python community

### Tooling - linters
Automatic code formatting is great but in addition to that, you should use static analyzer (linter) to detect potential pitfalls in your code.

#### [`ruff`](https://beta.ruff.rs/docs/)
* Most comprehensive linter. As a bonus, it's extremely fast.

### Tooling - pre-commit
#### [`pre-commit`](https://pre-commit.com/)
Ideally, all project contributors should follow the best practices of the project, let it be e.g. respecting PEP8 or making sure there's no linting errors or security vulnerabilities in their change sets. However, as code formatters and linters are (mainly) local tools, this can not be guaranteed. `pre-commit` let's you configure (.pre-commit-config.yaml file) a set of hooks that will be run as pre actions to a commit/push. After a developer has called once `pre-commit install`, these hooks will be then automatically ran prior each commit/push.
* Run formatting before commit
* Fail the commit in case linting errors
* Even exercise the test suite before the code ends up to remote (might be time consuming in most scenarios though)
* Easy to configure [your own hooks](https://pre-commit.com/#new-hooks) 
* And use the [existing ones](https://github.com/pre-commit/pre-commit-hooks)
* There's also [pre-push option](https://pre-commit.com/#pre-commit-during-push)
* Written in Python but supports also other languages, such as Ruby, Go, and Rust
* Less failed CI builds!

## Structure your code and projects
<img style="float: left;" src="../img/bad_code.jpg">

### Why
* Package and module structure gives an overview about the project
* Modular design == better reusability

### How
Some general guidelines:
* Don't put too much stuff into one module
* Split project into packages
* Be consistent with your naming conventions

A few words about structuring your projects. If you're developing, say, a relative big business application, it makes sense to separate some of the non-core business logic packages into a separate project and publish that as separate package. This way the "main" repository doesn't get bloated and it's more approachable for newcomers. Additionally, there's a change that you (or someone else) can easily reuse this "separated" package in the future, which is often the case e.g. for different kinds of utility functionalities. 

Let's take a practical example. If your team has two different applications which interact with the same third party, it's beneficial to implement a separate client library for communication with it. This way a change is needed only in one place (in the client library) if the third party decides to make a backwards incompatible change in their API. 

### Tooling
#### [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/)
<img style="float: left;" src="../img/cookiecutter.jpg">

Cookiecutter is a tool which let's you create projects from predefined templates. 

* Rapid set-up of new projects, no need to copy paste from existing ones
* Consistent development practices across all projects (project structure as well as e.g. `pre-commit`, `tox`, and CI configuration)
* You can create one yourself or use some of the [existing ones](https://cookiecutter.readthedocs.io/en/latest/readme.html#python)
* Written in Python but is applicable for non-Python projects as well, even non-programming related directory and file structures

## Use continuous integration and deployment
<img style="float: left;" src="../img/ci.jpg">

CI & CD belong to the best practices of software development without controversy, no matter what is the technology stack used for development. From Python point of view, CI is the place where we want to make sure that the other best practices described above are followed. For example, in bigger projects, it may not be even practical/possible to run the full test suite on developer's machine.

### Why
* Make sure the tests pass
* CI is the place where it's possible to run also some time consuming tests which the impatient developers prefer to skip on their local machines
* Make sure there's no linting errors
* Ideally, the place to test against all target versions and platforms
* Overall, CI is the last resort for automatically ensuring the quality 
* Manual deployments are time consuming and error-prone, CD is automated and deterministic
* You want to automate as much as possible, human time is expensive
* Minimize the time required for code reviews - what could be detected with automatic tools, should be detected by using those tools. Human time is expensive. 

### Tooling
Tooling depends on which git repository manager option you've chosen and what kind of requirements you have. For example:
* [GitHub Actions](https://github.com/features/actions)
* If you're using Gitlab, it also has [integrated CI/CD](https://about.gitlab.com/features/gitlab-ci-cd/)
* Same for [BitBucket](https://www.atlassian.com/continuous-delivery/continuous-integration-tutorial)


## Utilize the capabitilies of your editor

### Why
* Efficient and fluent development
* There's plenty of tools to make your daily programming easier, why would you not use them

### Tooling
As there's a number of different editors and IDEs available, not to mention that everyone has their own preferences, I'll just focus on highlighting some of the features of my favorite IDE, PyCharm, which I highly recommend for Python development.

#### [PyCharm](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)
* Good integration with `pytest`, e.g. run single tests / test classes / test modules
* Git integration (in case you don't like command line)
* Easy to configure to use automatic formatting, e.g [`black`](https://github.com/ambv/black#pycharm)
* Intuitive searching capabilities
* Refactoring features
* Debugger
* Jupyter Notebook integration
* Free community edition already contains all you need

## Use existing solutions
<img style="float: left;" src="../img/reinvent.jpg">

### Why
* Python Standard Library is extensive - and stable!
* There are over 150k packages in [PyPI](https://pypi.org/)
* Someone has most likely solved the problem you're trying to solve
* Spend 5 minutes doing a google research before starting to solve a new problem, e.g. [stackoverflow](https://stackoverflow.com/) is a magical place.

## Learn how to debug efficiently
<img style="float: left;" src="../img/debugging.jpg">

### Why
* You won't write completely stable code anyway - impossible looking conditions will occur. 
* When something is not working as expected, there are plenty of tools out there to help you figure out what's going on. 

### Tooling - debuggers
#### [`pdb`](https://docs.python.org/3/library/pdb.html)
* Part of the Standard Library
* Sufficient for most use cases

#### [`ipdb`](https://pypi.org/project/ipdb/)
* Feature rich `pdb` with similar API

#### [`pdb++`](https://pypi.org/project/pdbpp/)
* Drop-in replacement for `pdb` with additional features

### Tooling - profilers

#### [`memray`](https://bloomberg.github.io/memray/)
* Probably the only memory profiler you'll ever need

#### [`py-spy`](https://github.com/benfred/py-spy)
* Profile running Python program without the need for modifying the source code or restarting the target process
* Potential tool for identifying problems of e.g. a web application in production 

### Tooling - runtime error tracking
These are especially useful with web applications as you'll get reports - and notifications - of runtime exceptions with full tracebacks and variable values. This information is often enough for identifying the root cause of the problem, which is a huge benefit considering the time required for implementing and deploying the fix.

#### [Sentry](https://docs.sentry.io/?platform=python)
* Complete stack traces with relevant variable (`locals()`) values
* Browser and OS information of the client
* Support for other languages as well

### Tooling - misc

#### Use logging instead of prints
<img style="float: left;" src="../img/prints.jpg">

* [`logging`](https://docs.python.org/3/library/logging.html) is part of the Standard Library
* With logging you can redirect the output to a file
* Logs are usually the first place to look at after an end user reports an issue
* You can specify the runtime level - no need to remove the debug prints

### General guidelines
* If you're building applications, use the latest Python.
* If you're building libraries, make sure they support also older Python versions. 
* Develop in branches. Even if you're the only person in the project, branching makes it possible to easily switch between different features / bug fixes.
* If you're not developing alone, practice code reviews. It's one of the best ways to learn for both parties.
* Document your master pieces

