
# coding: utf-8

# # Import PDF and analyze content
# 
# Example notebook for how to read content and metadata of  PDF files

# #### Python environment installation instructions
# 
# General Packages:
# 
#     conda install numpy scipy matplotlib jupyter
# 
# PDF-specific packages:
# 
#     pip install pypdf2
#     conda install tika

# #### Example PDF file
# 
# The PDF file used in the example below can be downloaded from:
# 
#     https://doi.org/10.1073/pnas.1117201109

# In[1]:


# set PDF filename/filepath parameter; this PDF file will be used in all examples; 
pdf_name = '12980.full.pdf'


# ## Get Text and Metadata from PDF using PyPDF2
# 
# https://pythonhosted.org/PyPDF2/

# In[2]:


# import PyPDF2
import PyPDF2


# In[3]:


# read the example pdf defined above
file = open(pdf_name, 'rb')


# In[4]:


# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)


# In[5]:


# print the number of pages in pdf file
print(fileReader.numPages)


# In[6]:


# get document metadata
fileReader.documentInfo


# In[7]:


page = fileReader.getPage(0)


# In[8]:


page_content = page.extractText()


# In[9]:


print (page_content.encode('utf-8'))


# ## Get text and metadata from PDF using TIKA
# 
# General information about TIKA
# https://cwiki.apache.org/confluence/display/TIKA/TikaServer
# 
# TIKA python API
# https://github.com/chrismattmann/tika-python

# In[10]:


# import parser from TIKA
from tika import parser


# In[11]:


# read example PDF definded above
parsedPDF = parser.from_file(pdf_name)


# In[12]:


print(parsedPDF)


# In[13]:


# parsed pdf is stored as a dictionary; here we get the keys
parsedPDF.keys()


# In[14]:


# one of the keys provides the content
print(parsedPDF['content'])


# In[15]:


# one of the keys provides the metadata
parsedPDF['metadata']


# ### Analyze PDF text with generic tools

# In[16]:


# store content in variable
cont = parsedPDF['content']


# In[17]:


# separate content by a specified sequence of characters
cont.split('ei')


# In[18]:


# separate all lines in the PDF file
cont.splitlines()


# In[19]:


# get a conent Partition at a specific word
meth = cont.partition('quasispecies')


# In[20]:


print(meth[0])

