# Technical Assessment - Data Science Internship - Clermont Foot 63
### Author : Vincent GRAILLAT

## Description

- **Purpose**:
  Create a dashboard to identify the quality of a player in a championship. 

- **Database**:
  Use of the StatsBomb open access database: https://github.com/statsbomb/open-data.

- **Season chosen**:
  This study focuses on the 2015-2016 La Liga season

- **Results displayed**
  The app gives access to different types of informations:
    - **Players Performances**:
      This tab allows you to select a player and then displays 4 barplots showing the selected player's performances in various statistics depending on his position. The value of each statistics his the quantile of the player in this statistics, meaning the percentages of players he is better than in this statistics. The 4 barplots are for the quantiles in total quantities, within all players and within players of the same position, and the quantile in per 90 minutes quantities, within all players and within players of the same position. To complete this analysis, you can the find tables recapitulating the stats of the selected player, at the bottom of the page. 
    - **Players Comparison**:
      This tab allows you to select two players and then shows radar charts of the quantiles of both players. This is done for both total and per 90 minutes quantities. You cannot select a goalkeeper and a field player but you can select two goalkeepers.
    - **Best Players by position**
      This tab allow you to select a position within this list ['Goalkeeper', 'Left/Right Back', 'Center Back', 'Defensive Midfielder', 'Central/Attacking Midfielder', 'Left/Right Winger', 'Striker'] and then displays the 5 best players for this position, and their performances comparad to players playing the same position in a few selected statistics, in the form of the same barplots as in the first tab. To choose the 5 best players, a mean of the quantiles is computed, with weights associated to stats depending on the position.

## Folders and Files

- **data**, **doc** and **img**:
  Contains the original elements from the StatsBomb's Database

- **Dockerfile**:
  Contains the instructions to build the Docker image for the application. It sets up the environment, installs dependencies, and specifies how to run the app.

- **docker-compose.yml**:
  Defines the Docker services, volumes, and network configurations.

- **requirements.txt**:
  Lists the Python dependencies required by the application. These packages will be installed in the Docker image during the build process.

- **Preparation_datasets.ipynb**:
  Jupyter Notebook that extracts all useful data from StatsBomb's files and creates usable datasets for the app. 

- **data_app**:
  Folder containing the datasets created in `Preparation_datasets.ipynb` and saved as CSV files. Those are the datasets used by the web application.

- **app**:
  Folder containing the main script for the web application.
  - **pages**:
    Subfolder within `app` that contains the three pages of the web application. Each page is a separate script that forms part of the overall app.

## Set-up of the app
- **Run docker-compose build**:
  Run  ```docker-compose build ``` in your terminal. This step ensures that all dependencies and configurations are correctly set up within a Docker image. Make sure you are in the right folder, I had issue with the zip extraction creating a new folder.

- **Run docker-compose up**:
  Run  ```docker-compose up ``` in your terminal. This command will start the application defined in the `docker-compose.yml` file.

- **Follow the link**:
  Once the Docker containers are running, you can access the web application through the URL provided in the terminal output (typically `http://localhost:8501`).

## Limits
- **Unclear Statistics**
  There are a few events in StatsBomb database that are not clear. For example, it is quite hard to understand what ball_receipt that are incomplete are, and their link with miscontrol or even dispossessed events. For this reason, it is possible that some statistics are not 100% true to the real statistics

- **Ranking players per position**
  The weights used for the computing of players's quantiles score have not been scientifically thought, and are just meant to reflect what is associated with a good player for a given position. Those weights can be easily improve but by lack of time, they are what they are. 
