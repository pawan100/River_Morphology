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

# clip study area mobile river

#classification

# reclassify to 0 no water and 1 water

# median filter

#plot band 
plot.show(band3)
#ndwi
