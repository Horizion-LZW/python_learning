# arcpy库

```python
list1 = [[2.3, 5.4], [9.4, 6.2], [1.2, 9.3],[2.5, 5.7],[9.2, 6.5]]
dict1={}
for i in range (1,11):
    for j in range (1,11):
        dict1[i,j]=0

for x in list1:
    row=int(x[0])
    col=int(x[1])
    dict1[row,col]+=1

for i in range (1,11):
    for j in range (1,11):
        print(dict1[i,j],end=' ')
    print()
```

## 批处理

clip函数
Clio_analysis (in_features, clip_features, out_feature_class, {cluster_tolerance})

```python
import arcpy
from arcpy import env
env.workspace = "D:/data"#设置工作空间
clip_features = "D:/data/parks.shp"#设置裁剪要素
fcs = arcpy.ListFeatureClasses()#获取工作空间下的所有要素类
for fc in fcs:
    outFeatureClass = os.path.join("D:/output", fc)
    arcpy.Clip_analysis(fc, clip_features, "D:/output/" + fc)#裁剪
```

## 批处理分割操作
split函数
Split_analysis (in_features, split_features, split_field, {out_workspace}, 
{cluster_tolerance})#分割要素，分割要素，分割字段，输出工作空间，聚类容差
```python
import arcpy
from arcpy import env
import os
env.workspace = "D:/data"
splitFeatures = "D:/data/parks.shp"
fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    path="D:\\data\\output\\"+fc.split(".")[0]
    outFeatureClass = os.path.join("D:/output", fc)
    arcpy.Split_analysis(fc, splitFeatures, "NAME", path)
```

## 线简化
SimplifyLine_cartography (in_features, out_feature_class, algorithm, {tolerance})

```python
import arcpy
from arcpy import env
import arcpu.cartography as CA
env.workspace = "D:/data"
for r in range(1,11):
    fc="D:/data/roads"+str(r)+".shp"
    outFeatureClass = "D:/output/roads"+str(r)+"_s.shp"
    CA.SimplifyLine_cartography(fc, outFeatureClass, "POINT_REMOVE", "100 Meters")
```