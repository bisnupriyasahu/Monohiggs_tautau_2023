#!/bin/bash
set -e  # exit when any command fails

# keep track of the last executed command
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
# echo an error message before exiting
trap 'echo "\"${last_command}\" command filed with exit code $?."' EXIT

./rootcom mutau_analyzer analyze_mutau

outFile="study_mutau_110k.root"
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

outFile="study_mutau_dy.root"
echo "dy sample analysis....."
#./analyze_mutau /hdfs/store/user/jmadhusu/2018_skimmed/mutau/DY1JetsToLL_00.root DY1JetsToLL_00_test.root $nEvents 1000 2018_test MC DY1JetsToLL_00
./analyze_mutau /hdfs/store/user/jmadhusu/2018_skimmed/mutau/DYJetsToLL_02.root DYJetsToLL_02_test.root $nEvents 1000 2018 MC DYJetsToLL_02 
# outFile="study_mutau_wj.root"
# echo "wjets sample analysis....."
#./analyze_mutau /hdfs/store/user/jmadhusu/2018_skimmed/zprimeBaryonic/Zpbaryonic_00.root Zpbaryonic2018_test_2.root $nEvents 1000 2018 MC Zpbaryonic2018 41






end=`date +%s`
runtime=$((end-start))
echo "Runtime = $runtime"
echo "Elapsed: $(($runtime / 3600))hrs $((($runtime / 60) % 60))min $(($runtime % 60))sec"

