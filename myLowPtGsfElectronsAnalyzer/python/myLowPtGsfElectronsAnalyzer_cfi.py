import FWCore.ParameterSet.Config as cms

simple = cms.EDAnalyzer("myLowPtGsfElectronsAnalyzer",
                        electrons = cms.InputTag("lowPtGsfElectrons"),
                        genParticles = cms.InputTag("prunedGenParticles"),
                        genInfo = cms.InputTag("generator"),
                        mvaIds = cms.InputTag("lowPtGsfElectronID"),
                        mvaSeeds = cms.VInputTag( cms.InputTag("lowPtGsfElectronSeedValueMaps:unbiased"),
                                                  cms.InputTag("lowPtGsfElectronSeedValueMaps:ptbiased") ),
                        )
