# importing pandas library 
import pandas as pd 
# importing matplotlib library 
import matplotlib.pyplot as plt 
  
# creating dataframe 
df = pd.DataFrame({ 
    'Object': [24, 23, 29, 24], 
    'Price': [24, 23, 29, 24] 
}) 
  
# plotting a pie chart 
plt.pie(df["Price"], labels=df["Object"]) 
plt.show() 