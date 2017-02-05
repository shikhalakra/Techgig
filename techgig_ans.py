import numpy as np
import math
import pandas as pd
df=pd.read_csv('train.csv')
df_test2=pd.read_csv('test.csv')
df_test2_result=pd.read_csv('test_result.csv')
#print df['outlet_no'], df['total_sales']
#print df_train.corr()

f=open("result2.txt",'w+')
for i in range(0,len(df_test2['employee_size'])):
	predicted_sale = df_test2.iloc[i]['employee_size']*124
    	f.write(str(predicted_sale))
	f.write('\n')
	#df_test2_result[i]['prediction']=predicted_sale
	
f.close()
		


