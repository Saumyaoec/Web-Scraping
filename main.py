import requests
from bs4 import BeautifulSoup

url ="https://www.codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content  
# print(htmlContent)     #it will show all  html content form url in terminal in ununiformal

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify())   #it will show all the html content in prettify comment out upper htmlContent

# Step 3: Comment 

markup ="<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
# print(soup2.p)  #print the comment out paragraph
# exit()  #it use for exit don't print below line not nessary
# print(type(soup2.p.string)) #show the comment object 
# exit()

#Step 4: HTML Tree traversal

# Commonly used type of objects:
 # 1.Tag
# title = soup.title
# print(title)   #print only html title tag
# print(type(title))  # give class tag

# 2.NavigableString
# print(type(title.string))

# # 3.Beautifulsoup
# print(type(soup))


# Get the title of the html page
title = soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)

# Get only first element in the html page
# print(soup.find('p')) 

#Get class of any element in the html page (if class not use then KeyError: 'class')
# print(soup.find('p')['class']) 
# exit()

#Get id of any element in the html page (if class not use then KeyError: 'id')
# print(soup.find('p')['id'])   

# find all the elementa with class lead
# print(soup.find_all("p", class_="text-sm"))  #text-sm is class name of paragraph


#Get the text from the tags/soup
# print(soup.find('p').get_text())

#print all the text in html page
# print(soup.get_text()) 


# Get all the anchor tags from the page
anchors = soup.find_all('a')

# print(anchors)

#Get all the link on the page 
# for link in anchors:
# 	if(link !='#'):   # dont show comment out link
# 		print(link.get('href'))


# same thing as above get all the link only
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
	if(link.get('href')  !='#'):   # don't show comment out link
		linkText = "https://www.codewithharry.com" +link.get('href')
		all_links.add(link)
		# print(linkText)


navbarSupportedContent = soup.find(id='navbarSupportedContent')

# print(navbarSupportedContent.children) 
# print(navbarSupportedContent.content)  #get all the element content in the content like ul,li,td,div,form whatever avilable show all

# .children - A Tag's are avilable as a generato
# .contents - A Tag's are avilable as a list 

for elem in navbarSupportedContent.contents:  #elem is element (in .contents element store in a memory )
# 	print(elem)

#elem is element(in .children element not store in memory you can get element by using  itret or next function it only required for big page for small page it don't required )

# for elem in navbarSupportedContent.children:  
# 	print(elem)

# for item in navbarSupportedContent.strings: #get all the string from id you use 
# 	print(item)

# for item in navbarSupportedContent.stripped_strings:  #get the all the string
# 	print(item)


# print(navbarSupportedContent.parent) #print the parent class by help of .parent


# .parents here you can  iterate
# print(navbarSupportedContent.parents)

# now  iterate you can get all elements parents

# for item in navbarSupportedContent.parents:
	# print(item)
	# print(item.name)

# in next_sibling or previous_siblings spaces are count a elememet
# print(navbarSupportedContent.next_sibling) #get empty string
# print(navbarSupportedContent.next_sibling.next_sibling)  #None
# print(navbarSupportedContent.previous_siblings.previous_siblings #space new line also take as a previous_sibling



elem = soup.select('.modal-footer')   #.modal-footer here is a class name (# use for id)
print(elem)  # show all the .modal-footer class element















