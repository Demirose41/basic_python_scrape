from bs4 import BeautifulSoup
## What is beautiful soup?
# A library that lets us navigate through HTML with Python
# It does NOT download HTML - for this, we need to requests module!

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
## Selecting by HTML
soup = BeautifulSoup(html, "html.parser")
print(soup)
print(type(soup))
print(soup.body) ## returns the body 
print(soup.body.div) ## only returns first div 
print(soup.find("div")) ## Only returns first div that is NOT a string but a bs4 class

d = soup.find_all("div") ## returns all divs
print(d)

f = soup.find(id="first")
print(f)

g = soup.find_all(class_ ="special") ## remember class_ must have the _ or python will not be happy Always gives a list back
print(g)
print(type(g))

h = soup.find_all(attrs={"data-example": "yes"})
print(h)

##Selecting by CSS

q = soup.select("#first") ##Always gives a list back
print(q)