"""
This program obtains the robots from a website.
Extracted data: price, name and the link of the publication.
"""

from requests_html import HTMLSession

def GetRobot(elemento):
    
    nombre = elemento.find('div.item-name')[0].text
    precio = elemento.find('span.currency_price')[0].text
    link = list(elemento.find('a')[0].absolute_links)[0]

    robot = {
            'nombre':nombre,
            'precio':precio,
            'link':link
    }
    return robot

def GetHTMLObject(url):
    
    session = HTMLSession()
    response = session.get(url)
    response.html.render()

    return response.html

def GetAspiradoras():

    objHtml = GetHTMLObject(r'https://tiendamia.com/ar/search?amzs=robots%20aspiradora')

    table = objHtml.find('div.item.button-border')
    
    robots = {}
    for elemento in table:
        robot = GetRobot(elemento)

        robots[robot['nombre']]= robot

    print(robots)

    return robots


if __name__ == '__main__':

    robots = GetAspiradoras()
    for robot in robots:
        print(robot)