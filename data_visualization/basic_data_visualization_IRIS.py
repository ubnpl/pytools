#!/usr/bin/env python
# coding: utf-8

# **Data Literacy: needs and competencies** 
# &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
# **Building a digital toolbox for scientific data handling**  
# 7th National Meet&Greet of Swiss Medical Librarians 
# &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp;
# Jupyter-Notebook to Basic Data Visualization Methods 
# 3 September 2020 
# &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
# Author: Michael Horn

# ---

# # Basic Data Visualization Methods

# This Notebook will present some basic methods to visualize data. It uses the open source programming language   
# - **Python, version 3.7**  
# 
# and the open source Python-libraries  
# - **matplotlib** and
# - **pandas**. 
# 
# In a first step we import the required libraries:

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd


# ## 1. The Data Set

# In this Notebook we are using a data set classically employed for data analysis and visualization tasks, the **Iris data set**. 
# You can download it for example from the **UCI Machine Learning Repository** (https://archive.ics.uci.edu/ml/datasets/Iris) and then save it as a .csv-file on your computer. This data set is ideal for introducing basic data visualization techniques. 

# The UCI Machine Learning Repository provides some information about the Iris data set: it has 150 data points with
# 4 attributes and 3 classes (species).
#   
# The **attribute names** are:  
# - sepal length in cm 
# - sepal width in cm
# - petal length in cm
# - petal width in cm
#   
# The **species names** are:  
# - Iris Setosa
# - Iris Versicolour
# - Iris Virginica

# ## 2. The Iris Data Set in a Pandas Data Frame

# In order to work with the data set, we load the data in a **pandas data frame**. A pandas dataframe is a data structure, that makes data processing and visualization very efficient and user friendly.

# Data in a pandas dataframe is organized in rows an columns. In case of the data set we use, we are free to assign the column names.

# In[2]:


# We read the iris-dataset from the .csv-file and define a pandas-dataframe:
dataframe = pd.read_csv("iris_dataset.csv", names=["sepal_length (cm)","sepal_width (cm)", "petal_length (cm)",
                                                   "petal_width (cm)","species"])


# Now we can look at the data set in the data frame:

# In[3]:


# First we set the display option so that we can see all rows:
pd.set_option("display.max_rows", None)
# Then we look at the data frame:
dataframe


# ## 3. Data Visualization: Scatter Plots

# **Scatter plots** visualize data in a very comprehensive way. Every data point is reflected as a dot in a 2- or 3-dimensional diagram. 

# In a typical 2-dimensional scatter plot, two columns of a data set are plotted, one on the x-axis, the other o the y-axis.   
# The diagram below shows a plot of the first two columns of the Iris data set ("sepal_length (cm)" and "sepal_width (cm)"). So far, the different Iris species are not reflected by the data visualization. 

# In[4]:


# Generates a figure ("fig") of a certain size ("figsize"), which can contain sub-figures ("ax"), arranged in rows ("nrows") and
# columns ("ncols").
fig, ax = plt.subplots(figsize=(4,4), nrows=1, ncols=1)

# Defines a plot ("scatter_plot") by applying the method "plot" to our data frame ("dataframe") using the following parameters:
# - "x" and "y": the columns containing the data to be plotted. One can specify the column name (e.g. x="sepal_length (cm)") 
#   or the column index number (e.g x=0 (Python starts counting at 0, not at 1))
# - "kind": the type of plot, a scatter plot in this case
# - "color": the color of the data dots
# - "s": the size of the data dots
scatter_plot = dataframe.plot(ax=ax, x="sepal_length (cm)", y="sepal_width (cm)", kind="scatter", color="green", s=60)

# The method "set_title" sets the plot title and defines the letter size ("fontsize"), color, letter weigth ("fontweight") 
# and the title distance to the axis ("pad"). 
scatter_plot.set_title("Scatter Plot", fontsize=18, pad=10, color="black", fontweight="bold")

# The methods "set_xlabel" and "set_ylabel" set the labels for the x- and y-axis. The label distance to the axis 
# is defined by the parameter "labelpad".
scatter_plot.set_xlabel("sepal length (cm)", fontsize=16, fontweight="light", labelpad=8)
scatter_plot.set_ylabel("sepal width (cm)", fontsize=16, fontweight="light", labelpad=8)

# The method "tick_params" allows to adjust the tick parameters and define for example the size of the ticks.
# "axis": the axis, where the ticks to be adjusted are located
# "labelsize": tick size
scatter_plot.tick_params(axis="both", labelsize=14)

# Displays the visualization result.
plt.show()


# In order to visualize the data with respect to the three different Iris species, we use the pandas **grouby**-method. This method allows us to access the data in a clustered way, groups being specified by the species names. 

# In[5]:


fig, ax = plt.subplots(figsize=(4,4), nrows=1, ncols=1)

# Generates the grouped data frame:
grouped_dataframe = dataframe.groupby("species")

# Generates a dictionary, that attributes a colour to each Iris species: 
colors = {"Iris-setosa":"red", "Iris-versicolor":"blue", "Iris-virginica":"green"}

# Accesses the key (in this case the "species" column) and the data (the other columns of the Iris data set) of the 
# grouped data frame. 
for key, data in grouped_dataframe:
    
    # Defines a plot as described above. The parameter "Label" uses the key of the grouped data frame as species name.
    # The parameter "color" uses the colours listed in the dictionary "colors" to stain the data points according to the
    # Iris species.
    # Note that the plotted columns (x and y) are now specified by their index number (0 and 1), and not by the 
    # corresponding column name in the pandas dataframe.
    sl_sw_species = data.plot(ax=ax, x=0, y=1, kind="scatter", label=key, color=colors[key], s=60)
    
    sl_sw_species.set_title("Scatter Plot", fontsize=18, pad=10, color="black", fontweight="bold")
    sl_sw_species.set_xlabel("sepal length (cm)", fontsize=16, fontweight="light", labelpad=8)
    sl_sw_species.set_ylabel("sepal width (cm)", fontsize=16, fontweight="light", labelpad=8)
    sl_sw_species.tick_params(axis="both", labelsize=14)
    # The method "legend" automatically generates the legend of a plot. We can adjust parameters such as the legend location
    # "loc". When set to "best", the legend will be placed at the optimal position in the plot.
    sl_sw_species.legend(loc="best")

plt.show()


# A common way to visualize multidimensional data completely when using scatter plots is to visualize the data of two columns each for all possible combinations of columns. In our case the combinations would be:
# - sepal length and sepal width
# - sepal length and petal length
# - sepal length and petal width
# - sepal width and petal length
# - sepal width and petal width
# - petal length and petal width

# The diagram below shows a set of scatter plots that visualizes the entire Iris data set with respect to the differences between the Iris species:

# In[6]:


# Generates a figure with 6 subplots located on a grid with 2 rows and 3 columns
fig, axes = plt.subplots(figsize=(18,9), nrows=2, ncols=3)

# Defines the space between the individual subplots
plt.subplots_adjust(left=None, right=None, bottom=None, top=None, wspace=0.3, hspace=0.4)

colors = {"Iris-setosa":"red", "Iris-versicolor":"blue", "Iris-virginica":"green"}

grouped_dataframe = dataframe.groupby("species")

for key, data in grouped_dataframe:
    
    # "axes[p,q]": defines the location of the subplot on the grid. 
    # "p": row number on grid. 
    # "q": column number on grid.
    sl_sw = data.plot(ax=axes[0,0], x=0, y=1, kind="scatter", label=key, color=colors[key], s=60)
    sl_sw.set_xlabel("sepal length (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sl_sw.set_ylabel("sepal width (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sl_sw.tick_params(axis="both", labelsize=14)
    sl_sw.legend(loc="best")
    
    # The methods are now applied to all combinations of columns:
    
    sl_pl = data.plot(ax=axes[0,1], x=0, y=2, kind="scatter", label=key, color=colors[key], s=60)
    sl_pl.set_xlabel("sepal length (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sl_pl.set_ylabel("petal length (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sl_pl.tick_params(axis="both", labelsize=14)
    sl_pl.legend(loc="best")
    
    sl_pw = data.plot(ax=axes[0,2], x=0, y=3, kind="scatter", label=key, color=colors[key], s=60)
    sl_pw.set_xlabel("sepal length (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sl_pw.set_ylabel("petal width (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sl_pw.tick_params(axis="both", labelsize=14)
    sl_pw.legend(loc="best")
    
    sw_pl = data.plot(ax=axes[1,0], x=1, y=2, kind="scatter", label=key, color=colors[key], s=60)
    sw_pl.set_xlabel("sepal width (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sw_pl.set_ylabel("petal length (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sw_pl.tick_params(axis="both", labelsize=14)
    sw_pl.legend(loc="best")
    
    sw_pw = data.plot(ax=axes[1,1], x=1, y=3, kind="scatter", label=key, color=colors[key], s=60)
    sw_pw.set_xlabel("sepal width (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sw_pw.set_ylabel("petal width (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sw_pw.tick_params(axis="both", labelsize=14)
    sw_pw.legend(loc="best")
    
    pl_pw = data.plot(ax=axes[1,2], x=2, y=3, kind="scatter", label=key, color=colors[key], s=60)
    pl_pw.set_xlabel("petal length (cm)", fontsize=16, fontweight="bold", labelpad=8)
    pl_pw.set_ylabel("petal width (cm)", fontsize=16, fontweight="bold", labelpad=8)
    pl_pw.tick_params(axis="both", labelsize=14)
    pl_pw.legend(loc="best")
    
plt.show()


# An alternative way to visualize a multidimensional data set in a scatter plot is to represent a specific attribute (that is the data in a specific column) as feature of the dot size.  
# Below, we visualize the entire Iris data set in just two subplots, using the attributes "sepal length (cm)" and "sepal width (cm)" to define the axes and the attributes "petal length (cm)" and "petal width (cm)" to define the sizes of the dots.

# In[7]:


fig, axes = plt.subplots(figsize=(18,4), nrows=1, ncols=2)

plt.subplots_adjust(left=None, right=None, bottom=None, top=None, wspace=0.2, hspace=0.4)

colors = {"Iris-setosa":"red", "Iris-versicolor":"blue", "Iris-virginica":"green"}

grouped = dataframe.groupby("species")

for key, group in grouped:
    
    # note that "s" is now a function of the variable "petal_length (cm)"
    # "alpha": transparency level of the dots.
    sl_sw_pl = group.plot(ax=axes[0], x=0, y=1, kind="scatter", label=key, color=colors[key], s=100*group["petal_length (cm)"], 
                          fontsize=12, alpha=0.3)
    sl_sw_pl.set_title("Dot Size relative to Petal Length", fontsize=18, pad=12, color="black", fontweight="bold")
    sl_sw_pl.set_xlabel("sepal length (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sl_sw_pl.set_ylabel("sepal width (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sl_sw_pl.tick_params(axis="both", labelsize=14)
    sl_sw_pl.legend(scatterpoints=1, loc="best", markerscale=1)
    
    sl_sw_pw = group.plot(ax=axes[1], x=0, y=1, kind="scatter", label=key, color=colors[key], s=100*group["petal_width (cm)"], 
                          fontsize=12, alpha=0.3)
    sl_sw_pw.set_title("Dot Size relative to Petal Width", fontsize=18, pad=12, color="black", fontweight="bold")
    sl_sw_pw.set_xlabel("sepal length (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sl_sw_pw.set_ylabel("sepal width (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sl_sw_pw.tick_params(axis="both", labelsize=14)
    sl_sw_pw.legend(loc="best")
    
plt.show()


# ## 4. Data Visualization: Histograms

# **Histograms** visualize data according to a frequency distribution. The data set is represented by a series of intervals called **bins**. These intervals reflect the amount of data points exhibiting certain numeric values. 

# **Binning** has an effect upon data representation. Depending on the amount of **bins** chosen (that is: the amount of valid intervals for data representation), the histogram will look differently.

# The following diagramm shows the effect of binning for the visualization of the Iris data in column "sepal_length (cm)". Note that the generation of a histogram only requires minor changes in the code previously used for the generation of scatter plots. 

# In[8]:


fig, axes = plt.subplots(figsize=(20,10), nrows=2, ncols=2)

plt.subplots_adjust(left=None, right=None, bottom=None, top=None, wspace=0.4, hspace=0.5)

colors = {"Iris-setosa":"red", "Iris-versicolor":"blue", "Iris-virginica":"green"}

grouped_dataframe = dataframe.groupby("species")

for key, data in grouped_dataframe:
    
    # The data column to be visualized is accessed in "data" (e.g. "sepal_length (cm)").
    # "kind": note that the plotting type has changed to "hist", since we now plot histograms.
    # "alpha": transparency level of the histograms.
    # "bins": number of bins.
    sl_h_5 = data["sepal_length (cm)"].plot(ax=axes[0,0], kind="hist", label=key, color=colors[key], alpha=0.5, bins=5)
    sl_h_5.set_title("Bins: 5", fontsize=18, pad=10, color="black", fontweight="bold")
    sl_h_5.set_xlabel("sepal length (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sl_h_5.set_ylabel("Frequency", fontsize=16, fontweight="bold", labelpad=8)
    sl_h_5.tick_params(axis="both", labelsize=14)
    sl_h_5.legend(loc="best")
    
    sl_h_10 = data["sepal_length (cm)"].plot(ax=axes[0,1], kind="hist", label=key, color=colors[key], alpha=0.5, bins=10)
    sl_h_10.set_title("Bins: 10", fontsize=18, pad=10, color="black", fontweight="bold")
    sl_h_10.set_xlabel("sepal length (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sl_h_10.set_ylabel("Frequency", fontsize=16, fontweight="bold", labelpad=8)
    sl_h_10.tick_params(axis="both", labelsize=14)
    sl_h_10.legend(loc="best")
    
    sl_h_15 = data["sepal_length (cm)"].plot(ax=axes[1,0], kind="hist", label=key, color=colors[key], alpha=0.5, bins=15)
    sl_h_15.set_title("Bins: 15", fontsize=18, pad=10, color="black", fontweight="bold")
    sl_h_15.set_xlabel("sepal length (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sl_h_15.set_ylabel("Frequency", fontsize=16, fontweight="bold", labelpad=8)
    sl_h_15.tick_params(axis="both", labelsize=14)
    sl_h_15.legend(loc="best")
    
    sl_h_20 = data["sepal_length (cm)"].plot(ax=axes[1,1], kind="hist", label=key, color=colors[key], alpha=0.5, bins=20)
    sl_h_20.set_title("Bins: 20", fontsize=18, pad=10, color="black", fontweight="bold")
    sl_h_20.set_xlabel("sepal length (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sl_h_20.set_ylabel("Frequency", fontsize=16, fontweight="bold", labelpad=8)
    sl_h_20.tick_params(axis="both", labelsize=14)
    sl_h_20.legend(loc="best")
    
plt.show()


# ## 5. Data Visualization: Kernel-Density-Estimation Plots (KDE-Plots)

# **Kernel-Density-Estimation Plots (KDE-Plots)** are closely related to histograms. Unlike histograms, however, KDE-Plots enable data representation using continuous curves. KDE-Plots are based on specific statistical methods required to calculate the shapes of the curves.

# In[9]:


fig, axes = plt.subplots(figsize=(20,5), nrows=1, ncols=2)

colors = {"Iris-setosa":"red", "Iris-versicolor":"blue", "Iris-virginica":"green"}

grouped_dataframe = dataframe.groupby("species")

for key, data in grouped_dataframe:
    
    # "kind": note that the plotting type is now "kde".
    sl_kde = data["sepal_length (cm)"].plot(ax=axes[0], kind="kde", label=key, color=colors[key])
    sl_kde.set_title("KDE-Plot", fontsize=18, pad=10, color="black", fontweight="bold")
    sl_kde.set_xlabel("sepal length (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sl_kde.set_ylabel("Density", fontsize=16, fontweight="bold", labelpad=8)
    sl_kde.tick_params(axis="both", labelsize=14)
    sl_kde.legend(loc="best")
    
    sl_kde_hist = data["sepal_length (cm)"].plot(ax=axes[1], kind="kde", label=key, color=colors[key])
    sl_kde_hist.set_title("Combined Histogram and KDE-Plot", fontsize=18, pad=10, color="black", fontweight="bold")
    sl_kde_hist.set_xlabel("sepal length (cm)", fontsize=16, fontweight="bold", labelpad=8)
    sl_kde_hist.set_ylabel("Density", fontsize=16, fontweight="bold", labelpad=8)
    sl_kde_hist.tick_params(axis="both", labelsize=14)
    # The method "hist" generates a histogram of the specified dataframe and includes it into the corresponding KDE-Plot.
    # "fill": fills the histogramm.
    # "alpha": transparency level of the histogram.
    # "density": returns a probability density, integrating the area under the histogram to 1.
    sl_kde_hist.hist(data["sepal_length (cm)"], fill = True, alpha = 0.3, color = colors[key], density=True)
    sl_kde_hist.legend(loc="best")

plt.show()


# ## 6. Data Visualization: Boxplots

# **Box Plots** are used in descriptive statistics. They visualize data by displaying five key features of a data set:  
# - **minimum** (minimal value of the data set excluding outliers)
# - **maximum** (maximal value of the data set excluding outliers)
# - **median** (middle value of the data set)
# - **first quartile** (median of the lower half of the data set)
# - **third quartile** (median of the higher half of the data set)
# 
# The first and third quartile represent the lower and upper edges of the **box**. The upper and lower **caps** display the maximum and minimum. The **whiskers** connect the box-edges to the caps.  
# 
# Box plots are often used to compare data distribution between different groups of data. In case of the Iris data set, box plots show very nicely how the sizes of the different leaves differ between the Iris species.

# In[10]:


# Defines layout features of the boxplots.
boxprops = dict(linestyle='-', linewidth=2)                                   # layout features of the boxes ar defined.
medianprops = dict(linestyle='-', linewidth=2)                                # layout features of the median lines ar defined.
whiskerprops = dict(linestyle='-', linewidth=2)                               # layout features of the whisker lines ar defined.
capprops = dict(linestyle='-', linewidth=2)                                   # layout features of the cap lines ar defined.
flierprops = dict(marker='o', markerfacecolor='none', markersize=8)           # layout features of the outliers ar defined.
color = dict(boxes="Green", whiskers="Orange", medians="Blue", caps="Gray")   # boxplot colours are defined


# In[11]:


fig, axes = plt.subplots(figsize=(20,10), nrows=2, ncols=2)

plt.subplots_adjust(left=None, right=None, bottom=None, top=None, wspace=0.4, hspace=0.35)

# The method "boxplot" generates a boxplot of a dataframe. The following parameters are relevant:
# "column": defines the relevant column in the data frame
# "by": groups the data frame according to the categories in the specified column
# "grid": includes a grid if set to "True".
# "showfliers": displays outliers if set to "True".
# "boxprops" etc.: includes the features defined above to the boxplot.
# "patch_artist": filles boxes with colour if set to "True".
sl = dataframe.boxplot(ax=axes[0,0], column="sepal_length (cm)", by="species", grid=False, showfliers=True, color=color,
                       boxprops=boxprops, medianprops=medianprops, whiskerprops=whiskerprops, capprops=capprops, 
                       flierprops=flierprops, patch_artist=False)
sl.set_title("Sepal length", fontsize=18, pad=10, color="black", fontweight="bold")
sl.set_xlabel(" ")
sl.set_ylabel("Size (cm)", fontsize=16, fontweight="bold", labelpad=8)
# The method "set_xticklabels" allows to set the ticklabels on the x-axis.
sl.set_xticklabels(["Iris setosa", "Iris versicolor", "Iris virginica"])
sl.tick_params(axis="both", labelsize=16)
# The method "get_figure().suptitle" adjusts the subtitles in the boxplot. In this case it removes automatically generated 
# subtitles.
sl.get_figure().suptitle('')

sw = dataframe.boxplot(ax=axes[0,1], column="sepal_width (cm)", by="species", grid=False, showfliers=True, color=color,
                       boxprops=boxprops, medianprops=medianprops, whiskerprops=whiskerprops, capprops=capprops, 
                       flierprops=flierprops)
sw.set_title("Sepal width", fontsize=18, pad=10, color="black", fontweight="bold")
sw.set_xlabel(" ")
sw.set_ylabel("Size (cm)", fontsize=16, fontweight="bold", labelpad=8)
sw.set_xticklabels(["Iris setosa", "Iris versicolor", "Iris virginica"])
sw.tick_params(axis="both", labelsize=16)
sw.get_figure().suptitle('')

pl = dataframe.boxplot(ax=axes[1,0], column="petal_length (cm)", by="species", grid=False, showfliers=True, color=color,
                       boxprops=boxprops, medianprops=medianprops, whiskerprops=whiskerprops, capprops=capprops, 
                       flierprops=flierprops)
pl.set_title("Petal length", fontsize=18, pad=10, color="black", fontweight="bold")
pl.set_xlabel(" ")
pl.set_ylabel("Size (cm)", fontsize=16, fontweight="bold", labelpad=8)
pl.set_xticklabels(["Iris setosa", "Iris versicolor", "Iris virginica"])
pl.tick_params(axis="both", labelsize=16)
pl.get_figure().suptitle('')

pw = dataframe.boxplot(ax=axes[1,1], column="petal_width (cm)", by="species", grid=False, showfliers=True, color=color,
                       boxprops=boxprops, medianprops=medianprops, whiskerprops=whiskerprops, capprops=capprops, 
                       flierprops=flierprops)
pw.set_title("Petal width", fontsize=18, pad=10, color="black", fontweight="bold")
pw.set_xlabel(" ")
pw.set_ylabel("Size (cm)", fontsize=16, fontweight="bold", labelpad=8)
pw.set_xticklabels(["Iris setosa", "Iris versicolor", "Iris virginica"])
pw.tick_params(axis="both", labelsize=16)
pw.get_figure().suptitle('')

plt.show()


# ---

# # Appendix: Additional Data Visualization Techniques

# This section aims to illustrate additional data visualization techniques. Being "under construction", the code is not fully commented yet.

# ## Data Visualization using **Seaborn**

# **Seaborn** is a library that builds on **matplotlib**. It enables a beautiful and user friendly visualization of **pandas** dataframes. User friendliness results from the substantially reduced amount of code required for the generation of certain plots.   

# Before working with **seaborn**, we need to import it.

# In[12]:


import seaborn as sns


# **Pairplots** automatically plot all possible attribute combinations of multidimensional data in a matrix of scatter plots. The diagonal visualizes a distribution function of the corresponding variable, for example a histogram or a KDE-Plot.  

# With basically 2-3 lines of code, we obtain a complete visualization of the Iris data set.

# In[13]:


palette = {'Iris-setosa':'red', 'Iris-versicolor':'blue', 'Iris-virginica':'green'}


# In[14]:


sns.pairplot(dataframe, hue="species", palette=palette, height=2, diag_kind="kde")
plt.show()


# ## Alternative Ways to Data Visualization

# With the techniques presented above, we can perform high level data visualization. In Python there usually are many different ways to achieve a certain task. **Seaborn** for instance allows a very fast and user-friendly data visualization approach. Sometimes, however, we might want to have a higher level of control upon our data visualization output. In this case we might want to use alternative methods that are more transparent. These methods usually require more code.   

# Below, there is an example of a combined histogram and KDE-plot that has been generated slightly differently from the methods described above. In this case we use two additional Python libraries, **numpy** and **scipy**.

# We import these libraries:

# In[15]:


import numpy as np
from scipy import stats


# We generate three sub-dataframes (**df_setosa**, **df_virginica**, **df_versicolor**) out of the initial dataframe and avoid using the **groupby**-method that we applied above.

# In[16]:


df_setosa = dataframe[dataframe['species']=='Iris-setosa']
df_virginica = dataframe[dataframe['species']=='Iris-virginica']
df_versicolor = dataframe[dataframe['species']=='Iris-versicolor']


# We now use these sub-dataframes to generate the plot.

# In[17]:


fig, ax = plt.subplots(figsize=(6,4))

kde = stats.gaussian_kde(df_setosa["sepal_length (cm)"])
xs = np.linspace(3.5, 9, num=100)
ys = kde(xs)
ax.plot(xs, ys, color = "darkblue", label = 'Iris Setosa')
ax.hist(df_setosa["sepal_length (cm)"], fill = True, alpha = 0.2, histtype = "step", color = "darkblue", bins = 10,
        density = True)
plt.fill_between(xs,ys, color = "darkblue", alpha = 0.2)

kde = stats.gaussian_kde(df_virginica["sepal_length (cm)"])
xs = np.linspace(3.5, 9, num=100)
ys = kde(xs)
ax.plot(xs, ys, color = "orange", label = "Iris Virginica")
ax.hist(df_virginica["sepal_length (cm)"], fill = True, alpha = 0.2, histtype = "step", color = "orange", bins = 10,
        density = True)
plt.fill_between(xs,ys, color = "orange", alpha = 0.2)

kde = stats.gaussian_kde(df_versicolor["sepal_length (cm)"])
xs = np.linspace(3.5, 9, num=100)
ys = kde(xs)
ax.plot(xs, ys, color = "green", label = "Iris Versicolor")
ax.hist(df_versicolor["sepal_length (cm)"], fill = True, alpha = 0.2, histtype = "step", color = "green", bins = 10,
        density = True)
plt.fill_between(xs,ys, color = "green", alpha = 0.2)

plt.legend()
plt.xlabel("Sepal Length (cm)", fontsize=14, fontweight="bold")
plt.ylabel("Density", fontsize=14, fontweight="bold")
plt.title("Sepal Length: KDE and Histo-Plot", fontsize=16, pad=10, color="black", fontweight="bold")

plt.show()


# In[ ]:




