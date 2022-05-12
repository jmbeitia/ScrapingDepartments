"""
This program obtains the first 15 apartments with 1 bedroom and 1 bathroom from a website.
Extracted data: price, location, m2 and the link of the publication.
"""

from requests_html import HTMLSession

def GetHtmlFromUrl(url):

    session = HTMLSession()
    request = session.get(url)
    request.html.render()
    htmlObject = request.html

    return htmlObject

def GetDepartamentoByRow(row):

    precio = float(row.find('span.price-tag-fraction')[0].text)
    superficie = row.find('li.ui-search-card-attributes__attribute')[0].text
    ubicacion = row.find('p.ui-search-item__group__element.ui-search-item__location')[0].text
    link = list(row.find('a')[0].absolute_links)[0]

    departamento = {'precio': precio,
                    'superficie': superficie,
                    'ubicacion': ubicacion,
                    'link': link}

    return departamento

def GetDepartamentos():

    # number = 1
    # url = f'https://www.portalinmobiliario.com/arriendo/departamento/1-dormitorio/providencia-metropolitana/_OrderId_PRICE_Banos_{number}_NoIndex_True'
    htmlObject = GetHtmlFromUrl('https://www.portalinmobiliario.com/arriendo/departamento/1-dormitorio/providencia-metropolitana/_OrderId_PRICE_Banos_1_NoIndex_True')

    table = htmlObject.find('ol')[0]
    rows = table.find('li.ui-search-layout__item')[:15]

    departamentos = []
    for row in rows:

        departamento = GetDepartamentoByRow(row)
        departamentos.append(departamento)

    departamentos.sort(key=lambda x: x['precio'])

    return departamentos


if  __name__ == '__main__':
    
    departamentos = GetDepartamentos()
    for depto in departamentos:
        print(depto)