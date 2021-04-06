import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.array([[1, 2, 3], ['aa', 5, 6], [7, 8, 9]]), index= [2, 'A', 4], columns=['a', 49, 50])

df.to_excel("test_save.xlsx")



