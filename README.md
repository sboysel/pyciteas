# pyciteas

https://citeas.org/api

## development

```
pipx install flit
mkdir -p pyciteas
cd pyciteas
python -m venv env
source env/bin/activate
flit install
pytest --cov=src test/
```
