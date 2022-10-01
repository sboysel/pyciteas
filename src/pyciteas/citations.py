from src.pyciteas.request import request

def citations(product):
    """"""
    data = request(product)
    if not data:
        raise ValueError('No data returned')
    return Citations(data)


class Citations:
    """https://citeas.org/api#citations-object"""
    def __init__(self, data):
        self.citations = {x['style_shortname']: Citation(x) for x in data['citations']}
        self.exports = {x['export_name']: Export(x) for x in data['exports']}
        self.metadata = Metadata(data['metadata'])
        self.name = data['name']
        self.provenance = [Provenance(x) for x in data['provenance']]
        self.url = data['url']
    def __repr__(self):
        return 'Citations()'
    def __str__(self):
        s = f'name: {self.name}\n'
        s += f'url: {self.url}\n'
        return s

class Citation:
    """https://citeas.org/api#citations-object"""
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
    """https://citeas.org/api#citations-object"""
    def __init__(self, data):
        self.export = data['export']
        self.export_name = data['export_name']
    def __repr__(self):
        return 'Export()'
    def __str__(self):
        s = f'export: {self.export}\n'
        s += f'export_name: {self.export_name}\n'
        return s

class Metadata:
    """https://citeas.org/api#citations-object"""
    def __init__(self, data):
        """
        From the documentation:

                Metadata varies by source, but typically includes the below fields.

        """
        self.DOI = data['DOI']
        self.URL = data['URL']
        self.abstract = data['abstract']
        self.author = data['author']
        self.id = data['id']
        self.title = data['title']
        self.year = data['year']
        # any additional fields
        self.metadata_all = data

    def __repr__(self):
        return 'Metadata()'
    def __str__(self):
        s = f'DOI: {self.DOI}\n'
        s += f'URL: {self.URL}\n'
        s += f'abstract: {self.abstract}\n'
        s += f'author: {self.author}\n'
        s += f'id: {self.id}\n'
        s += f'title: {self.title}\n'
        s += f'year: {self.year}\n'
        return s

class Provenance:
    """https://citeas.org/api#citations-object"""
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

if __name__ == '__main__':
    c = citations('https://github.com/datacite/maremma')
    print(c)
    print(c.citations['apa'])
    print(c.exports['bibtex'])
    print(c.metadata)
    print(c.provenance[0])
