from tabula import read_pdf
import numpy as np
import pandas as pd


#----2018
df = read_pdf('SnP_2018.pdf',pages='all',multiple_tables=False,Lattice=True,stream=True,
               area = "476,34,715,504",columns = (34,110.0,155.5,197.5,286.5,330.1,368.0,396.5,430.5,457.5),guess = False,pandas_options={'header':None})
#df.to_excel('SnP_2018.xlsx',index=False)

# End This code works for SnP File /

#cleanup the data from above

Default_file = df.drop(df.index[0:11])
Default_file.drop(Default_file.columns[[0,2,4,5,8,9]], axis=1, inplace=True)
Default_file.columns = ['Company_Name', 'Country', 'Default_Date', 'Last_Rating','First_Rating_Date']


#----Removing instance if all the values are NaN
Default_file = Default_file.dropna(how='all')

#----Fill Company Name with bottom one in case of NA
for col in ['Company_Name']:
    Default_file[col] = Default_file[col].bfill()

#----filling for NaN (backfilling and Front Filling)
Default_file = Default_file.replace('', np.nan).ffill().bfill()
#Default_file

#----sorting based on default dates
Default_file.sort_values(by=['Default_Date'])
#Default_file
#----Filtering for countries
Default_file1 = Default_file['Country'].isin(['USA','U.S.','US','Canada'])
DF = Default_file[Default_file1]

#Addind special character before merging
DF = DF.assign(Company_Name = DF.Company_Name + '-')

#Merging rows based in column values
DF = DF.groupby([DF.Default_Date,DF.First_Rating_Date,DF.Country,DF.Last_Rating],as_index=True).sum()
DF = DF['Company_Name'].str.replace('-',' ')
DF = DF.replace('', np.nan).ffill().bfill()

#Grab dataframe from another excel sheet

#Open existing excel file
path = r'C:\Users\mamta\MMAI 2020\Learning\Self Learning and ML\Get Default Data/Merged_Default_Data.xlsx'
writer = pd.ExcelWriter(path, engine='openpyxl')

#Add dataframe to excel file
DF.to_excel(writer,sheet_name="2018")
writer.save()
writer.close()