import os, sys, random
import numpy as np
import glob
import subprocess
import sys,string
import ConfigParser
AnalysisName = sys.argv [1]
Sample_Name = sys.argv [2]

def checkAndMakeDir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

def clearDir(dir):
    for fil in glob.glob(dir+"/*"):
        os.remove(fil)
#pufile='file:root://xrootd.unl.edu/'+pufilelist[random.randint(0,len(pufilelist))]

#print pufile
if Sample_Name == "QCD":
    SampleName = "QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8_RunIISummer19UL17RECO-106X_mc2017_realistic_v6-v2_AODSIM"
if Sample_Name == "m10"or Sample_Name =="M10" or Sample_Name == "10":
    SampleName = "TCP_m10_w1_htjmin400_RunIISummer17DR94Premix"
if Sample_Name == "m50" or Sample_Name =="M50" or Sample_Name == "50":
    SampleName = "TCP_m50_w1_htjmin400_RunIISummer17DR94Premix"

#AnalysisName= "ETauEHad"
configDir = "/uscms_data/d3/nbower/FSU/9_6_METTest/CMSSW_9_4_4/src/myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer/configs/"+SampleName+"/"+AnalysisName+"/"
checkAndMakeDir(configDir)
clearDir(configDir)
outputDir = "/store/user/nbower/plots/"+SampleName+"/"
checkAndMakeDir("/eos/uscms/"+outputDir)

outputDir = "/store/user/nbower/plots/"+SampleName+"/"+AnalysisName+"/"
checkAndMakeDir("/eos/uscms/"+outputDir)

clearDir("/eos/uscms/"+outputDir)

#masses=[30, 50]
masses=[10]

jobs=np.linspace(100,1,100)
#jobs=[2,68,92,93,94,95,96,97,98,99,100]
#jobs=[41, 49]
#listdirectory = '//uscms_data/d3/nbower/FSU/LowPtIDStudies/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer/macros/fileLists/TCP_w1_htjmin400_RunIISummer17DR94Premix/m50/'
localdir = 'myLowPtGsfElectronsAnalyzer/macros/fileLists/TCP/m10/'
listdirectory = '/uscms_data/d3/nbower/FSU/9_6_METTest/CMSSW_9_4_4/src/myLowPtGsfElectronsAnalyzer/'+localdir

for file in os.listdir(listdirectory):
    cfg=open(configDir+file.replace(".txt","cfg.py"),"w")
    print (configDir+file.replace(".txt","cfg.py"),"w")
    cfg.writelines("""
# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: test2 -s RAW2DIGI,L1Reco,RECO --datatier RECO --era=Run2_2018 --conditions auto:phase1_2018_realistic --eventcontent RECO --filein file:test.root --no_exec
import FWCore.ParameterSet.Config as cms
#f = open("/uscms_data/d3/nbower/FSU/TestLowPt/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer/macros/fileLists/m50_ALP_fileList.txt","r")
#f = open('./myLowPtGsfElectronsAnalyzer/macros/fileLists/TCP_w1_htjmin400_RunIISummer17DR94Premix/m50/"""+file+"""','r')
f = open('./"""+localdir +file+"""','r')

infiles = f.readlines()
f.close()
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('python')
options.setDefault('maxEvents',-1)
options.setDefault('inputFiles',infiles)


options.parseArguments()



process = cms.Process('TEST') # ,eras.bParkingOpen

# import of standard configurations


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)



# Output definition


# Path and EndPath definitions
process.load('myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer_cfi')



# Schedule definition

process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('root://cmseos.fnal.gov/"""+outputDir+file.replace(".txt","_"+AnalysisName+".root")+"""')
                                   )


process.p = cms.Path(process.simple)
# Customisation from command line


# End adding early deletion

#open('pydump.py','w').write(process.dumpPython())

""")
