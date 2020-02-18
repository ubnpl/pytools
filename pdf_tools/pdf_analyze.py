
# coding: utf-8

# # Import PDF and analyze

# ## Test PyPDF2

# In[1]:


import PyPDF2


# In[2]:


# creating an object 
file = open('nchemex.pdf', 'rb')


# In[3]:


# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)


# In[4]:


# print the number of pages in pdf file
print(fileReader.numPages)


# In[5]:


fileReader.documentInfo


# In[6]:


page = fileReader.getPage(0)


# In[7]:


page_content = page.extractText()


# In[8]:


print (page_content.encode('utf-8'))


# In[9]:


page_content


# ## Test Tabula

# In[10]:


from tabula import read_pdf


# In[11]:


df = read_pdf('BJ-2008.pdf')


# In[12]:


df


# ## Test Tika

# In[13]:


from tika import parser


# In[14]:


parsedPDF = parser.from_file("nchemex.pdf")


# In[15]:


parsedPDF


# In[16]:


parsedPDF.keys()


# In[17]:


parsedPDF['content']


# In[18]:


parsedPDF['metadata']


# In[19]:


cont = parsedPDF['content']


# In[20]:


cont.split('\n')


# In[21]:


cont.splitlines()


# In[22]:


meth = cont.partition('Fabritiis')


# In[23]:


meth[0]


# ## Process Text with Natural Language Toolkit

# In[24]:


import nltk


# In[25]:


sentence = cont


# In[26]:


tokens = nltk.word_tokenize(sentence)


# In[27]:


tokens


# In[28]:


text = nltk.Text(tokens)


# In[29]:


textname = text.name
print(textname)
text.name


# In[30]:


# Collocations: words occuring together
text.collocations(num=10)


# In[31]:


# find common context of two words
text.common_contexts(["binding", "association"])


# In[32]:


# occurances of expression within context
text.concordance('Markov' and 'molecular' and 'atomic', width=100, lines=3)


# In[33]:


# occurances of expression within context as list
conclist = text.concordance_list('Markov' and 'molecular' and 'atomic')
for n, item in enumerate(conclist):
    print (n)
    print (conclist[n])


# In[34]:


# count number of occurences
text.count('Markov')


# In[35]:


# Dispersion plot for word occurences
text.dispersion_plot(['simulation', 'kinetics', 'Markov'])


# In[36]:


text.findall("<MD><simulations>")


# In[37]:


text.index('MD')


# In[38]:


text[82:89]


# In[39]:


text.plot(30)


# In[40]:


text.similar('simulation')


# In[41]:


text.unicode_repr()


# In[42]:


# analyze text vocabulary
vocabulary = text.vocab()
vocabulary


# In[43]:


vocabulary.freq('simulation')


# In[44]:


vocabulary.most_common(n=5)


# In[45]:

# get vocabulary keys
vocabulary.keys()


# In[46]:


vocabulary['simulation']

