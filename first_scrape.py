# https://www.rithmschool.com/blog    
import requests 
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
#print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
#print(articles)

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["Title","Link","Date"])
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        # print(article.find("a").attrs['href']) or more simply
        #print(article.find("a")['href'])
        url = a_tag['href']
        date = article.find("time")["datetime"]
        csv_writer.writerow([title,url,date])

        # date

    
