
# coding: utf-8

# # Search and download pictures in a webpage
# 
# This is an example for how to download files from a simple webpage (Wikipedia) in order to learn the basic principles of how to do this with urllib and beautifulsoup in python. This is done using two  packages:
# 
#     Beautifulsoup https://pypi.org/project/beautifulsoup4/
#     Urllib3 https://urllib3.readthedocs.io/en/latest/
# 
# --------------------------install specifically required packages-------------------------------------
# 
#     conda install beautifulsoup4
#     conda install urllib3

# #### Import packages

# In[1]:


# general imports
import shutil
import re, os


# In[2]:


# imports for displaying pictures in notebook
from IPython.display import Image
from IPython.core.display import HTML 


# In[3]:


# specific imports
import urllib3
from bs4 import BeautifulSoup


# ### Read webpage content
# 
# The example here is a wikipedia page

# In[4]:


# first specify the page URL
url = "https://en.wikipedia.org/wiki/Cat_intelligence"


# Below a request is sent for the webpage content. Here, minimal request information is used; this should be extended for larger requests with appropriate identification (see UrlLib3 documentation for details.

# In[5]:


# setup pool manager for urllib3
http = urllib3.PoolManager()


# In[6]:


# get web page content
response = http.request('GET', url)


# In[7]:


# analyze web page content with beautifulsoup
soup = BeautifulSoup(response.data)


# In[8]:


# print webpage content
print (soup)


# ### Find pictures in webpage content

# In[9]:


# find images in the page and store them in a list
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))


# In[10]:


# print the list of images
for image in images:
    print(image)


# In[11]:


# for each item in the list, you can create a URL as follows:
url2 = 'https:'+images[1]
print(url2)


# In[12]:


# Display image based on url
Image(url=url2)


# In[13]:


# download image to a file named testfile.png
filename = 'testfile.png'


# In[14]:


# download request: again, minimal request information used here; should be extended for larger requests
c = urllib3.PoolManager()

with c.request('GET',url2, preload_content=False) as resp, open(filename, 'wb') as out_file:
    shutil.copyfileobj(resp, out_file)

resp.release_conn()  


# ### Specify pictures to download
# 
# Now we repeat the download for a list of files.

# In[15]:


# we search for all pictures with 'cat' in their name in the list of images created before
image_list = []
for image in images:
    if any(re.findall(r'cat', image, re.IGNORECASE)):
        urlx = 'https:'+image
        image_list.append(urlx)


# In[16]:


# print the list with the cat images
print(image_list)


# In[17]:


# each list entry can be further decomposed into words
words = image_list[0].split('/')
words


# In[18]:


words[-2]


# ### Download all specified pictures

# In[19]:


# make a folder for downloading pictures
folder = 'catpictures'
if not os.path.exists(folder):
    os.mkdir(folder)


# Below all selected pictures are downloaded; again,minimal request information is used here (see above)

# In[20]:


c = urllib3.PoolManager()

for image in image_list:
    words = image.split('/')
    filename = os.path.join(folder,words[-2]) # filename for picture download
    with c.request('GET',image, preload_content=False) as resp, open(filename, 'wb') as out_file:
        shutil.copyfileobj(resp, out_file)

resp.release_conn()  

