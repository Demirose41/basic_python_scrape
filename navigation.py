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
    <li class="special super-special">This list item is also special.</li>
    <li>This list item is not special.</li>
    <li class="special">This list item is special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

data = soup.body.contents
#       print(data)
# ['\n', <div id="first">
# <h3 data-example="yes">hi</h3>
# <p>more text.</p>
# </div>, '\n', <ol>
# <li class="special">This list item is special.</li>
# <li class="special">This list item is also special.</li>
# <li>This list item is not special.</li>
# </ol>, '\n', <div data-example="yes">bye</div>, '\n']
#       print(data[1].next_sibling.next_sibling)
# <ol>
# <li class="special">This list item is special.</li>
# <li class="special">This list item is also special.</li>
# <li>This list item is not special.</li>
# </ol>

#       bata = soup.find(class_="super-special").parent.parent

shmayta = soup.find(id="first").find_next_sibling() # this will skip the /n until it finds the actuall next sibling !!!! 

#print(shmayta)

jayta = soup.select("[data-example]")[1].find_previous_sibling()

#print(jayta)

kayta = soup.find(class_="super-special").find_next_sibling(class_="special")
#print(kayta)

data2 = soup.find("h3").find_parent("html")
print(data2)

help(data2)