<<<<<<< HEAD
# bytebankTDD

<a href="https://pypi.org/project/virtualenv/">
  <img src="https://img.shields.io/badge/virtualenv-v20.23.0-blue" alt="latest release" />
</a>
<a href="https://pypi.org/project/pytest/#histor">
  <img src="https://img.shields.io/badge/pytest-v7.3.2-blue" alt="latest release" />
</a>
<a href="https://pypi.org/project/pytest-cov/">
  <img src="https://img.shields.io/badge/pytestcov-v4.1.0-blue" alt="latest release" /> 
</a>

<br>
## used API "virtualenv"
To import the package that can be used to work with the virtual environment.

```sh
pip install virtualenv
```

## Terminal
To create a "virtual environment" for your project and generate the "venv" or "yourVenv" folder
```python
>>> virtualenv -p python3 Venv
reated virtual environment
```

## Activate the environment
To activate the environment, we'll run `source venv/bin/activate`. From now on, there will be a tag (venv) at the beginning of the line in the terminal, indicating that we are in this virtual environment.
`venv\Scripts\Activate`

### for MacOS or Linux:
```python
>>> source venv/bin/activate
```

### For Windows: 
before using the command `(venv\Scripts\Activate)`, you need to release the security system with the following commands:
```python
>>> Get-ExecutionPolicy 
Restricted
>>> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
>>>  venv\Scripts\Activate
```

## used framework "pytest"
To import the package that can be used to work with pytest. Pytest is a framework specialized in tests.
```sh
pip install pytest
```
### 
Running the `pip freeze` command in the terminal, we will receive a list of all packages installed in our virtual environment. It is a good practice to create a .txt file to gather the information of everything we are installing, to keep our project organized. The `pip freeze > requirements.txt` command is for generating this file.
```sh
pip freeze
```
```sh
pip freeze > requirements.txt
```

### Test
to test "pytest" use command in terminal
```sh
pytest -v
```

## used "pytest-cov"
help us verify test coverage! Pytest has an extension called pytest-cov.
```sh
pip install pytest-cov
```
### Test 
to test "pytest-cov" use command in terminal
```sh
pytest --cov
```
<br>
To find out which code snippets are missing from the tests, use the command below and the return will be a table, if you have cloned it in this project
```sh
pytest --cov=codigo project/tests/
```


### 📖 Documentation: <br>
[virtualenv](https://virtualenv.pypa.io/en/latest/) <br>
[pytest](https://docs.pytest.org/en/7.3.x/) <br>
[pytest-cov](https://pytest-cov.readthedocs.io/en/latest/readme.html#installation:~:text=software%3A%20MIT%20license-,Installation%C2%B6,-Install%20with%20pip) <br>
=======
# bytebankTDD

<a href="https://pypi.org/project/virtualenv/">
  <img src="https://img.shields.io/badge/virtualenv-v20.23.0-blue" alt="latest release" />
</a>
<a href="https://pypi.org/project/pytest/#histor">
  <img src="https://img.shields.io/badge/pytest-v7.3.2-blue" alt="latest release" /> <br>
</a>
<a href="https://pypi.org/project/pytest-cov/">
  <img src="https://img.shields.io/badge/pytest-cov-v4.1.0-blue" alt="latest release" /> <br>
</a>

## used API "virtualenv"
To import the package that can be used to work with the virtual environment.

```sh
pip install virtualenv
```

## Terminal
To create a "virtual environment" for your project and generate the "venv" or "yourVenv" folder
```python
>>> virtualenv -p python3 Venv
reated virtual environment
```

## Activate the environment
To activate the environment, we'll run `source venv/bin/activate`. From now on, there will be a tag (venv) at the beginning of the line in the terminal, indicating that we are in this virtual environment.
`venv\Scripts\Activate`

### for MacOS or Linux:
```python
>>> source venv/bin/activate
```

### For Windows: 
before using the command `(venv\Scripts\Activate)`, you need to release the security system with the following commands:
```python
>>> Get-ExecutionPolicy 
Restricted
>>> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
>>>  venv\Scripts\Activate
```

## used framework "pytest"
To import the package that can be used to work with pytest. Pytest is a framework specialized in tests.
```sh
pip install pytest
```
### 
Running the `pip freeze` command in the terminal, we will receive a list of all packages installed in our virtual environment. It is a good practice to create a .txt file to gather the information of everything we are installing, to keep our project organized. The `pip freeze > requirements.txt` command is for generating this file.
```sh
pip freeze
```
```sh
pip freeze > requirements.txt
```

### Test
to test "pytest" use command in terminal
```sh
pytest -v
```

## used "pytest-cov"
help us verify test coverage! Pytest has an extension called pytest-cov.
```sh
pip install pytest-cov
```
### Test 
to test "pytest-cov" use command in terminal
```sh
pytest --cov
```
<br>
To find out which code snippets are missing from the tests, use the command below and the return will be a table, if you have cloned it in this project

```sh
pytest --cov=codigo project/tests/
```


### 📖 Documentation: <br>
[virtualenv](https://virtualenv.pypa.io/en/latest/) <br>
[pytest](https://docs.pytest.org/en/7.3.x/) <br>
[pytestcov](https://pytest-cov.readthedocs.io/en/latest/readme.html#installation:~:text=software%3A%20MIT%20license-,Installation%C2%B6,-Install%20with%20pip) <br>
