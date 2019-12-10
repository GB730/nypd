import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
from google.oauth2 import service_account
import pandas_gbq
from pylab import rcParams

# Accessing BigQuery from python pandas 
credentials = service_account.Credentials.from_service_account_file(
    r'C:\Users\Ahmad\Desktop\Python\19FA Introduction to Programming (CS-701-501, GB-731-501, CS-701-601, GB-731-601)\Intro_Data_Science-Project\DataScienceProject-a3519fd89c36.json',
)

NYPD_Accident_Data = """SELECT
  borough,
  contributing_factor_vehicle_1,
  contributing_factor_vehicle_2,
  number_of_cyclist_injured,
  number_of_cyclist_killed,
  number_of_motorist_injured,
  number_of_motorist_killed,
  number_of_pedestrians_injured,
  number_of_pedestrians_killed,
  number_of_persons_injured,
  number_of_persons_killed,
  vehicle_type_code1,
  vehicle_type_code2,
  zip_code
FROM
  `bigquery-public-data.new_york_mv_collisions.nypd_mv_collisions`
"""
# Creating a DataFrame of the entire data created from bigquery SQL 
df = pandas_gbq.read_gbq(NYPD_Accident_Data, project_id="datascienceproject-260913", credentials=credentials)
type(df)

# Seperating each data by bourough 
# adding a new column that includes the number of total accidents that includes all the categories 
df_Queens = df.loc[df['borough'] == "QUEENS"]
df_Queens['Total Accidents'] = df_Queens.iloc[:, 3:11].sum(axis = 1)
# data clean up 
df_Queens = df_Queens.drop(columns = ['borough'])
df_Queens = df_Queens.reset_index()
df_Queens = df_Queens.drop(columns = ['index'])

#Graphing Accident frequency with the Various Zip codes
plt.rcParams['figure.figsize'] = [80,40]
byZip_code1 = df_Queens.groupby(['zip_code'])
Zip_code_data_Queens = pd.DataFrame(byZip_code1.describe())
y_posQ = np.arange(len(Zip_code_data_Queens.index))
plt.bar(x = y_posQ, y= Zip_code_data_Queens.iloc[:,0].sort_values(ascending=False))
plt.xticks(y_posQ,Zip_code_data_Queens.index)
plt.yticks([0,2000,6000,10000,14000,18000],
           ['0','2000A','6000A','10000A','14000A','18000A'])
plt.xlabel('Zip Codes')
plt.ylabel('Number of Accidents')
plt.title('Frequency of Accidents VS Zip codes (Queens)')
plt.show()

#create a pie chart 
plt.style.use('ggplot')
labels = ['11001','11004', '11005','11040','11101']
plt.pie([15600,13400,12800,11000,10000], labels = labels, 
autopct = '%.2f %%', pctdistance = 0.8,)

plt.title('% Highest # of Accidents by Zip Codes (Queens)')
plt.rcParams['figure.figsize'] = [30,10]
plt.show()


Zip_code_data_Queens1 = pd.DataFrame(byZip_code1)
# adding a new column that includes the number of total accidents that includes all the categories 
df_Bronx = df.loc[df['borough'] == "BRONX"]
df_Bronx['Total Accidents'] = df_Bronx.iloc[:, 3:11].sum(axis = 1)
# data clean up 
df_Bronx = df_Bronx.drop(columns = ['borough'])
df_Bronx = df_Bronx.reset_index()
df_Bronx = df_Bronx.drop(columns = ['index'])

#Graphing Accident frequency with the Various Zip codes
byZip_code2 = df_Bronx.groupby(['zip_code'])
Zip_code_data_Bronx = pd.DataFrame(byZip_code2.describe())
y_posBr = np.arange(len(Zip_code_data_Bronx.index))
plt.bar(y_posBr, Zip_code_data_Bronx.iloc[:,0].sort_values(ascending=False))
plt.xticks(y_posBr,Zip_code_data_Bronx.index)
plt.yticks([0,2000,6000,10000,12000],
           ['0','2000A','6000A','10000A','12000A'])
plt.xlabel('Zip Codes')
plt.ylabel('Number of Accidents')
plt.title('Frequency of Accidents VS Zip codes (Bronx)')
plt.show()

Zip_code_data_Bronx1 = pd.DataFrame(byZip_code2)

#create a pie chart 
plt.style.use('ggplot')
labels = ['10451','10452', '10453','10454','10455']
plt.pie([11000,9200,8800,8200,8000], labels = labels, 
autopct = '%.2f %%', pctdistance = 0.8,)

plt.title('% Highest # of Accidents by Zip Codes (Bronx)')
plt.rcParams['figure.figsize'] = [30,10]
plt.show()

# adding a new column that includes the number of total accidents that includes all the categories 
df_Manhattan = df.loc[df['borough'] == "MANHATTAN"]
df_Manhattan['Total Accidents'] = df_Manhattan.iloc[:, 3:11].sum(axis = 1)
# data clean up 
df_Manhattan = df_Manhattan.drop(columns = ['borough'])
df_Manhattan = df_Manhattan.reset_index()
df_Manhattan = df_Manhattan.drop(columns = ['index'])

#Graphing Accident frequency with the Various Zip codes 
byZip_code3 = df_Manhattan.groupby(['zip_code'])
Zip_code_data_Manhattan = pd.DataFrame(byZip_code3.describe())
y_posM = np.arange(len(Zip_code_data_Manhattan.index))
plt.bar(y_posM, Zip_code_data_Manhattan.iloc[:,0].sort_values(ascending=False))
plt.xticks(y_posM,Zip_code_data_Manhattan.index)
plt.yticks([0,2000,6000,10000,14000,18000],
           ['0','2000A','6000A','10000A','14000A','18000A'])
plt.xlabel('Zip Codes')
plt.ylabel('Number of Accidents')
plt.title('Frequency of Accidents VS Zip codes (Manhattan)')
plt.rcParams['figure.figsize'] = [80,30]
plt.show()

Zip_code_data_Manhattan1 = pd.DataFrame(byZip_code3)

#create a pie chart 
plt.style.use('ggplot')
labels = ['10000','10001', '10002','10003','10004']
plt.pie([16200,15500,15000,14000,13800], labels = labels, 
autopct = '%.2f %%', pctdistance = 0.8,)

plt.title('% Highest # of Accidents by Zip Codes (Manhattan)')
plt.rcParams['figure.figsize'] = [30,10]
plt.show()

# adding a new column that includes the number of total accidents that includes all the categories 
df_Brooklyn = df.loc[df['borough'] == "BROOKLYN"]
df_Brooklyn['Total Accidents'] = df_Brooklyn.iloc[:, 3:11].sum(axis = 1)
# data clean up 
df_Brooklyn = df_Brooklyn.drop(columns = ['borough'])
df_Brooklyn = df_Brooklyn.reset_index()
df_Brooklyn = df_Brooklyn.drop(columns = ['index'])

#Graphing Accident frequency with the Various Zip codes 
plt.rcParams['figure.figsize'] = [50,25]
byZip_code4 = df_Brooklyn.groupby(['zip_code'])
Zip_code_data_Brooklyn = pd.DataFrame(byZip_code4.describe())
y_posB = np.arange(len(Zip_code_data_Brooklyn.index))
plt.bar(y_posB, Zip_code_data_Brooklyn.iloc[:,0].sort_values(ascending=False))
plt.xticks(y_posB,Zip_code_data_Brooklyn.index)
plt.yticks([0,2000,6000,10000,14000,18000],
           ['0','2000A','6000A','10000A','14000A','18000A'])
plt.xlabel('Zip Codes')
plt.ylabel('Number of Accidents')
plt.title('Frequency of Accidents VS Zip codes (Brooklyn)')
plt.show()

Zip_code_data_Brooklyn1 = pd.DataFrame(byZip_code4)

#create a pie chart 
plt.style.use('ggplot')
labels = ['11201','11203', '11204','11205','11206']
plt.pie([22000,14200,13800,13700,13500], labels = labels, 
autopct = '%.2f %%', pctdistance = 0.8,)

plt.title('% Highest # of Accidents by Zip Codes (Brooklyn)')
plt.rcParams['figure.figsize'] = [30,10]
plt.show()

# adding a new column that includes the number of total accidents that includes all the categories 
df_StatenIsland = df.loc[df['borough'] == "STATEN ISLAND"]
df_StatenIsland['Total Accidents'] = df_StatenIsland.iloc[:, 3:11].sum(axis = 1)
# data clean up 
df_StatenIsland = df_StatenIsland.drop(columns = ['borough'])
df_StatenIsland = df_StatenIsland.reset_index() 
df_StatenIsland = df_StatenIsland.drop(columns = ['index'])

#Graphing Accident frequency with the Various Zip codes
byZip_code5 = df_StatenIsland.groupby(['zip_code'])
Zip_code_data_StatenIsland = pd.DataFrame(byZip_code5.describe())
y_posS = np.arange(len(Zip_code_data_StatenIsland.index))
plt.bar(y_posS, Zip_code_data_StatenIsland.iloc[:,0].sort_values(ascending=False))
plt.xticks(y_posS,Zip_code_data_StatenIsland.index)
plt.yticks([0,2000,6000,10000],
           ['0','2000A','6000A','10000A'])
plt.xlabel('Zip Codes')
plt.ylabel('Number of Accidents')
plt.title('Frequency of Accidents VS Zip codes (Staten Island)')
plt.show()

Zip_code_data_StatenIsland1 = pd.DataFrame(byZip_code5)

#create a pie chart 
plt.style.use('ggplot')
labels = ['10301','10302', '10303','10304','10305']
plt.pie([9000,7000,6500,6400,5000], labels = labels, 
autopct = '%.2f %%', pctdistance = 0.8,)

plt.title('% Highest # of Accidents by Zip Codes (Staten Island)')
plt.rcParams['figure.figsize'] = [30,10]
plt.show()

#create a pie chart 
plt.style.use('ggplot')
labels = ['Cyclists','Motorists', 'Pedestrians','Person']
explode = (.05,.05,.05,.05)
plt.pie([df.iloc[:,3].sum() ,df.iloc[:,5].sum(),
         df.iloc[:,7].sum() ,df.iloc[:,9].sum()], labels = labels, 
autopct = '%.2f %%', pctdistance = 0.8, explode = explode)

plt.title('% injuries by category ')
plt.rcParams['figure.figsize'] = [30,10]
plt.show()

"""
#create a box and whiskers chart
plt.style.use('default')
plt.boxplot([df.iloc[:,4] ,df.iloc[:,6],
         df.iloc[:,8],df.iloc[:,10]])
plt.yticks([0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,.1])
plt.show()
"""