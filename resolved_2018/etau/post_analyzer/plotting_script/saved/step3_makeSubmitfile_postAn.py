import os
sampleListDict = {
    'DY1JetsToLL' : ['DY1JetsToLL', 'ZTT', '0'], 
    'DY2JetsToLL' : ['DY2JetsToLL', 'ZTT', '0'], 
    'DY3JetsToLL' : ['DY3JetsToLL', 'ZTT', '0'], 
    'DY4JetsToLL' : ['DY4JetsToLL', 'ZTT', '0'], 
    'DYJetsToLL'  : ['DYJetsToLL' , 'ZTT', '0'], 
    'DYJetsToLL_M10to50' : ['DYJetsToLL_M10to50', 'ZTT', '0'], 

    'DYJetsToLL_0J_Incl' : ['DYJetsToLL_0J_Incl', 'ZTT_0J', '0'],
    'DYJetsToLL_2J_Incl' : ['DYJetsToLL_2J_Incl', 'ZTT_2J', '0'], 
    'DYJetsToLL_Incl_HT'  : ['DYJetsToLL_Incl_HT' , 'ZTT_HT', '0'],
    'DYJetsToLL_HT100-200' : ['DYJetsToLL_HT100-200', 'ZTT_HT', '0'],
    'DYJetsToLL_HT1200-2500' : ['DYJetsToLL_HT1200-2500', 'ZTT_HT', '0'],
    'DYJetsToLL_HT200-400' : ['DYJetsToLL_HT200-400', 'ZTT_HT', '0'],
    'DYJetsToLL_HT2500-Inf': ['DYJetsToLL_HT2500-Inf', 'ZTT_HT', '0'],
    'DYJetsToLL_HT400-600' : [ 'DYJetsToLL_HT400-600', 'ZTT_HT', '0'],
    'DYJetsToLL_HT600-800' : ['DYJetsToLL_HT600-800',  'ZTT_HT', '0'],
    'DYJetsToLL_HT70-100' : [ 'DYJetsToLL_HT70-100',  'ZTT_HT', '0'],
    'DYJetsToLL_HT800-1200' : ['DYJetsToLL_HT800-1200',  'ZTT_HT', '0'],

    'DY1JetsToLL_stitch' : ['ZTT1jet', 'ZTTjet', '0'],
    'DY2JetsToLL_stitch' : ['ZTT2jet', 'ZTTjet', '0'],
    'DY3JetsToLL_stitch' : ['ZTT3jet', 'ZTTjet', '0'],
    'DY4JetsToLL_stitch' : ['ZTT4jet', 'ZTTjet', '0'],
    'DYJetsToLL_stitch'  : ['ZTTjet_inc' , 'ZTTjet', '0'],

    'EWKWMinus2Jets_WToLNu' : ['EWKWMinus2Jets', 'EWKWMinus', '0'], 
    'EWKWPlus2Jets_WToLNu' : ['EWKWPlus2Jets', 'EWKWPlus', '0'], 
    'EWKZ2Jets_ZToLL' : ['EWKZ2Jets_ZToLL', 'EWKZ2Jets', '0'], 
    'EWKZ2Jets_ZToNuNu' : ['EWKZ2Jets_ZToNuNu', 'EWKZ2Jets', '0'], 
    'GluGluHToTauTau' : ['GluGluHToTauTau', 'GluGluH', '0'], 
    'GluGluHToWWTo2L2Nu' : ['GluGluHToWWTo2L2Nu', 'GluGluH', '0'], 
    'GluGluZH_HToWW' : ['GluGluZH_HToWW', 'GluGluZH', '0'], 
    'HWminusJ_HToWW' : ['HWminusJ_HToWW', 'HWminusJ', '0'], 
    'HWplusJ_HToWW' : ['HWplusJ_HToWW', 'HWplusJ', '0'], 
    'ZZTo4L' : ['ZZTo4L', 'VV', '0'], 
    'HZJ_HToWW' : ['HZJ_HToWW', 'HZJ', '0'], 
    'ST_t-channel_antitop' : ['ST_t-channel_antitop', 'ST_t', '0'], 
    'ST_t-channel_top' : ['ST_t-channel_top', 'ST_t', '0'], 
    'ST_tW_antitop' : ['ST_tW_antitop', 'ST_t', '0'], 
    'ST_tW_top' : ['ST_tW_top', 'ST_t', '0'], 

    'EGamma2018A' : ['data_obs', 'data_obs', '0'], 
    'EGamma2018B' : ['data_obs', 'data_obs', '0'], 
    'EGamma2018C' : ['data_obs', 'data_obs', '0'], 
    'EGamma2018D' : ['data_obs', 'data_obs', '0'], 
    'TTTo2L2Nu_powheg' : ['TTTo2L2Nu', 'TT', '0'], 
    'TTToHadronic_powheg' : ['TTToHadronic', 'TT', '0'], 
    'TTToSemiLeptonic_powheg' : ['TTToSemiLeptonic', 'TT', '0'], 
    'VBFHToTauTau' : ['VBFHToTauTau', 'VBFH', '0'], 
    'VBFHToWWTo2L2Nu' : ['VBFHToWWTo2L2Nu', 'VBFH', '0'], 
    'VVTo2L2Nu' : ['VVTo2L2Nu', 'VV', '0'], 
    'W1JetsToLNu' : ['W1JetsToLNu', 'WJets', '0'], 
    'W2JetsToLNu' : ['W2JetsToLNu', 'WJets', '0'], 
    'W3JetsToLNu' : ['W3JetsToLNu', 'WJets', '0'], 
    'W4JetsToLNu' : ['W4JetsToLNu', 'WJets', '0'],
    'WJetsToLNu_Incl' : ['WJetsToLNu', 'WJets', '0'],
    
    'W1JetsToLNu_stitch' : ['W1Jet', 'WJets_jets', '0'],
    'W2JetsToLNu_stitch' : ['W2Jet', 'WJets_jets', '0'],
    'W3JetsToLNu_stitch' : ['W3Jet', 'WJets_jets', '0'],
    'W4JetsToLNu_stitch' : ['W4Jet', 'WJets_jets', '0'],
    'WJetsToLNu_Incl_stitch'  : ['WJets_inc' , 'WJets_jets', '0'],
    
    'WJetsToLNu_Incl_HT' : [ 'WJetsToLNu_Incl_HT' , 'WJets_HT', '0'],
    'WJetsToLNu_0J_Incl' : [ 'WJetsToLNu_0J_Incl' , 'WJets_HT', '0'],
    'WJetsToLNu_1J_Incl' : [ 'WJetsToLNu_1J_Incl' , 'WJets_HT', '0'],
    'WJetsToLNu_2J_Incl' : ['WJetsToLNu_2J_Incl' , 'WJets_HT', '0'],
    'WJetsToLNu_HT100-200' : [ 'WJetsToLNu_HT100-200' , 'WJets_HT', '0'],
    'WJetsToLNu_HT1200-2500' : [ 'WJetsToLNu_HT1200-2500' , 'WJets_HT', '0'],
    'WJetsToLNu_HT200-400' : [ 'WJetsToLNu_HT200-400' , 'WJets_HT', '0'],
    'WJetsToLNu_HT2500-Inf' : [ 'WJetsToLNu_HT2500-Inf' , 'WJets_HT', '0'],
    'WJetsToLNu_HT400-600' : [ 'WJetsToLNu_HT400-600' , 'WJets_HT', '0'],
    'WJetsToLNu_HT600-800' : [ 'WJetsToLNu_HT600-800' , 'WJets_HT', '0'],
    'WJetsToLNu_HT70-100' : [ 'WJetsToLNu_HT70-100' , 'WJets_HT', '0'],
    'WJetsToLNu_HT800-1200' : [ 'WJetsToLNu_HT800-1200' , 'WJets_HT', '0'],
    
    'WGToLNuG' : ['WGToLNuG', 'WGToLNuG', '0'], 
    'WWTo1L1Nu2Q' : ['WWTo1L1Nu2Q', 'VV', '0'], 
    'WWToLNuQQ' : ['WWToLNuQQ', 'VV', '0'], 
    'WZTo3LNu' : ['WZTo3LNu', 'VV', '0'], 
    'WminusHToTauTau' : ['WminusHToTauTau', 'WminusH', '0'], 
    'WplusHToTauTau' : ['WplusHToTauTau', 'WplusH', '0'], 
    'ZHToTauTau' : ['ZHToTauTau', 'ZH', '0'], 
    'ZZTo2L2Q' : ['ZZTo2L2Q', 'VV', '0'], 
    'ggZH_HToTauTau_ZToLL' : ['ggZH_HToTauTau_ZToLL', 'ggZH', '0'], 
    'ggZH_HToTauTau_ZToNuNu' : ['ggZH_HToTauTau_ZToNuNu', 'ggZH', '0'], 
    'ggZH_HToTauTau_ZToQQ' : ['ggZH_HToTauTau_ZToQQ', 'ggZH', '0'], 
    'ttHToNonbb' : ['ttHToNonbb', 'ttH', '0'], 
    'WWW' :  ['WWW' , 'VVV' ,'0' ],
    'WWZ' :  ['WWZ' , 'VVV' ,'0' ],
    'WZZ' :  ['WZZ' , 'VVV' ,'0' ],
    'ZZZ' :  ['ZZZ' , 'VVV' ,'0' ],
    'ZJetsToNuNu_HT100-200' :   ['ZJetsToNuNu_HT100-200'   , 'ZJetsToNuNu' ,'0'],
    'ZJetsToNuNu_HT1200-2500' : ['ZJetsToNuNu_HT1200-2500' , 'ZJetsToNuNu' ,'0'],
    'ZJetsToNuNu_HT200-400' :   ['ZJetsToNuNu_HT200-400'   , 'ZJetsToNuNu' ,'0'],
    'ZJetsToNuNu_HT2500-Inf' :  ['ZJetsToNuNu_HT2500-Inf'  , 'ZJetsToNuNu' ,'0'],
    'ZJetsToNuNu_HT400-600' :   ['ZJetsToNuNu_HT400-600'   , 'ZJetsToNuNu' ,'0'],
    'ZJetsToNuNu_HT600-800' :   ['ZJetsToNuNu_HT600-800'   , 'ZJetsToNuNu' ,'0'],
    'ZJetsToNuNu_HT800-1200' :  ['ZJetsToNuNu_HT800-1200'  , 'ZJetsToNuNu' ,'0' ],
    
    'MH3_200_MH4_100' : ['MH3_200_MH4_100' , 'signal_MH3_200_MH4_100' , '0' ],
    'MH3_200_MH4_150' : ['MH3_200_MH4_150' , 'signal_MH3_200_MH4_150' , '0' ],
    'MH3_300_MH4_100' : ['MH3_300_MH4_100' , 'signal_MH3_300_MH4_100' , '0' ],
    'MH3_300_MH4_150' : ['MH3_300_MH4_150' , 'signal_MH3_300_MH4_150' , '0' ],
    'MH3_400_MH4_100' : ['MH3_400_MH4_100' , 'signal_MH3_400_MH4_100' , '0' ],
    'MH3_400_MH4_150' : ['MH3_400_MH4_150' , 'signal_MH3_400_MH4_150' , '0' ],
    'MH3_400_MH4_200' : ['MH3_400_MH4_200' , 'signal_MH3_400_MH4_200' , '0' ],
    'MH3_400_MH4_250' : ['MH3_400_MH4_250' , 'signal_MH3_400_MH4_250' , '0' ],
    'MH3_500_MH4_150' : ['MH3_500_MH4_150' , 'signal_MH3_500_MH4_150' , '0' ],
    'MH3_500_MH4_200' : ['MH3_500_MH4_200' , 'signal_MH3_500_MH4_200' , '0' ],
    'MH3_500_MH4_250' : ['MH3_500_MH4_250' , 'signal_MH3_500_MH4_250' , '0' ],
    'MH3_500_MH4_300' : ['MH3_500_MH4_300' , 'signal_MH3_500_MH4_300' , '0' ],
    'MH3_600_MH4_100' : ['MH3_600_MH4_100' , 'signal_MH3_600_MH4_100' , '0' ],
    'MH3_600_MH4_150' : ['MH3_600_MH4_150' , 'signal_MH3_600_MH4_150' , '0' ],
    'MH3_600_MH4_200' : ['MH3_600_MH4_200' , 'signal_MH3_600_MH4_200' , '0' ],
    'MH3_600_MH4_250' : ['MH3_600_MH4_250' , 'signal_MH3_600_MH4_250' , '0' ],
    'MH3_600_MH4_300' : ['MH3_600_MH4_300' , 'signal_MH3_600_MH4_300' , '0' ],
    'MH3_600_MH4_350' : ['MH3_600_MH4_350' , 'signal_MH3_600_MH4_350' , '0' ],
    'MH3_600_MH4_400' : ['MH3_600_MH4_400' , 'signal_MH3_600_MH4_400' , '0' ],
    'MH3_600_MH4_500' : ['MH3_600_MH4_500' , 'signal_MH3_600_MH4_500' , '0' ],
    'MH3_700_MH4_250' : ['MH3_700_MH4_250' , 'signal_MH3_700_MH4_250' , '0' ],
    'MH3_700_MH4_300' : ['MH3_700_MH4_300' , 'signal_MH3_700_MH4_300' , '0' ],
    'MH3_700_MH4_350' : ['MH3_700_MH4_350' , 'signal_MH3_700_MH4_350' , '0' ],
    'MH3_700_MH4_400' : ['MH3_700_MH4_400' , 'signal_MH3_700_MH4_400' , '0' ],
    'MH3_800_MH4_250' : ['MH3_800_MH4_250' , 'signal_MH3_800_MH4_250' , '0' ],
    'MH3_800_MH4_300' : ['MH3_800_MH4_300' , 'signal_MH3_800_MH4_300' , '0' ],
    'MH3_800_MH4_350' : ['MH3_800_MH4_350' , 'signal_MH3_800_MH4_350' , '0' ],
    'MH3_800_MH4_500' : ['MH3_800_MH4_500' , 'signal_MH3_800_MH4_500' , '0' ],
    'MH3_900_MH4_300' : ['MH3_900_MH4_300' , 'signal_MH3_900_MH4_300' , '0' ],
    'MH3_900_MH4_350' : ['MH3_900_MH4_350' , 'signal_MH3_900_MH4_350' , '0' ],
    'MH3_900_MH4_400' : ['MH3_900_MH4_400' , 'signal_MH3_900_MH4_400' , '0' ],
    'MH3_900_MH4_500' : ['MH3_900_MH4_500' , 'signal_MH3_900_MH4_500' , '0' ],

}

filelist=os.listdir("../files_initial")
filelist = [item for item in filelist if '.root' in item]

samplelist=[]
samplelist = list(map(lambda x: 
                      x.replace('.root','')
                      .replace('_final','')
                      , filelist))

#for n,g in zip(filelist, samplelist):
#    print(n+'\t\t\t'+g)
outFile = open("_postAnalyzer_mutau.sh", "w")
outFile.write(
"""
#!/bin/bash 
set -e 
if [ -f "f_mutau_initial.root" ]; then
    echo "deleting existing f_mutau_initial.root file ....."
    rm f_mutau_initial.root
fi
if [ "$(ls -A files_nominal/*.root)" ]; then
    echo "deleting existing files in directory files_nominal ....."
    rm files_nominal/*.root
fi


./Make.sh postAnalyzer_mutau_v2.C 

"""
)
for j in range(len(filelist)) :
    tmp = samplelist[j]
    samplename=sampleListDict[tmp]
    outoutFilename=filelist[j]
    outFile.write('./postAnalyzer_mutau_v2.exe ../files_initial/{} files_nominal/{} {} {} {} \n'
                  .format(filelist[j], outoutFilename, samplename[0], samplename[1], samplename[2]))
    st_tmp=tmp+'_stitch'
    if st_tmp in sampleListDict :
        samplename=sampleListDict[st_tmp]
        outoutFilename=samplelist[j]+'_stitch_final.root'
        outFile.write('./postAnalyzer_mutau_v2.exe ../files_initial/{} files_nominal/{} {} {} {} \n'
                      .format(filelist[j], outoutFilename, samplename[0], samplename[1], samplename[2]))
    st_tmp=tmp+'_HT'
    if st_tmp in sampleListDict :
        samplename=sampleListDict[st_tmp]
        outoutFilename=samplelist[j]+'_stitch_final.root'
        outFile.write('./postAnalyzer_mutau_v2.exe ../files_initial/{} files_nominal/{} {} {} {} \n'
                      .format(filelist[j], outoutFilename, samplename[0], samplename[1], samplename[2]))

outFile.write(
"""
hadd -f f_mutau_initial.root files_nominal/*.root 
hadd -f f_mutau_up.root files_up/*.root
hadd -f f_mutau_down.root files_down/*.root

echo "*************** root file made ***************" 
sh do_make_plots.sh 
echo "*************** plots made ***************" 
"""
)

outFile.close()

print("""
output written to _postAnalyzer_mutau.sh


""")
