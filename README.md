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

## todo
 
- [x] requests against status endpoint
- [x] requests against status endpoint
- [x] object: Status
- [x] object: Citations
- [x] object: Citation
- [x] object: Export
- [x] object: Metadata
- [x] object: Provenance
- [ ] integrate with bibtex parser (e.g. [sciunto-org/python-bibtexparser](https://github.com/sciunto-org/python-bibtexparser))
- [ ] improve test coverage
- [ ] CI with GH actions
- [ ] sphinx documentation
- [ ] GH pages documnetation site
