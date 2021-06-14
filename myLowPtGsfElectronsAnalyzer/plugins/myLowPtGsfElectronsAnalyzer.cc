#include "DataFormats/CaloRecHit/interface/CaloCluster.h"
#include "DataFormats/CaloRecHit/interface/CaloClusterFwd.h"
#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/EcalRecHit/interface/EcalRecHit.h"
#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronCore.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronCoreFwd.h"
#include "DataFormats/EgammaReco/interface/SuperCluster.h"
#include "DataFormats/EgammaReco/interface/SuperClusterFwd.h"
#include "DataFormats/GsfTrackReco/interface/GsfTrack.h"
#include "DataFormats/GsfTrackReco/interface/GsfTrackFwd.h"
#include "DataFormats/ParticleFlowReco/interface/GsfPFRecTrack.h"
#include "DataFormats/ParticleFlowReco/interface/GsfPFRecTrackFwd.h"
#include "DataFormats/ParticleFlowReco/interface/PFCluster.h"
#include "DataFormats/ParticleFlowReco/interface/PFClusterFwd.h"
#include "DataFormats/ParticleFlowReco/interface/PFRecTrack.h"
#include "DataFormats/ParticleFlowReco/interface/PFRecTrackFwd.h"
#include "DataFormats/ParticleFlowReco/interface/PreId.h"
#include "DataFormats/ParticleFlowReco/interface/PreIdFwd.h"
#include "DataFormats/TrajectorySeed/interface/TrajectorySeed.h"
#include "DataFormats/TrackCandidate/interface/TrackCandidate.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include <string>
#include <vector>
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"
#include "TH2.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"
#include "TLorentzVector.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

using namespace std;
using namespace reco;
float muonIsoCut(pat::Muon m);
bool checkID( pat::ElectronRef e, int iD, double rho, float Esc);
bool sortEleByPt(pat::ElectronRef i, pat::ElectronRef j);
bool sortMuByPt(pat::Muon i, pat::Muon j);
bool sortJetByPt(pat::Jet i, pat::Jet j);
bool sortGenByPt(reco::GenParticle *i, reco::GenParticle *j);
bool sortTauByPt(pat::Tau i, pat::Tau j);
float deltaPhiCorrected(TLorentzVector a, TLorentzVector b);




void eHadSelection(std::vector<pat::ElectronRef> s_Eles,
std::vector<pat::Tau> s_Taus,
std::vector<pat::Jet> s_Jets,
TLorentzVector s_met, 
std::vector<TH2F**> Variable_Histos, 
TH1F **Selection_Histo, 
float w,
bool is_matched
);


void STD_Electron_Plotting(std::vector<pat::ElectronRef>  electrons,
std::vector<TH1F**> IDHists_m,
std::vector<TH1F**> IDHists_f,

std::vector<TH1F**> IDHists,
float w,
double rho,
std::vector<reco::GenParticle*> g_electrons);


void eHadSelection_Gen(std::vector<reco::GenParticle*> g_electrons, 
reco::GenParticle *g_tauhad, 
reco::GenParticle *g_nutauhad,
std::vector<pat::Jet> s_Jets, 
TLorentzVector s_met, 
std::vector<TH2F**> Variable_Histos, 
TH1F **Selection_Histo, 
float w,
bool diTauHad
);
std::pair<pat::ElectronRef*, pat::Tau*> eHad_Pair_Selection(std::vector<pat::ElectronRef> &s_electrons, 
std::vector<pat::Tau> &s_taus,
std::vector<std::pair<pat::ElectronRef*,pat::Tau*>> &pairVector
);

class myLowPtGsfElectronsAnalyzer: public edm::EDAnalyzer {

public:
  
  explicit myLowPtGsfElectronsAnalyzer( const edm::ParameterSet& );

  ~myLowPtGsfElectronsAnalyzer() {
  
  }

private:
  virtual void analyze( const edm::Event&, const edm::EventSetup& );
  const edm::EDGetTokenT<std::vector<reco::GenParticle> > genParticles_;
  const edm::EDGetTokenT<GenEventInfoProduct> genInfo_;
  const edm::EDGetTokenT< std::vector<pat::Electron> > electrons_;
  const edm::EDGetTokenT<double> eventrho_;
  const edm::EDGetTokenT<std::vector<pat::Muon>> muons_;
  const edm::EDGetTokenT<std::vector<reco::Vertex>> vertex_;
  const edm::EDGetTokenT<std::vector<pat::Jet>> jets_;
  const edm::EDGetTokenT<std::vector<reco::GenJet>> genJets_;
  const edm::EDGetTokenT<std::vector<pat::MET>> mets_;
  const edm::EDGetTokenT<std::vector<reco::GenMET>>  genMets_;
  const edm::EDGetTokenT<std::vector<pat::Tau>> taus_;
  const edm::EDGetTokenT<reco::ConversionCollection> convs_;
  const edm::EDGetTokenT<reco::BeamSpot> thebs_;
  const edm::EDGetTokenT< std::vector<pat::Electron> > gedElectrons_;

  TH1F *nLowPTElectron;
  TH1F *nGedElectron;

  TH2F *idHoverE;
  TH2F *idsigmaIetaIeta;
  TH2F *idPt;

  TH1F *nMu;
  TH1F *muPt;
  TH1F *muonIso;
  TH1F *nJets;
  TH1F *jetPt;
  TH1F *nIdSelected;
  TH1F *nMuPerEvent;
  TH1F *nJetPerEvent;
  TH1F *MET;
  TH1F *nElePerEvent;
  TH1F *vertexPt;
  TH1F *tauPt;
  TH1F *nTau;
  TH1F *nTauPerEvent;

  TH1F *nEvent_eHad_gen;
  TH1F *nEvent_eHad_Standard_NoID_m;
  TH2F *eHad_geometry_NoID_Standard_m;
  TH2F *eHad_MET_VS_JdPhiM_NoID_Standard_m;
  TH2F *eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m;
  TH2F *eHad_ID_PT_postGeo_NoID_Standard_m;
  TH2F *eHad_ID_PT_NoID_Standard_m;
  TH2F *eHad_Mvis_NoID_Standard_m;
  TH2F *eHad_METtoTau_JettoTau_NoID_Standard_m;
  TH2F *eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m;
  TH2F *eHad_METtoTau_JettoTau_PostMET_NoID_Standard_m;
  TH2F *eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m;

  


};

myLowPtGsfElectronsAnalyzer::myLowPtGsfElectronsAnalyzer( const edm::ParameterSet& cfg ) :
  genParticles_{consumes<std::vector<reco::GenParticle> >(edm::InputTag(std::string("prunedGenParticles")))},
  genInfo_{consumes<GenEventInfoProduct> (edm::InputTag(std::string("generator")))},
  electrons_{consumes< std::vector<pat::Electron> >(edm::InputTag(std::string("slimmedElectrons")))},  
  eventrho_{consumes<double>(edm::InputTag(std::string("fixedGridRhoFastjetAll")))},
  muons_{consumes<std::vector<pat::Muon>> (edm::InputTag(string("slimmedMuons")))},
  vertex_{consumes<std::vector<reco::Vertex>  >(edm::InputTag(std::string("offlineSlimmedPrimaryVertices")))},
  jets_{consumes<std::vector<pat::Jet>  >(edm::InputTag(std::string("slimmedJets")))},
  genJets_{consumes<std::vector<reco::GenJet>  >(edm::InputTag(std::string("slimmedGenJets")))},
  mets_{consumes<std::vector<pat::MET>> (edm::InputTag(std::string("slimmedMETs")))},
  taus_{consumes<std::vector<pat::Tau>> (edm::InputTag(std::string("slimmedTaus")))},
  gedElectrons_{consumes< std::vector<pat::Electron> >(edm::InputTag(std::string("slimmedElectrons")))}  

{

  edm::Service<TFileService> fs;
    //std::cout<<"create analyzer/n";

  nLowPTElectron = fs->make<TH1F>("nLowPTElectron", "N LowPT Electrons: " , 3,0,3);
  nGedElectron = fs->make<TH1F>("nGedElectron", "N Standard Electrons: " , 3,0,3);
//Event selection plots
//General Kinematic plots

  nMu = fs->make<TH1F>("nMuon", "NMu (Progressive Cuts): ", 6, 0 ,6);
  muPt = fs->make<TH1F>("muPt" , "Muon pt: " , 500 , 0 , 500 );
  jetPt = fs->make<TH1F>("jetPt" , "jet pt: " , 500 , 0 , 500 );
  tauPt = fs->make<TH1F>("tauPt" , "Tau pt" , 500 , 0 , 500 );
  muonIso = fs->make<TH1F>("muonIso" , "Muon Iso: " , 10 , 0 , 1 );
//Particle count plots
  nJets = fs->make<TH1F>("nJets", "NJets : ", 10, 0 ,10);
  nIdSelected = fs->make<TH1F>("nIdSelected" , "Electron ID: " , 50 ,0, 9.5 );
  nElePerEvent = fs->make<TH1F>("nElePerEvent", "NSelected Elec/event : ", 4, 0 ,4);
  nMuPerEvent = fs->make<TH1F>("nMuPerEvent", "NSelected Mu/event : ", 4, 0 ,4); 
  nJetPerEvent = fs->make<TH1F>("nJetPerEvent", "NSelected Jets/event : ", 8, 0 ,8);
  vertexPt = fs->make<TH1F>("VertexPt" , "Vertex Pt: " , 500 , 0 , 500 );
  MET = fs->make<TH1F>("MET" , "MET: " , 500 , 0 , 500 );
  tauPt = fs->make<TH1F>("tauPt" , "Tau Pt: " , 500 , 0 , 500 );
  nTauPerEvent = fs->make<TH1F>("nTauPerEvent", "NSelected Taus/event : ", 4, 0 ,4);
  nTau = fs->make<TH1F>("nTau", "NTaus : ", 3, 0 ,3);
  nEvent_eHad_Standard_NoID_m =fs->make<TH1F>("nEvent_eHad_Standard_NoID_m", "N Event (EHAD,Standard,NoID,Matched)" , 5,0,5);

  eHad_geometry_NoID_Standard_m=fs->make<TH2F>("eHad_geometry_NoID_Standard_m", "dR (Ele,Tau) Vs dR(Jet,Ele)  (EHAD,Standard,NoID,Matched) ",  120 , 0 , 6, 120,0,6);
  eHad_MET_VS_JdPhiM_NoID_Standard_m= fs->make<TH2F>("eHad_MET_VS_JdPhiM_NoID_Standard_m", "dPhi (MET,Jet) Vs Met  (EHAD,Standard,NoID,Matched) ",  20 ,-3.14 , 3.14, 500 , 0 , 500 );
  eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m= fs->make<TH2F>("eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m", "dPhi (MET,Jet) Vs Met postGeo (EHAD,Standard,NoID,Matched) ",  20 ,-3.14 , 3.14, 500 , 0 , 500 );
  eHad_ID_PT_NoID_Standard_m = fs->make<TH2F>("eHad_ID_PT_NoID_Standard_m" , "EHad Standard ID Val vs. Pt (EHAD,Standard,NoID,Matched)" , 50 , 0 , 10  , 30 , 0 , 400 );
  eHad_ID_PT_postGeo_NoID_Standard_m = fs->make<TH2F>("eHad_ID_PT_postGeo_NoID_Standard_m" , "EHad Standard ID Val vs. Pt (PostGeo) (EHAD,Standard,NoID,Matched)" , 50 , 0 , 10  , 30 , 0 , 400 );
  eHad_Mvis_NoID_Standard_m = fs->make<TH2F>("eHad_Mvis_NoID_Standard_m" , "EHad Mvis (EHAD,Standard,NoID,Matched)" , 1,0,1, 50, 0 , 50);
  eHad_METtoTau_JettoTau_NoID_Standard_m= fs->make<TH2F>("eHad_METtoTau_JettoTau_NoID_Standard_m", "dPhi (MET,Tau) Vs Dr(Jet,Tau)  (EHAD,NoID,Matched) ",  20 ,-3.14 , 3.14, 120,0,6 );
  eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m= fs->make<TH2F>("eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m", "dPhi (MET,Tau) Vs Dr(Jet,Tau) PostGeo  (EHAD,NoID,Matched) ",  20 ,-3.14 , 3.14, 120,0,6 );
  eHad_METtoTau_JettoTau_PostMET_NoID_Standard_m= fs->make<TH2F>("eHad_METtoTau_JettoTau_PostMET_NoID_Standard_m", "dPhi (MET,Tau) Vs Dr(Jet,Tau) PostMET  (EHAD,NoID,Matched) ",  20 ,-3.14 , 3.14, 120,0,6 );
  eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m= fs->make<TH2F>("eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m", "dPhi (MET,Jet) Vs Met postMET (EHAD,Standard,NoID,Matched) ",  20 ,-3.14 , 3.14, 500 , 0 , 500 );

}
void myLowPtGsfElectronsAnalyzer::analyze( const edm::Event& iEvent, 
					 const edm::EventSetup& iSetup )
{
//Standard NoID Matched Histos
  std::vector<TH2F**> eHad_Standard_NoID_Matched_TH2F;
  eHad_Standard_NoID_Matched_TH2F.push_back(&eHad_geometry_NoID_Standard_m);
  eHad_Standard_NoID_Matched_TH2F.push_back(&eHad_MET_VS_JdPhiM_NoID_Standard_m);
  eHad_Standard_NoID_Matched_TH2F.push_back(&eHad_ID_PT_NoID_Standard_m);
  eHad_Standard_NoID_Matched_TH2F.push_back(&eHad_Mvis_NoID_Standard_m);
  eHad_Standard_NoID_Matched_TH2F.push_back(&eHad_MET_VS_JdPhiM_postGeo_NoID_Standard_m);
  eHad_Standard_NoID_Matched_TH2F.push_back(&eHad_ID_PT_postGeo_NoID_Standard_m);
  eHad_Standard_NoID_Matched_TH2F.push_back(&eHad_METtoTau_JettoTau_NoID_Standard_m);
  eHad_Standard_NoID_Matched_TH2F.push_back(&eHad_METtoTau_JettoTau_PostGeo_NoID_Standard_m);
  eHad_Standard_NoID_Matched_TH2F.push_back(&eHad_METtoTau_JettoTau_PostMET_NoID_Standard_m);
  eHad_Standard_NoID_Matched_TH2F.push_back(&eHad_MET_VS_JdPhiM_postMET_NoID_Standard_m);


  string dataSet = "eMu";
/////////////////vertex loading///////////////////
  edm::Handle<std::vector<reco::Vertex>> hvertex;///Produce a pt distribution of vertex pt and sort vertex by pt.
  try{iEvent.getByToken(vertex_, hvertex);}
  catch (...){;}
  std::vector<reco::Vertex> vertex=*hvertex.product();
  for (unsigned int iVert=0; iVert<vertex.size(); ++iVert){
    reco::Vertex vert = vertex[iVert];
    vertexPt->Fill(vert.p4().Pt());
  }
//Get Particles
  edm::Handle<std::vector<pat::Jet>> jets;
  try{iEvent.getByToken(jets_, jets);}
  catch(...){;}
  std::vector<pat::Jet>  jetsV = *jets.product();  
  edm::Handle<std::vector<reco::GenJet>> genJets;
  try{iEvent.getByToken(genJets_, genJets);}
  catch(...){;}
  std::vector<pat::Jet>  genJetsV = *jets.product();

  edm::Handle< std::vector<reco::GenParticle> > genParticles;
  try{iEvent.getByToken(genParticles_, genParticles);}
  catch (...) {;}
  std::vector<reco::GenParticle>  genParticles_vec= *genParticles.product();


  edm::Handle<std::vector<pat::Tau>> taus;
  try{iEvent.getByToken(taus_, taus);}
  catch(...){;}
  std::vector<pat::Tau>  tausV = *taus.product();  


  edm::Handle< std::vector<pat::Electron> > gedElectrons;
  try { iEvent.getByToken(gedElectrons_, gedElectrons); }
  catch (...) {;}

  edm::Handle<std::vector<pat::MET>> mets;
  try{iEvent.getByToken(mets_, mets);}
  catch(...){;}
  std::vector<pat::MET> met_vec= *mets.product();
  pat::MET m = met_vec[0];
  //edm::Handle<std::vector<reco::GenMET>> genMets;
  //try{iEvent.getByToken(genMets_, genMets);}
  //catch(...){;}
  //std::vector<reco::GenMET> genMet_vec= *genMets.product();
  //reco::GenMET m = genMet_vec[0];
  TLorentzVector met;
  met.SetPtEtaPhiM(m.pt(),m.phi(),m.eta(),m.mass());

  edm::Handle<std::vector<pat::Muon>> muons;
  try{iEvent.getByToken(muons_, muons);}
  catch (...) {;}
  std::vector<pat::Muon> muonsV=*muons.product();
  //std::cout<<"Particles\n";
//Event level Info
  edm::Handle<GenEventInfoProduct>  genInfoHandle;
  try{iEvent.getByToken(genInfo_, genInfoHandle);}
  catch(...){;}
  double genWeight=genInfoHandle->weight();
  
  edm::Handle<double> eventrho;
  try {iEvent.getByToken(eventrho_, eventrho);}    
  catch (...) {;}
  double Rho = *eventrho.product();
  //std::cout<<"Event Info\n";
//############ ID#################
  //It Seems there may be two mva IDs in other parts of the code. 
  //currently I'm storing this as a vector with only one value
  //I'm not super confident in how these IDS are implimented
  // but I want to
  //std::vector< edm::Handle< edm::ValueMap<float> > > mvaIds;
  //for ( const auto& token : mvaIds_ ) { 
  //  edm::Handle< edm::ValueMap<float> > h;
  //  try { iEvent.getByToken(token, h); }
  //  catch (...) {;}
  //  mvaIds.push_back(h);
  //}

  //std::cout<<"Ids\n";
////////////////////Sort Gen Particles///////////////////////////////////
  std::vector<reco::GenParticle*> genElectrons;
  std::vector<reco::GenParticle*> genMuons;
  std::vector<reco::GenParticle*> genTaus;
  reco::GenParticle *genNuTau=NULL; //////These are just the tau neutrinos
  reco::GenParticle *genNuTauBar=NULL; //////These are just the tau neutrinos


  for(auto& gen : genParticles_vec){
    if(abs(gen.pdgId())==11 &&
      gen.isDirectHardProcessTauDecayProductFinalState()&&
      gen.pt()>1 &&
      abs(gen.eta())<2.5) {
        genElectrons.push_back(&gen);
    }
    if (abs(gen.pdgId())==13 &&
    gen.isDirectHardProcessTauDecayProductFinalState()&&
    gen.pt()>1 &&
    abs(gen.eta())<2.5){
      genMuons.push_back(&gen);
    }
    if (abs(gen.pdgId())==15 && gen.isHardProcess()){
      genTaus.push_back(&gen);
    }
    if (gen.pdgId()==16 && gen.isDirectHardProcessTauDecayProductFinalState()){
      genNuTau = &gen;
    }
    if (gen.pdgId()==-16 && gen.isDirectHardProcessTauDecayProductFinalState()){
      genNuTauBar = &gen;
    }
  }

//std::cout<<"Sort Gen\n";
//find gen tau had by checking charge of leptonic decay. Matching Nutrino to respetive Tau
  reco::GenParticle *genTauHad=NULL;
  reco::GenParticle *genNuTauHad=NULL;
  bool DiTauHad=false;
  if(genNuTauBar==NULL||genNuTau==NULL){
    //std::cout<<"Null Nu \n";
  }

  for (auto& gen : genTaus){
    if ((genElectrons.size()==1&& genMuons.size()==0)){
      if ((*genElectrons[0]).charge()<0&&(*gen).charge()>0){
            //std::cout<<"e-\n";

        genTauHad = gen;
        genNuTauHad = genNuTauBar;
      }
      if ((*genElectrons[0]).charge()>0&&(*gen).charge()<0){
                    //std::cout<<"e+\n";
        genTauHad = gen;
        genNuTauHad = genNuTau;
      }
    }
    else if((genElectrons.size()==0&& genMuons.size()==1)){
      if ((*genMuons[0]).charge()<0&&(*gen).charge()>0){
        //std::cout<<"m-\n";
        genTauHad = gen;
        genNuTauHad = genNuTauBar;
      }
      if ((*genMuons[0]).charge()>0&&(*gen).charge()<0){
        //std::cout<<"m+\n";
        genTauHad= gen;
        genNuTauHad = genNuTau;
      }

    }
          else{
        DiTauHad=true;
      }
  }
  

//Match Taus to their Neutrino in the case where 


/////////////////////////////////////////////////////////
/////             MUON Selection          ////////////////////////////////
///////////////////////////////////////////////////////
  std::vector<pat::Muon> selected_muons;
  for (unsigned int iMu=0; iMu<muonsV.size(); ++iMu){
    bool matched = false;
    pat::Muon muon = muonsV[iMu];
    nMu->Fill(.5,genWeight);


    if (muon::isLooseMuon(muon)==false){continue;}////////////Loose Muon ID

    nMu->Fill(1.5,genWeight);

    nMu->Fill(2.5,genWeight);
    if((muon.pt())<3|| muon.eta()>2.4){continue;} 
    nMu->Fill(3.5, genWeight);

    if (muonIsoCut(muon)>.25){continue;}
    nMu->Fill(4.5,genWeight);
    for(unsigned int iGenMu=0; iGenMu<genMuons.size(); iGenMu++){
      reco::GenParticle gen = *genMuons[iGenMu];
      TLorentzVector mu;
      TLorentzVector genMu;
      mu.SetPtEtaPhiM(muon.pt(), muon.eta(), muon.phi(), muon.mass());
      genMu.SetPtEtaPhiM(gen.pt(), gen.eta(), gen.phi(), gen.mass());
      float dr = genMu.DeltaR(mu);
      if(dr <.1){matched = true;}
    }
    if (matched==false){continue;}
    nMu->Fill(5.5,genWeight);
    selected_muons.push_back(muon);
    muPt->Fill(muon.pt());
  }

  //std::cout<<"Mus\n";

////////////////////////////////Tau Selection/////////////////////

  std::vector<pat::Tau> selected_taus_unmatched;
  std::vector<pat::Tau> selected_taus_matched;
  for (unsigned int iTau = 0; iTau<tausV.size();iTau++){
    pat::Tau tau = tausV[iTau];
    nTau->Fill(.5, genWeight);
    if (tau.pt()<10 || abs(tau.eta())>2.4){continue;}
    //if (tau.tauID("decayModeFinding")==false){continue;}
    nTau->Fill(1.5, genWeight);
    TLorentzVector t;
    TLorentzVector genT;
    TLorentzVector genNu;
    //std::cout<<"Tau Pre Null check\n";
    if(genTauHad==nullptr||genNuTauHad==nullptr){continue;}
    if(DiTauHad==true){continue;}
    //std::cout<<"Tau post Null check\n";

    reco::GenParticle thad =*genTauHad;
        //std::cout<<"Gen Tau assignment check\n";

    reco::GenParticle nt = *genNuTauHad;
    //std::cout<<"Gen nu assignment check\n";

    t.SetPtEtaPhiM(tau.pt(), tau.eta(), tau.phi(), tau.mass());
    //std::cout<<"TLorentz Vector Tau\n";

    genT.SetPtEtaPhiM(thad.pt(), thad.eta(), thad.phi(), thad.mass());
        //std::cout<<"TLorentz Vector genTau\n";

    genNu.SetPtEtaPhiM(nt.pt(), nt.eta(), nt.phi(), nt.mass());
        //std::cout<<"TLorentz Vector NuTau\n";

    if(t.DeltaR(genT-genNu)>.1){continue;}
            //std::cout<<"Delta R\n";

    nTau->Fill(2.5, genWeight);
    selected_taus_matched.push_back(tau);
  }
   //std::cout<<"Taus\n";


///////////////////////   Jet Selection /////////////////////////////////////////
  std::vector<pat::Jet> selected_jets;
  std::vector<pat::Jet> selected_bjets;
  for (unsigned int iJet=0;iJet<jetsV.size(); iJet++){
    pat::Jet jet = jetsV[iJet];
    nJets->Fill(.5,genWeight);
    if (jet.pt()>500 && abs(jet.eta())<2.5 ){
      nJets->Fill(1.5,genWeight);

      float NHF  = jet.neutralHadronEnergyFraction();
      float NEMF = jet.neutralEmEnergyFraction();
      float CHF  = jet.chargedHadronEnergyFraction();
      float MUF  = jet.muonEnergyFraction();
      float CEMF = jet.chargedEmEnergyFraction();
      float NumConst = jet.chargedMultiplicity()+jet.neutralMultiplicity();
      float CHM = jet.chargedMultiplicity();
      if (CEMF>0.8){continue;}
      nJets->Fill(2.5,genWeight);
      if (CHM<0){continue;}
      nJets->Fill(3.5,genWeight);
      if (CHF <0){continue;}
      nJets->Fill(4.5,genWeight);

      if (NumConst<1){continue;}
      nJets->Fill(5.5,genWeight);

      if (NEMF>0.9){continue;}
      nJets->Fill(6.5,genWeight);
      if (MUF>0.8){continue;}
      nJets->Fill(7.5,genWeight);
      if (NHF>.9){continue;}
      nJets->Fill(8.5,genWeight);

      nJets->Fill(9.5,genWeight);
      TLorentzVector j;
      TLorentzVector genj;
      j.SetPtEtaPhiM(jet.pt(),jet.eta(),jet.phi(),jet.mass());

      for (auto& gen: genJetsV){
        genj.SetPtEtaPhiM(gen.pt(),gen.eta(),gen.phi(),gen.mass());

        if(j.DeltaR(genj)>.1){continue;} 
        else {
          selected_jets.push_back(jet); 
          break;
        }
      }
      
        //std::cout<<"testjets";
                
    }
  }


/////////////////////////// MVAElectron Selection //////////////////




  
//std::cout<<"MVAELEs\n";

/////////////////////////// GEDElectron Selection //////////////////

  std::vector<pat::ElectronRef> selected_standard_electrons_LooseID_matched;
  std::vector<pat::ElectronRef> selected_standard_electrons_MediumID_matched;
  std::vector<pat::ElectronRef> selected_standard_electrons_noID_matched;
  std::vector<pat::ElectronRef> selected_standard_electrons_TightID_matched;
  std::vector<pat::ElectronRef> selected_standard_electrons_LooseID_unmatched;
  std::vector<pat::ElectronRef> selected_standard_electrons_MediumID_unmatched;
  std::vector<pat::ElectronRef> selected_standard_electrons_noID_unmatched;
  std::vector<pat::ElectronRef> selected_standard_electrons_TightID_unmatched;
  std::vector<pat::ElectronRef> selected_standard_electrons_TightID_antimatched;
  std::vector<pat::ElectronRef> selected_standard_electrons_MediumID_antimatched;
  std::vector<pat::ElectronRef> selected_standard_electrons_noID_antimatched;
  std::vector<pat::ElectronRef> selected_standard_electrons_LooseID_antimatched;
  for(unsigned int iElec = 0; iElec<gedElectrons->size(); iElec++){
    pat::ElectronRef ele (gedElectrons, iElec);
    nGedElectron->Fill(.5, genWeight);
    bool matched = false;//For TCP
    float drmin=99999.9;
    if (ele->pt()>7 &&
    ele.isNonnull() &&
    abs(ele->eta())<2.5){
      nGedElectron->Fill(1.5, genWeight);
      float E_c=ele->superCluster()->energy();
      selected_standard_electrons_noID_unmatched.push_back(ele);
      if (checkID(ele, 1, Rho, E_c)==true){
        selected_standard_electrons_LooseID_unmatched.push_back(ele);
      }
      if (checkID(ele, 2, Rho, E_c)==true){
        selected_standard_electrons_MediumID_unmatched.push_back(ele);
      }
      if (checkID(ele, 3, Rho, E_c)==true){
        selected_standard_electrons_TightID_unmatched.push_back(ele);
      }
      for(unsigned int iGenE=0; iGenE<genElectrons.size(); iGenE++){
        reco::GenParticle gen = *genElectrons[iGenE];
        TLorentzVector e;
        TLorentzVector genE;
        e.SetPtEtaPhiM(ele->pt(), ele->eta(), ele->phi(), ele->mass());
        genE.SetPtEtaPhiM(gen.pt(), gen.eta(), gen.phi(), gen.mass());
        float dr = genE.DeltaR(e);
        if(dr <.1&& ele->pt()>1&&dr<drmin){
          matched = true;
          drmin=dr;
        }
      }
      if (matched==true){
        nGedElectron->Fill(2.5, genWeight);
        selected_standard_electrons_noID_matched.push_back(ele);
        if (checkID(ele, 1, Rho, E_c)==true){
          selected_standard_electrons_LooseID_matched.push_back(ele);
        }
        if (checkID(ele, 2, Rho, E_c)==true){
          selected_standard_electrons_MediumID_matched.push_back(ele);
        }
        if (checkID(ele, 3, Rho, E_c)==true){
          selected_standard_electrons_TightID_matched.push_back(ele);
        }
      }
      else{
        selected_standard_electrons_noID_antimatched.push_back(ele);
        if (checkID(ele, 1, Rho,E_c)==true){
          selected_standard_electrons_LooseID_antimatched.push_back(ele);
        }
        if (checkID(ele, 2, Rho, E_c)==true){
          selected_standard_electrons_MediumID_antimatched.push_back(ele);
        }
        if (checkID(ele, 3, Rho, E_c)==true){
          selected_standard_electrons_TightID_antimatched.push_back(ele);
        }
      }
    }
  }
//std::cout<<"standard eles\n";

///////////////Sorting//////////////////
  sort(selected_jets.begin(),selected_jets.end(), sortJetByPt);
  sort(selected_muons.begin(),selected_muons.end(), sortMuByPt);
  sort(selected_standard_electrons_noID_unmatched.begin(),selected_standard_electrons_noID_unmatched.end(), sortEleByPt);
  sort(selected_standard_electrons_LooseID_unmatched.begin(),selected_standard_electrons_LooseID_unmatched.end(), sortEleByPt);
  sort(selected_standard_electrons_MediumID_unmatched.begin(),selected_standard_electrons_MediumID_unmatched.end(), sortEleByPt);
  sort(selected_standard_electrons_TightID_unmatched.begin(),selected_standard_electrons_TightID_unmatched.end(), sortEleByPt);
  sort(selected_standard_electrons_noID_antimatched.begin(),selected_standard_electrons_noID_antimatched.end(), sortEleByPt);
  sort(selected_standard_electrons_LooseID_antimatched.begin(),selected_standard_electrons_LooseID_antimatched.end(), sortEleByPt);
  sort(selected_standard_electrons_MediumID_antimatched.begin(),selected_standard_electrons_MediumID_antimatched.end(), sortEleByPt);
  sort(selected_standard_electrons_TightID_antimatched.begin(),selected_standard_electrons_TightID_antimatched.end(), sortEleByPt);
  
  sort(selected_standard_electrons_noID_matched.begin(),selected_standard_electrons_noID_matched.end(), sortEleByPt);
  sort(selected_standard_electrons_LooseID_matched.begin(),selected_standard_electrons_LooseID_matched.end(), sortEleByPt);
  sort(selected_standard_electrons_MediumID_matched.begin(),selected_standard_electrons_MediumID_matched.end(), sortEleByPt);
  sort(selected_standard_electrons_TightID_matched.begin(),selected_standard_electrons_TightID_matched.end(), sortEleByPt);


  sort(genElectrons.begin(),genElectrons.end(), sortGenByPt);
//std::cout<<"Sorting\n";

  sort(selected_taus_matched.begin(),selected_taus_matched.end(), sortTauByPt);

  ///////////////////////////////////EMu Event/ electron selection ////////////////////////////
  ///////////////////////////////////////////////////////////////////////////////////////////


        //std::cout<<"Pair Creation: stdfake\n";

  

  /////////////////////////////////////////////////////
  //////////////////TauE Tau Had//////////////////////////
  ///////////////////////////////////////////////////////
  //std::cout<<"STD Plots\n";


    eHadSelection(selected_standard_electrons_noID_matched, selected_taus_matched, selected_jets, met, eHad_Standard_NoID_Matched_TH2F,&nEvent_eHad_Standard_NoID_m,genWeight, true);
}

//std::cout<<"Done with Fuckin everything\n";
   //std::cout<<"JEts\n";

///////Standard ID Cut Method////////////////////////
bool checkID(pat::ElectronRef e, int iD, double rho, float Esc) {
  float hoverECut=0.0;
  float SigmaIeIeCut=0;
  float EinvPinvCut = 0;
  unsigned int missingHitsCut=0;
  float dEtaInSeedCut=0;
  float dPhiCut=0;
  float ePt = e->pt();
  bool result=false;
  float dEtaInSeed = e->deltaEtaSuperClusterTrackAtVtx()-e->superCluster()->eta()+e->superCluster()->seed()->eta();
  float GsfEleEInverseMinusPInverse = abs((1.0-e->eSuperClusterOverP())/e->ecalEnergy());
  constexpr reco::HitPattern::HitCategory missingHitType = reco::HitPattern::MISSING_INNER_HITS;
  const unsigned int mhits = e->gsfTrack()->hitPattern().numberOfAllHits(missingHitType);
  if (e->isEB()){
    if (iD==0){
      hoverECut = .05+1.16/Esc+.0324*rho/Esc;
      SigmaIeIeCut =.0126;
      dEtaInSeedCut = .00463;
      dPhiCut = .148;
      EinvPinvCut = .209;
      missingHitsCut = 2;
    }
    else if (iD==1){
      hoverECut = .05+1.16/Esc+.0324*rho/Esc;
      SigmaIeIeCut =.0112;
      dEtaInSeedCut = .00377;
      dPhiCut = .0884;
      EinvPinvCut = .193;
      missingHitsCut = 1;
    }
    else if (iD==3){
      hoverECut = .05+1.16/Esc+.0324*rho/Esc;
      SigmaIeIeCut =.0104;
      dEtaInSeedCut = .00255;
      dPhiCut = .022;
      EinvPinvCut = .159;
      missingHitsCut = 1;
    }
    else if (iD==2){
      hoverECut = .05+1.16/Esc+.0324*rho/Esc;
      SigmaIeIeCut =.0106;
      dEtaInSeedCut = .0032;
      dPhiCut = .0547;
      EinvPinvCut = .184;
      missingHitsCut = 1;
    } 
  }
  if (e->isEE()){
    if (iD==0){
      hoverECut = .05+2.54/Esc+.183*rho/Esc;
      SigmaIeIeCut =.0457;
      dEtaInSeedCut = .00814;
      dPhiCut = .19;
      EinvPinvCut = .132;
      missingHitsCut = 3;
    }
    else if (iD==1){
      hoverECut = .05+2.54/Esc+.183*rho/Esc;
      SigmaIeIeCut =.0425;
      dEtaInSeedCut = .00674;
      dPhiCut = .169;
      EinvPinvCut = .111;
      missingHitsCut = 1;
    }
    else if (iD==2){
      hoverECut = .05+2.54/Esc+.183*rho/Esc;
      SigmaIeIeCut =.0387;
      dEtaInSeedCut = .00632;
      dPhiCut = .0394;
      EinvPinvCut = .0721;
      missingHitsCut = 1;
    }
    else if (iD==3){
      hoverECut = .05+2.54/Esc+.183*rho/Esc;
      SigmaIeIeCut =.0353;
      dEtaInSeedCut = .00501;
      dPhiCut = .0236;
      EinvPinvCut = .0197;
      missingHitsCut = 1;
    } 
  }
  if(e->full5x5_sigmaIetaIeta()<SigmaIeIeCut &&
  e->hadronicOverEm()<hoverECut &&
  dEtaInSeed<dEtaInSeedCut &&
  e->deltaPhiSuperClusterTrackAtVtx()<dPhiCut &&
  GsfEleEInverseMinusPInverse<EinvPinvCut&&
  mhits <= missingHitsCut&& ePt>7
  ){
    result =  true;
  }
  else{result =  false;}
  return result;
}
////////////////Isolation Cut////////////////
float muonIsoCut(pat::Muon m){
  float  iso = (m.pfIsolationR04().sumPhotonEt+m.pfIsolationR04().sumNeutralHadronEt-0.5*m.pfIsolationR04().sumPUPt)/m.pt();
  if  (iso<0){iso=0;}
  iso = iso+ m.pfIsolationR04().sumChargedHadronPt/m.pt();
  return iso;
}



///////////////////EHAD_UNMATCH//////////////////
void eHadSelection(std::vector<pat::ElectronRef> s_Eles,
std::vector<pat::Tau> s_Taus,
std::vector<pat::Jet> s_Jets,
TLorentzVector s_met, 
std::vector<TH2F**> Variable_Histos, 
TH1F **Selection_Histo, 
float w,
bool is_matched
){
  (*Selection_Histo)->Fill(.5,w);
  //std::cout<<"Len of plots:\n";
  if(s_Eles.size()>0){
    (*Selection_Histo)->Fill(1.5,w);
    //std::cout<<"Len of plots:"<<to_string((s_Eles).size())<<"\n";

    if(s_Taus.size()>0){
      (*Selection_Histo)->Fill(2.5,w);
      if(s_Jets.size()>0){
        (*Selection_Histo)->Fill(3.5,w);
        TLorentzVector j;
        if ((s_Eles.size()>1) &&((s_Eles[0]->pt())<(s_Eles[1]->pt()))){
          //std::cout<<"Electrons out of order";
        }
        if ((s_Taus.size()>0) &&(s_Taus[0].pt()<s_Taus[1].pt())){
          //std::cout<<"Taus out of order";
        }        
        if ((s_Jets.size()>0) && (s_Jets[0].pt()<s_Jets[1].pt())){
          //std::cout<<"Jets out of order";
        }
        j.SetPtEtaPhiM(s_Jets[0].pt(), s_Jets[0].eta(), s_Jets[0].phi(), s_Jets[0].mass());
        TLorentzVector e;
        e.SetPtEtaPhiM(s_Eles[0]->pt(), s_Eles[0]->eta(), s_Eles[0]->phi(), s_Eles[0]->mass());
        TLorentzVector t;
        t.SetPtEtaPhiM(s_Taus[0].pt(), s_Taus[0].eta(), s_Taus[0].phi(), s_Taus[0].mass());
        float metphi=s_met.Phi();
        //std::cout<<"get metphi";

        (*Variable_Histos[0])->Fill(e.DeltaR(t),e.DeltaR(j),w);
        (*Variable_Histos[1])->Fill(reco::deltaPhi(metphi,s_Jets[0].phi()),s_met.Pt(),w); 
        //std::cout<<"try Dphi";
        float idVal = 0.50;

        float elept = s_Eles[0]->pt();
        (*Variable_Histos[2])->Fill(idVal,elept, w);
        (*Variable_Histos[6])->Fill(reco::deltaPhi(metphi,s_Taus[0].phi()),t.DeltaR(j), w);

        if (t.DeltaR(e)<.4 && t.DeltaR(j)>.8 && e.DeltaR(j)>.8){

          (*Variable_Histos[4])->Fill(reco::deltaPhi(metphi,s_Jets[0].phi()),s_met.Pt(),w);

          (*Selection_Histo)->Fill(4.5,w);
          if(s_met.Pt()>100){
            if(s_Eles[0]->charge()*s_Taus[0].charge()<0){
              float mvis= (e+t).M();
              (*Variable_Histos[8])->Fill(reco::deltaPhi(metphi,s_Taus[0].phi()),t.DeltaR(j), w);
              (*Variable_Histos[9])->Fill(reco::deltaPhi(metphi,s_Jets[0].phi()),s_met.Pt(),w);

              (*Variable_Histos[3])->Fill(0. , mvis, w);
            }
          }
          
          (*Variable_Histos[5])->Fill(idVal,elept, w);
          (*Variable_Histos[7])->Fill(reco::deltaPhi(metphi,s_Taus[0].phi()),t.DeltaR(j), w);


        }
      }
    }
  }
}

void STD_Electron_Plotting(std::vector<pat::ElectronRef>  &electrons,
std::vector<TH1F**> IDHists_m,
std::vector<TH1F**> IDHists_f,
std::vector<TH1F**> IDHists,
float w,
double rho,
std::vector<reco::GenParticle*> g_electrons
){
  for (unsigned int iD = 0; iD<4; iD++){
    for (auto& ele : electrons){
      float elePt = (ele)->pt();
      float Esc=ele->superCluster()->energy();
      bool matched = false;
      bool passID=false;
      if (iD==0){
        passID=true;
      }
      else{
        passID=checkID(ele,iD-1,rho,Esc);
      }
      if (passID){
        for(auto& gen:g_electrons){
          TLorentzVector e;
          e.SetPtEtaPhiM(ele->pt(), ele->eta(), ele->phi(), ele->mass());
          TLorentzVector g;
          g.SetPtEtaPhiM((*gen).pt(), (*gen).eta(), (*gen).phi(), (*gen).mass());
          if(e.DeltaR(g)<.1){matched=true;}
        }
        (*IDHists[iD])->Fill(elePt, w);
        if (matched==true){
          (*IDHists_m[iD])->Fill(elePt, w);
        }
        else{(*IDHists_f[iD])->Fill(elePt, w);}
        break;
      }
    }
  }
}

void eHadSelection_Gen(std::vector<reco::GenParticle*> g_electrons, 
reco::GenParticle *g_tauhad, 
reco::GenParticle *g_nutauhad,
std::vector<pat::Jet> s_Jets, 
TLorentzVector s_met, 
std::vector<TH2F**> Variable_Histos, 
TH1F **Selection_Histo, 
float w,
bool diTauHad
){ 
  (*Selection_Histo)->Fill(.5,w);
  if(g_electrons.size()==1){
    (*Selection_Histo)->Fill(1.5,w);
    if (g_tauhad!=NULL){
      if(g_nutauhad!=NULL){
        if(diTauHad==false){
          (*Selection_Histo)->Fill(1.5,w);
          if(s_Jets.size()>0){
            (*Selection_Histo)->Fill(2.5,w);
            //std::cout<<"GenJets\n";
            reco::GenParticle ele = *(g_electrons[0]);
            //std::cout<<"GenEle\n";
            TLorentzVector j;
            j.SetPtEtaPhiM(s_Jets[0].pt(), s_Jets[0].eta(), s_Jets[0].phi(), s_Jets[0].mass());
            TLorentzVector e;
            e.SetPtEtaPhiM(ele.pt(), ele.eta(), ele.phi(), ele.mass());
            TLorentzVector t;
            //std::cout<<"Gene\n";
            t.SetPtEtaPhiM((*g_tauhad).pt(), (*g_tauhad).eta(), (*g_tauhad).phi(), (*g_tauhad).mass());
            TLorentzVector n;
            //std::cout<<"Gen TauH\n";
            n.SetPtEtaPhiM((*g_nutauhad).pt(), (*g_nutauhad).eta(), (*g_nutauhad).phi(), (*g_nutauhad).mass());
            //std::cout<<"Gen Nu\n";
            (*Variable_Histos[0])->Fill(e.DeltaR(t-n),e.DeltaR(j),w);
            (*Variable_Histos[1])->Fill(deltaPhiCorrected(j,s_met),s_met.Pt(),w);
            (*Variable_Histos[2])->Fill(.5,ele.pt(), w);
            //std::cout<<"0-3GenPlots\n";
            if ((t-n).DeltaR(e)<.4 && (t-n).DeltaR(j)>.8 && e.DeltaR(j)>.8 && s_met.Pt()>100){
              float mvis=(e+t-n).M();
              (*Variable_Histos[3])->Fill(0. ,mvis, w);
                //std::cout<<"5GenPlots\n";

              (*Variable_Histos[4])->Fill(deltaPhiCorrected(j,s_met),s_met.Pt(),w);
              (*Selection_Histo)->Fill(3.5,w);
              (*Variable_Histos[5])->Fill(0.5, ele.pt(), w);
            //std::cout<<"5GenPlots\n";

              
            }
          }
        }
      } 
    }    
  }
}

std::pair<pat::ElectronRef*,pat::Tau*> eHad_Pair_Selection(std::vector<pat::ElectronRef> &s_electrons, 
std::vector<pat::Tau> &s_taus,
std::vector<std::pair<pat::ElectronRef*,pat::Tau*>> &pairVector
){

  std::pair<pat::ElectronRef*,pat::Tau*> best_pair (nullptr,nullptr);
  float minDr=9999.9;
  if(s_taus.empty() ||s_electrons.empty()){return best_pair;}
  for(auto& ele : s_electrons){
    for(auto& tau : s_taus){
      TLorentzVector e;
      e.SetPtEtaPhiM((ele)->pt(),(ele)->eta(),(ele)->phi(),(ele)->mass());
      TLorentzVector t;
      t.SetPtEtaPhiM((tau).pt(), (tau).eta(), (tau).phi(), (tau).mass());
      //std::cout<<"Pair Creation: TVector\n";
      if (e.DeltaR(t)>.05){
        std::pair<pat::ElectronRef*,pat::Tau*> etau (&ele,&tau);
        (pairVector).push_back(std::pair<pat::ElectronRef*,pat::Tau*> (&ele, &tau));
        if (e.DeltaR(t)<minDr){
          best_pair=etau;
          minDr=e.DeltaR(t);
        }
      }
    }
  }
  return best_pair;
}
float deltaPhiCorrected(TLorentzVector a, TLorentzVector b){
  float d=a.DeltaPhi(b);
  float pi = 3.14159265358979323846; 
  //std::cout<<"DeltaPhi Test Pre Correction "<< to_string(d)<<"\n";

  if (d>pi){
    d = d-2*pi;
  }
  if(d<-pi){d = d+2*pi;}
  //std::cout<<"DeltaPhi Test Post Correction "<< to_string(d)<<"\n";
  return d;
}



bool sortEleByPt(pat::ElectronRef i, pat::ElectronRef j){return i->pt()> j->pt();}
bool sortGenByPt(reco::GenParticle *i, reco::GenParticle *j){return (*i).pt()> (*j).pt();}

bool sortMuByPt(pat::Muon i, pat::Muon j){return i.pt()> j.pt();}
bool sortJetByPt(pat::Jet i, pat::Jet j){return i.pt()> j.pt();}
bool sortTauByPt(pat::Tau i, pat::Tau j){return i.pt()> j.pt();}

bool sortVertByPt(reco::Vertex i, reco::Vertex j){return i.p4().Pt()>j.p4().Pt();}

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(myLowPtGsfElectronsAnalyzer);
