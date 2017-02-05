import numpy as np
import math
import pandas as pd
df=pd.read_csv('train.csv')
df_train=df[:175]
df_test=df[176:]
#print df['outlet_no'], df['total_sales']
#print df_train.corr()
output=[]
error_array=[]
for x in range(100,130):
	total_error=0
	temp=[]
	for i in range(0,len(df_train['employee_size'])):
    		predicted_sale = df_train.iloc[i]['employee_size']*x
		error=(predicted_sale-df_train.iloc[i]['total_sales'])*(predicted_sale-df_train.iloc[i]['total_sales'])
		total_error=total_error+error
	temp.append(x)
	temp.append(math.sqrt(total_error))
	error_array.append(temp)
#print error_array
#print min(error_array)
total_error=0
#print len(df_test['employee_size'])
for i in range(0,len(df_test['employee_size'])):
	predicted_sale = df_train.iloc[i]['employee_size']*124
	error=(predicted_sale-df_train.iloc[i]['total_sales'])*(predicted_sale-df_train.iloc[i]['total_sales'])
	total_error=total_error+error
print total_error
print math.sqrt(total_error)
		


