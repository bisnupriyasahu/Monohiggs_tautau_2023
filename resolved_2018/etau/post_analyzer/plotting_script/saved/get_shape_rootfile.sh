set -e

if [ -f "f_etau_initial.root" ]; then
    echo "deleting existing root file ....."
    rm *.root
fi

hadd -f f_etau_initial.root files_nominal/*.root 
hadd -f f_etau_up.root files_up/*.root
hadd -f f_etau_down.root files_down/*.root


python get_zll.py
python get_small_mc.py
python get_jetFakes.py
python get_jetFakes_unc.py
#python gather_hist.py
python gather_hist_v2.py
