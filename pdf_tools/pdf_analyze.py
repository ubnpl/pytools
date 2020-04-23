
# coding: utf-8

# # Import PDF and analyze content
# 
# Example notebook for how to read and analyze PDF files

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
# 
# Text analysis:
# 
#     conda install nltk
# 
#     Download additional nltk ressources in python shell
# 
#         python nltk.download('punkt')
#         python nltk.download('averaged_perceptron_tagger')
#         python nltk.download('maxent_ne_chunker')
#         python nltk.download('words')
#         python nltk.download('treebank')
#         python nltk.download('stopwords')

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


# ## Analyze PDF text with Natural Language Toolkit
# 
# Analysis of the text in the PDF can be done using NLTK: https://www.nltk.org

# In[21]:


import nltk


# In[22]:


sentence = cont


# In[23]:


# first we tokenize the whole text
tokens = nltk.word_tokenize(sentence)


# In[24]:


tokens


# In[25]:


text = nltk.Text(tokens)


# In[26]:


textname = text.name
print(textname)
text.name


# In[27]:


# Collocations: words occuring together
text.collocations(num=10)


# In[28]:


# find common context of two words
text.common_contexts(["with", "and"])


# In[29]:


# occurances of expression within context
text.concordance('virus' and 'cell', width=100, lines=3)


# In[30]:


# occurances of expression within context
text.concordance('RNA' and 'virus', width=100, lines=3)


# In[31]:


# occurances of expression within context as list
conclist = text.concordance_list('RNA' and 'virus')
for n, item in enumerate(conclist):
    print (n)
    print (conclist[n])


# In[32]:


# count number of occurences
text.count('virus')


# In[33]:


# Dispersion plot for word occurences
text.dispersion_plot(['virus', 'cell', 'RNA'])


# In[34]:


# find specific expression in text
text.findall("<virus><dynamics>")


# In[35]:


text.index('virus')


# In[36]:


text[82:89]


# In[37]:


# plot frequency of words in text
text.plot(30)


# In[38]:


# find similar words according to context
text.similar('model')


# In[39]:


text.unicode_repr()


# In[40]:


# analyze text vocabulary
vocabulary = text.vocab()
vocabulary


# In[41]:


# get frequency of given word
vocabulary.freq('model')


# In[42]:


# get most common words in vocabulary
vocabulary.most_common(n=5)


# In[43]:


# get all vocabulary terms
vocabulary.keys()


# In[44]:


# get occurrence of given word in vocabulary
vocabulary['model']

