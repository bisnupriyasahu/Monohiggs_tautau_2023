import os
import re
# new ntuples with changes /hdfs/store/user/jmadhusu/MC2018_Autumn18_monoHiggs_11May2021
#os.popen('ls -d /hdfs/store/user/jmadhusu/MC2018_Autumn18_monoHiggs_16May2021/*/*/*/* > mc_dir_list')
#os.popen('ls -d /hdfs/store/user/jmadhusu/MC2018_Autumn18_monoHiggs_17Oct2022/*/*/*/* > mc_dir_list')

os.popen('ls -d /hdfs/store/user/jmadhusu/MC2018_Autumn18_monoHiggs_28Aug2022/*/*/*/* > mc_dir_list')
inputFile=open("mc_dir_list", "r")
outFile = open("do_skim_mt_mc.sh", "w")
outFile.write("""
./rootcom skimm_tt_2018 analyze_tautau_skim 
outDir="Out_MC_$(date +"%d-%m-%Y_%H-%M")" 
mkdir $outDir 

""")

def replaceAll(line, searchExp,replaceExp):
    if searchExp in line:
        line = line.replace(searchExp,replaceExp)
    return line
def replaceEnd(line):
    line=line.strip()
    searchExp=line[-6:]
    sample = re.search('/crab_job_(.*)/22', line)
    #print (sample)
    sampleName = sample.group(1)
    replaceExp = searchExp+"/ "+sampleName+"_"+searchExp[-2:]+".root -1 1000 2018 MC "+sampleName+"_"+searchExp[-2:]+" $outDir"+" \n"
    line = line.replace(searchExp,replaceExp)
    return line

for line in inputFile:
    line =replaceAll(line, "/hdfs/store/","./MakeCondorFiles.csh analyze_tautau_skim /hdfs/store/")
    print(line)
    line = replaceEnd(line)
    outFile.write(line)



inputFile.close()
outFile.close()
print """
created do_skim_mt_mc.sh
do 
  bash do_skim_mt_mc.sh
in /nfs_scratch/ directory with required files
"""


#os.popen('ls -d /hdfs/store/user/jmadhusu/data2018_16May2021/Tau/*/*/* > data_dir_list')
os.popen('ls -d //hdfs/store/user/jmadhusu/data2018_28Aug2022/Tau/*/*/* > data_dir_list')
inputFile=open("data_dir_list", "r")
outFile = open("do_skim_mt_data.sh", "w")
outFile.write("""
./rootcom skimm_tt_2018 analyze_tautau_skim 
outDir="Out_DATA_$(date +"%d-%m-%Y_%H-%M")" 
mkdir $outDir 

""")

def replaceAll(line, searchExp,replaceExp):
    if searchExp in line:
        line = line.replace(searchExp,replaceExp)
    return line
def replaceEnd(line):
    line=line.strip()
    searchExp=line[-6:]
    sample = re.search('/crab_job_(.*)/22', line)
    sampleName = sample.group(1)
    replaceExp = searchExp+"/ "+sampleName+"_"+searchExp[-2:]+".root -1 1000 2018 DATA "+sampleName+"_"+searchExp[-2:]+" $outDir"+" \n"
    line = line.replace(searchExp,replaceExp)
    return line

for line in inputFile:
    line =replaceAll(line, "/hdfs/store/","./MakeCondorFiles.csh analyze_tautau_skim /hdfs/store/")
    line = replaceEnd(line)
    outFile.write(line)



inputFile.close()
outFile.close()
print """
created do_skim_mt_data.sh
do 
  bash do_skim_mt_data.sh
in /nfs_scratch/ directory with required files
"""
