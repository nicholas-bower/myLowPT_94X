import ROOT
import numpy as np
import glob
import subprocess
import sys,string
import string,math,os

import ConfigParser
import matplotlib.pyplot as plt
import numpy as np
c = ROOT.TCanvas("c","c",600,600)      
c.SetBorderSize(0)   
c.SetFrameBorderMode(0)
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetTitleBorderSize(0)
ROOT.gStyle.SetOptStat(0)
def checkAndMakeDir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

def clearDir(dir):
    for fil in glob.glob(dir+"/*"):
        os.remove(fil)
def Make_PT_Overlays_Leading_only(Unmatched_Hist_Name, Mass, canvas, inFi,  matched ,outDir):
    if (matched == True):
        title = "Leading Only (Matched, "+Mass+")"
        fiName= "Leading_Overlayed_Matched_mva_"+Mass
    else:
        title = "Leading Only Considered (Fake, "+Mass+")"
        fiName= "Leading_Overlayed_Fake_mva_"+Mass                                      
    print 'simple/'+Unmatched_Hist_Name.replace("REPLACEME","NoID")
    NoID_PtT2H= inFi.Get('simple/'+Unmatched_Hist_Name.replace("REPLACEME","NoID"))
    NoID_Pt=NoID_PtT2H.ProjectionY()
    NoID_Pt.SetTitle(title)
    NoID_Pt.SetLineColor(ROOT.kBlack)

    NoID_Pt.Draw()
    Loose_Pt= NoID_PtT2H.ProjectionY("Loose_Pt",11,50,"")
    Loose_Pt.SetLineColor(ROOT.kRed)
    Loose_Pt.Draw("SAME")
    Medium_Pt= NoID_PtT2H.ProjectionY("Medium_Pt",21,50,"")
    Medium_Pt.SetLineColor(ROOT.kCyan)
    Medium_Pt.Draw("SAME")
    Tight_Pt= NoID_PtT2H.ProjectionY("Tight_Pt",31,50,'')
    Tight_Pt.SetLineColor(ROOT.kGreen)
    Tight_Pt.Draw("SAME")
    leg = ROOT.TLegend(.73,.32,.97,.53)
    leg.SetBorderSize(0)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.035)

    leg.AddEntry(NoID_Pt,"ID>0","L")
    leg.AddEntry(Loose_Pt,"ID>2","L")
    leg.AddEntry(Medium_Pt,"ID>4","L")
    leg.AddEntry(Tight_Pt,"ID>6","L")

    leg.Draw()
    c.SaveAs(outDir+fiName+".png")
    ROOT.gPad.SetLogy()
    c.SaveAs(outDir+fiName+"LOGY.png")
    c.Clear()
    ROOT.gPad.SetLogy(0)

def Make_PT_Overlays(Unmatched_Hist_Name, Mass, canvas, inFi, matched, outDir):
    NoID_Pt= inFi.Get('simple/'+Unmatched_Hist_Name.replace("REPLACEME","NoID")).ProjectionY()
    if (matched == "m"):
        title = "Electrons PT (MVA,Matched, "+Mass+")"
        fiName= "Electron_PT_Overlayed_Matched_mva_"+Mass
    elif(matched == "f"):
        title = "Electrons PT  (MVA,Fake, "+Mass+")"
        fiName= "Electron_PT_Overlayed_Fake_mva_"+Mass
    else:
        title = "Electrons PT (MVA,All, "+Mass+")"
        fiName= "Electron_PT_Overlayed_All_mva_"+Mass
    NoID_Pt.SetTitle(title)
    NoID_Pt.SetLineColor(ROOT.kBlack)
    NoID_Pt.Draw()
    Loose_Pt= inFi.Get('simple/'+Unmatched_Hist_Name.replace("REPLACEME","2")).ProjectionY()
    Loose_Pt.SetLineColor(ROOT.kRed)
    Loose_Pt.Draw("SAME")
    Medium_Pt= inFi.Get('simple/'+Unmatched_Hist_Name.replace("REPLACEME","4")).ProjectionY()
    Medium_Pt.SetLineColor(ROOT.kCyan)
    Medium_Pt.Draw("SAME")
    Tight_Pt= inFi.Get('simple/'+Unmatched_Hist_Name.replace("REPLACEME","6")).ProjectionY()
    Tight_Pt.SetLineColor(ROOT.kGreen)
    Tight_Pt.Draw("SAME")
    leg = ROOT.TLegend(.73,.32,.97,.53)
    leg.SetBorderSize(0)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.035)

    leg.AddEntry(NoID_Pt,"ID>0","L")
    leg.AddEntry(Loose_Pt,"ID>2","L")
    leg.AddEntry(Medium_Pt,"ID>4","L")
    leg.AddEntry(Tight_Pt,"ID>6","L")

    leg.Draw()
    c.SaveAs(outDir+fiName+".png")
    ROOT.gPad.SetLogy()
    c.SaveAs(outDir+fiName+"LogY.png")
    c.Clear()
    ROOT.gPad.SetLogy(0)

def Make_PT_Overlays_Std(Unmatched_Hist_Name, Mass, canvas, inFi, matched, outDir,nelec,ngen):
    NoID_Pt= inFi.Get('simple/'+Unmatched_Hist_Name.replace("REPLACEME","NoID"))
    if (matched == "m"):
        title = "Electrons PT (std,Matched, "+Mass+")"
        fiName= "Electron_PT_only_Overlayed_Matched_std_"+Mass
    elif(matched=="f"):
        title = "Electrons PT(std, Fake, "+Mass+")"
        fiName= "Electron_PT_only_Overlayed_Fake_std_"+Mass
    else:
        title = "Electrons PT (std, All, "+Mass+")"
        fiName= "Electron_PT_only_Overlayed_All_std_"+Mass

    NoID_Pt.SetTitle(title)
    NoID_Pt.SetLineColor(ROOT.kBlack)
    NoID_Pt.Draw()
    Loose_Pt= inFi.Get('simple/'+Unmatched_Hist_Name.replace("REPLACEME","Loose"))
    Loose_Pt.SetLineColor(ROOT.kRed)
    Loose_Pt.Draw("SAME")
    Medium_Pt= inFi.Get('simple/'+Unmatched_Hist_Name.replace("REPLACEME","Medium"))
    Medium_Pt.SetLineColor(ROOT.kCyan)
    Medium_Pt.Draw("SAME")
    Tight_Pt= inFi.Get('simple/'+Unmatched_Hist_Name.replace("REPLACEME","Tight"))
    Tight_Pt.SetLineColor(ROOT.kGreen)
    Tight_Pt.Draw("SAME")
    leg = ROOT.TLegend(.73,.32,.97,.53)
    leg.SetBorderSize(0)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.035)

    leg.AddEntry(NoID_Pt,"NoID","L")
    leg.AddEntry(Loose_Pt,"Loose","L")
    leg.AddEntry(Medium_Pt,"Medium","L")
    leg.AddEntry(Tight_Pt,"Tight","L")

    leg.Draw()
    c.SaveAs(outDir+fiName+".png")
    ROOT.gPad.SetLogy()
    c.SaveAs(outDir+fiName+"LogY.png")
    c.Clear()
    ROOT.gPad.SetLogy(0)
    if (matched == "m"):
        title = "IDIntegral (std,Matched, "+Mass+")"
        fiName= "ID_integral_Matched_std_"+Mass
    elif(matched == "f"):
        title = "ID Integrals (std, Fake, "+Mass+")"
        fiName= "ID_integral_Fake_std_"+Mass
    else:
        title = "ID Integrals (std, all, "+Mass+")"
        fiName= "ID_integral_All_std_"+Mass

    Integral_plot = ROOT.TH1F('Integral_plot', title+'(1/NLeading Candidates)',  4 ,0, 4)
    Integral_plot.SetBinContent(1,NoID_Pt.Integral(0,-1))
    Integral_plot.SetBinContent(2,Loose_Pt.Integral(0,-1))
    Integral_plot.SetBinContent(3,Medium_Pt.Integral(0,-1))
    Integral_plot.SetBinContent(4,Tight_Pt.Integral(0,-1))
    Integral_plot.Scale(1/nelec)
    Integral_plot.Draw()
    c.SaveAs(outDir+fiName+"Scale_nele.png")
    Integral_plot.Scale(nelec/ngen)
    Integral_plot.SetTitle(title+'(1/ngen)')
    Integral_plot.Draw()
    c.SaveAs(outDir+fiName+"Scale_ngen.png")

    


mass="QCD"
outdir = '/uscms_data/d3/nbower/FSU/LowPtIDStudies/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/myLowPtGsfElectronsAnalyzer/graphs/1_21_'+mass+"_Redo/"
checkAndMakeDir(outdir)
SFile = "/uscms_data/d3/nbower/FSU/LowPtIDStudies/CMSSW_10_6_12/src/myLowPtGsfElectronsAnalyzer/1_21_Redo_"+mass+".root"
signal =ROOT.TFile.Open(SFile ,"READ")
LeadingOnly_m = ROOT.TH1F('LeadingOnly_m', ' Matched Electron ID Efficiency (Leading Candidate Only)(1/NLeading Candidates)',  50 ,0, 10)
LeadingOnly_f = ROOT.TH1F('LeadingOnly_f', ' Fake Electron ID Efficiency (Leading Candidate Only)(1/NLeading Candidates)',  50 ,0, 10)
genElectrons_h= signal.Get('simple/Leading_Gen_Electron')
total_electrons_h = signal.Get('simple/All_Leading_electrons')
n_leading_electrons= total_electrons_h.ProjectionX().Integral(0,-1)
n_gen=genElectrons_h.Integral(0,-1)
if n_gen==0:
    n_gen=1
Electron_ID_PT_NoID_m = signal.Get('simple/Electron_ID_PT_NoID_m')
Electron_ID_PT_NoID_f = signal.Get('simple/Electron_ID_PT_NoID_f')
Make_PT_Overlays_Leading_only('Electron_ID_PT_REPLACEME_m',mass,c,signal,True,outdir)
Make_PT_Overlays_Leading_only('Electron_ID_PT_REPLACEME_f',mass,c,signal,False,outdir)
Make_PT_Overlays('Electron_ID_PT_REPLACEME_m', mass, c, signal, "m", outdir)
Make_PT_Overlays('Electron_ID_PT_REPLACEME_f', mass, c, signal, "f", outdir)
Make_PT_Overlays('Electron_ID_PT_REPLACEME', mass, c, signal, "", outdir)

for i in range (1,50):
    real=Electron_ID_PT_NoID_m.ProjectionX().Integral(i,50)
    fake = Electron_ID_PT_NoID_f.ProjectionX().Integral(i,50)
    LeadingOnly_m.SetBinContent(i,real)
    LeadingOnly_f.SetBinContent(i,fake)


LeadingOnly_f.Scale(1/n_leading_electrons)
LeadingOnly_m.Scale(1/n_leading_electrons)
LeadingOnly_f.Draw()
c.SaveAs(outdir+'Leading_electronOnly_fake_Total_eNorm_'+mass+".png")

LeadingOnly_m.Draw()
c.SaveAs(outdir+'Leading_electronOnly_real_Total_eNorm_'+mass+".png")
LeadingOnly_f.Scale(n_leading_electrons/n_gen)
LeadingOnly_m.Scale(n_leading_electrons/n_gen)
LeadingOnly_f.Draw()
LeadingOnly_m.SetTitle("Matched Electron ID Efficiency (Leading Candidate Only)(1/NGen Candidates)")
LeadingOnly_m.Draw()
c.SaveAs(outdir+'Leading_electronOnly_real_gen_eNorm_'+mass+".png")
LeadingOnly_f.SetTitle("Fake Electron ID Efficiency (Leading Candidate Only)(1/NGen Candidates)")
LeadingOnly_f.Draw()
c.SaveAs(outdir+'Leading_electronOnly_fake_gen_eNorm_'+mass+".png")
AllElectronsMatched=ROOT.TH1F ("AllElectronsMatched", "Electrons ID Matched Efficiency (Testing All Electrons)(1/NCandidates) "+mass, 10 ,0, 10  )
c.Clear()


for i in range(0,10):
    if i ==0:
        string = "Electron_ID_PT_NoID_m"
    else:
        string = "Electron_ID_PT_"+str(i)+"_m"
    print('simple/'+string)
    nevents = signal.Get('simple/'+string).ProjectionX().Integral(0,-1)
    AllElectronsMatched.SetBinContent(i+1,nevents)
AllElectronsMatched.Scale(1/n_leading_electrons)
AllElectronsMatched.Draw()
c.SaveAs(outdir+"Matched_Electron_Efficiency_AllConsidered_"+mass+".png")
AllElectronsFake=ROOT.TH1F ("AllElectronsFake", "Electrons ID Fake Efficiency(Testing All Electrons)(1/NCandidates) "+mass, 10 ,0, 10  )

AllElectrons=ROOT.TH1F ("AllElectrons", "Electrons ID  Efficiency (1/NCandidates) "+mass, 10 ,0, 10  )
c.Clear()


for i in range(0,10):
    if i ==0:
        string = "Electron_ID_PT_NoID"
    else:
        string = "Electron_ID_PT_"+str(i)
    print('simple/'+string)
    nevents = signal.Get('simple/'+string).ProjectionX().Integral(0,-1)
    AllElectrons.SetBinContent(i+1,nevents)
AllElectrons.Scale(1/n_leading_electrons)
AllElectrons.Draw()
c.SaveAs(outdir+"Electron_ID_Efficency_"+mass+".png")
for i in range(0,10):
    if i ==0:
        string = "Electron_ID_PT_NoID_f"
    else:
        string = "Electron_ID_PT_"+str(i)+"_f"
    nevents = signal.Get('simple/'+string).ProjectionX().Integral(0,-1)
    print(str(nevents)+"HEY OVERHERE DUMMY"+str(i+1)+"\n")
    AllElectronsFake.SetBinContent(i+1,nevents)


AllElectronsFake.Scale(1/n_leading_electrons)
AllElectronsFake.Draw()
c.SaveAs(outdir+"Fake_Electron_Efficiency_AllConsidered_"+mass+".png")
AllElectronsFake.SetTitle("Electrons ID Fake Efficiency   (Testing All Electrons)(1/NGen)")
AllElectronsFake.Scale(n_leading_electrons/n_gen)
AllElectronsFake.Draw()
c.SaveAs(outdir+"Fake_Electron_Efficiency_AllConsidered_"+mass+"ngen_scaled.png")
AllElectronsMatched.SetTitle("Electrons ID Matched Efficiency   (Testing All Electrons)(1/NGen)")
AllElectronsMatched.Scale(n_leading_electrons/n_gen)
AllElectronsMatched.Draw()
c.SaveAs(outdir+"Matched_Electron_Efficiency_AllConsidered_"+mass+"ngen_scaled.png")
AllElectrons.SetTitle("Electrons ID Matched Efficiency   (Testing All Electrons)(1/NGen)")
AllElectrons.Scale(n_leading_electrons/n_gen)
AllElectrons.Draw()
c.SaveAs(outdir+"Electron_Efficiency_AllConsidered_"+mass+"ngen_scaled.png")

Make_PT_Overlays_Std("std_ele_pt_REPLACEME_m", mass, c, signal, "m", outdir, n_leading_electrons,n_gen)
Make_PT_Overlays_Std("std_ele_pt_REPLACEME_f", mass, c, signal, "f", outdir, n_leading_electrons,n_gen)
Make_PT_Overlays_Std("std_ele_pt_REPLACEME", mass, c, signal, "", outdir, n_leading_electrons,n_gen)

NoID_Pt_m= signal.Get('simple/Electron_ID_PT_NoID_m').ProjectionY()
NoID_Pt_f= signal.Get('simple/Electron_ID_PT_NoID_f').ProjectionY()
NoID_Stack=ROOT.THStack("NoID_Stack", "NoID MVA ElePT Stack "+mass)
NoID_Pt_f.SetFillColor(ROOT.kBlue)
NoID_Pt_f.SetLineColor(ROOT.kBlue)
NoID_Stack.Add(NoID_Pt_f)
NoID_Pt_m.SetFillColor(ROOT.kGreen)
NoID_Pt_m.SetLineColor(ROOT.kGreen)
NoID_Stack.Add(NoID_Pt_m)
NoID_Stack.Draw()
leg = ROOT.TLegend(.73,.32,.97,.41)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
leg.AddEntry(NoID_Pt_m,"Matched","f")
leg.AddEntry(NoID_Pt_f,"Fake","f")

leg.Draw()
c.SaveAs(outdir+"NoID_MVA_Stacked"+mass+".png")    
c.Clear()

ID2_m= signal.Get('simple/Electron_ID_PT_2_m').ProjectionY()
ID2_f= signal.Get('simple/Electron_ID_PT_2_f').ProjectionY()
ID2_Stack=ROOT.THStack("ID2_Stack", "2 MVA ElePT Stack "+mass)
ID2_f.SetFillColor(ROOT.kBlue)
ID2_f.SetLineColor(ROOT.kBlue)
ID2_Stack.Add(ID2_f)
ID2_m.SetFillColor(ROOT.kGreen)
ID2_m.SetLineColor(ROOT.kGreen)
ID2_Stack.Add(ID2_m)
ID2_Stack.Draw()
leg = ROOT.TLegend(.73,.32,.97,.41)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
leg.AddEntry(ID2_m,"Matched","f")
leg.AddEntry(ID2_f,"Fake","f")

leg.Draw()
c.SaveAs(outdir+"2_MVA_Stacked"+mass+".png")    
c.Clear()
ID6_m= signal.Get('simple/Electron_ID_PT_6_m').ProjectionY()
ID6_f= signal.Get('simple/Electron_ID_PT_6_f').ProjectionY()
ID6_Stack=ROOT.THStack("ID6_Stack", "6 MVA ElePT Stack "+mass)
ID6_f.SetFillColor(ROOT.kBlue)
ID6_f.SetLineColor(ROOT.kBlue)
ID6_Stack.Add(ID6_f)
ID6_m.SetFillColor(ROOT.kGreen)
ID6_m.SetLineColor(ROOT.kGreen)
ID6_Stack.Add(ID6_m)
ID6_Stack.Draw()
leg = ROOT.TLegend(.73,.32,.97,.41)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
leg.AddEntry(ID6_m,"Matched","f")
leg.AddEntry(ID6_f,"Fake","f")

leg.Draw()
c.SaveAs(outdir+"6_MVA_Stacked"+mass+".png")    
c.Clear()
ID4_m= signal.Get('simple/Electron_ID_PT_4_m').ProjectionY()
ID4_f= signal.Get('simple/Electron_ID_PT_4_f').ProjectionY()
ID4_Stack=ROOT.THStack("ID4_Stack", "4 MVA ElePT Stack "+mass)
ID4_f.SetFillColor(ROOT.kBlue)
ID4_f.SetLineColor(ROOT.kBlue)
ID4_Stack.Add(ID4_f)
ID4_m.SetFillColor(ROOT.kGreen)
ID4_m.SetLineColor(ROOT.kGreen)
ID4_Stack.Add(ID4_m)
ID4_Stack.Draw()
leg = ROOT.TLegend(.73,.32,.97,.41)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
leg.AddEntry(ID4_m,"Matched","f")
leg.AddEntry(ID4_f,"Fake","f")

leg.Draw()
c.SaveAs(outdir+"4_MVA_Stacked"+mass+".png")    
c.Clear()

std_NoID_m=signal.Get('simple/std_ele_pt_NoID_m')
std_NoID_f=signal.Get('simple/std_ele_pt_NoID_f')
std_NoID_Stack=ROOT.THStack("std_NoID_Stack", "NoID Std ElePT Stack "+mass)
std_NoID_m.SetFillColor(ROOT.kBlue)
std_NoID_m.SetLineColor(ROOT.kBlue)
std_NoID_f.SetFillColor(ROOT.kRed)
std_NoID_f.SetLineColor(ROOT.kRed)
std_NoID_Stack.Add(std_NoID_f)
std_NoID_Stack.Add(std_NoID_m)
std_NoID_Stack.Draw()

leg = ROOT.TLegend(.73,.32,.97,.41)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
leg.AddEntry(std_NoID_m,"Matched","f")
leg.AddEntry(std_NoID_f,"Fake","f")

leg.Draw()
c.SaveAs(outdir+"std_NoID_Stacked"+mass+".png")    
c.Clear()
std_Medium_m=signal.Get('simple/std_ele_pt_Medium_m')
std_Medium_f=signal.Get('simple/std_ele_pt_Medium_f')
std_Medium_Stack=ROOT.THStack("std_Medium_Stack", "Medium Std ElePT Stack "+mass)
std_Medium_m.SetFillColor(ROOT.kBlue)
std_Medium_m.SetLineColor(ROOT.kBlue)
std_Medium_f.SetFillColor(ROOT.kRed)
std_Medium_f.SetLineColor(ROOT.kRed)
std_Medium_Stack.Add(std_Medium_f)
std_Medium_Stack.Add(std_Medium_m)
std_Medium_Stack.Draw()

leg = ROOT.TLegend(.73,.32,.97,.41)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
leg.AddEntry(std_Medium_m,"Matched","f")
leg.AddEntry(std_Medium_f,"Fake","f")

leg.Draw()
c.SaveAs(outdir+"std_Medium_Stacked"+mass+".png")    
c.Clear()
std_Loose_m=signal.Get('simple/std_ele_pt_Loose_m')
std_Loose_f=signal.Get('simple/std_ele_pt_Loose_f')
std_Loose_Stack=ROOT.THStack("std_Loose_Stack", "Loose Std ElePT Stack "+mass)
std_Loose_m.SetFillColor(ROOT.kBlue)
std_Loose_m.SetLineColor(ROOT.kBlue)
std_Loose_f.SetFillColor(ROOT.kRed)
std_Loose_f.SetLineColor(ROOT.kRed)
std_Loose_Stack.Add(std_Loose_f)
std_Loose_Stack.Add(std_Loose_m)
std_Loose_Stack.Draw()

leg = ROOT.TLegend(.73,.32,.97,.41)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
leg.AddEntry(std_Loose_m,"Matched","f")
leg.AddEntry(std_Loose_f,"Fake","f")

leg.Draw()
c.SaveAs(outdir+"std_Loose_Stacked"+mass+".png")    
c.Clear()
std_Tight_m=signal.Get('simple/std_ele_pt_Tight_m')
std_Tight_f=signal.Get('simple/std_ele_pt_Tight_f')
std_Tight_Stack=ROOT.THStack("std_Tight_Stack", "Tight Std ElePT Stack "+mass)
std_Tight_m.SetFillColor(ROOT.kBlue)
std_Tight_m.SetLineColor(ROOT.kBlue)
std_Tight_f.SetFillColor(ROOT.kRed)
std_Tight_f.SetLineColor(ROOT.kRed)
std_Tight_Stack.Add(std_Tight_f)
std_Tight_Stack.Add(std_Tight_m)
std_Tight_Stack.Draw()

leg = ROOT.TLegend(.73,.32,.97,.41)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
leg.AddEntry(std_Tight_m,"Matched","f")
leg.AddEntry(std_Tight_f,"Fake","f")

leg.Draw()
c.SaveAs(outdir+"std_Tight_Stacked"+mass+".png")    
c.Clear()


Electron_ID_PT_NoID_m=signal.Get("simple/Electron_ID_PT_NoID_m")
Electron_ID_PT_NoID_m.GetXaxis().SetTitle("MVA ID")
Electron_ID_PT_NoID_m.GetYaxis().SetTitle("Electron PT")
Electron_ID_PT_NoID_m.Draw("COL Z CJUST")
c.SaveAs(outdir+"TH2F_MVA_matched_"+mass+".png")
Electron_ID_NoID_m=Electron_ID_PT_NoID_m.ProjectionX()
Electron_ID_NoID_m.SetTitle("ID Distribution of Matched Leading Electrons")
Electron_ID_NoID_m.Draw()
c.SaveAs(outdir+"ID_MVA_matched_"+mass+".png")

Electron_ID_PT_NoID_f=signal.Get("simple/Electron_ID_PT_NoID_f")
Electron_ID_PT_NoID_f.GetXaxis().SetTitle("MVA ID")
Electron_ID_PT_NoID_f.GetYaxis().SetTitle("Electron PT")
Electron_ID_PT_NoID_f.Draw("COL Z CJUST")
c.SaveAs(outdir+"TH2F_MVA_fake_"+mass+".png")
Electron_ID_NoID_f=Electron_ID_PT_NoID_f.ProjectionX()
Electron_ID_NoID_f.SetTitle("ID Distribution of Fake Leading Electrons")
Electron_ID_NoID_f.Draw()
c.SaveAs(outdir+"ID_MVA_fake_"+mass+".png")
