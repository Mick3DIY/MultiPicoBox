# MultiPicoBoxV2 Python unit tests documentation (Linux)

1. Create the virtual environnement, only one time in 'tests' folder

```shell
python3 -m venv .venv
```

_The second parameter '.venv' is the default folder name for the virtual environnement_

2. Activate the virtual environnement

```shell
source .venv/bin/activate
```

3. Install project dependencies

```shell
pip install --requirement requirements.txt
```

4. Run the project test with some details

```shell
pytest -rpP
```

  4.1 Run the tests covering with line numbers (optional)
    
  ```shell
  pytest --cov --cov-report=term-missing
  ```

5. Deactivate the virtual environnement

```shell
deactivate
```

6. Delete the virtual environnement from 'tests' folder

```shell
rm -rf .venv
```

## Documentation :

Python : https://www.python.org/doc/

Pip via the Python Package Index (PyPI) : https://pypi.org

Pytest : https://docs.pytest.org/en/stable/

## Python pip useful commands

```shell
# Install the latest version of a package
pip install <package>

# Install all dependencies listed in this project file
pip install --requirement requirements.txt

# Upgrade a specific package
pip install --upgrade <package>

# Remove a specific package
pip uninstall <package>

# Display all installed packages and their versions
pip list

# Identify packages that have newer versions available
pip list --outdated

# Save the current environment state to this project file
pip freeze > requirements.txt
```

Happy testing & have fun ! :partying_face:
