import requests
from bs4 import BeautifulSoup

username = "02361605163"
password = "pjemaaple01*"

# Create a session to maintain the login session
session = requests.session()

# Login to the website
login_url = "https://pje.tjmg.jus.br/pje/login.seam?loginComCertificado=false"
login_data = {
    "username": username,
    "password": password,
    "submit": "Login",
}

response = session.post(login_url, data=login_data)
response.raise_for_status()

# Define the URL of the page you want to scrape
url = 'https://pje.tjmg.jus.br/pje/Processo/ConsultaProcesso/Detalhe/listProcessoCompletoAdvogado.seam?id=626694660&ca=bd66b39027eb118e3ff2f7c8ac57ea3075151e667aa08ea183f41c334f7d5e37cdcce1168a5f1f9a00bf8276591ae90fa33474c74e0ad67d&aba='

# Send an HTTP GET request to the URL
response = session.get(url)
response.raise_for_status()  # Check for any download errors

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the <a> tags with the 'mailto' protocol
    email_links = soup.find_all('a')#, href=lambda href: href and href.startswith('<img alt='))

    # Extract the email addresses
    email_addresses = [link['href'][7:] for link in email_links]

    # Print the extracted email addresses
    for email in email_addresses:
        print(email)
else:
    print('Failed to retrieve the webpage.')
