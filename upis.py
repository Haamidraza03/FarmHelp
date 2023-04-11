# import requests
# from bs4 import BeautifulSoup
# import lxml
# import re

# html = requests.get("https://vikaspedia.in/agriculture/agri-insurance/unified-package-insurance-scheme")
# soup = BeautifulSoup(html.text, "lxml")

# with open("upis.txt", "w", encoding="utf-8") as output:
#     output.write(soup.prettify())


# upis = soup.findAll('div', class_ = 'noScreen col')
# print(upis)

#NOT WORKING AS VIKASPEDIA DOESN'T ALLOW WEB SCRAPPING