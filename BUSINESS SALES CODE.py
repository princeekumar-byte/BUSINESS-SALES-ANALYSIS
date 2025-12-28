import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(
    r"C:\Users\princ\OneDrive\문서\practice folder\archive\Business_sales_EDA.csv", 
    sep=';', 
    usecols=['Promotion', 'currency', 'Seasonal', 'Product Category', 'Product ID', 'brand', 'name', 'price', 'material', 'Product Position', 'Sales Volume']
)

group_data=data.groupby('Promotion')['Sales Volume'].mean().plot(kind='bar')
plt.show()

group_data=(data.groupby('Product Position')['Sales Volume'].sum()).plot(kind='pie')
plt.show()

data['revenue'] = data['price'] * data['Sales Volume']
total_by_name=data.groupby('name')['revenue'].sum().sort_values(ascending=False).plot(kind='hist')
plt.show()

data['material sales']=(data.groupby('material')['price'].transform('sum')).plot(kind='line')
plt.show()