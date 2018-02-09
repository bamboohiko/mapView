#mapView

[TOC]

##简介

###区域划分

    1.  数据库连接

        建立数据库连接，并从其中提取路网数据,并格式化为geojson
        在本程序中使用的是postgreSQL数据库,使用psycopg2模块建立连接和进行查询
        使用模块：csv,psycopg2

    2.  数据清洗
        从数据库中并按照类型进行选择，提取所需数据并格式化为geojson格式
        使用了GDAM数据库作为边界，需要导入.shp文件
        使用了postGIS函数
        使用模块：geojson，psycopg2

    3.  路网分割
        首先将矢量数据像素化为图片，之后对图片进行侵蚀，扩张，在此基础上查找各联通快的边界作为划分区域，并建立像素点与经纬度坐标之间的映射，将像素图片转换回矢量数据
        使用模块：matplotlib.pyplot,numpy,geojson,cv2,os

    4.  区域边界处理
        对划分区域边界点进行压缩，平滑边界
        （需要改进）

    5.  可视化
        将得到的划分在地图上标记
        使用了BingMap控件


###区域合并
*（需要测试）*

    提供区域合并及附加功能

    1.  区域合并

    2.  合并回退

    3.  清除合并

    4.  输出合并结果

##代码结构

- mapView
    + roadSegmentation
        * databaseConnection.py 
        * dataCleaning.py
        * areaDivide.py
        * boundaryCompression.py
    + areaUnion
        * mapView.html
        * _Getmap.js
        * areaUnion.js
        * data.js
        * readme.txt
    + example
        * mapView.html
        * _Getmap.js
        * divideData.js
        * example.py
    + dist
        * mapView-0.1.tar.gz
    + readme.md

##部署说明

pip install dist/mapView-0.1.tar.gz

##示例

导入数据库之后，运行example\example.py，可以在example\mapView.html中看到划分结果

##参考文档


