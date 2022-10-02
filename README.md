# pyciteas

A Python client for the CiteAs API.

From the CiteAs [About page](https://citeas.org/about):

> CiteAs is a way to get the correct citation for diverse research products
> including, software, datasets, preprints, and traditional articles. By making
> it easier to cite software and other "alternative" scholarly products, we aim
> to help the creators of such products get full credit for their work.
>
> CiteAs is a small part of a collaborative grant between OurResearch and James
> Howison at the University of Texas-Austin. Funded by the Alfred P. Sloan
> Foundation, the focus of this grant is to create a big database of research
> software, automatically extracted from millions of open-access scholarly
> articles using machine-learning techniques. Along with the database, we'll
> also make three small prototype applications to show off how the data can be
> used in cool ways. CiteAs is one of these applications.
>
> We're still working on creating the database. But while that's in progress, we
> thought it'd be cool to release CiteAs, even though it still is missing the
> majority of data it will ultimately use. Feel free to kick the tires, and let
> us know what you think!

[API Documentation](https://citeas.org/api)

## Usage

CiteAs requests API users include their email address with queries so that they
can track API usage.  Create a config file named `pyciteas.ini` containing your
email address in the project root directory. 

```ini
[pyciteas]
email = test@example.com
```

`pyciteas` will default to `test@example.com` if no proper config file is found.

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

## Development

```
pipx install flit
mkdir -p pyciteas
cd pyciteas
python -m venv env
source env/bin/activate
flit install
pytest --cov=src test/
```

## TODO
 
- [x] requests against status endpoint
- [x] requests against status endpoint
- [x] object: Status
- [x] object: Citations
- [x] object: Citation
- [x] object: Export
- [x] object: Provenance
- [ ] Save citation export to file
- [ ] CLI utility
- [ ] Integrate with proper bibtex parser (e.g. [sciunto-org/python-bibtexparser](https://github.com/sciunto-org/python-bibtexparser))
- [ ] Improve test coverage
- [ ] CI with GH actions
- [ ] MkDocs documentation
- [ ] GH pages documnetation site
