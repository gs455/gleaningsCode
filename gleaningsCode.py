import requests
from bs4 import BeautifulSoup
import random
import keyboard

# URL of the website containing the excerpts
url = 'https://www.bahai.org/library/authoritative-texts/bahaullah/gleanings-writings-bahaullah/gleanings-writings-bahaullah.xhtml?35eabf49'

# Send a request to the website and get the HTML response
response = requests.get(url)
html = response.content

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all the divs with class 'cd' which contain the excerpts
divs = soup.find_all('div', {'class': 'cd'})

# Create a list of excerpts
excerpts = []
for div in divs:
    excerpt = div.get_text()
    # Add the extracted excerpt to the list
    excerpts.append(excerpt)

input("Press Enter to continue...")

# Loop until the user presses the "h" key on the keyboard
while True:
    # Wait for the user to enter the letter "h"
    print('Press the "h" key to display a random excerpt...')
    keyboard.wait('h')

    # Generate a random index and display the corresponding excerpt
    random_index = random.randint(0, len(excerpts)-1)
    print('-'*50)
    print(excerpts[random_index])
    print('='*50)



