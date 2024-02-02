from bs4 import BeautifulSoup
import requests


def get_docker_desktop_deb_package():
    try:
        url = 'https://docs.docker.com/desktop/install/ubuntu/'
        response = requests.get(url)
        response.raise_for_status()  # Lanzar una excepción en caso de error HTTP
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        a_link = soup.find('a', class_='link external-link')
        docker_url = ''
        # Verificar si se encontró la etiqueta
        if not a_link:
            return docker_url
        a_link_text = a_link['href']
        docker_url = a_link_text
        return docker_url
    except requests.exceptions.RequestException as e:
        print(f'Error al cargar la página: {e}')
        return ''


def get_gradle_binary():
    try:
        url = 'https://gradle.org/releases/'
        response = requests.get(url)
        response.raise_for_status()  # Lanzar una excepción en caso de error HTTP
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        div_resources = soup.find('div', {'class': 'resources-contents'})
        gradle_url = ''
        if not div_resources:
            return gradle_url
        div_indent = div_resources.find('div', {'class': 'indent'})
        if not div_indent:
            return gradle_url
        a_js_download = div_indent.find('a', {'class': 'js-download-link'})
        if not a_js_download:
            return gradle_url
        gradle_url = a_js_download['href']
        return gradle_url
    except requests.exceptions.HTTPError as e:
        print(f'Error al cargar la página.')
        return ''


def get_jdk17():
    try:
        url = 'https://www.oracle.com/java/technologies/downloads/#java17'
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('tbody')
        jdk_url = ''
        if not table:
            return jdk_url
        rows = table.find_all('tr')
        if not rows:
            return jdk_url
        for row in rows:
            if 'x64 Debian Package' in row.text:
                jdk_url = row.find('a')['href']
                break
        return jdk_url
    except requests.exceptions.HTTPError as e:
        print(f'Error al cargar la página.')
        return ''


def get_maven():
    try:
        url = 'https://maven.apache.org/download.cgi'
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        tables = soup.find_all('table')
        maven_url = ''
        if len(tables) < 2:
            return maven_url
        table = tables[1]
        if not table:
            return maven_url
        rows = table.find_all('tr')
        if not rows:
            return maven_url
        for row in rows:
            if 'Binary tar.gz archive' in row.text:
                maven_url = row.find('a')['href']
                break
        return maven_url
    except requests.exceptions.HTTPError as e:
        print(f'Error al cargar la página.')
        return ''


def get_nodejs():
    try:
        url = 'https://nodejs.org/en/download/current/'
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        deb_package_url = ''
        if not table:
            return deb_package_url
        rows = table.find_all('tr')
        if not rows:
            return deb_package_url
        for row in rows:
            if 'Linux Binaries' in row.text:
                deb_package_url = row.find('a')['href']
                break
        return deb_package_url
    except requests.exceptions.HTTPError as e:
        print(f'Error al cargar la página.')
        return ''


def modify_shell_script(script, line_to_modify, var_to_update, new_content):
    with open(script, 'r') as file:
        lines = file.readlines()

    if 0 < line_to_modify <= len(lines):
        if new_content != '':
            lines[line_to_modify - 1] = f'{var_to_update}="{new_content}"\n'

    with open(script, 'w') as file:
        file.writelines(lines)


# modify_shell_script("docker_cli_installer.sh", 3,
#                     "DOCKER_DEB_PACKAGE", get_docker_desktop_deb_package())
# modify_shell_script("gradle_installer.sh", 3,
#                     "GRADLE_DOWNLOAD_LINK", get_gradle_binary())
# modify_shell_script("jdk-17_installer.sh", 3,
#                     "JDK_DOWNLOAD_LINK", get_jdk17())
# modify_shell_script("maven_installer.sh", 3,
#                     "MAVEN_DOWNLOAD_LINK", get_maven())
# modify_shell_script("nodejs_installer.sh", 3,
#                     "NODE_DOWNLOAD_LINK", get_nodejs())

print(get_docker_desktop_deb_package())
print(get_gradle_binary())
print(get_jdk17())
print(get_maven())
print(get_nodejs())








