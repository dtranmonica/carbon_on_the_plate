#Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Cleaning the data
#Load and inspect the data
food = pd.read_csv('/Users/macos/Documents/data_projects/food_production_emissions/data/raw/Food_Production.csv')
food.head(10)

#Rename columns
food.columns = [col.strip().lower().replace(' ', '_')
                   .replace('(', '')
                   .replace(')', '')
                   .replace('/', '_')
                   .replace('²', '2')
                   .replace('₄', '4')
                   for col in food.columns]
food.rename(columns = {'packging':'packaging','eutrophying_emissions_per_1000kcal_gpo4eq_per_1000kcal':'eutrophying_per_1000kcal','eutrophying_emissions_per_kilogram_gpo4eq_per_kilogram':'eutrophying_per_kilogram', 'eutrophying_emissions_per_100g_protein_gpo4eq_per_100_grams_protein':'eutrophying_per_100g_protein'}, inplace = True)
food.rename(columns = {'freshwater_withdrawals_per_1000kcal_liters_per_1000kcal':'freshwater_per_1000kcal','freshwater_withdrawals_per_100g_protein_liters_per_100g_protein':'freshwater_per_100g_protein','freshwater_withdrawals_per_kilogram_liters_per_kilogram':'freshwater_per_kilogram'},inplace = True)
food.rename(columns = {'greenhouse_gas_emissions_per_1000kcal_kgco₂eq_per_1000kcal':'greenhouse_per_1000kcal','greenhouse_gas_emissions_per_100g_protein_kgco₂eq_per_100g_protein':'greenhouse_per_100g_protein','land_use_per_1000kcal_m2_per_1000kcal':'land_use_per_1000kcal','land_use_per_kilogram_m2_per_kilogram':'land_use_per_kilogram','land_use_per_100g_protein_m2_per_100g_protein':'land_use_per_100g_protein'}, inplace = True)
food.rename(columns = {'scarcity-weighted_water_use_per_kilogram_liters_per_kilogram':'scarcity-weighted_water_use_per_kilogram','scarcity-weighted_water_use_per_100g_protein_liters_per_100g_protein':'scarcity-weighted_water_use_per_100g_protein','scarcity-weighted_water_use_per_1000kcal_liters_per_1000_kilocalories':'scarcity-weighted_water_use_per_1000kcal'}, inplace = True)


#Check for missing values
print(food.isnull().sum())

#Drop collumns with excessive missing values
food = food.drop(columns = ['eutrophying_per_1000kcal','eutrophying_per_kilogram', 'eutrophying_per_100g_protein','freshwater_per_1000kcal','freshwater_per_100g_protein','freshwater_per_kilogram','scarcity-weighted_water_use_per_kilogram','scarcity-weighted_water_use_per_100g_protein','scarcity-weighted_water_use_per_1000kcal', 'greenhouse_per_1000kcal','greenhouse_per_100g_protein','land_use_per_1000kcal','land_use_per_kilogram','land_use_per_100g_protein'])
print(food.info())

#Fill missing values in 'packaging' column with 'Unknown'
food['packaging'] = food['packaging'].fillna('Unknown')

#Round 'total_emissions' column to two decimal places
food['total_emissions'] = food['total_emissions'].round(2)
print(food.head(20))

#Standardize columns name to snake_case
food.columns = [col.lower().replace(' ','_') for col in food.columns]

#Validate total_emissions values
food['total_emissions'] = (food['land_use_change'] + food['animal_feed'] + food['farm'] + food['processing'] + food['transport'] + food['packaging'] + food['retail'])

#Visual inspection of cleaned data
plt.figure(figsize = (10,6))
plt.hist(food['food_product'], bins = 30, color = 'skyblue', edgecolor = 'black')
plt.title('Distribution of Food Products', fontsize = 16)
plt.xlabel('Food Product', fontsize = 14)
plt.ylabel('Frequency', fontsize = 14)
plt.xticks(rotation = 45)
plt.tight_layout()
#plt.show()

#Save cleaned data to a new CSV file
food.to_csv('/Users/macos/Documents/data_projects/food_production_emissions/data/clean.csv', index = False)
