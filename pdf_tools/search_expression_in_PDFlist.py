
# coding: utf-8

# # Search for expression in a list of PDFs
# 
# Go through a list of PDFs and search for a given expression

# #### Python environment installation instructions
# 
# General Packages:
# 
#     conda install numpy scipy matplotlib jupyter
# 
# Specific packages:
# 
#     conda install tika

# #### Example PDF files
# 
# This example uses 5 PDF files. They can be downloaded from the link list below and should be copied to a folder called 'pdfs' in the working directory. Link list
# 
#     https://doi.org/10.1073/pnas.1117201109
#     https://doi.org/10.1073/pnas.1919182117
#     https://doi.org/10.1073/pnas.1911622116
#     https://doi.org/10.1073/pnas.2000414117
#     https://doi.org/10.1073/pnas.1815432116

# In[1]:


# set path to directory with pdfs
pdf_path = './pdfs/'


# ### Import required packages

# In[2]:


# representation of plots
get_ipython().run_line_magic('pylab', 'inline')


# In[3]:


# import required packages
import os,re
import fnmatch
from tika import parser


# ## Get PDF list
# 
# First we get a list of all pdfs by searching the specified directory for files with the .pdf extension; this could potentially also include subfolders of the given folder path.

# In[4]:


# define search pattern to include files in list
pattern = '*.pdf'


# In[5]:


# find all files in path recursively
file_list = []
for dirpath, dirnames, filenames in os.walk(pdf_path):
    if not filenames:
        continue
    pdf_files = fnmatch.filter(filenames, pattern)
    if pdf_files:
        for file in pdf_files:
            file_list.append('{}/{}'.format(dirpath, file))
            #print('{}/{}'.format(dirpath, file))


# In[6]:


# print the file list with numbers
for num, item in enumerate(file_list):
    print (num, item)


# ## Search regular expression in all PDFs
# 
# Loop over the PDF list and search for a specified expression

# ### Define search pattern and search

# In[7]:


# search pattern
s_pattern = '.*.immune.*.response.*'


# In[8]:


# now we loop over the file list and and store the results
found_num = []    # store number of matches in each file here
found_list = []   # store list of files with matching patterns here
found_obj = []    # store matches here
for n in range (len(file_list)):
    l = file_list[n]
    print (str(n)+' : ',l)
    parsedPDF = parser.from_file(l)
    pdftext = parsedPDF['content']
    findObj = re.findall(s_pattern, pdftext, re.M|re.I)
    found_num.append(len(findObj))
    print('number of matches found in file '+str(n)+': ', len(findObj))
    if len(findObj) > 0:
        found_list.append(l)
        found_obj.append(findObj)


# ### Look at search results

# In[9]:


# List of matching files and search results
for num, item in enumerate(found_list):
    print ('-------------------------------------------------------------------------------------------------')
    print ('file name = ', item)
    for matchtxt in found_obj[num]:
        print (' - ',matchtxt)
    print ('-------------------------------------------------------------------------------------------------')

