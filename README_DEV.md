# Running test

```
pytest
```

# Install local dtt

`pip install dist/dtt-{version}.tar.gz`

# Upload to test.pypi.org

```sh
rm -rf dist/*
python setup.py sdist bdist_wheel
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

# Upload to pypi.org

```sh
rm -rf dist/*
python setup.py sdist bdist_wheel
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```
