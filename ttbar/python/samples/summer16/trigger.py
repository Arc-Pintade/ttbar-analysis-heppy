from CMGTools.ttbar.analyzers.TriggerAnalyzer import TriggerFilterMatch

############################################################################
# 2016
############################################################################

mc_triggers = [
    'HLT_Ele27_WPTight_Gsf_v*',
    'HLT_IsoTkMu24_v*',
    'HLT_IsoMu24_v*',
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v*',
    'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*',
 ]


data_triggers = {}

data_triggers['A'] = [
    # electron
    'HLT_Ele27_WPTight_Gsf_v*',
    'HLT_Ele25_eta2p1_WPTight_Gsf_v*',
    'HLT_Ele32_eta2p1_WPTight_Gsf_v*',
    #'HLT_Ele38_WPTight_Gsf_v*',
    #'HLT_Ele40_WPTight_Gsf_v*',
    # double electron
    'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*',
    #'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v*',
    'HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v*',
    # muon
    'HLT_IsoTkMu24_v*',
    'HLT_IsoMu24_v*',
    'HLT_IsoMu22_eta2p1_v*',
    'HLT_IsoTkMu22_eta2p1_v*',
    #'HLT_IsoMu27_v*',
    # double muon
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*',
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*',
    # electron-muon
    'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*',
    'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*',
    'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v*',
    'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*',
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v*',
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*',
  
]
data_triggers['B'] = data_triggers['A']
data_triggers['C'] = data_triggers['A']
data_triggers['D'] = data_triggers['A']
data_triggers['E'] = data_triggers['A']
data_triggers['F'] = data_triggers['A']
data_triggers['G'] = data_triggers['A']
data_triggers['H'] = data_triggers['A']


















