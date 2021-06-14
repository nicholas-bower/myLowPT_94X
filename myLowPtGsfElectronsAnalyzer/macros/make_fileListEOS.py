import subprocess
import sys,string,math,os
import ConfigParser
import glob
import numpy as np


filesPerList=50


def checkAndMakeDir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

def clearDir(dir):
    for fil in glob.glob(dir+"/*"):
        os.remove(fil)

prefix= "root://cmseos.fnal.gov/"
rootFileDir="/store/user/nbower/Events/ALP/m40_w1_htjmin100_RunIISummer17DR94Premix/"
os.system('xrdfsls' + rootFileDir)
#query = 'eosls '+ rootFileDir
query = 'xrdfs ' + prefix + " ls " + rootFileDir
os.system(query)
files=os.popen(query).read().split()
out = open("/uscms_data/d3/nbower/FSU/LowPtIDStudies/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer/macros/fileLists/m10_w1_htjmin400_RunIISummer17DR94Premix.txt", "w")
for nf in range(1, len(files)+1):
    filelistIdx=int((nf-1))
    
    out.write(prefix+files[nf-1]+"\n")
