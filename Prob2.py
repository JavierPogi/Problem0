import pandas as pd

box = pd.DataFrame({'Box': ['Box1', 'Box1', 'Box1', 'Box2', 'Box2', 'Box2'],'Dimension':['Length','Width','Height','Length','Width','Height'
                    ],'Value':[6,4,2,5,3,4]})
tidy=box.pivot_table(index='Box', columns='Dimension', values='Value')
l = tidy.Length
w = tidy.Width
h = tidy.Height
v = l * w * h
tidy['Volume']= v