# Project title: carbon_on_the_plate
Exploratory Data Analysis (EDA) and statistical testing of Green House Gas (GHG) emissions in the food supply chain using Python, Pandas, and Scipy.

# Project overview
Data has been collected from Kaggle.com then be processed and visualised with Python and its libraries. The analysis aims to examine food production with significant or marginal carbon footprint then analyse stages in agri-food supply chain and its contribution to the total GHG emissions. 

# Business questions
Stage 1: Total Emissions rankings
- Which are the lowest-emitting food products?
- Which are the highest-emitting food products? 
Stage 2: Agro-chain structural analysis
- What are the most dominant stages in creating GHG emissions?
- Which stages contribute the least GHG emissions?
Stage 3: Agri-chain correlation analysis
- What is the ratio between the upstream and downstream phases?

# Data description
The dataset contains 43 records of food product and 9 variables (order and category).

# Tools and technologies
- Python (pandas, matplotlib, sciPy)
- VS Code
- Jupyter Notebook

# Insights
- Ruminant food production is the highest emitters and plant-based foods are the lowest emitters.
- Farming practices produce the highest volume of emissions while retail contributes the least.
- Upstream phase is mainly responsible for the carbon emissions instead of downstream phase.

# Project structure
carbon_on_the_plate/  
├── data/&nbsp;&nbsp;&nbsp;&nbsp; # Data storage\
│&nbsp;├── raw/&nbsp;&nbsp;&nbsp;# Original, immutable data\
│&nbsp;└── processed/&nbsp;&nbsp;&nbsp; # Cleaned data used for analysis\
├── notebooks/&nbsp;&nbsp;&nbsp; # Jupyter Notebooks\
│&nbsp;└── data_visualisation.ipynb
├── reports/ &nbsp;&nbsp;&nbsp;&nbsp;# Saved results\
├── README.md &nbsp;&nbsp;&nbsp;&nbsp; # Project overview and "The Story"\      
├── src/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Cleaning data Python script\
&nbsp;└── data_cleaning.py
  
# Limitations
- Limited availability: A number of variables were removed due to high proportion of missing values. Consequently, the analysis focuses on a reduced set of indicators and cannot examine additional environmental aspects.
- Small sample size: The dataset contains only 43 observations, which limits statistical power and the generalizability of results.
- Potential bias from data cleaning when removing variables with missing values.
- Descriptive analysis only: observed relationships should not be interpreted as causal.
- Lack of automation: the current workflow is exploratory and notebook-based, without reusable or automated data pipeline. 

# Future improvements
- Develop a reusable and automated data pipeline to handle data ingestion, cleaning, validation, and storage.
- Expand the dataset with more observations, time periods, or geographic coverage to improve statistical power and generalizability. 
- Apply more advanced statistical methods to move beyond descriptive insights.
- Build an interactive dashboard to improve communication with non-technical audiences.
- Store processed data in relational database (SQL) to support scalable querying and integration with visualisation tools. 
