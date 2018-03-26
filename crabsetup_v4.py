
from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.workArea = 'crab_projects/'
config.General.requestName = 'Bc_JpsiPi_Mucuts_Pythia8_GENSIMRAW_v4'


config.section_('JobType')
config.JobType.psetName = 'step0_cfg_76x_SIM_RAW_HLT.py'
config.JobType.pluginName = 'PrivateMC'
config.JobType.numCores = 4
#config.JobType.outputFiles = ['WPiGammaAnalysis_output.root']

config.section_('Data')
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 20
config.Data.publication = True
config.Data.outputPrimaryDataset = 'CRAB_PrivateMC'
config.Data.totalUnits = 200000

config.section_('Site')
config.Site.storageSite = 'T2_IT_Legnaro'

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException
    from multiprocessing import Process

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    #############################################################################################
