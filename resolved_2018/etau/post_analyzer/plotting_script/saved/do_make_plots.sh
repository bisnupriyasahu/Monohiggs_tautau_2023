set -e

inFile=f_etau_initial.root
#inFile=$1
declare -a plotList=("elePt" "eleEta" "elePhi" "eleDz" "eleD0" "electronID" "relEleIso" "eleCharge" "tauPt" "tauEta" "tauPhi" "tauIso" "tauDecayMode" "tauCharge" "tauAntiEle" "tauAntiMu" "deltaR" "higgsPt" "nJet" "visMass" "mT_eleMet" "trigger" "genMatch" "met" "metPhi" "deltaPhi" "deltaEta" "metLongXaxis" "tot_TMass") 
declare -a indexList=("_5" "_6" "_7" "_8" "_9")


declare -a plotList_a=("elePt_a" "elePt_b" "elePt_c" "elePt_d" "elePt_e" "elePt_f" "elePt_g" "elePt_h" "elePt_i" "elePt_j")

rm eventYield.csv
for i in "${indexList[@]}"
do
    for j in "${plotList[@]}"
    do 
	hist=$j$i
	#echo "$hist"
	#python ~/monoHiggs_2018_wDnn/CMSSW_10_2_18/src/analysis/MacrosAndScripts/makeplot.py -in $inFile -name $i -cat 0 -ch etau -xaxis $i -year 2017 
	python makeplot.py -in $inFile -name $hist -cat 0 -ch etau -xaxis $hist -year 2018 --blindingRatio 5 & 
	#python makeplot_fbkg.py -in $inFile -name $hist -cat 0 -ch etau -xaxis $hist -year 2018 &
    done
    wait
done

wait
python makeplot.py -in $inFile -name cutflow_n -cat 0 -ch etau -xaxis "cutflow" -lY  -year 2018  --blindingRatio 5
