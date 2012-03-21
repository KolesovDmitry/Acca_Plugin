﻿#!/usr/bin/env python
import sys
import osgeo.gdal as gdal
import numpy
import os
import time
import math
from event import *

#printf from C
def printf(fstr,*param):
    string=fstr % param
    sys.stdout.write (string)
    sys.stdout.flush()

class CAcca:
    __NO_CLOUD=0
    __NO_DEFINED=1
    __IS_SHADOW=20
    __IS_COULD=1
    __COLD_CLOUD=30
    __WARM_CLOUD=50
    __IS_COLD_CLOUD=6
    __IS_WARM_CLOUD=9

    def __init__(self, metafile, maskfile):
        pass
    #using
    def using():
        print "Using:\n\t", sys.argv[0],  "<metafile> <mask file>"

    def shadow_algorithm(band,mask):
        numpy.putmask(mask[0],(mask[0]==__NO_DEFINED)&((band[3]<0.07) & (((1-band[4])*band[6])>240.) & ((band[4]/band[2]>1.)) & ((band[3]-band[5])/(band[3]+band[5])<0.10)),IS_SHADOW)

    #Acca algorithm, first pass
    def acca_first(band, mask):
        boolmask=numpy.invert(numpy.zeros(band[2].shape,dtype=bool))

        ndsi=(band[2]-band[5])/(band[2]+band[5])
        rat55=(1.-band[5])*band[6]

        mask.append(numpy.empty(band[2].shape,dtype=numpy.uint8))
        mask[0][:]=NO_DEFINED
        numpy.putmask(mask[0],((band[2]==0.) | (band[3]==0.) | (band[4]==0.) | (band[5]==0.) | (band[6]==0.)),NO_CLOUD)

        if "WITH_SHADOW" in self.__metadata:
            if self.__metadata["WITH_SHADOW"]==True:
                shadow_algorithm(band,mask);

        boolmask_prev=(mask[0]==NO_DEFINED)

        numpy.putmask(mask[0],boolmask_prev,NO_CLOUD)

        self.__metadata["count"]["TOTAL"]+=numpy.sum(boolmask)
        boolmask=boolmask&boolmask_prev

        #filter 1                                                                          
        boolmask_prev = (band[3]>0.08)
        numpy.putmask(mask[0],numpy.invert(boolmask_prev)&boolmask&(band[3]<0.07),NO_CLOUD)
        numpy.putmask(mask[0],numpy.invert(boolmask_prev)&boolmask&(band[3]>0.07),NO_DEFINED)
        boolmask=boolmask&boolmask_prev

        #filter 2 (ndsi)
        boolmask_prev = (ndsi>-0.25) & (ndsi<0.70)
        numpy.putmask(mask[0],numpy.invert(boolmask_prev)&boolmask,NO_CLOUD)
        self.__metadata["count"]["SNOW"]+=numpy.sum(numpy.invert(boolmask_prev)&(ndsi>0.08))
        boolmask=boolmask&boolmask_prev

        #filter 3
        boolmask_prev = (band[6]<300)
        numpy.putmask(mask[0],numpy.invert(boolmask_prev)&boolmask,NO_CLOUD)
        boolmask=boolmask&boolmask_prev

        #filter 4
        boolmask_prev = (rat56<225)
        numpy.putmask(mask[0],numpy.invert(boolmask_prev)&boolmask&(band[5]<0.8),NO_CLOUD)
        numpy.putmask(mask[0],numpy.invert(boolmask_prev)&boolmask&(band[5]>0.8),NO_DEFINED)
        boolmask=boolmask&boolmask_prev

        #filter 5
        boolmask_prev = ((band[4]/band[3])<2.35)
        numpy.putmask(mask[0],numpy.invert(boolmask_prev)&boolmask,NO_DEFINED)
        boolmask=boolmask&boolmask_prev

        #filter 6
        boolmask_prev = ((band[4]/band[2])<2.16248)
        self.__metadata["count"]["SOIL"]+=numpy.sum(boolmask_prev&boolmask)
        self.__metadata["count"]["SOIL"]+=numpy.sum(numpy.invert(boolmask_prev)&boolmask)
        numpy.putmask(mask[0],numpy.invert(boolmask_prev)&boolmask,NO_DEFINED)
        boolmask=boolmask&boolmask_prev

        #filter 7
        boolmask_prev = ((band[4]/band[5])>1.0)
        numpy.putmask(mask[0],numpy.invert(boolmask_prev)&boolmask,NO_DEFINED)
        boolmask=boolmask&boolmask_prev

        numpy.putmask(mask[0],boolmask & (rat56<210.),COLD_CLOUD)
        numpy.putmask(mask[0],boolmask & (rat56>=210.),WARM_CLOUD)
        self.__metadata["stats"]["SUM_COLD"]+=numpy.sum(boolmask & (rat56<210.))
        self.__metadata["stats"]["SUM_WARM"]+=numpy.sum(boolmask & (rat56>=210.))
        tmax=numpy.max(band[6])
        tmin=numpy.min(band[6])
        if (tmax>self.__metadata["stats"]["KMAX"]): self.__metadata["stats"]["KMAX"]=tmax
        if (tmin<self.__metadata["stats"]["KMIN"]): self.__metadata["stats"]["KMIN"]=tmin

    #Parsing metafile
    def parsing(list):
        self.__metadata={}
        path=list[0]
        self.__metadata["MASK_FILE_NAME"]=list[1]
        if not os.path.exists(path):
            print "ERROR: Can`t open metafile"
            return None
        metafile=open(path)
        for line in metafile:
            key,param=line.strip().split('=')
            self.__metadata[key]=param
        for i in range(2,7):
            self.__metadata["BAND"+str(i)+"_FILE_NAME"]=os.path.join(os.path.dirname(path),os.path.basename(self.__metadata["BAND"+str(i)+"_FILE_NAME"]))
        return self.__metadata

    #Loading bands from file
    def load_bands():
        gdalData=[]

        for i in 2,3,4,5,6:
            if "BAND"+str(i)+"_FILE_NAME" in self.__metadata:
                gdalData.append(gdal.Open(self.__metadata["BAND"+str(i)+"_FILE_NAME"], gdal.GA_ReadOnly))
                if gdalData[-1] is None:
                    print "ERROR: Can`t open raster"
                    return None
                #print "Driver short name", gdalData[-1].GetDriver().ShortName
                #print "Driver long name", gdalData[-1].GetDriver().LongName
                #print "Raster size", gdalData[-1].RasterXSize, "x", gdalData[-1].RasterYSize
                #print "Number of bands", gdalData[-1].RasterCount
                #print "Projection", gdalData[-1].GetProjection()
                #print "Geo transform", gdalData[-1].GetGeoTransform()
                #print "Channels count", gdalData[-1].RasterCount
                print "INFO: File ", self.__metadata["BAND"+str(i)+"_FILE_NAME"], "loaded"

            else:
                print "ERROR: Missing one or more band."
                return None
        return gdalData

    def close_bands(gdalData):
        print "INFO: Closing dataset"
        gdalData[0]=None
        gdalData[1]=None
        gdalData[2]=None
        gdalData[3]=None
        gdalData[4]=None

    def processing(gdalData):
        raster=[]
        format="GTiff"
        driver=gdal.GetDriverByName(format)
        projection=gdalData[0].GetProjection()
        transform=gdalData[0].GetGeoTransform()
        xsize=gdalData[0].RasterXSize
        ysize=gdalData[0].RasterYSize
        drvMeta=driver.Getself.__metadata()
        if drvMeta.has_key( gdal.DCAP_CREATE ) and drvMeta[ gdal.DCAP_CREATE ] == "YES":
            mask=driver.Create(self.__metadata["MASK_FILE_NAME"], xsize, ysize, 1, gdal.GDT_Byte)
            mask.SetProjection(projection)
            mask.SetGeoTransform(transform)
        else:
            print "INFO: Driver %s does not support Create() method." % format
            return None

        step=2000
        x=gdalData[0].RasterXSize
        y=gdalData[0].RasterYSize
        area=x*y
        processed_area=0
        need_new_row=True
        need_new_column=True
        print "INFO: Running first pass"
        self.__metadata["stats"]={"SUM_COLD":0.,"SUM_WARM":0.,"KMAX":0.,"KMIN":10000.}
        self.__metadata["count"]={"WARM":0.,"COLD":0.,"SNOW":0.,"SOIL":0.,"TOTAL":0.}
        self.__metadata["value"]={"WARM":0.,"COLD":0.,"SNOW":0.,"SOIL":0.}
        for i in range(0,x,step):
            need_new_row=True
            for j in range(0,y,step):
                if i+step > x:
                    stepx=x-i
                else:
                    stepx=step
                if j+step > y:
                    stepy=y-j
                else:
                    stepy=step
                mask_arg=[]
                acca_first ({2:gdalData[0].ReadAsArray(i,j,stepx,stepy).astype(numpy.float32),\
                            3:gdalData[1].ReadAsArray(i,j,stepx,stepy).astype(numpy.float32),\
                            4:gdalData[2].ReadAsArray(i,j,stepx,stepy).astype(numpy.float32),\
                            5:gdalData[3].ReadAsArray(i,j,stepx,stepy).astype(numpy.float32),\
                            6:gdalData[4].ReadAsArray(i,j,stepx,stepy).astype(numpy.float32)},\
                            mask_arg)
                if need_new_row:
                    mask_r=mask_arg[0].copy()
                    need_new_row=False
                else:
                    mask_r=numpy.vstack((mask_r,mask_arg[0]))
                processed_area+=stepx*stepy
                stat=processed_area*100.0/area
                printf ("\rACCA first pass: %.2f%s",stat,"%")

        if need_new_column:
            mask_c=mask_r.copy()
            need_new_column=False
        else:
            mask_c=numpy.hstack((mask_c,mask_r))
        print "INFO: Writing mask"
        mask.GetRasterBand(1).WriteArray(mask_c)
        print "INFO: Closing mask"
        mask=None


    def start():
        self.__metadata=parsing()
        if (self.__metadata == None):
            return None
        self.__metadata["WITH_SHADOW"]=True
        gdalData=load_bands()
        if (gdalData == None):
            return None
        if (processing(gdalData) == None):
            return None
        close_bands(gdalData)
        return True
