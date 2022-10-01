# pyciteas

https://citeas.org/api

## usage

Get the status of the CiteAs API.  Returns a `Status()` object if the request
returns a `200` code.

```python
>> from pyciteas.status import status
>> print(status())
documentation_url: https://citeas.org/api
msg: Don't panic
version: 0.1
```

Get citations for a reference

```python
>> from pyciteas.citations import citations
>> c = citations('https://github.com/datacite/maremma')
>> print(c)
name: Maremma: a Ruby library for simplified network calls
url: https://github.com/datacite/maremma
```

Get the citation in a particular style

```python
>> print(c.citations['apa'])
citation: Fenner, M. (2017, February 24). Maremma: a Ruby library for simplified network calls. DataCite. http://doi.org/10.5438/QEG0-3GM3
style_fullname: American Psychological Association 6th edition
style_shortname: apa
```

Get the citation export in a particular format

```python
>> print(c.exports['bibtex'])
export: @article{ITEM1, title={Maremma: a Ruby library for simplified network calls},
journal={},
volume={},
number={},
pages={},
year={2017},
publisher={DataCite},
author={Fenner, Martin}}
export_name: bibtex
```

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
