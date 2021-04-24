import pandas as pd
from .models import concatenation_points, distance_multiplier

# def readex():
#
#     file =('dm.ods')
#     df1 = pd.read_excel(file)
#     df1 = df1.iloc[:, 14:16]
#     print(df1)
#     df1.columns = ["CONCATENATION", "Conj"]
#     print(df1)
#     # for index, row in df1.iterrows():
#     #     print("##################")
#     #     type = ">150"
#     #     name = row.CONCATENATION
#     #     points = row.Conj
#     #     print(type,name, points)
#     #     s = concatenation_points(con_type=type, con_name=name, con_points=points)
#     #     s.save()

def readdm():
    file = ('dm.ods')
    df1 = pd.read_excel(file)
    # for index, row in df1.iterrows():
    #     print(row.DISTANCE, row.MULTIPLIER)
    #     s = distance_multiplier(distance=row.DISTANCE, multiplier=row.MULTIPLIER)
    #     s.save()
    # print(df1)