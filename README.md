## README.md

### Restaurants Analyse

This repository contains data analysis scripts and notebooks for analyzing restaurant data. The data includes information about various restaurants, such as their names, locations, review counts, ratings, and types.

### Contents

- `G_MAP_DATA/`: This directory contains the dataset used for analysis.
- `analyse.ipynb`: Jupyter Notebook containing data analysis and visualization scripts.
- `combined_data.xlsx`: Excel file containing the combined data from multiple sources.
- `requirements.txt`: Text file listing the required Python packages for running the analysis.

### Getting Started

To run the analysis scripts and notebooks in this repository, follow these steps:

1. Clone this repository to your local machine:

```
git clone https://github.com/Ismat-Samadov/Restaurants_Analyse.git
```

2. Install the required Python packages:

```
pip install -r requirements.txt
```

3. Open the `analyse.ipynb` notebook using Jupyter Notebook or JupyterLab.
4. Run the notebook cells to execute the analysis scripts and visualize the results.

### Data Description

The dataset contains the following columns:

- `name`: Name of the business.
- `latitude`: Latitude coordinate of the business's location.
- `longitude`: Longitude coordinate of the business's location.
- `review_count`: Number of reviews for the business.
- `rating`: Average rating of the restaurant.
- `types`: Type of the business.
- `city`: City where the business is located.

### Analysis Overview

The `analyse.ipynb` notebook contains the following sections:

1. Data Loading and Preprocessing: Load the dataset and perform preprocessing steps such as handling missing values and data cleaning.
2. Exploratory Data Analysis (EDA): Explore the dataset through descriptive statistics, visualizations, and insights about restaurant ratings, review counts, and types.
3. Geospatial Analysis: Visualize the geographical distribution of restaurants using interactive maps.
4. Conclusion: Summarize the key findings and insights from the analysis.

### Contributing

Contributions to this repository are welcome. Feel free to submit bug reports, feature requests, or pull requests.

---

## analyse.ipynb Explanation

The `analyse.ipynb` notebook is a Jupyter Notebook that contains Python code for data analysis and visualization of restaurant data. Here's a breakdown of its contents:

1. **Data Loading and Preprocessing**: This section loads the dataset (`combined_data.xlsx`) into a Pandas DataFrame and performs preprocessing steps such as handling missing values and cleaning the data.

2. **Exploratory Data Analysis (EDA)**: This section explores the dataset through descriptive statistics and visualizations. It includes analyses of restaurant ratings, review counts, and types. Visualizations such as histograms, bar plots, and scatter plots are used to gain insights into the data.

3. **Geospatial Analysis**: This section focuses on visualizing the geographical distribution of restaurants using interactive maps. It utilizes the Folium library to create an interactive map that displays restaurant locations as markers on a map.

4. **Conclusion**: This section summarizes the key findings and insights from the analysis. It provides a concise overview of the main takeaways from the data exploration process.

Overall, the `analyse.ipynb` notebook serves as a comprehensive guide to analyzing and understanding the restaurant data, providing valuable insights for stakeholders in the food industry.