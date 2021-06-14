import ROOT
import sys
import subprocess
import string,math,os
import ConfigParser
import glob
import numpy as np

inFileName = sys.argv [1]
samp_mass = sys.argv [2]
label = sys.argv [3]

Mass=samp_mass

print " Reading from ", inFileName 
inFile = ROOT.TFile.Open(inFileName ,"READ") 
histos = {}
c = ROOT.TCanvas("c","c",600,600)      
c.SetBorderSize(0)   
c.SetFrameBorderMode(0)

ROOT.gStyle.SetTitleBorderSize(0)
ROOT.gStyle.SetOptStat(0)
#ROOT.TColor.Colorpalettes(195)
#ROOT.gStyle.SetPalette(156)
#inFile.cd('simple')
def checkAndMakeDir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

def clearDir(dir):
    for fil in glob.glob(dir+"/*"):
        os.remove(fil)
outDir = ('/uscms_data/d3/nbower/FSU/LowPtIDStudies/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer/graphs/'+samp_mass+"_"+label+"/")
checkAndMakeDir(outDir)
eHad_geometry_NoID_Standard_m = inFile.Get('simple/eHad_geometry_NoID_Standard_m')
ETau=eHad_geometry_NoID_Standard_m.ProjectionX()
ETau.SetTitle(eHad_geometry_NoID_Standard_m.GetTitle().replace("dR (Ele,Tau) Vs dR(Jet,Ele)", "Delta R(e,tau)"))
ETau.Draw()
c.SaveAs(outDir+"FULL_TH1_eHad_geometry_NoID_Standard_m.png")
c.Clear()

eHad_geometry_NoID_Standard_m.Rebin2D(3,3)
eHad_geometry_NoID_Standard_m.SetTitle(inFile.Get("simple/eHad_geometry_NoID_Standard_m").GetTitle()+" || "+ Mass)
eHad_geometry_NoID_Standard_m.GetXaxis().SetTitle("dR(tau, e)")
eHad_geometry_NoID_Standard_m.GetYaxis().SetTitle("dR(e, jet)")
eHad_geometry_NoID_Standard_m.Draw("COL Z CJUST")
c.SaveAs(outDir+"FULL_ehad_geometry_NoID_Standard_m.png")
c.Clear()


eHad_METtoTau_JettoTau_NoID_Standard_m=inFile.Get("simple/eHad_METtoTau_JettoTau_NoID_Standard_m")
eHad_METtoTau_JettoTau_NoID_Standard_m.SetTitle(inFile.Get("simple/eHad_METtoTau_JettoTau_NoID_Standard_m").GetTitle()+" || "+ Mass)
eHad_METtoTau_JettoTau_NoID_Standard_m.Rebin2D(1,3)

eHad_METtoTau_JettoTau_NoID_Standard_m.GetXaxis().SetTitle("dPhi (MET,Tau)")
eHad_METtoTau_JettoTau_NoID_Standard_m.GetYaxis().SetTitle("dR (Tau,Jet)")
eHad_METtoTau_JettoTau_NoID_Standard_m.Draw("COL Z CJUST")
c.SaveAs(outDir+"eHad_METtoTau_JettoTau_NoID_Standard_m.png")
Projection=eHad_METtoTau_JettoTau_NoID_Standard_m.ProjectionY()
Projection.SetTitle(eHad_METtoTau_JettoTau_NoID_Standard_m.GetTitle().replace("dPhi (MET,Tau) Vs Dr(Jet,Tau)", "dR (Tau,Jet)"))
Projection.Draw()
c.SaveAs(outDir+"TH1_eHad_JettoTau_NoID_Standard_m.png")
c.Clear()
Projection=eHad_METtoTau_JettoTau_NoID_Standard_m.ProjectionX()
Projection.SetTitle(eHad_METtoTau_JettoTau_NoID_Standard_m.GetTitle().replace("dPhi (MET,Tau) Vs Dr(Jet,Tau)", "dPhi (Tau,Jet)"))
Projection.Draw()
c.SaveAs(outDir+"TH1_eHad_METtoTau_JettoTau_NoID_Standard_m".replace("MET_VS_JdPhiM","JdPhiM")+".png")
c.Clear()

eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m=inFile.Get("simple/eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m")
eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m.SetTitle(inFile.Get("simple/eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m").GetTitle()+" ||POSTGEO "+ Mass)
eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m.Rebin2D(1,3)
eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m.GetXaxis().SetTitle("dPhi (MET,Tau)")
eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m.GetYaxis().SetTitle("Dr(Jet,Tau)")
eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m.Draw("COL Z CJUST")
c.SaveAs(outDir+"eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m.png")
Projection=eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m.ProjectionY()
Projection.SetTitle(eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m.GetTitle().replace("dPhi (MET,Tau) Vs Dr(Jet,Tau)", "Dr(Jet,Tau)"))
Projection.Draw()
c.SaveAs(outDir+"TH1_eHad_METDiphi_Standard_m.png")
c.Clear()
Projection=eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m.ProjectionX()
Projection.SetTitle(eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m.GetTitle().replace("dPhi (MET,Tau) Vs Dr(Jet,Tau)", "dPhi (MET,Tau)"))
Projection.Draw()
c.SaveAs(outDir+"eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m".replace("MET_VS_JdPhiM","JdPhiM")+"postgeo.png")
c.Clear()




eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m=inFile.Get("simple/eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m")
eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m.SetTitle(inFile.Get("simple/eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m").GetTitle()+" ||POST geo"+ Mass)
eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m.Rebin2D(1,3)
eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m.GetXaxis().SetTitle("dPhi (MET,Tau)")
eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m.GetYaxis().SetTitle("Dr(Jet,Tau)")
eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m.Draw("COL Z CJUST")
c.SaveAs(outDir+"eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m.png")
Projection=eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m.ProjectionY()
Projection.SetTitle(eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m.GetTitle().replace("dPhi (MET,Tau) Vs Dr(Jet,Tau) ", "Dr(Jet,Tau)"))
Projection.Draw()
c.SaveAs(outDir+"TH1_eHad_JdPhiM_postGeo_NoID_Standard_m.png")
c.Clear()
Projection=eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m.ProjectionX()
Projection.SetTitle(eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m.GetTitle().replace("dPhi (MET,Tau) Vs Dr(Jet,Tau) ", "dPhi (MET,Tau)"))
Projection.Draw()
c.SaveAs(outDir+"eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m".replace("MET_VS_JdPhiM","JdPhiM")+"postgeo.png")
c.Clear()

eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m=inFile.Get("simple/eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m")
eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m.SetTitle(inFile.Get("simple/eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m").GetTitle()+" ||POST MET"+ Mass)
eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m.Rebin2D(1,3)
eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m.GetXaxis().SetTitle("dPhi (MET,Jet)")
eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m.GetYaxis().SetTitle("Met GEV")
eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m.Draw("COL Z CJUST")
c.SaveAs(outDir+"eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m.png")
Projection=eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m.ProjectionY()
Projection.SetTitle(eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m.GetTitle().replace("dPhi (MET,Jet) Vs Met", "MET Post met"))
Projection.Draw()
c.SaveAs(outDir+"TH1_eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m.png")
c.Clear()
Projection=eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m.ProjectionX()
Projection.SetTitle(eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m.GetTitle().replace("dPhi (MET,Jet) Vs Met", "dPhi (MET,Jet) postmet"))
Projection.Draw()
c.SaveAs(outDir+"eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m".replace("MET_VS_JdPhiM","JdPhiM")+"postmet.png")
c.Clear()