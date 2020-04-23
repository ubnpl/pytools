
# coding: utf-8

# # Analyze PDF content with NLTK
# 
# Example notebook for how analyze a PDF file with the Natural Language Toolkit

# #### Python environment installation instructions
# 
# General Packages:
# 
#     conda install numpy scipy matplotlib jupyter
# 
# PDF-specific packages:
# 
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


# ### Read PDF content using TIKA
# 
# General information about TIKA
# https://cwiki.apache.org/confluence/display/TIKA/TikaServer
# 
# TIKA python API
# https://github.com/chrismattmann/tika-python

# In[2]:


# import parser from TIKA
from tika import parser


# In[3]:


# read example PDF definded above
parsedPDF = parser.from_file(pdf_name)


# In[4]:


# parsed pdf is stored as a dictionary; here we get the keys
parsedPDF.keys()


# In[5]:


# one of the keys provides the content
print(parsedPDF['content'])


# ## Analyze PDF text with Natural Language Toolkit
# 
# Analysis of the text in the PDF can be done using NLTK: https://www.nltk.org

# In[6]:


import nltk


# In[7]:


sentence = parsedPDF['content']


# In[8]:


# first we tokenize the whole text
tokens = nltk.word_tokenize(sentence)


# In[9]:


tokens


# In[10]:


text = nltk.Text(tokens)


# In[11]:


textname = text.name
print(textname)
text.name


# In[12]:


# Collocations: words occuring together
text.collocations(num=10)


# In[13]:


# find common context of two words
text.common_contexts(["with", "and"])


# In[14]:


# occurances of expression within context
text.concordance('virus' and 'cell', width=100, lines=3)


# In[15]:


# occurances of expression within context
text.concordance('RNA' and 'virus', width=100, lines=3)


# In[16]:


# occurances of expression within context as list
conclist = text.concordance_list('RNA' and 'virus')
for n, item in enumerate(conclist):
    print (n)
    print (conclist[n])


# In[17]:


# count number of occurences
text.count('virus')


# In[18]:


# Dispersion plot for word occurences
text.dispersion_plot(['virus', 'cell', 'RNA'])


# In[19]:


# find specific expression in text
text.findall("<virus><dynamics>")


# In[20]:


text.index('virus')


# In[21]:


text[82:89]


# In[22]:


# plot frequency of words in text
text.plot(30)


# In[23]:


# find similar words according to context
text.similar('model')


# In[24]:


text.unicode_repr()


# In[25]:


# analyze text vocabulary
vocabulary = text.vocab()
vocabulary


# In[26]:


# get frequency of given word
vocabulary.freq('model')


# In[27]:


# get most common words in vocabulary
vocabulary.most_common(n=5)


# In[28]:


# get all vocabulary terms
vocabulary.keys()


# In[29]:


# get occurrence of given word in vocabulary
vocabulary['model']

