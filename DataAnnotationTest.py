import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def get_google_doc_content(url):
    # Assuming the URL is a direct link to the text content of the Google Doc
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Failed to retrieve Google Doc content")

def parse_doc_content(doc_content):
    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(doc_content, 'html.parser')
    # Find all the rows in the table
    rows = soup.find_all('tr')
    # Extract data from each row
    data = []
    for row in rows:
        # Find all cells in the row
        cells = row.find_all('td')
        if cells:
            # Extract text from each cell
            row_data = [cell.get_text(strip=True) for cell in cells]
            data.append(row_data)
    return data

def print_unicode_grid_from_doc(url):
    doc_content = get_google_doc_content(url)
    parsed_data = parse_doc_content(doc_content)
    return parsed_data

# Example usage:
url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"  # Replace with the actual URL
list = print_unicode_grid_from_doc(url)[1:]

# Initial dictionary with keys and empty lists as values
my_dict = {"0f": [], "0e": [], "1f": [], "1e": [], "2f": [], "2e": [], "3f": [], "3e": [], "4f": [], "4e": [], "5f": [], "5e": [], "6f": [], "6e": []}

for elem in list:
    if elem[1] == "█":
        my_dict[f"{int(elem[2])}f"].append(int(elem[0]))
    else:
        my_dict[f"{int(elem[2])}e"].append(int(elem[0]))

str_lst = []
for i in range(7):
    str = ""
    for j in range(90):
        if j in my_dict[f"{i}f"]:
            str = str + "█"
        elif j in my_dict[f"{i}e"]:
            str = str + "░"
        else:
            str = str + " "
    str_lst.append(str)

print(f"{str_lst[0]}\n{str_lst[1]}\n{str_lst[2]}\n{str_lst[3]}\n{str_lst[4]}\n{str_lst[5]}\n{str_lst[6]}\n")

    



