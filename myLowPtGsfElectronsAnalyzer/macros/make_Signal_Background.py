import ROOT
import numpy as np
import glob
import subprocess
import sys,string
import string,math,os

import ConfigParser
import matplotlib.pyplot as plt
import numpy as np
def checkAndMakeDir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

def clearDir(dir):
    for fil in glob.glob(dir+"/*"):
        os.remove(fil)
checkAndMakeDir('/uscms_data/d3/nbower/FSU/LowPtIDStudies/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer/graphs/QCD_Generalm10/')
pi = math.pi

c_t = 1
m_t = 1.77686
fa = 1000

m_a = [10,30,50]
xsec_gt = [1.0256092e-07, 3.133914e-07, 5.077e-07]

Br = [0, 6.8 , 9.7 , 5.7 , 6.2 , 3.0 , 3.0 , 9.7 , 0.88 , 1.9 , 1.8 , 2.1 , 2.9] #so Model 1 is M[_][1]

xsec_M = [[],[],[]]

for j in range (3):
    for i in range (13):
        Gamma_tt = ((c_t**2*m_a[j]/(8*pi))*m_t**2*math.sqrt(1-4*m_t**2/m_a[j]**2))/fa**2
        xsec_g_TCP = xsec_gt[j] / Gamma_tt
        xsec_M_list = xsec_g_TCP * Br[i]
        xsec_M[j].append(xsec_M_list)
        print xsec_M[j][i]

xsec_TCP10 = xsec_M[0][1]*41.12e3
xsec_TCP30 = xsec_M[1][1]*41.12e3
xsec_TCP50 = xsec_M[2][1]*41.12e3
xsec_QCD = 1.354e09*41.12e3
BFile = "/uscms_data/d3/nbower/FSU/LowPtIDStudies/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8_RunIISummer19UL17RECO-106X_mc2017_realistic_v6-v2_AODSIM_ETauEHad.root"
SFile = "/uscms_data/d3/nbower/FSU/LowPtIDStudies/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/TCP_m10_w1_htjmin400_RunIISummer19UL17RECO_AODSIM_Updated_EHad_9_29.root"
signal =ROOT.TFile.Open(SFile ,"READ")
background =ROOT.TFile.Open(BFile ,"READ")
genElectrons = signal.Get('simple/nEvent_eMu_LooseEle')
sig_Background = ROOT.TH1F ("sig_Background", " Signal vs Sqrt(Background)[TCPm10 pt400/QCD]", 50 ,0, 9.5  )
sig = ROOT.TH1F('sig', 'Signal IntegralsTCPm10pt400',  50 ,0, 9.5)
bkg = ROOT.TH1F('bkg', 'BKG Integrals QCD',  50 ,0, 9.5)
#bkgEvents_h=background.Get('simple/nEvent_eMu_LooseEle')
sigEvents_h=signal.Get('simple/nEvent_eMu_LooseEle')
genElectrons
bkgEvents=bkgEvents_h.Integral(1,1)
sigEvents=sigEvents_h.Integral(1,1)
c = ROOT.TCanvas("c","c",600,600)
c.SetBorderSize(0)
c.SetFrameBorderMode(0)
ROOT.gStyle.SetTitleBorderSize(0)
ROOT.gStyle.SetOptStat(0)


QCD_ID = background.Get('simple/idHist')
#QCD_ID = background.Get('simple/eHad_eleID')
QCD_ID.Scale(xsec_QCD/bkgEvents)
print "QCD integral = " +str( bkgEvents)+ "; Scale = " + str( xsec_QCD/bkgEvents)
QCD_ID.Draw()
c.SaveAs('/uscms_data/d3/nbower/FSU/LowPtIDStudies/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer/graphs/QCD_Generalm10/eHad_QCD_ID.png')

TCP_ID=signal.Get('simple/idHist')
#TCP_ID = signal.Get('simple/eHad_eleID')
print "TCP integral = " +str( sigEvents)+ "; Scale = " + str( xsec_TCP50/sigEvents)

TCP_ID.Scale(xsec_TCP10/sigEvents)
TCP_ID.Draw()
c.SaveAs('/uscms_data/d3/nbower/FSU/LowPtIDStudies/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer/graphs/QCD_Generalm10/EHAD_TCP_m10_eMu_ID.png')

binwidth = 9.5/50

for i in range (1,50):
    s_point=TCP_ID.Integral(i,50)
    sig.SetBinContent(i, s_point)
    b_point = QCD_ID.Integral(i,50)
    bkg.SetBinContent(i,b_point)
    b_point = np.sqrt(b_point)
    print str(b_point.item())
    #print "sqrt bkg = "+str(type(b_point))+ "spoint = "+ str(type(s_point))
    if b_point!=0:
        sob=s_point/b_point.item()
    else:
        sob=0
    sig_Background.SetBinContent(i,sob)

print 'Max Sig/ background occurs at  = '+ str(sig_Background.GetMaximumBin()) + ', ID Val = ' + str((sig_Background.GetMaximumBin()-1)*binwidth)
sig_Background.Draw()
c.SaveAs('/uscms_data/d3/nbower/FSU/LowPtIDStudies/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer/graphs/QCD_Generalm10/xc_weight_m10_SignalVBackground.png')
sig.Draw()
c.SaveAs('/uscms_data/d3/nbower/FSU/LowPtIDStudies/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer/graphs/QCD_Generalm10/xc_weight_m10_Sig_Int.png')
bkg.Draw()
c.SaveAs('/uscms_data/d3/nbower/FSU/LowPtIDStudies/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer/graphs/QCD_Generalm10/xc_weight_m10_Bkg.png')

###############Cross Sections##############
#TCP m10 