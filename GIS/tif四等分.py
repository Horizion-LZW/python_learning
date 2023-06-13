import numpy as np
from osgeo import gdal

# 读取数据
filename = r"C:\Users\25830\OneDrive - oganneson\桌面\学习\python学习\python_learning\GIS\dem_fengle.tif"
ds = gdal.Open(filename)
band = ds.GetRasterBand(1)
data = band.ReadAsArray()

# 四等分
halves = np.vsplit(data, 2)
quarters = [np.hsplit(half, 2) for half in halves]

# 创建输出文件
driver = gdal.GetDriverByName("GTiff")

# 获取原始文件的地理坐标信息
x_origin, pixel_width, _, y_origin, _, pixel_height = ds.GetGeoTransform()

# 计算新的x_origin和y_origin的增量
delta_x = (data.shape[1] / 2) * pixel_width
delta_y = (data.shape[0] / 2) * abs(pixel_height)

# 循环遍历并保存四个部分
for i in range(2):
    for j in range(2):
        # 获取当前区块
        quarter = quarters[i][j]

        # 使用增量计算新的x_origin和y_origin
        new_x_origin = x_origin + j * delta_x
        new_y_origin = y_origin - i * delta_y

        # 新的仿射变换参数
        new_geotransform = (new_x_origin, pixel_width, 0, new_y_origin, 0, pixel_height)

        # 输出文件名
        output_file = r"C:\Users\25830\OneDrive - oganneson\桌面\学习\python学习\python_learning\GIS\output{}.tif".format(
            i * 2 + j + 1)

        # 创建新的数据集
        outds = driver.Create(output_file, quarter.shape[1], quarter.shape[0], 1, gdal.GDT_Float32)

        # 设置仿射变换参数
        outds.SetGeoTransform(new_geotransform)

        # 将数组数据写入栅格波段
        outds.GetRasterBand(1).WriteArray(quarter)

        # 刷新缓存以确保所有数据写入
        outds.FlushCache()
        outds = None

# 清理
ds = None
band = None
data = None
