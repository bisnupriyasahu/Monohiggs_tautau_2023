
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

./postAnalyzer_mutau_v2.exe ../files_initial/DY1JetsToLL_final.root files_nominal/DY1JetsToLL_final.root DY1JetsToLL ZTT 0 
./postAnalyzer_mutau_v2.exe ../files_initial/DY1JetsToLL_final.root files_nominal/DY1JetsToLL_stitch_final.root ZTT1jet ZTTjet 0 
./postAnalyzer_mutau_v2.exe ../files_initial/DY2JetsToLL_final.root files_nominal/DY2JetsToLL_final.root DY2JetsToLL ZTT 0 
./postAnalyzer_mutau_v2.exe ../files_initial/DY2JetsToLL_final.root files_nominal/DY2JetsToLL_stitch_final.root ZTT2jet ZTTjet 0 
./postAnalyzer_mutau_v2.exe ../files_initial/DY3JetsToLL_final.root files_nominal/DY3JetsToLL_final.root DY3JetsToLL ZTT 0 
./postAnalyzer_mutau_v2.exe ../files_initial/DY3JetsToLL_final.root files_nominal/DY3JetsToLL_stitch_final.root ZTT3jet ZTTjet 0 
./postAnalyzer_mutau_v2.exe ../files_initial/DY4JetsToLL_final.root files_nominal/DY4JetsToLL_final.root DY4JetsToLL ZTT 0 
./postAnalyzer_mutau_v2.exe ../files_initial/DY4JetsToLL_final.root files_nominal/DY4JetsToLL_stitch_final.root ZTT4jet ZTTjet 0 
./postAnalyzer_mutau_v2.exe ../files_initial/DYJetsToLL_final.root files_nominal/DYJetsToLL_final.root DYJetsToLL ZTT 0 
./postAnalyzer_mutau_v2.exe ../files_initial/DYJetsToLL_final.root files_nominal/DYJetsToLL_stitch_final.root ZTTjet_inc ZTTjet 0 
./postAnalyzer_mutau_v2.exe ../files_initial/DYJetsToLL_M10to50_final.root files_nominal/DYJetsToLL_M10to50_final.root DYJetsToLL_M10to50 ZTT 0 
./postAnalyzer_mutau_v2.exe ../files_initial/EGamma2018A_final.root files_nominal/EGamma2018A_final.root data_obs data_obs 0 
./postAnalyzer_mutau_v2.exe ../files_initial/WWW_final.root files_nominal/WWW_final.root WWW VVV 0 
./postAnalyzer_mutau_v2.exe ../files_initial/EGamma2018B_final.root files_nominal/EGamma2018B_final.root data_obs data_obs 0 
./postAnalyzer_mutau_v2.exe ../files_initial/EGamma2018C_final.root files_nominal/EGamma2018C_final.root data_obs data_obs 0 
./postAnalyzer_mutau_v2.exe ../files_initial/EGamma2018D_final.root files_nominal/EGamma2018D_final.root data_obs data_obs 0 
./postAnalyzer_mutau_v2.exe ../files_initial/WWZ_final.root files_nominal/WWZ_final.root WWZ VVV 0 
./postAnalyzer_mutau_v2.exe ../files_initial/EWKWMinus2Jets_WToLNu_final.root files_nominal/EWKWMinus2Jets_WToLNu_final.root EWKWMinus2Jets EWKWMinus 0 
./postAnalyzer_mutau_v2.exe ../files_initial/EWKWPlus2Jets_WToLNu_final.root files_nominal/EWKWPlus2Jets_WToLNu_final.root EWKWPlus2Jets EWKWPlus 0 
./postAnalyzer_mutau_v2.exe ../files_initial/EWKZ2Jets_ZToNuNu_final.root files_nominal/EWKZ2Jets_ZToNuNu_final.root EWKZ2Jets_ZToNuNu EWKZ2Jets 0 
./postAnalyzer_mutau_v2.exe ../files_initial/GluGluHToTauTau_final.root files_nominal/GluGluHToTauTau_final.root GluGluHToTauTau GluGluH 0 
./postAnalyzer_mutau_v2.exe ../files_initial/GluGluZH_HToWW_final.root files_nominal/GluGluZH_HToWW_final.root GluGluZH_HToWW GluGluZH 0 
./postAnalyzer_mutau_v2.exe ../files_initial/HWminusJ_HToWW_final.root files_nominal/HWminusJ_HToWW_final.root HWminusJ_HToWW HWminusJ 0 
./postAnalyzer_mutau_v2.exe ../files_initial/HWplusJ_HToWW_final.root files_nominal/HWplusJ_HToWW_final.root HWplusJ_HToWW HWplusJ 0 
./postAnalyzer_mutau_v2.exe ../files_initial/HZJ_HToWW_final.root files_nominal/HZJ_HToWW_final.root HZJ_HToWW HZJ 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_200_MH4_100_final.root files_nominal/MH3_200_MH4_100_final.root MH3_200_MH4_100 signal_MH3_200_MH4_100 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_200_MH4_150_final.root files_nominal/MH3_200_MH4_150_final.root MH3_200_MH4_150 signal_MH3_200_MH4_150 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_300_MH4_100_final.root files_nominal/MH3_300_MH4_100_final.root MH3_300_MH4_100 signal_MH3_300_MH4_100 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_300_MH4_150_final.root files_nominal/MH3_300_MH4_150_final.root MH3_300_MH4_150 signal_MH3_300_MH4_150 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_400_MH4_100_final.root files_nominal/MH3_400_MH4_100_final.root MH3_400_MH4_100 signal_MH3_400_MH4_100 0 
./postAnalyzer_mutau_v2.exe ../files_initial/WZZ_final.root files_nominal/WZZ_final.root WZZ VVV 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_400_MH4_150_final.root files_nominal/MH3_400_MH4_150_final.root MH3_400_MH4_150 signal_MH3_400_MH4_150 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_400_MH4_200_final.root files_nominal/MH3_400_MH4_200_final.root MH3_400_MH4_200 signal_MH3_400_MH4_200 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_400_MH4_250_final.root files_nominal/MH3_400_MH4_250_final.root MH3_400_MH4_250 signal_MH3_400_MH4_250 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_500_MH4_150_final.root files_nominal/MH3_500_MH4_150_final.root MH3_500_MH4_150 signal_MH3_500_MH4_150 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_500_MH4_200_final.root files_nominal/MH3_500_MH4_200_final.root MH3_500_MH4_200 signal_MH3_500_MH4_200 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_500_MH4_250_final.root files_nominal/MH3_500_MH4_250_final.root MH3_500_MH4_250 signal_MH3_500_MH4_250 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_500_MH4_300_final.root files_nominal/MH3_500_MH4_300_final.root MH3_500_MH4_300 signal_MH3_500_MH4_300 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_600_MH4_100_final.root files_nominal/MH3_600_MH4_100_final.root MH3_600_MH4_100 signal_MH3_600_MH4_100 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_600_MH4_150_final.root files_nominal/MH3_600_MH4_150_final.root MH3_600_MH4_150 signal_MH3_600_MH4_150 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_600_MH4_200_final.root files_nominal/MH3_600_MH4_200_final.root MH3_600_MH4_200 signal_MH3_600_MH4_200 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_600_MH4_250_final.root files_nominal/MH3_600_MH4_250_final.root MH3_600_MH4_250 signal_MH3_600_MH4_250 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_600_MH4_300_final.root files_nominal/MH3_600_MH4_300_final.root MH3_600_MH4_300 signal_MH3_600_MH4_300 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_600_MH4_350_final.root files_nominal/MH3_600_MH4_350_final.root MH3_600_MH4_350 signal_MH3_600_MH4_350 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_600_MH4_400_final.root files_nominal/MH3_600_MH4_400_final.root MH3_600_MH4_400 signal_MH3_600_MH4_400 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_600_MH4_500_final.root files_nominal/MH3_600_MH4_500_final.root MH3_600_MH4_500 signal_MH3_600_MH4_500 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_700_MH4_250_final.root files_nominal/MH3_700_MH4_250_final.root MH3_700_MH4_250 signal_MH3_700_MH4_250 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_700_MH4_300_final.root files_nominal/MH3_700_MH4_300_final.root MH3_700_MH4_300 signal_MH3_700_MH4_300 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_700_MH4_350_final.root files_nominal/MH3_700_MH4_350_final.root MH3_700_MH4_350 signal_MH3_700_MH4_350 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_700_MH4_400_final.root files_nominal/MH3_700_MH4_400_final.root MH3_700_MH4_400 signal_MH3_700_MH4_400 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_800_MH4_250_final.root files_nominal/MH3_800_MH4_250_final.root MH3_800_MH4_250 signal_MH3_800_MH4_250 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_800_MH4_300_final.root files_nominal/MH3_800_MH4_300_final.root MH3_800_MH4_300 signal_MH3_800_MH4_300 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_800_MH4_350_final.root files_nominal/MH3_800_MH4_350_final.root MH3_800_MH4_350 signal_MH3_800_MH4_350 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_800_MH4_500_final.root files_nominal/MH3_800_MH4_500_final.root MH3_800_MH4_500 signal_MH3_800_MH4_500 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_900_MH4_300_final.root files_nominal/MH3_900_MH4_300_final.root MH3_900_MH4_300 signal_MH3_900_MH4_300 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_900_MH4_350_final.root files_nominal/MH3_900_MH4_350_final.root MH3_900_MH4_350 signal_MH3_900_MH4_350 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_900_MH4_400_final.root files_nominal/MH3_900_MH4_400_final.root MH3_900_MH4_400 signal_MH3_900_MH4_400 0 
./postAnalyzer_mutau_v2.exe ../files_initial/MH3_900_MH4_500_final.root files_nominal/MH3_900_MH4_500_final.root MH3_900_MH4_500 signal_MH3_900_MH4_500 0 
./postAnalyzer_mutau_v2.exe ../files_initial/ST_t-channel_antitop_final.root files_nominal/ST_t-channel_antitop_final.root ST_t-channel_antitop ST_t 0 
./postAnalyzer_mutau_v2.exe ../files_initial/ZZTo4L_final.root files_nominal/ZZTo4L_final.root ZZTo4L VV 0 
./postAnalyzer_mutau_v2.exe ../files_initial/ST_t-channel_top_final.root files_nominal/ST_t-channel_top_final.root ST_t-channel_top ST_t 0 
./postAnalyzer_mutau_v2.exe ../files_initial/ST_tW_antitop_final.root files_nominal/ST_tW_antitop_final.root ST_tW_antitop ST_t 0 
./postAnalyzer_mutau_v2.exe ../files_initial/ZZZ_final.root files_nominal/ZZZ_final.root ZZZ VVV 0 
./postAnalyzer_mutau_v2.exe ../files_initial/ST_tW_top_final.root files_nominal/ST_tW_top_final.root ST_tW_top ST_t 0 
./postAnalyzer_mutau_v2.exe ../files_initial/TTTo2L2Nu_powheg_final.root files_nominal/TTTo2L2Nu_powheg_final.root TTTo2L2Nu TT 0 
./postAnalyzer_mutau_v2.exe ../files_initial/TTToHadronic_powheg_final.root files_nominal/TTToHadronic_powheg_final.root TTToHadronic TT 0 
./postAnalyzer_mutau_v2.exe ../files_initial/TTToSemiLeptonic_powheg_final.root files_nominal/TTToSemiLeptonic_powheg_final.root TTToSemiLeptonic TT 0 
./postAnalyzer_mutau_v2.exe ../files_initial/VBFHToTauTau_final.root files_nominal/VBFHToTauTau_final.root VBFHToTauTau VBFH 0 
./postAnalyzer_mutau_v2.exe ../files_initial/VBFHToWWTo2L2Nu_final.root files_nominal/VBFHToWWTo2L2Nu_final.root VBFHToWWTo2L2Nu VBFH 0 
./postAnalyzer_mutau_v2.exe ../files_initial/W1JetsToLNu_final.root files_nominal/W1JetsToLNu_final.root W1JetsToLNu WJets 0 
./postAnalyzer_mutau_v2.exe ../files_initial/W1JetsToLNu_final.root files_nominal/W1JetsToLNu_stitch_final.root W1Jet WJets_jets 0 
./postAnalyzer_mutau_v2.exe ../files_initial/W2JetsToLNu_final.root files_nominal/W2JetsToLNu_final.root W2JetsToLNu WJets 0 
./postAnalyzer_mutau_v2.exe ../files_initial/W2JetsToLNu_final.root files_nominal/W2JetsToLNu_stitch_final.root W2Jet WJets_jets 0 
./postAnalyzer_mutau_v2.exe ../files_initial/W3JetsToLNu_final.root files_nominal/W3JetsToLNu_final.root W3JetsToLNu WJets 0 
./postAnalyzer_mutau_v2.exe ../files_initial/W3JetsToLNu_final.root files_nominal/W3JetsToLNu_stitch_final.root W3Jet WJets_jets 0 
./postAnalyzer_mutau_v2.exe ../files_initial/W4JetsToLNu_final.root files_nominal/W4JetsToLNu_final.root W4JetsToLNu WJets 0 
./postAnalyzer_mutau_v2.exe ../files_initial/W4JetsToLNu_final.root files_nominal/W4JetsToLNu_stitch_final.root W4Jet WJets_jets 0 
./postAnalyzer_mutau_v2.exe ../files_initial/WGToLNuG_final.root files_nominal/WGToLNuG_final.root WGToLNuG WGToLNuG 0 
./postAnalyzer_mutau_v2.exe ../files_initial/WJetsToLNu_Incl_final.root files_nominal/WJetsToLNu_Incl_final.root WJetsToLNu WJets 0 
./postAnalyzer_mutau_v2.exe ../files_initial/WJetsToLNu_Incl_final.root files_nominal/WJetsToLNu_Incl_stitch_final.root WJets_inc WJets_jets 0 
./postAnalyzer_mutau_v2.exe ../files_initial/WJetsToLNu_Incl_final.root files_nominal/WJetsToLNu_Incl_stitch_final.root WJetsToLNu_Incl_HT WJets_HT 0 
./postAnalyzer_mutau_v2.exe ../files_initial/WJetsToLNu_Incl_HT_final.root files_nominal/WJetsToLNu_Incl_HT_final.root WJetsToLNu_Incl_HT WJets_HT 0 
./postAnalyzer_mutau_v2.exe ../files_initial/WWTo1L1Nu2Q_final.root files_nominal/WWTo1L1Nu2Q_final.root WWTo1L1Nu2Q VV 0 
./postAnalyzer_mutau_v2.exe ../files_initial/WWToLNuQQ_final.root files_nominal/WWToLNuQQ_final.root WWToLNuQQ VV 0 
./postAnalyzer_mutau_v2.exe ../files_initial/WZTo3LNu_final.root files_nominal/WZTo3LNu_final.root WZTo3LNu VV 0 
./postAnalyzer_mutau_v2.exe ../files_initial/WplusHToTauTau_final.root files_nominal/WplusHToTauTau_final.root WplusHToTauTau WplusH 0 
./postAnalyzer_mutau_v2.exe ../files_initial/ZHToTauTau_final.root files_nominal/ZHToTauTau_final.root ZHToTauTau ZH 0 
./postAnalyzer_mutau_v2.exe ../files_initial/ZJetsToNuNu_HT1200-2500_final.root files_nominal/ZJetsToNuNu_HT1200-2500_final.root ZJetsToNuNu_HT1200-2500 ZJetsToNuNu 0 
./postAnalyzer_mutau_v2.exe ../files_initial/ZJetsToNuNu_HT200-400_final.root files_nominal/ZJetsToNuNu_HT200-400_final.root ZJetsToNuNu_HT200-400 ZJetsToNuNu 0 
./postAnalyzer_mutau_v2.exe ../files_initial/ZJetsToNuNu_HT2500-Inf_final.root files_nominal/ZJetsToNuNu_HT2500-Inf_final.root ZJetsToNuNu_HT2500-Inf ZJetsToNuNu 0 
./postAnalyzer_mutau_v2.exe ../files_initial/ZJetsToNuNu_HT400-600_final.root files_nominal/ZJetsToNuNu_HT400-600_final.root ZJetsToNuNu_HT400-600 ZJetsToNuNu 0 
./postAnalyzer_mutau_v2.exe ../files_initial/ZJetsToNuNu_HT800-1200_final.root files_nominal/ZJetsToNuNu_HT800-1200_final.root ZJetsToNuNu_HT800-1200 ZJetsToNuNu 0 
./postAnalyzer_mutau_v2.exe ../files_initial/ZZTo2L2Q_final.root files_nominal/ZZTo2L2Q_final.root ZZTo2L2Q VV 0 

hadd -f f_etau_initial.root files_nominal/*.root 
hadd -f f_etau_up.root files_up/*.root
hadd -f f_etau_down.root files_down/*.root


echo "*************** root file made ***************" 
#sh do_make_plots.sh 
echo "*************** plots made ***************" 
