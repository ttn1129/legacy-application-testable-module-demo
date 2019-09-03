# coding:utf-8
import config
import os
import shutil
from datetime import datetime

screenshotDirectoryName = config.screenshotDirectoryName
screenshotBasePath = config.screenshotBasePath
backupBasePath = config.backupBasePath
uploadFileDirectoryName = config.uploadFileDirectoryName
uploadFileBasePath = config.uploadFileBasePath
downloadsDirectoryName = config.downloadsDirectoryName
downloadsFilePath = config.downloadsFilePath

class OsModule(object):
    def makeBackup(self)->None:
        datetimeText = datetime.now().strftime('%Y%m%d_%H%M%S')
        shutil.copytree(screenshotBasePath, backupBasePath + 'bk_' + screenshotDirectoryName + ('_%s' % datetimeText ))
        shutil.copytree(uploadFileBasePath, backupBasePath + 'bk_' + uploadFileDirectoryName + ('_%s' % datetimeText ))
        shutil.copytree(downloadsFilePath, backupBasePath + 'bk_' + downloadsDirectoryName + ('_%s' % datetimeText ))
        return 

    def makeDirectoryIfNotExist(self, directoryName:str):
        if not os.path.exists(directoryName):
            os.mkdir(directoryName)
        return

    def deleteScreenShots(self):
        filenameList = [ f for f in os.listdir(screenshotDirectoryName) if f.endswith(".png") ]
        for filename in filenameList:
            os.remove(os.path.join(screenshotDirectoryName, filename))
        return

    def deleteUploadExcelFiles(self):
        filenameList = [ f for f in os.listdir(uploadFileDirectoryName) if f.endswith(".xlsx") ]
        for filename in filenameList:
            os.remove(os.path.join(uploadFileDirectoryName, filename))
        return

    def getLatestDownloadedFileName(self):
        if len(os.listdir(downloadsFilePath)) == 0:
            return None
        return max (
            [downloadsFilePath+ f for f in os.listdir(downloadsFilePath)], 
            key=os.path.getctime
        )
