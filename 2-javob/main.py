import requests
import threading
import os

def download_pdf(url, filename):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)

# Links from the website
links = [
    "https://tilshunos.com/omonims/?page=12",
  

]

# Directory to save PDF files
directory = 'omonimlar'
if not os.path.exists(directory):
    os.makedirs(directory)

# Creating threads for each PDF download
threads = []
for i, link in enumerate(links, start=12):
    filename = f"{directory}/page_{i}.pdf"
    thread = threading.Thread(target=download_pdf, args=(link, filename))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("PDF files downloaded successfully.")
