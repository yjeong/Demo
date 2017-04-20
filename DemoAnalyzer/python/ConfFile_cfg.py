import FWCore.ParameterSet.Config as cms

process = cms.Process("PatTest")

#process.dump=cms.EDAnalyzer('EventContentAnalyzer')

process.load("FWCore.MessageService.MessageLogger_cfi")
#process.load("Configuration.Geometry.GeometryIdeal_cff")
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.globaltag = cms.string('START53_V27::All')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("DemoTree.DemoAnalyzer.CfiFile_cfi")

#process.load("PhysicsTools.PatAlgos.producersLayer1.pfParticleProducer_cfi")
#process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")

#process.demo.minTracks=1000

process.MessageLogger.cerr.threshold ='INFO'
process.MessageLogger.categories.append('Demo')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(

		limit = cms.untracked.int32(-1)
		)

process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('ERROR')
    ),
    destinations = cms.untracked.vstring('cout')
)


process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
	#replace 'myfile.root' with the source file you want to use
		fileNames = cms.untracked.vstring(
#	'file:/afs/cern.ch/user/y/yjeong/CMSSW_7_4_15/src/Demo/DemoAnalyzer/data_8TeV_ev1000.root'
#	'file:/afs/cern.ch/user/y/yjeong/CMSSW_7_4_15/src/Demo/DemoAnalyzer/TTJets_8TeV_53X.root'
#	'file:/afs/cern.ch/user/y/yjeong/CMSSW_7_4_15/src/Demo/PAT/ZZ.root'
#	'file:/u/user/yonghojeong57/TTJets_8TeV_53x.root'
#	'file:/u/user/yonghojeong57/data_8TeV_ev1000.root'
#	'file:/cms/scratch/yonghoJeong57/reco.root'
	'file:/cms/scratch/yonghoJeong57/patTuple_DY_3438.root'
	)
)
#located a DemoAnalyzer.cc file name
process.demo = cms.EDAnalyzer('DemoAnalyzer',
		Gen = cms.string('genParticles'),
		Tracks = cms.string('generalTracks'),
		Pmu = cms.string('selectedPatMuons'),
		Gmu = cms.string('globalMuons'),
		#Ver = cms.string('offlinePrimaryVertices'),
		minTracks = cms.untracked.uint32(0)
		)

#process.out = cms.OutputModule("PoolOutputModule",
#	fileName = cms.untracked.string('histoZZ.root')
#	fileName = cms.untracked.string('histoPAT.root')
#	fileName = cms.untracked.string('histodemo.root')
#	fileName = cms.untracked.string('histodata.root')
#)
process.demo.SaveHisto = cms.bool(True)


#process.outpath = cms.EndPath(process.out)
#process.TFileService = cms.Service("TFileService",
#	fileName = cms.string('histodemo.root')
#	)

#process.Tracer = cms.Service("Tracer")
#process.p = cms.Path(process.demo*process.dump)
process.p = cms.Path(process.demo)
