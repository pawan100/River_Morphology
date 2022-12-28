#import required libraries
import rasterio
#from rasterio 
from rasterio import plot
#
import matplotlib.pyplot as plt
import numpy as np

# % matplotlib inline
#https://hatarilabs.com/ih-en/ndvi-calculation-from-landsat8-images-with-python-3-and-rasterio-tutorial
#https://earthpy.readthedocs.io/en/latest/gallery_vignettes/plot_calculate_classify_ndvi.html

import os
os.listdir('D:\OneDrive - The University of Alabama\Paper\PCD\Satelliteimage\Landsat8_2022')

#import bands as separate 1 band raster
band3 = rasterio.open('D:\OneDrive - The University of Alabama\Paper\PCD\Satelliteimage\Landsat8_2022/LC08_L2SP_021039_20211201_20211209_02_T1_SR_B3.tif') #red
band6 = rasterio.open('D:\OneDrive - The University of Alabama\Paper\PCD\Satelliteimage\Landsat8_2022/LC08_L2SP_021039_20211201_20211209_02_T1_SR_B6.tif') #swir

#sentinel 2
band3S = rasterio.open('D:\OneDrive - The University of Alabama\Paper\PCD\Satelliteimage\T16RDV_20221213T163709_B03_10m') #red
band9 = rasterio.open('D:\OneDrive - The University of Alabama\Paper\PCD\Satelliteimage\S2B_MSIL2A_20221213T163709_N0509_R083_T16RDV_20221213T190508.SAFE\GRANULE\L2A_T16RDV_A030139_20221213T164134\IMG_DATA\R60m\T16RDV_20221213T163709_B09_60m.tif') #swir


# clip study area mobile river

#classification

# reclassify to 0 no water and 1 water

# median filter

#plot band 
#plot.show(band3)
plot.show (band3S)
#ndwi
#try
