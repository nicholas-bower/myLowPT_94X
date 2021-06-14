import subprocess
import sys,string,math,os
import ConfigParser
import glob
import numpy as np
from sampleAndMasses import *

filesPerList=-1


def checkAndMakeDir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

def clearDir(dir):
    for fil in glob.glob(dir+"/*"):
        os.remove(fil)
first_step=True
if __name__ == "__main__":
    if Sample == 'TCP':
        for mass in masses:
            fileListDir="/uscms_data/d3/nbower/FSU/LowPtIDStudies/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer/macros/fileLists/TCP_w1_htjmin400_RunIISummer17DR94Premix/"+mass+"/"
            checkAndMakeDir("/uscms_data/d3/nbower/FSU/LowPtIDStudies/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer/macros/fileLists/TCP_w1_htjmin400_RunIISummer17DR94Premix/")
            checkAndMakeDir(fileListDir)
            clearDir(fileListDir)
            #rootFileDir="/store/user/nbower/Events/ALP/m10_w1_htjmin100_RunIISummer17DR94Premix/"
            rootFileDir="/eos/uscms/store/user/zhangj/events/ALP/RunIISummer19UL17RECO/TCP_"+mass+"_w1_htjmin400_RunIISummer19UL17RECO_AODSIM_*.root"


            #query = 'xrdfs ' + prefix + " ls " + rootFileDir
            query = "ls " + rootFileDir
            os.system(query)
            files=os.popen(query).read().split()
            for nf in range(1, len(files)+1):
                filelistIdx=int((nf-1)/filesPerList)
                root 
                if nf%filesPerList==1:
                    out=open(fileListDir+"TCP_"+mass+"_w1_htjmin400_RunIISummer19UL17RECO_AODSIM_"+str(filelistIdx)+".txt","w")
                out.write(prefix+files[nf-1]+"\n")
                
    else:
        for mass in masses:
#            fileListDir="./filelists_LM/"+Sample+"/"+mass+"/"
#            checkAndMakeDir("./filelists_LM/"+Sample)
            fileListDir="/uscms_data/d3/nbower/FSU/LowPtIDStudies/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer/macros/fileLists/"+filename+"/"
            if first_step==True:
                checkAndMakeDir(fileListDir)
                clearDir(fileListDir)
            #print mass
            first_step=False
            searchString=preSearchString.replace("REPLACEME",mass)
            os.system('dasgoclient --query "'+searchString+'"')
            query = 'dasgoclient --query "file dataset='+searchString+'"'
            files=os.popen(query).read().split()
            
            for nf in range(1, len(files)+1):
                filelistIdx=int((nf-1)/filesPerList)
                if nf%filesPerList==1:
                    out=open(fileListDir+filename+"_"+str(filelistIdx)+".txt","w")
                out.write(prefix+files[nf-1]+"\n")
            
