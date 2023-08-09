# import requests

# file_url = "https://pje.tjmg.jus.br/pje/seam/resource/rest/pje-legacy/documento/download/9834690001"

# # <embed type="application/x-google-chrome-pdf" src="chrome-extension://mhjfbmdgcfjbbpaeojofohoefgiehjai/f84a194b-1e45-45ab-89ff-4e7640f38faf" original-url="https://pje.tjmg.jus.br/pje/seam/resource/rest/pje-legacy/documento/download/9834690001" background-color="4283586137" javascript="allow">

# r = requests.get(file_url)

# with open("processo.pdf", "wb") as pdf:
#     for chunk in r.iter_content(chunk_size=1024):
#         if chunk:
#             pdf.write(chunk)

import requests

# Replace the following placeholders with your actual credentials
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
response.raise_for_status()  # Check for any login errors

# Access the page with the PDF file
pdf_url = "https://pje.tjmg.jus.br/pje/seam/resource/rest/pje-legacy/documento/download/9834690001"
response = session.get(pdf_url, stream= True)
response.raise_for_status()  # Check for any download errors

# Save the PDF file
with open("downloaded_file.pdf", "wb") as file:
    file.write(response.content)

print("PDF file downloaded successfully.")