#!/bin/bash
set -e  # exit when any command fails

# keep track of the last executed command
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
# echo an error message before exiting
trap 'echo "\"${last_command}\" command filed with exit code $?."' EXIT


f_exe="analyze_tautau_test"
if [ -f "$f_exe" ]; then
    echo "$f_exe exists, removing file"
    rm $f_exe
fi

./rootcom tautau_analyzer $f_exe


outFile="study_tautau_110k.root"
start=`date +%s`
nEvents=10000
sample='dy'
plottingOn=0
while getopts n:s:p option
do
    case "${option}"
	in
	n) nEvents=${OPTARG};;
	p) plottingOn=1 ;;
	s) sample=${OPTARG};;
esac
done

# echo "dy sample analysis....."
./$f_exe /hdfs/store/user/jmadhusu/2018_skimmed/tautau/DYJetsToLL_00.root DYJetsToLL_00_test.root $nEvents 1000 2017 MC DY1JetsToLL_00

# echo "ttbar sample analysis....."
# ./$f_exe /hdfs/store/user/jmadhusu/2018_skimmed/tautau/TTToSemiLeptonic_powheg_00.root TTToSemiLeptonic_TuneCP5_00_test.root $nEvents 1000 2017 MC TTToSemiLeptonic_TuneCP5_00 

echo "data sample analysis....."
./$f_exe /hdfs/store/user/jmadhusu/2018_skimmed/tautau/TauA_02.root TauA_02_test.root $nEvents 1000 2017 DATA Tau_EraA

end=`date +%s`
runtime=$((end-start))
echo "Runtime = $runtime"
echo "Elapsed: $(($runtime / 3600))hrs $((($runtime / 60) % 60))min $(($runtime % 60))sec"
