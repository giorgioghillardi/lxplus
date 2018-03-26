import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8PtGun",
    maxEventsToPrint = cms.untracked.int32(5),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    PGunParameters = cms.PSet(
        MaxPt = cms.double(100.),
        MinPt = cms.double(0.),
        ParticleID = cms.vint32(541),
        AddAntiParticle = cms.bool(False), 
        MaxEta = cms.double(2.4),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-2.4),
        MinPhi = cms.double(-3.14159265359), ## in radians
       # TFunction_string = cms.string('x*((1.+1./(3.357-2.)*x*x/2.085)^(-3.357))'),
       # TFunction_min = cms.double(10.),
       # TFunction_max = cms.double(120.)
                                    ),
   PythiaParameters = cms.PSet(
       pythia8CommonSettingsBlock,
       pythia8CUEP8M1SettingsBlock,


       pythiaJpsiDecays = cms.vstring(
                                      '541:onMode = off',                               # Turn off Bc  decays
                                      '541:onIfMatch = 443 211',                        # just let Bc->Jpsi+pi+   decays
                                      '443:onMode = off',                              # Turn off J/psi decays
                                      '443:onIfMatch = 13 -13',                        # just let J/psi -> mu+ mu-
       ),
       parameterSets = cms.vstring('pythia8CommonSettings',
                                   'pythia8CUEP8M1Settings',
                                   'pythiaJpsiDecays'
                                                           )
   )
)

###########
# Filters #
###########

#bfilter = cms.EDFilter(
#    "PythiaFilter", 
#    MaxEta = cms.untracked.double(2.4),
#    MinEta = cms.untracked.double(-2.4),
#    ParticleID = cms.untracked.int32(541)  ## Bc    )

decayfilter = cms.EDFilter(
    "PythiaDauVFilter",
    verbose         = cms.untracked.int32(1),
    MotherID        = cms.untracked.int32(541),
    NumberDaughters = cms.untracked.int32(2),
    ParticleID      = cms.untracked.int32(443), ##J/Psi
    DaughterIDs     = cms.untracked.vint32(-13, 13),  ## mu+, mu-
    MinPt           = cms.untracked.vdouble(2.8, 2.8 ),
    MinEta          = cms.untracked.vdouble( -2.4, -2.4),
    MaxEta          = cms.untracked.vdouble( 2.4, 2.4)
    )



ProductionFilterSequence = cms.Sequence(generator*decayfilter)


















