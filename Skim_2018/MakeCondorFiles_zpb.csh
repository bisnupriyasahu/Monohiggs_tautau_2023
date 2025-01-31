#!/bin/sh

currentDir=${PWD}
outDir=${9}
#export CMSSW_RELEASE_BASE=/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_9_4_1/
export CMSSW_RELEASE_BASE=/cvmfs/cms.cern.ch/slc7_amd64_gcc630/cms/cmssw/CMSSW_9_4_13/
cat> $outDir/Job_${8}.sh<<EOF
#!/bin/sh
source /cvmfs/cms.cern.ch/cmsset_default.sh 
cd $CMSSW_RELEASE_BASE
eval `scramv1 runtime -sh`
cd \${_CONDOR_SCRATCH_DIR}


for i in {1..10}
do

./${1} ${2} ${3}_\${i}.root ${4} ${5} ${6} ${7} ${8} \${i}

xrdcp ${3}_\${i}.root root://cmsxrootd.hep.wisc.edu:1094//store/user/jmadhusu/with_boostedtau/2017_skimmed/zprime_baryonic/

rm ${3}_\${i}.root

sleep 30

done

sleep  30

echo "Done!"

EOF

chmod 775 $outDir/Job_${8}.sh
cat > $outDir/condor_${8}<<EOF
x509userproxy = /tmp/x509up_u10044
universe = vanilla
Executable = $outDir/Job_${8}.sh
Notification         = never
#WhenToTransferOutput = On_Exit
ShouldTransferFiles  = yes
Requirements = (OpSysAndVer == "CENTOS7" && TARGET.Arch == "X86_64" && (MY.RequiresSharedFS=!=true || TARGET.HasAFS_OSG) && (TARGET.HAS_OSG_WN_CLIENT =?= TRUE || TARGET.IS_GLIDEIN=?=true) && IsSlowSlot=!=true)
#on_exit_remove       = (ExitBySignal == FALSE && (ExitCode == 0 || ExitCode == 42 || NumJobStarts>3))
+IsFastQueueJob      = True
getenv               = True
request_memory       = 4000
request_disk         = 5G

#OutputDestination = ${outdir}
#Initialdir = Out_${8}       
Transfer_Input_Files = ${currentDir}/${1} 

output               = $outDir/\$(Cluster)_\$(Process)_${8}.out
error                = $outDir/\$(Cluster)_\$(Process)_${8}.err
Log                  = $outDir/\$(Cluster)_\$(Process)_${8}.log
Queue
EOF

condor_submit $outDir/condor_${8}
