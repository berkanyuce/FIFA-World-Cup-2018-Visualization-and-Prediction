# FIFA World Cup 2018 Visualization and Prediction Project

<p align="center">
<img src="https://raw.githubusercontent.com/berkanyuce/FIFA-World-Cup-2018-Visualization/main/data/images/App%20Logo/app_logo-v3.png" width="250" height="250" align="center">
<a href="https://share.streamlit.io/berkanyuce/fifa-world-cup-2018-visualization/main/codes/sidebar.py" target="_blank" rel="noopener noreferrer"><br><br>Click for run project</a>
</p>

**Table of Contents**

<!--ts-->
   * [About The Project](#about-the-project)
      * [Built With](#built-with) 
      * [Libraries Used](#libraries-used)
   * [Getting Started](#getting-started)
      * [Installation](#installation)
      * [Prerequisites](#prerequisites)
   * [Usage](#usage)
   * [Roadmap](#roadmap)
   * [Contact](#contact)
   * [Acknowledgements](#acknowledgements)
<!--te-->

# About The Project
https://user-images.githubusercontent.com/61622650/129944576-86ba076e-d48c-4d42-9f4f-823f307f2d95.mp4

This project was created to visualize the FIFA World Cup 2018 data collected from Statsbomb and predict the last 16 matches. In this project, you can see the visualizations of statistics of the matches and look at the results of the machine learning model made for the tournament.

The visualized statistics are: **lineups**, **goals**, **heat maps**, **pass maps**, **shot maps**, **xG graphs**, **pass networks**.
In addition, the development process of the machine learning model is also visualized.

This is the first version of the project. In the future, improvements can be made to the codes and visualizations.
### Built With
* [Streamlit](https://streamlit.io)

### Libraries Used
* [Statsbomb Open Data](https://github.com/statsbomb/open-data)
* [MPL Soccer](https://mplsoccer.readthedocs.io/en/latest/index.html)
* [Matplotlib](https://matplotlib.org)
* [Seaborn](https://seaborn.pydata.org)
* [Pandas](https://pandas.pydata.org)
* [Numpy](https://numpy.org)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Scikit-Learn](https://scikit-learn.org/stable/)
* [Plotly](https://plotly.com)

# Getting Started
If you want to run the codes on your own computer, you need to download the mandatory libraries. These libraries and how to install them are mentioned below.

<i>The computer used during the development of the project is Macbook Air M1 8GB RAM</i>
### Installation
After clone this project, open terminal and run:

`streamlit run project_directory/sidebar.py`

### Prerequisites
This project uses different libraries. There is a list how to install them.

* Statsbomb Open Data
`pip install statsbombpy`

* Streamlit
`pip install streamlit`

* MPL Soccer
`pip install mplsoccer`

* Matplotlib
`python -m pip install -U pip`
`python -m pip install -U matplotlib`
or install via conda `conda install matplotlib` 

* Seaborn
`pip install seaborn` 

* Pandas
`pip install pandas`

* Numpy
`pip install numpy`

* Plotly
`pip install plotly`

* Scikit-Learn
`pip install -U scikit-learn`

* BeautifulSoup
`pip install beautifulsoup4`

* requests
`pip install requests`

* urllib
`pip install urllib3`

# Usage
The project provides visualizations of all matches and tournament prediction. To run the match visualizations, follow these steps in the left sidebar:

Example,
Match Analyze &rarr; Final Match &rarr; France 4-2 Croatia 

<img width="329" alt="Ekran Resmi 2021-08-18 20 46 18" src="https://user-images.githubusercontent.com/61622650/129946951-88eb2152-2889-4a2a-8aae-f3c761252e6b.png">

After that, you can select visualization type from header menu. The options are **lineups**, **goals**, **heat maps**, **pass maps**, **shot maps**, **xG graphs**, **pass networks**. Pass networks and shot maps placed in **Compare Type** menu.

<img width="997" alt="Ekran Resmi 2021-08-18 20 47 51" src="https://user-images.githubusercontent.com/61622650/129947072-9455be93-a6cb-4950-b175-a31954ec6698.png">

# Roadmap
Future planned developments are as follows: <br>
* Goals Visualization : Display of passes before the goal. <br>
* Pass Network Visualization: Include all passes in the match and resize the nodes. <br>
* Machine Learning Model: Preparing for the 2022 world cup with new datasets.

# Contact
I'm open to advices. Please contact me.

Berkan Yuce <br> contact@berkanyuce.com <br> [Linkedin](https://www.linkedin.com/in/berkanyuce/)

# Acknowledgements
* [Statsbomb](https://statsbomb.com)
* [McKay Johns](https://t.co/YjZoakacqm?amp=1)
* [Friends of Tracking](https://www.youtube.com/channel/UCUBFJYcag8j2rm_9HkrrA7w)
