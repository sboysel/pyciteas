"""
Examples: https://github.com/ourresearch/citeas-api/blob/master/README.md
"""
from src.pyciteas.citations import (citations, Citations, Citation, Export,
    Provenance)

REFERENCES = [
    'https://fftw.org/',
    '10.5281/zenodo.160400',
    'https://doi.org/10.5281/zenodo.160400',
]

CITATIONS = [citations(r) for r in REFERENCES]

def test_citations_citation():
    """Check that citation objects are created properly"""
    for c in CITATIONS:

        assert isinstance(c, Citations)

        for _, citation in c.citations.items():
            assert isinstance(citation, Citation)

def test_citations_export():
    """Check that export objects are created properly"""
    for c in CITATIONS:

        for _, export in c.exports.items():
            assert isinstance(export, Export)

def test_citations_metadata():
    """Check that metadata dicts are created properly"""
    for c in CITATIONS:

        assert isinstance(c.metadata, dict)

def test_citations_provenance():
    """Check that provenance objects are created properly"""
    for c in CITATIONS:

        for p in c.provenance:
            assert isinstance(p, Provenance)

def test_bibtex():
    s = ('@journal-article{ITEM1, title={The Design and Implementation of FFTW3}'
         ',journal={Proceedings of the IEEE},volume={93},number={},pages={216--231}'
         ',year={2005},publisher={Institute of Electrical and Electronics Engineers'
         ' (IEEE)},author={Frigo, M. and Johnson, S.G.}}')
    assert CITATIONS[0].bibtex() == s

