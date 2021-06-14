import os, sys, random
import numpy as np
import glob
import subprocess
import sys,string
import ConfigParser


HistParams=[
    ["eHad_geometry_REPLACEME",' "dR (Ele,Tau) Vs dR(Jet,Ele)  (EHAD,REPLACEME) ",  120 , 0 , 6, 120,0,6)'],
    ["eHad_MET_VS_JdPhiM_REPLACEME",' "dPhi (MET,Jet) Vs Met  (EHAD,REPLACEME) ",  20 ,-3.14 , 3.14, 500 , 0 , 500 )'],
    ["eHad_ID_PT_REPLACEME",' "EHad Standard ID Val vs. Pt (EHAD,REPLACEME)" , 50 , 0 , 10  , 30 , 0 , 400 )'],
    ["eHad_Mvis_allPairs_REPLACEME",' "EHad Mvis (EHAD,REPLACEME)" , 1,0,1, 50, 0 , 50)'],
    ["eHad_MET_VS_JdPhiM_postGeo_REPLACEME",' "dPhi (MET,Jet) Vs Met postGeo (EHAD,REPLACEME) ",  20 ,-3.14 , 3.14, 500 , 0 , 500 )'],
    ["eHad_ID_PT_postGeo_REPLACEME",' "EHad Standard ID Val vs. Pt (PostGeo) (EHAD,REPLACEME)" , 50 , 0 , 10  , 30 , 0 , 400 )'],
    ["eHad_geometry_allPairs_REPLACEME",' "dR (Ele,Tau) Vs dR(Jet,Ele)  [All Pairs] (EHAD,REPLACEME) ",  120 , 0 , 6, 120,0,6)'],
    ["eHad_ID_PT_allPairs_REPLACEME",' "EHad Standard ID Val vs. Pt [All Pairs] (EHAD,REPLACEME)" , 50 , 0 , 10  , 30 , 0 , 400 )'],
    ["eHad_Mvis_allPairs_REPLACEME",' "EHad Mvis [All Pairs] (EHAD,REPLACEME)" , 1,0,1, 50, 0 , 50)'],
    ["eHad_METtoTau_JettoTau_REPLACEME",' "dPhi (MET,Tau) Vs Dr(Jet,Tau)  (EHAD,REPLACEME) ",  20 ,-3.14 , 3.14, 120,0,6 )'],
    ["eHad_METtoTau_JettoTau_PostGeo_REPLACEME", ' "dPhi (MET,Tau) Vs Dr(Jet,Tau) PostGeo  (EHAD,REPLACEME) ",  20 ,-3.14 , 3.14, 120,0,6 )']
]
Matching=[
    ["Fake","_f"],
    ["Matched","_m"],
    ["Unmatched",""]
]
Reco=["MVA","Standard"]
IDCuts=["NoID","Loose","Medium","Tight"]


def Build_Declarations(hnames, matching, recos, IDs):
    Declaration_String = ""
    for match in matching:
        for ID in IDs:
            for reco in recos:
                Declaration_String += "\\\\"+ID+" "+match[0]+" "+reco+";\n" 
                for histname in histogram_names:
                    Declaration_String+= "   TH2F *"+histname[0].replace("REPLACEME", ID+"_"+reco+match[1])+""+";\n"
    return Declaration_String

def Build_MakeHists(hnames, matching, recos, IDs):
    Declaration_String = ""
    for match in matching:
        for ID in IDs:
            for reco in recos:
                Declaration_String += "\\\\"+ID+" "+match[0]+" "+reco+";\n" 
                for histname in hnames:
                    Declaration_String+= "   "+histname[0].replace("REPLACEME", ID+"_"+reco+match[1])+'=fs->make<TH1F>("'+histname[0].replace("REPLACEME", ID+"_"+reco+match[1])+'","'+hnames[1].replace("REPLAME",reco+","+ID+","+match)+";\n"
    return Declaration_String
def Build_Vectors(hnames, matching, recos, IDs):
    vectorstring=""
    for match in matching:
        for ID in IDs:
            for reco in recos:
                vectorstring+= "std::vector<TH2F**> eHad_"+reco+"_"+ID+"_"+match[0]+"_TH2F;"
                for histname in hnames:
                    vectorstring+="eHad_"+reco+"_"+ID+"_"+match[0]+"_TH2F.push_back(&"+histname[0].replace("REPLACEME", ID+"_"+reco+match[1])+");"





#cfg=open(configDir+file.replace(".txt","cfg.py"),"w")