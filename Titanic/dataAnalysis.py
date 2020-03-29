#-----------------------------------------------------
# Editor:Chanyeol Liu    Date:2020/03/28
# Code:CL200328
# Purpose:任务二：基于深度学习的文本分类
#-----------------------------------------------------

import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame

data_train = pd.read_csv("data/train.csv")
print(data_train.describe())
