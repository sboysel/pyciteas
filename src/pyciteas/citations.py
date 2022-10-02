from src.pyciteas.request import request

def citations(product):
    """
    Query the citations endpoint of the CiteAs API for the reference data for a
    specified product.

    Reference: https://citeas.org/api#citations-object

    Parameters
    ----------
    product : str
        Reference to query.

    Raises
    ------
    ValueError
        If the request returns a non-200 status code, there is no data returned
        and therefore nothing to be parsed.

    Returns
    -------
    Citations
        A Citations object containing the structured data from response of the
        request to the citations endpoint.
    """

    data = request(product)

    if not data:
        raise ValueError('No data returned')

    return Citations(data)


class Citations:
    """
    Reference: https://citeas.org/api#citations-object
    """

    def __init__(self, data):
        self.citations = {x['style_shortname']: Citation(x) for x in data['citations']}
        self.exports = {x['export_name']: Export(x) for x in data['exports']}
        self.metadata = data['metadata']
        self.name = data['name']
        self.provenance = [Provenance(x) for x in data['provenance']]
        self.url = data['url']

    def __repr__(self):
        return 'Citations()'

    def __str__(self):
        s = f'name: {self.name}\n'
        s += f'url: {self.url}\n'
        return s

    def export(self, name, strip_newlines=False):
        """
        Return citation export as a string in a format specified by name.  Optionally
        removes all newline characters.

        Parameters
        ----------
        name : str
            Must be one of 'bibtex', 'csv', 'ris', 'enw'.
        strip_newlines : bool
            If True, removes all newline characters from the exported citation
            string.  Default: False.

        Returns
        -------
        export
            A string for the citation in the format specified by name
        """

        exp = self.exports[name].export

        if strip_newlines:
            exp = ''.join(exp.splitlines())

        return exp

    def bibtex(self, strip_newlines=False):
        """
        Bibtex export
        """
        return self.export('bibtex', strip_newlines=strip_newlines)

    def csv(self, strip_newlines=False):
        """
        CSV export
        """
        return self.export('csv', strip_newlines=strip_newlines)

    def enw(self, strip_newlines=False):
        """
        ENW export
        """
        return self.export('enw', strip_newlines=strip_newlines)

    def ris(self, strip_newlines=False):
        """
        RIS export
        """
        return self.export('ris', strip_newlines=strip_newlines)


class Citation:
    """
    Reference: https://citeas.org/api#citations-object
    """

    def __init__(self, data):
        self.citation = data['citation']
        self.style_fullname = data['style_fullname']
        self.style_shortname = data['style_shortname']

    def __repr__(self):
        return 'Citation()'

    def __str__(self):
        s = f'citation: {self.citation}\n'
        s += f'style_fullname: {self.style_fullname}\n'
        s += f'style_shortname: {self.style_shortname}\n'
        return s


class Export:
    """
    Reference: https://citeas.org/api#citations-object
    """

    def __init__(self, data):
        self.export = data['export']
        self.export_name = data['export_name']

    def __repr__(self):
        return 'Export()'

    def __str__(self):
        s = f'export: {self.export}\n'
        s += f'export_name: {self.export_name}\n'
        return s


class Provenance:
    """
    Reference: https://citeas.org/api#citations-object
    """

    def __init__(self, data):
        """
        From the documentation:

                Describes steps the software took to try and find citation data,
                and whether citation data was found.

        """
        self.content_url = data['content_url']
        self.found_via_proxy_type = data['found_via_proxy_type']
        self.has_content = data['has_content']
        self.host = data['host']
        self.name = data['name']
        self.parent_step_name = data['parent_step_name']
        self.parent_subject = data['parent_subject']
        self.subject = data['subject']

    def __repr__(self):
        return 'Metadata()'

    def __str__(self):
        s = f'content_url: {self.content_url}\n'
        s += f'found_via_proxy_type: {self.found_via_proxy_type}\n'
        s += f'host: {self.has_content}\n'
        s += f'name: {self.name}\n'
        s += f'parent_step_name: {self.parent_step_name}\n'
        s += f'parent_subject: {self.parent_subject}\n'
        s += f'subject: {self.subject}\n'
        return s
