# bytebankTDD

<a href="https://pypi.org/project/virtualenv/">
  <img src="https://img.shields.io/badge/virtualenv-20.23.0-blue" alt="latest release" />
</a>
<a href="https://pypi.org/project/pytest/#histor">
  <img src="https://img.shields.io/badge/pytest-7.3.2-blue" alt="latest release" /> <br>
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
To activate the environment, we'll run source 'venv/bin/activate. From now on, there will be a tag (venv) at the beginning of the line in the terminal, indicating that we are in this virtual environment.
venv\Scripts\Activate

### for Linux:
```python
>>> source venv/bin/activate
```

### For Windows: 
before using the command (venv \Scripts\Activate), you need to release the security system with the following commands:
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

### 📖 Documentation: <br>
[virtualenv](https://virtualenv.pypa.io/en/latest/) <br>
[pytest](https://docs.pytest.org/en/7.3.x/) <br>
