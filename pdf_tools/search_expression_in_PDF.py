
# coding: utf-8

# # Search for regular expression in a PDF
# 
# Example notebook for regular expression searching options using the built-in python RegEx Module https://www.w3schools.com/python/python_regex.asp as well as NLTK https://www.nltk.org

# #### Python environment installation instructions
# 
# General Packages:
# 
#     conda install numpy scipy matplotlib jupyter
# 
# Specific packages:
# 
#     conda install tika

# #### Example PDF file
# 
# The PDF file used in the example below can be downloaded from:
# 
#     https://doi.org/10.1073/pnas.1117201109

# In[1]:


# set PDF filename/filepath parameter; this PDF file will be used in all examples; 
pdf_name = '12980.full.pdf'


# ### Import required packages

# In[2]:


# representation of plots
get_ipython().run_line_magic('pylab', 'inline')


# In[3]:


# import required packages
import os
import fnmatch
from tika import parser
import nltk


# ## Search regular expression in a specific PDF

# #### Read PDF

# In[4]:


# read example PDF definded above
parsedPDF = parser.from_file(pdf_name)


# In[5]:


pdftext = parsedPDF['content']


# In[6]:


pdftext


# ### Search for first instance of given pattern
# 
# Use RegEx to find a specific expression defined in the 'pattern'-parameter below.

# In[7]:


# search pattern
pattern = ' quasispecies '


# In[8]:


# search for first instance of pattern in pdftext, re.M:mulitline, re.I:ignore case
searchObj = re.search(pattern, pdftext, re.M|re.I)


# In[9]:


# search results
print ('search pattern found: ', searchObj.group())
print ('position of pattern in text: ', searchObj.span())


# In[10]:


# now check at the given text position
print (pdftext[searchObj.span()[0]:searchObj.span()[1]])


# ### Search for all instances of a given pattern

# In[11]:


# search for all instances of pattern in pdftext, re.M:mulitline, re.I:ignore case
findObj = re.findall(pattern, pdftext, re.M|re.I)
print('number of instances found: ', len(findObj))


# In[12]:


# The result is a list of pattern matching instances
findObj


# In[13]:


# Now we want to get a list of all instances and their positions
for match in re.finditer(pattern, pdftext, re.M|re.I):
    print("%s:%s\t%s" % (match.start(), match.end(), match.group()))


# In[14]:


# Check for positions of given istances in pdftext
pdftext[24438:24452]


# ### Different search patterns and wild cards
# 
# RegEx search is possible for exact patterns or using wildcards

# In[15]:


# Look for exact expression match
re.findall("viral load", pdftext, re.M|re.I)


# In[16]:


# Look for expression within context
re.findall("viral load.*", pdftext, re.M|re.I)


# In[17]:


# different search: exact expression does not return results if words are not directly adjacent
re.findall("viral levels.*", pdftext, re.M|re.I)


# In[18]:


# search for two words within same sentence
re.findall("viral.* levels.*", pdftext, re.M|re.I)


# ## Process PDF with Natural Language Toolkit
# 
# NLTK provides a number of different and complementary options for pattern matching

# ### NLTK tokenization options
# 
# NLTK Tokenizer can be costumized to yield specific types of expressions

# #### Tokenize option 1: Sentence tokenizer
# 
# Tokenizer splits text in whole sentences.

# In[19]:


# tokenize
sen_tokens = nltk.sent_tokenize(pdftext)


# In[20]:


# print sentences
for num, sentence in enumerate(sen_tokens):
    print("sentence Nr. ", num, ":")
    print(sentence)
    print('----------------------------------------------------------------------------')


# #### Tokenize option 2: regular expression tokenizer without numbers

# In[21]:


# setup custom tokenizer
rtokenizer = nltk.RegexpTokenizer('[a-zA-Z]\w+\'?\w*') 


# In[22]:


# get tokens
rtokenizer.tokenize(pdftext)


# In[23]:


# get tokenizer spans (locations in text)
spans = list(rtokenizer.span_tokenize(pdftext))
spans


# #### Tokenize option 3: only expressions with dashes
# 
# Reduce tokenizer to specific expression; here we use dashes

# In[24]:


#setup custom tokenizer
rtokenizer = nltk.RegexpTokenizer('\w*[a-zA-Z]-[a-zA-Z]\w+\'?\w*') 


# In[25]:


# tokenize
rtokenizer.tokenize(pdftext)


# #### Tokenize option 4: only numbers
# 
# Reduce tokenizer to specific numters and special characters

# In[26]:


# setup custom tokenizer
rtokenizer = nltk.RegexpTokenizer('[0-9_]\w+\'?\w*') 


# In[27]:


# tokenize and print number of tokens and tokens list
rtokens = rtokenizer.tokenize(pdftext)
print (len(rtokens))
rtokens


# #### Tokenize option 5: standard option
# 
# Get all expressions from tokenizer

# In[28]:


# standard word tokenizer
tokens = nltk.word_tokenize(pdftext)
print (len(tokens))


# In[29]:


tokens


# ## NLTK analysis of tokenized text
# 
# Use different NLTK options to analyze tokenize text

# #### General options for tokenized text

# In[30]:


text = nltk.Text(tokens)


# In[31]:


# text name
print ('text name: ', text.name)


# In[32]:


# Collocations: words occuring together
text.collocations(num=10)


# #### Find sepcific expression and context information within tokenized text

# In[33]:


# occurances of expression within context
text.concordance('immune', width=100, lines=3)


# In[34]:


text.concordance("quasispecies", width=100, lines=3)


# In[35]:


# count number of occurences
text.count('quasispecies')


# In[36]:


# Dispersion plot for word occurences
text.dispersion_plot(['immune', 'quasispecies'])


# In[37]:


# find other words which appear in the same context
text.similar('immune')


# In[38]:


# find other words which appear in the same context
text.similar('quasispecies')


# ### Find text pattern with NLTK findall()
# 
# Patterns can be found with the findall() functions; this provides partially the same information as RegEx above, but also has additional options

# #### Different options for finding a regular expression

# In[39]:


# find regular expression
text.findall(r"<immune><response>")


# In[40]:


# find regular expression and context option 1
text.findall(r"<.*><immune><response>")


# In[41]:


# find regular expression and context option 2
text.findall(r"<.*><immune><response><.*>")


# In[42]:


# find expression context
text.findall(r"(<.*>)<immune><response><.*>")


# In[43]:


# find regular expression and one word of context before and after expression
text.findall(r"<..*><immune><response><..*>")


# In[44]:


# find regular expression and two words of context before and after expression
text.findall(r"<.*><.*><immune><response><.*><.*>")


# In[45]:


# find regular expression and context using wildcards
text.findall(r"<.*><.*><.*m.*><response><.*><.*>")


# #### Different options for finding patterns in the text

# In[46]:


# sequence of three equal first letters starting with t
text.findall(r"<t.*>{3,}")


# In[47]:


# sequence of two equal first letters starting with e
text.findall(r"<e.*>{2,}")


# In[48]:


# sequence of two words ending on 'nd'
text.findall(r"<.*nd>{2,}")


# In[49]:


# sequence of two words containing 'nd'
text.findall(r"<.*nd.*>{2,}")


# In[50]:


# find two directly adjacent words
text.findall(r"<\w*> <and> <the> <\w*>")


# In[51]:


# find two words  with a word in between
text.findall(r"<the> <\w*> <immune> <\w*>")


# In[52]:


# find two words with two words in between
text.findall(r"<the> <\w*> <\w*> <immune> <\w*>")


# In[53]:


# find all digits
text.findall("<\d>")

