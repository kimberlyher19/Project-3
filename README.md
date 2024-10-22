# __Project 3__

# Group 5: Adolphus Momoh Jr, Dylan Phimister, Kimberly Her, Sanjana Prabhakar, and Viktor Bondarenko 

## Description: 

The Spotify Popularity Analysis Project investigates the characteristics of the most and least popular songs on Spotify. Specifically, this project compares the top 10% and bottom 10% of songs in terms of popularity, focusing on features like loudness and valence. By understanding how these musical attributes correlate with popularity, we aim to uncover patterns that can help predict the success of future tracks.

## Visuals: 

### Top 10 Artists by Number of Songs: 
![alt text](<Visuals_PNG(use _for_README)/Top_10_Artists_by_Number_of_Songs.png>)

This bar chart visualizes the top 10 artists with the most songs in the dataset. Each bar represents an artist, with the height of the bar corresponding to the total number of songs they have contributed to the dataset. This chart helps you quickly identify which artists are most prolific in terms of the number of songs they have in the dataset. It is useful for understanding the concentration of music production among top artists.

### Top 10 Artists by Number of Songs and Average Popularity: 
![alt text](<Visuals_PNG(use _for_README)/Top_10_Artists_by_Number_of_Songs_and_Popularity.png>)

This chart compares the top 10 artists in terms of both the number of songs they have and their average popularity score. Each artist is represented by two bars: one showing the number of songs and another showing their average popularity score. The chart helps to see not only which artists have the most songs but also whether they are popular on average. This gives a balanced view of both the quantity and the quality (in terms of popularity) of the songs contributed by the top 10 artists. You can identify whether prolific artists also tend to have higher popularity or not.

### Average Danceability and Energy of Top 10 Artists: 
![alt text](<Visuals_PNG(use _for_README)/Danceability_and_Energy.png>)

This visualizes the average danceability and energy scores for the top 10 artists. The bars represent the  artist, plotted based on their average danceability and energy. 

### Song Genres Distrbution: 
![alt text](<Visuals_PNG(use _for_README)/Song_Genres_Distribution.png>)

This chart displays the distribution of different genres within the dataset. This visualization gives an overview of the diversity of genres present in the dataset. Larger slices indicate genres that dominate the dataset, while smaller slices represent more niche genres

### Genre Distribution of Pop and Hip Hop: 
![alt text](<Visuals_PNG(use _for_README)/Genre_Distribution_of_Selected_Artists.png>)

Compares the distribution of songs across subgenres within the Pop and Hip Hop genres. The chart provides a deeper dive into the diversity within the Pop and Hip Hop genres. 

### Song Popularity Trends by Year for Top 10 Artists: 
![alt text](<Visuals_PNG(use _for_README)/Song_Popularity_Trends.png>)

This line chart tracks the popularity of songs over time for the top 10 artists. Each line represents an artist, and the y-axis reflects the average song popularity, while the x-axis shows the release years of the songs. This visualization reveals the trajectory of each artist's popularity over the years. By examining the trends, you can see if an artist's music has gained or lost popularity over time. It highlights the evolution of music preferences and artist success throughout different periods.

### Average Tempo Distribution by Genre: 
![alt text](<Visuals_PNG(use _for_README)/Average_Tempo_Distribution_by_Genre.png>)

This pie chart shows the proportion of different genres based on their average tempos. Each slice represents a genre, and the size of the slice corresponds to the average tempo of that genre relative to others. This visualization highlights which genres have higher average tempos. You can quickly identify if a genre is more characterized by fast-paced music (e.g., electronic genres) or slower rhythms (e.g., ballads).

### Top 10% Most Popular Songs: Loudness vs Valence: 
![alt text](<Visuals_PNG(use _for_README)/Top_10_Percent.png>)

This scatter plot shows the relationship between loudness (in decibels) and valence (a measure of musical positivity) for the top 10% most popular songs. Each point represents a song, and the size and shade of the points correspond to the song's popularity. Darker and larger points indicate higher popularity.

### Bottom 10% Most Popular Songs - Loudness vs. Valence: 
![alt text](<Visuals_PNG(use _for_README)/Bottom_10_Percent.png>)

This scatter plot shows the relationship between loudness and valence for the bottom 10% least popular songs. The plot follows a similar format as the previous chart but focuses on the least popular tracks.

## Dependecies and Libraries:
- Numpy as np
- Pandas as pd
- Matplotlib.pyplot as plt
- os
- Seaborn as sns
- Pymongo -> MongoClient
- Bokeh.io -> show
- Bokeh.plotting -> figure
- Bokeh.transform -> cumsum
- Bokeh.palettes -> Category20c
- Math -> pi
- Plotly.express as px

## Installation
1. Clone the repository 
2. Create a virtual environment
3. Install the required packages
4. Run the Jupyter Notebook

## Usage 
Data Analysis: The notebook contains multiple sections, each focusing on a different aspect of song popularity analysis. Run the cells sequentially to see the visualizations and outputs.

Visualizations: You can explore each chart interactively, zoom in on the scatter plots, and analyze key trends.

# Support 
For support, please reach out via GitLab’s issue tracker for this project. For technical assistance related to MongoDB, Python, or Plotly, refer to the documentation of each tool

# Roadmap
## Future improvements to this project include:

Expanding Dataset: Incorporating more genres and songs for deeper insights.

Additional Visualizations: Analyzing other song features like acousticness, liveness, and instrumentalness.

Machine Learning: Building predictive models to forecast a song's popularity based on its characteristics.

# Acknoweledgements 
This project was made possible through the collaborative efforts of an exceptional team. Special thanks to all the teammates who contributed their time and expertise to different aspects of the project, from data cleaning and storage to interactive visualizations and overall analysis. We would also like to extend our appreciation to the University of Minnesota's Data Analytics Bootcamp for providing guidance and support throughout this process. Additionally, the use of several key open-source libraries, including Pandas, Plotly, and MongoDB, played a crucial role in the successful completion of this project. Thank you all for your invaluable contributions. 


# References
The Spotify "Top Hits Spotify from 2000-2019" dataset is from Kaggle, reference the link here: https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019.

Codes were referenced from class activities and we used ChatGPT when our codes weren't running properly. 

# Project Status
This project is complete. All deliverables, including data analysis, visualizations, and documentation, have been successfully implemented. Future improvements and optimizations may be explored, but for now, the core objectives have been fully achieved.



