#Sample = 'TCP'
#Sample = 'DYJetsToLL_94X'
#Sample = 'DYJetsToLL'
#Sample = 'DYJetsToLLNLO'
#Sample = 'TTJets'
#Sample = 'ST'
#Sample = 'Diboson'
Sample = 'QCD_AOD'
#Sample = 'QCD_Mu'
#Sample = 'DYJetsToQQ'
#Sample = 'ZJetsToQQ'
#Sample = 'WJetsToQQ'

isHad = True
isCopy=True
version="vplots"
isGen=False
if Sample == 'TCP':
    masses=['m10', 'm30', 'm50']
    prefix="root://cmseos.fnal.gov//store/user/mwulansa/DIS/TCP/OutputMiniAODSIM/"
#if Sample == 'TCP':
#    masses=['m10','m50']
#    prefix="root://cmseos.fnal.gov/"

elif Sample == 'DYJetsToLL_94X':
    SampleText = 'DYJetsToLL'
    masses=['M-1to5_HT-70to100', 'M-1to5_HT-100to200', 'M-1to5_HT-200to400', 'M-1to5_HT-400to600', 'M-1to5_HT-600toInf']
    preSearchString="/"+SampleText+"_REPLACEME_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"
    prefix="root://xrootd.unl.edu/"
    
elif Sample == 'DYJetsToLL':
    masses=['M-5to50_HT-70to100', 'M-5to50_HT-100to200', 'M-5to50_HT-200to400', 'M-5to50_HT-400to600', 'M-5to50_HT-600toInf', 'M-50_HT-70to100', 'M-50_HT-100to200', 'M-50_HT-200to400', 'M-50_HT-400to600', 'M-50_HT-600to800', 'M-50_HT-800to1200', 'M-50_HT-1200to2500', 'M-50_HT-2500toInf', 'M-1To5_HT-150to200', 'M-1To5_HT-200to400', 'M-1To5_HT-400to600', 'M-1To5_HT-600toInf']
    preSearchString="/"+Sample+"_REPLACEME_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X*/MINIAODSIM"
    prefix="root://xrootd.unl.edu/"

elif Sample == 'DYJetsToLLNLO':
    SampleText = 'DYJetsToLL'
    masses=['M-10to50', 'M-50']
    preSearchString="/"+SampleText+"_REPLACEME_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6*v1/MINIAODSIM"
    prefix="root://xrootd.unl.edu/"
    
elif Sample == 'TTJets':
    masses=["Dilept"]
    preSearchString="/"+Sample+"_REPLACEME*/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"
    prefix="root://xrootd.unl.edu/"

elif Sample == 'ST':
    masses=['s-channel_4f_leptonDecays','t-channel_antitop_4f_inclusiveDecays', 't-channel_top_4f_inclusiveDecays', 'tW_top_5f_inclusiveDecays','tW_antitop_5f_inclusiveDecays']
    preSearchString="/"+Sample+"_REPLACEME_*TuneCUETP8M1*/RunIISummer16MiniAODv2-PUMoriond17_80X*/MINIAODSIM"
    prefix="root://xrootd.unl.edu/"

elif Sample == 'Diboson':
    masses=['WZ', 'WW', 'ZZ']
    preSearchString="/REPLACEME_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X*/MINIAODSIM"
    prefix="root://xrootd.unl.edu/"

elif Sample == 'QCD':
    masses=['HT200to300','HT300to500','HT500to700','HT700to1000','HT1000to1500','HT1500to2000','HT2000toInf']
    preSearchString="/"+Sample+"_REPLACEME_T*/RunIIFall17*_pmx_94X*/MINIAODSIM"
    prefix="root://cmsxrootd.fnal.gov/"

elif Sample == 'DYJetsToQQ':
    masses = ['HT180']
    preSearchString = "/"+Sample+"_REPLACEME_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"
    prefix = "root://xrootd.unl.edu/"

elif Sample == 'ZJetsToQQ':
    masses = ['HT600toInf']
    preSearchString="/"+Sample+"_REPLACEME_13TeV-madgraph*/RunIISummer16MiniAODv2-PUMoriond17_80X*/MINIAODSIM"
    prefix = "root://xrootd.unl.edu/"

elif Sample == 'WJetsToQQ':
    masses = ['HT-600ToInf']
    preSearchString="/"+Sample+"_REPLACEME_TuneCUETP8M1*/RunIISummer16MiniAODv2*/MINIAODSIM"
    prefix = "root://xrootc.unl.edu/"
elif Sample == 'QCD_AOD':
    masses = ['']
    preSearchString="/QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8/RunIISummer19UL17RECO-106X_mc2017_realistic_v6-v2/AODSIM"
    filename = "QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8_RunIISummer19UL17RECO-106X_mc2017_realistic_v6-v2_AODSIM"
    prefix = "root://cmseos.fnal.gov/"
elif Sample == 'QCD_Mu':
    masses = ['50to80', '80to120', '120to170']
    preSearchString="/QCD_Pt-REPLACEME_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIISummer19UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2/AODSIM"
    prefix = "root://cmseos.fnal.gov/"
else:
    print "Please Specify Sample Name!"
    sys.exit()

    
