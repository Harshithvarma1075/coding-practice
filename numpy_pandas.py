#DATA ANALYSIS

#Why this is needed ---this is critical because it converts raw data into actionable insights , enabling information to make decisions easy and improve operational efficiency

'''
1.Decision making
2.improved operational efficiencey
3.customer understandability
4.market insights
5.risk management
6.data driven strategies
'''

#LINECHART
'''
import matplotlib.pyplot as plt
x=[200,40,60,80]
y=[1,2,3,4]
plt.plot(y,x)
plt.show()
'''
#BAR GRAPH
'''
import matplotlib.pyplot as plt
plt.bar(["POGO","CN","KUSHI"] , [4,9,5])
plt.show()
'''
#PIE CHART
'''
import matplotlib.pyplot as plt
plt.pie([35,15,50] , labels =["surya","kartheek","varshini"])
plt.show()
'''
#HISTOGRAM
'''
import matplotlib.pyplot as plt
plt.hist([23,15,78,12])
plt.show()
'''

#NUMPY
'''
Numpy which is numerical python is the fundamental open source library for scientific computing in python , providing high performance , N-dimensional arrays
objects(ndarray) ,
---- this enables efficient numerical computation with linear algebra and data manipulation , also serving as the basis for tools like tensorflow and scipy

import numpy as np
arr= np.array([1,2,3])
print(arr - 1)
'''
#PANDAS
'''
this pandas is used for handling structured data in table format
'''
import pandas as pd
data = {"Name": ["harshith","mohan"] ,"Marks":[89,75]}
any=pd.DataFrame(data)
print(any)





















