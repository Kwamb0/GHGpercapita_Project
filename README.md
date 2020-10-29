# Greenhouse Gases Emitted per Capita
<p align="center">
 <img src="images/emissions.jpg">
</p>

# Background

Our goal was to create an interactive dashboard that is able to predict the amount of metric tons of greenhouse gases a county will emit based on their gross domestic product (GDP). Using data from [World Resouces Institute](https://datasets.wri.org/dataset/cait-country) which had data for 187 country's GDP, population, and greenhouse gas emessions from 1990-2012. We were able to create a model based on this data and forecast what a country's potential GHG emissions are based on an inputed GDP. 

# Tools Used
* Python
* HTML
* Flask
* Tableau 
* Javascript
* Heroku

# Process
The first step was to clean and fill in any missing data points from the data set. Some countries (mostly Soviet era countries) were missing GDP data so those points had to be entered manually. Once the data set was cleaned, the data was loaded into Juypter Notebook and a script was created to make a machine learning model (figure 1) that can accurately predict a country's GHG emmissions based on an inputed GDP. Then, using flask, heroku, and javascript we deployed the machine learning model to a webpage. This webpage also includes Tableau visualizations (figure 2) that show trends within the dataset. 

# Figure 1:
<p align="center">
 <img src="images/machine.png">
</p>

# Figure 2: 
<p align="center">
 <img src="images/tableau.png">
</p>

# Results
Our Tableau visualizations provided an easy and unique way to find trends within our data. In figure 3, there is some pretty distinct groupings of countries. One example of this group is the oil producing countries of the Middle East. Those countries were gerenally grouped in the top right of the graph showing they have a high green house gas emission as well as a higher GDP level. The northern European countries were mostly grouped at the bottom right of the graph indicating, they maintain a high GDP per capita while also have very low emission levels. One country, Bhutan, is the only country in the world that is carbon neutral meaning their green house gas emissions are in the negative. In our data set, there was a few other countries that were in the negatives (ex. Serbia) but upon further research, the data set we used had faulty numbers and outside research showed that. 

# Figure 3: 
<p align="center">
 <img src="images/fig3.png">
</p>

# Additional Research for the Future 
