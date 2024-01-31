from bs4 import BeautifulSoup
import requests

def getDockerDesktopDEBPackage():
    url = 'https://docs.docker.com/desktop/install/ubuntu/'
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        enlace_etiqueta = soup.find('a', class_='link external-link')
        # Verificar si se encontró la etiqueta
        if enlace_etiqueta:
            enlace = enlace_etiqueta['href']
            print(f'Enlace obtenido: {enlace}')
        else:
            print('No se encontró la etiqueta <a> con la clase "link external-link"')
    else:
        print(f'Error al cargar la página. Código de estado: {response.status_code}')

def getGraddleBinary():
    try:
        url = 'https://gradle.org/releases/'
        response = requests.get(url)
        response.raise_for_status()  # Lanzar una excepción en caso de error HTTP
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        div_resources = soup.find('div', {'class': 'resources-contents'})
        if not div_resources:
            raise Exception('No se encontró el div principal con clase "resources-contents"')

        div_indent = div_resources.find('div', {'class': 'indent'})
        if not div_indent:
            raise Exception('No se encontró ningún div con clase "indent" dentro del div principal')

        a_js_download = div_indent.find('a', {'class': 'js-download-link'})
        if not a_js_download:
            raise Exception('No se encontró la etiqueta <a> con la clase "js-download-link"')

        enlace = a_js_download['href']
        print(f'Enlace obtenido: {enlace}')
    except requests.exceptions.HTTPError as e:
        print(f'Error al cargar la página. Código de estado')

def getJDK17():
    try:
        url = 'https://www.oracle.com/java/technologies/downloads/#java17'
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('tbody')
        if not table:
            raise Exception('No se encontró la etiqueta <tbody>')
        rows = table.find_all('tr')
        if not rows:
            raise Exception('No se encontraron filas en la tabla')

        debPackageUrl = ''
        for row in rows:
             if 'x64 Debian Package' in row.text:
                 debPackageUrl = row.find('a')['href']
                 break

        if not debPackageUrl:
            raise Exception('No se encontró el enlace del paquete .deb')

        print(f'Enlace obtenido: {debPackageUrl}')

    except requests.exceptions.HTTPError as e:
        print(f'Error al cargar la página. Código de estado')

def getMaven():
    try:
        url = 'https://maven.apache.org/download.cgi'
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        tables = soup.find_all('table')
        if len(tables) < 2:
            raise Exception('No se encontraron dos tablas')
        table = tables[1]
        if not table:
            raise Exception('No se encontró la etiqueta <table> con la clase "table table-striped"')
        rows = table.find_all('tr')
        if not rows:
            raise Exception('No se encontraron filas en la tabla')
        mavenUrl = ''
        for row in rows:
            if 'Binary tar.gz archive' in row.text:
                mavenUrl = row.find('a')['href']
                break
        if not mavenUrl:
            raise Exception('No se encontró el enlace del paquete .tar.gz')
        print(f'Enlace obtenido: {mavenUrl}')

    except requests.exceptions.HTTPError as e:
        print(f'Error al cargar la página. Código de estado')

def getNodejs():
    try:
        url = 'https://nodejs.org/en/download/current/'
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        if not table:
            raise Exception('No se encontró la etiqueta <table>')
        rows = table.find_all('tr')
        if not rows:
            raise Exception('No se encontraron filas en la tabla')
        debPackageUrl = ''
        for row in rows:
            if 'Linux Binaries' in row.text:
                debPackageUrl = row.find('a')['href']
                break
        if not debPackageUrl:
            raise Exception('No se encontró el enlace del paquete .tar.xz')
        print(f'Enlace obtenido: {debPackageUrl}')
    except requests.exceptions.HTTPError as e:
        print(f'Error al cargar la página. Código de estado')





