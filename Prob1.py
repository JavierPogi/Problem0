import pandas as pd 
BearESAT = pd.DataFrame({'Student':['Ice Bear', 'Panda', 'Grizzly'], 'ESAT': [93,89,88]})
BearGeas = pd.DataFrame({'Student':['Ice Bear', 'Panda', 'Grizzly'], 'GEAS': [90,79,93]}).merge(BearESAT,on='Student')
BearElec = pd.DataFrame({'Student':['Ice Bear', 'Panda', 'Grizzly'], 'Electronics': [85,81,83]}).merge(BearGeas,on='Student')
BearMath = pd.DataFrame({'Student':['Ice Bear', 'Panda', 'Grizzly'], 'Math': [80,95,79]}).merge(BearElec,on='Student')
long=pd.melt(BearMath,id_vars=['Student'],var_name='Subject',value_name='Grades')
