# FIFA World Cup 2018 Visualization Project

<p align="center">
<img src="https://raw.githubusercontent.com/berkanyuce/FIFA-World-Cup-2018-Visualization/main/data/images/App%20Logo/app_logo-v3.png" width="250" height="250" align="center">
<a href="https://share.streamlit.io/berkanyuce/fifa-world-cup-2018-visualization/main/codes/sidebar.py"><br><br>Demo</a>
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

This project created for visualize FIFA World Cup 2018 datas which collected from Statsbomb. In this project, you can analyze matches, players and teams. 

There is only one match analyze in beta version. (France 4-2 Croatia, Final match) You can look **lineups**, **goals**, **heat maps**, **pass maps**, **shot maps**, **xG graphs**, **pass networks**.

Purpose of beta, see the main issues and performance of project.
### Built With
* [Streamlit](https://streamlit.io)

### Libraries Used
* [Statsbomb Open Data](https://github.com/statsbomb/open-data)
* [MPL Soccer](https://mplsoccer.readthedocs.io/en/latest/index.html)
* [Matplotlib](https://matplotlib.org)
* [Seaborn](https://seaborn.pydata.org)
* [Pandas](https://pandas.pydata.org)
* [Numpy](https://numpy.org)

# Getting Started
During in the beta, the project works for only one match.

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

# Usage
During in the beta, the project works for only final match. To run it follow these introductions on sidebar which is placed at left side:

Match Analyze &rarr; Final Match &rarr; France 4-2 Croatia 

<img width="329" alt="Ekran Resmi 2021-08-18 20 46 18" src="https://user-images.githubusercontent.com/61622650/129946951-88eb2152-2889-4a2a-8aae-f3c761252e6b.png">

After that, you can select visualization type from header menu. The options are **lineups**, **goals**, **heat maps**, **pass maps**, **shot maps**, **xG graphs**, **pass networks**. Pass networks and shot maps placed in **Compare Type** menu.

<img width="997" alt="Ekran Resmi 2021-08-18 20 47 51" src="https://user-images.githubusercontent.com/61622650/129947072-9455be93-a6cb-4950-b175-a31954ec6698.png">

# Roadmap
Because of beta, there are many technical, performance and visual issues on project. I add the other features as soon as possible.

# Contact
I am open to advices. Please contact me.

Berkan Yuce - contact@berkanyuce.com - [Linkedin](https://www.linkedin.com/in/berkanyuce/)

# Acknowledgements
* [Statsbomb](https://statsbomb.com)
* [McKay Johns](https://t.co/YjZoakacqm?amp=1)
* [Friends of Tracking](https://www.youtube.com/channel/UCUBFJYcag8j2rm_9HkrrA7w)
