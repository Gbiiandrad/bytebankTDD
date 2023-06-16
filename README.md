# bytebankTDD

<a href="https://pypi.org/project/virtualenv/">
  <img src="https://img.shields.io/badge/pypi-20.23.0-blue" alt="latest release" /> <br>
</a>

### used API "virtualenv"
To import the package that can be used to work with regular expressions.

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

## Example:
```python
>>> import requests
>>> r = requests.get("https://api.github.com")
>>> print(r)
200
```

### 📖 Documentation: <br>
[virtualenv](https://virtualenv.pypa.io/en/latest/) <br>
[link 2](https://realpython.com/python-requests/)

### Access the requests repository [here](https://github.com/psf/requests)
