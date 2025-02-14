#!/usr/bin/env python
import ROOT
import re
from array import array
from sys import argv
import ROOT as Root
import csv
from math import sqrt
from math import pi
import datetime
import argparse
from sys import path
#path.append("../../../MacrosAndScripts/")
from myPlotStyle import *
import systematics_unc


parser = argparse.ArgumentParser()
parser.add_argument("-name",
                    help="name of hist to be plotted")
parser.add_argument("-year",
                    help="dataset year")

parser.add_argument("-xaxis",
                    help="x axis label")

parser.add_argument("-lY", "--logYaxis", action="store_true",
                    help="set y axis log scale")

parser.add_argument("-pi", "--piAxis", action="store_true",
                    help="set x axis in intervals of pi")

parser.add_argument("-nL", "--noLegend", action="store_true",
                    help="remove legend from histogram")

parser.add_argument("-cat", "--category",
                    help="pick reco histogram category")

parser.add_argument("-ch", "--channel",
                    help="pick decay channel")
parser.add_argument("-bR", "--blindingRatio",
                    help="choose data fraction used for blinding")

now = datetime.datetime.now()
args =  parser.parse_args()
histoname=args.name
year_=args.year
category_=args.category
xaxis_label=args.xaxis
channel_=args.channel
blindingRatio_ = int(args.blindingRatio)
eventsPerBin=""
if ("muPt" in histoname or "tauPt" in histoname or "elePt" in histoname):
  eventsPerBin=" /2GeV"
if ("higgsPt" in histoname):
  eventsPerBin=" /10GeV"
if ("visMass" in  histoname):
  eventsPerBin=" /5GeV"
if ("met" in histoname):
  eventsPerBin=" /10GeV"
if ("mT_" in histoname):
  eventsPerBin=" /10GeV"
#print "Item / histogram name = ", histoname

if (args.piAxis):
  piAxis = 1
else :
  piAxis = 0
if ( "Phi" in histoname) :
  piAxis = 1

yaxisLog = 0
if (args.logYaxis):
  yaxisLog = 1

noLegend = 0
if (args.noLegend):
  noLegend = 1

 
ROOT.gStyle.SetFrameLineWidth(1)
ROOT.gStyle.SetLineWidth(2)
ROOT.gStyle.SetOptStat(0)

c, pad1, pad2 = get_canvas()
c.cd()
inputFile_='f_'+xaxis_label+'_initial.root'

print(inputFile_)

adapt=ROOT.gROOT.GetColor(12)
new_idx=ROOT.gROOT.GetListOfColors().GetSize() + 1
trans=ROOT.TColor(new_idx, adapt.GetRed(), adapt.GetGreen(),adapt.GetBlue(), "",0.5)
dirname = [histoname+"/",histoname, histoname+"_fr/", histoname+"_dyll/", histoname+"_dyll_fr/"]


OutFile=ROOT.TFile(inputFile_,"r")
mc_samples = [ 'ZTTjet', 'ZLLjet', 'TT' , 'otherMC' , 'STT', 'VVT'] 

ZTTselect="ZTTjet"
#WJetselect="WJets"
WJetselect="WJets_jets"
OutFile.cd()
data_hist_name = 'data_obs_'
if blindingRatio_!=1:
  data_hist_name = 'blinded_data_obs_'
print(dirname[0]+data_hist_name+histoname)
Data_hist    =OutFile.Get(dirname[0]+data_hist_name+histoname)
ZTT_hist     = OutFile.Get(dirname[0]+"ZTTjet_"+histoname)
Wjets_hist   = OutFile.Get(dirname[0]+"WJets_jets_"+histoname)
TT_hist      = OutFile.Get(dirname[0]+"TT_"+histoname)
ST_t_hist    = OutFile.Get(dirname[0]+"STT_"+histoname)
VV_hist      = OutFile.Get(dirname[0]+"VVT_"+histoname)
otherMC_hist  = OutFile.Get(dirname[0]+"otherMC_"+histoname)
#jetFakes_hist = OutFile.Get(dirname[0]+"jetFakes_"+histoname)

signal_MZp_100_MChi_1 = OutFile.Get(dirname[0]+"Signal_MZp_100_MChi_1_"+histoname)
signal_MZp_1000_MChi_1 = OutFile.Get(dirname[0]+"Signal_MZp_1000_MChi_1_"+histoname)
signal_MZp_1500_MChi_1 = OutFile.Get(dirname[0]+"Signal_MZp_1500_MChi_1_"+histoname)
#signal = "Signal_2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_200_"
#signal_MZp_100_MChi_1 = OutFile.Get(dirname[0]+"Signal_2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_200_"+histoname)
#print(dirname[0]+signal+histoname)
#signal_MZp_1000_MChi_1 = OutFile.Get(dirname[0]+"Signal_2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_"+histoname)
#signal_MZp_1500_MChi_1 = OutFile.Get(dirname[0]+"Signal_2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_250_"+histoname)




if 'muPt' in histoname or 'elePt' in histoname or 'higgsPt' in histoname or 'tauPt' in histoname or 'tau1Pt' in histoname or 'tau2Pt' in histoname:
  nbin_group = 3
  Data_hist.Rebin(nbin_group)
  Wjets_hist.Rebin(nbin_group)
  jetFakes_hist.Rebin(nbin_group)
  ZTT_hist.Rebin(nbin_group)
  TT_hist.Rebin(nbin_group)
  ST_t_hist.Rebin(nbin_group)
  VV_hist.Rebin(nbin_group)
  otherMC_hist.Rebin(nbin_group)


if 'tot_TMass_new' in histoname:
  #new_binning = array('d', [0, 20, 40, 60, 90, 120, 140, 180, 210, 230, 260, 280, 320, 400, 2000]) # 14 binns
  #new_binning = array('d', [40, 100, 200, 300, 400, 600, 2000])
  new_binning = array('d', [40, 60, 90, 120, 150, 180, 210, 230, 260, 320, 400, 500]) # 11 binns
  Data_hist = Data_hist.Rebin(11, 'hist', new_binning )
  Wjets_hist = Wjets_hist.Rebin(11, 'hist', new_binning )
  #  jetFakes_hist = jetFakes_hist.Rebin(11, 'hist', new_binning )
  #ZTT_hist = ZTT_hist.Rebin(11, 'hist', new_binning )
  TT_hist = TT_hist.Rebin(11, 'hist', new_binning )
  ST_t_hist = ST_t_hist.Rebin(11, 'hist', new_binning )
  VV_hist = VV_hist.Rebin(11, 'hist', new_binning )
  otherMC_hist = otherMC_hist.Rebin(11, 'hist', new_binning )
  signal_MZp_100_MChi_1 = signal_MZp_100_MChi_1.Rebin(11, 'hist', new_binning )
  signal_MZp_1000_MChi_1 = signal_MZp_1000_MChi_1.Rebin(11, 'hist', new_binning )
  signal_MZp_1500_MChi_1= signal_MZp_1500_MChi_1.Rebin(11, 'hist', new_binning )
'''


if 'tot_TMass_new' in histoname:
  new_binning = array('d', [40, 60, 90, 120, 140, 180, 210, 230, 260, 280, 320, 400, 2000]) # 14 binns
  #new_binning = array('d', [40, 100, 200, 300, 400, 600, 2000])
  Data_hist = Data_hist.Rebin(12, 'hist', new_binning )
  Wjets_hist = Wjets_hist.Rebin(12, 'hist', new_binning )
  jetFakes_hist = jetFakes_hist.Rebin(12, 'hist', new_binning )
  ZTT_hist = ZTT_hist.Rebin(12, 'hist', new_binning )
  TT_hist = TT_hist.Rebin(12, 'hist', new_binning )
  ST_t_hist = ST_t_hist.Rebin(12, 'hist', new_binning )
  VV_hist = VV_hist.Rebin(12, 'hist', new_binning )
  otherMC_hist = otherMC_hist.Rebin(12, 'hist', new_binning )
  signal_MZp_100_MChi_1 = signal_MZp_100_MChi_1.Rebin(12, 'hist', new_binning )
  signal_MZp_1000_MChi_1 = signal_MZp_1000_MChi_1.Rebin(12, 'hist', new_binning )
  signal_MZp_1500_MChi_1= signal_MZp_1500_MChi_1.Rebin(12, 'hist', new_binning )  
'''  
#sampleList    = [Data_hist,     TT_hist,   ST_t_hist, VV_hist, otherMC_hist ]
#sampleListRef = ['Data_hist',   'TT_hist', 'ST_t_hist', 'VV_hist', 'otherMC_hist']
sampleList    = [Data_hist,   ZTT_hist,  TT_hist,   ST_t_hist, VV_hist, otherMC_hist ]
sampleListRef = ['Data_hist', 'ZTT_hist',  'TT_hist', 'ST_t_hist', 'VV_hist', 'otherMC_hist']

Wjets_hist.SetFillColor(ROOT.TColor.GetColor(color_wjets))
#jetFakes_hist.SetFillColor(ROOT.TColor.GetColor(color_jetfake))
ZTT_hist.SetFillColor(ROOT.TColor.GetColor(color_ztt))
#ZLL_hist.SetFillColor(ROOT.TColor.GetColor(color_zll))
TT_hist.SetFillColor(ROOT.TColor.GetColor(color_tt))
ST_t_hist.SetFillColor(ROOT.TColor.GetColor(color_ggh))
VV_hist.SetFillColor(ROOT.TColor.GetColor(color_vv))
otherMC_hist.SetFillColor(ROOT.TColor.GetColor(color_otherMC))


signal_MZp_100_MChi_1.SetLineColor(55)
signal_MZp_1000_MChi_1.SetLineColor(65)
signal_MZp_1500_MChi_1.SetLineColor(95)

signal_MZp_100_MChi_1.SetLineWidth(5)
signal_MZp_1000_MChi_1.SetLineWidth(5)
signal_MZp_1500_MChi_1.SetLineWidth(5)


for i in range(len(sampleList)):
  sampleList[i].SetLineColor(1)

stack=ROOT.THStack("stack","stack")  
for i in range(len(sampleList)-1, 0, -1):
  #print(i, sampleList[i])
  stack.Add(sampleList[i])

 
databymc = Data_hist.Clone() 
numberOfBins = Data_hist.GetNbinsX()
for ibin in range(1, numberOfBins+1):
  Data_hist.SetBinContent(ibin, round(Data_hist.GetBinContent(ibin)))
  #print("in data: ",ibin)
  print(Data_hist.GetBinContent(ibin))
Data_hist.GetXaxis().SetTitle("")
Data_hist.GetXaxis().SetTitleSize(0)

mc_sum = sampleList[1].Clone()
for i in range(2, len(sampleList)):
  mc_sum.Add(sampleList[i])
  
#h3 = mc_sum.Clone()
for ibin in range(numberOfBins+1):
  bc_mc = mc_sum.GetBinContent(ibin+1)
  #  print()
  bc_data = Data_hist.GetBinContent(ibin+1)
  
  if bc_mc==0:   continue
  print("data: ",bc_data)
  print("mc: ",bc_mc)
  dbymc = bc_data/bc_mc  
  databymc.SetBinContent(ibin+1, dbymc)
  #  
  #diff_percent = (bc_data-bc_mc)
  #rnum = 0.2
  #print(ibin+1, diff_percent)
  #if diff_percent > 0.2:
  #  TT_hist.SetBinContent(ibin+1, TT_hist.GetBinContent(ibin+1)+rnum*(bc_data-bc_mc))
  #  ZTT_hist.SetBinContent(ibin+1, ZTT_hist.GetBinContent(ibin+1)+rnum*(bc_data-bc_mc))
  #  jetFakes_hist.SetBinContent(ibin+1, jetFakes_hist.GetBinContent(ibin+1)+rnum*(bc_data-bc_mc))
  #elif diff_percent < -0.2:
  #  TT_hist.SetBinContent(ibin+1, TT_hist.GetBinContent(ibin+1)+rnum*(bc_data-bc_mc))
  #  ZTT_hist.SetBinContent(ibin+1, ZTT_hist.GetBinContent(ibin+1)+rnum*(bc_data-bc_mc))    
  #  jetFakes_hist.SetBinContent(ibin+1, jetFakes_hist.GetBinContent(ibin+1)+rnum*(bc_data-bc_mc))    
    


   
#nDivXAxis=405
if piAxis == 1:
  nDivXAxis= -105
elif histoname=='cutflow_n' or histoname=='cutflow_n_fr':
  nDivXAxis= Data_hist.GetNbinsX()
  print("ndivisionX  ", nDivXAxis)
elif histoname=='relMuIso_5' :
  nDivXAxis= Data_hist.GetNbinsX()
elif histoname=='tauAntiEle_5' or histoname=='tauAntiMu_5':
  nDivXAxis= Data_hist.GetNbinsX()
elif histoname=='muCharge_5' or histoname=='tauCharge_5':
  nDivXAxis= Data_hist.GetNbinsX()
elif histoname=='tauDecayMode_5':
  nDivXAxis= Data_hist.GetNbinsX()

# #print 'histoname = ', histoname
if 'tot_TMass_full' in histoname or 'tot_TMass_new' in histoname:
  #print '************************ setting data bins'
  # blinding_massPoint = Data_hist.GetXaxis().FindBin(200)
  # print("blinding_massPoint = ",blinding_massPoint)
  for i in range(1, Data_hist.GetNbinsX()+1):
    #if i > blinding_massPoint:
    Data_hist.SetBinContent(i, 0)
  # Data_hist.SetMinimum(0.1)
  # Data_hist.SetMaximum(2*max(Data_hist.GetMaximum(),stack.GetMaximum()))
  # pad1.SetLogy()


Data_hist.GetXaxis().SetNdivisions(nDivXAxis)
Data_hist.GetXaxis().SetLabelSize(0)
Data_hist.GetYaxis().SetLabelFont(42)
Data_hist.GetYaxis().SetLabelOffset(0.01)
Data_hist.GetYaxis().SetLabelSize(0.04)
Data_hist.GetYaxis().SetTitleSize(0.05)
Data_hist.GetYaxis().SetTitleOffset(1.22)
Data_hist.SetTitle("")
Data_hist.GetYaxis().SetTitle("")


print("coming")
if histoname=='cutflow_n' or histoname=='cutflow_n_fr' :
  with open('eventYield.csv', mode='a') as yield_file:
    yield_write = csv.writer(yield_file, delimiter=',', quotechar='"')
    for i in range(1,16):
      j = str(i)
      mctot = (ZTT_hist.GetBinContent(i)+TT_hist.GetBinContent(i)+ST_t_hist.GetBinContent(i)+VV_hist.GetBinContent(i)+otherMC_hist.GetBinContent(i) )
      #mctot = (TT_hist.GetBinContent(i)+ST_t_hist.GetBinContent(i)+VV_hist.GetBinContent(i)+otherMC_hist.GetBinContent(i) )
      #print("%.3f " %(Data_hist.GetBinContent(i)/mctot))
      #yield_write.writerow(["%.3f " %signal_MZp_100_MChi_1.GetBinContent(i) ])
      print("%.3f " %(signal_MZp_1500_MChi_1.GetBinContent(i)))
      yield_write.writerow([ "%.3f " %( ZTT_hist.GetBinContent(i)+TT_hist.GetBinContent(i)+ST_t_hist.GetBinContent(i)+VV_hist.GetBinContent(i)+otherMC_hist.GetBinContent(i) )])
      #yield_write.writerow(["%.3f " %signal_MZp_1500_MChi_1.GetBinContent(i) ])
      
      #yield_write.writerow(["%.3f " %signal_MZp_1000_MChi_1.GetBinContent(i) ])
      
      #yield_write.writerow(['From Cutflow bin'+j ])
      #yield_write.writerow([Data_hist.GetBinContent(i) ])
      #yield_write.writerow([ZTT_hist.GetBinContent(i)  ])
      #yield_write.writerow([ST_t_hist.GetBinContent(i)  ])
      #yield_write.writerow([VV_hist.GetBinContent(i) ])
      #yield_write.writerow([TT_hist.GetBinContent(i) ])
      #yield_write.writerow([otherMC_hist.GetBinContent(i) ])
      #yield_write.writerow("%.3f " %['VV' ,  VV_hist.GetBinContent(i) ])
      #      yield_write.writerow(['mc sum',  ZTT_hist.Integral()+TT_hist.Integral()+ST_t_hist.Integral()+VV_hist.Integral()+otherMC_hist.Integral() ])
      


print(histoname)
if histoname=='higgsPt_9' :
  with open('eventYield.csv', mode='w') as yield_file:
    yield_write = csv.writer(yield_file, delimiter=',', quotechar='"')
    yield_write.writerow(['From tau charge, integral, with mT cut' ])
    yield_write.writerow(['Data_hist', Data_hist.Integral() ])
    yield_write.writerow(['ZTT',  ZTT_hist.Integral()  ])
    #yield_write.writerow(['ZLL',  ZLL_hist.Integral()  ])
    yield_write.writerow(['TT',   TT_hist.Integral() ])
    yield_write.writerow(['ST',   ST_t_hist.Integral() ])
    yield_write.writerow(['VV',   VV_hist.Integral() ])
    yield_write.writerow(['OtherMC',   otherMC_hist.Integral() ])
    #    yield_write.writerow(['jetFakes_hist', jetFakes_hist.Integral() ])


    #yield_write.writerow(['ggh',  GluGluH_hist.Integral() ])
    #yield_write.writerow(['mc sum',  ZTT_hist.Integral()+ZLL_hist.Integral()+F_bkg.Integral()+TT_hist.Integral()+GluGluH_hist.Integral() ])
    #yield_write.writerow(['mc sum',  ZTT_hist.Integral()+TT_hist.Integral()+ST_t_hist.Integral()+VV_hist.Integral()+otherMC_hist.Integral()+ ])

#for i in range(len(sampleList)):
#  name = sampleListRef[i].replace('_hist', '')
#  print ( name   )
#  print ( sampleList[i].Integral()  )



c.cd()
pad1.Draw()
pad1.cd()

Data_hist.SetMarkerStyle(20)
Data_hist.SetMarkerColor(1)
Data_hist.SetMarkerSize(1.5)

Data_hist.GetXaxis().SetTitle("")
Data_hist.GetYaxis().SetTitle("Events")
if yaxisLog == 1 :
  Data_hist.SetMaximum(100*max(Data_hist.GetMaximum(),stack.GetMaximum() ))
  Data_hist.SetMinimum(1.0)
elif 'cutflow_n' in histoname or 'cutflow_n_fr' in histoname:
  pad1.SetLogy()  
  #pad1.SetLogx()  
  Data_hist.SetMaximum(2*max(Data_hist.GetMaximum(),stack.GetMaximum()))
  Data_hist.SetMinimum(1.0)
  Data_hist.SetMaximum(1000000000.0)
else :
  if channel_=="mutau":
    Data_hist.SetMaximum(2.5*max(Data_hist.GetMaximum(),stack.GetMaximum()))
  if channel_=="etau":
    Data_hist.SetMaximum(2.5*max(Data_hist.GetMaximum(), stack.GetMaximum()))
  if channel_=="tautau":
    Data_hist.SetMaximum(2.5*max(Data_hist.GetMaximum(), stack.GetMaximum()))
  Data_hist.SetMinimum(0.1)

# if yaxisLog == 1 :
#   pad1.SetLogy()  
  
#if histoname == "cutflow_n":
#  Data_hist.SetMinimum(0)
errorBand = databymc.Clone()
Data_hist.Draw("e1")
stack.Draw("histsame")
if histoname == "cutflow_n" or histoname=="cutflow_n_fr" :
  signal_MZp_100_MChi_1.Draw("histsame")
  signal_MZp_1000_MChi_1.Draw("histsame")  
  signal_MZp_1500_MChi_1.Draw("histsame")  

# if histoname != "cutflow_n":
#errorBand.Draw("e2same")
#if 'tot_TMass_full' in histoname or 'tot_TMass_new' in histoname:

#signal_MZp_1500_MChi_1.Draw("histsame")
Data_hist.Draw("e1same")
if histoname == "cutflow_n" or histoname=="cutflow_n_fr" :
  Data_hist.Draw("e0psame")

legendNameList = {
  'Data_hist'  : 'Data obs',
  'ZTT_hist'   : 'Z->tautau',
  'ZLL_hist'   : 'Z-> ll',
  'Wjets_hist' : 'WJets',
  'jetFakes_hist'      : 'jet-tau fake', 
  'TT_hist'    : 'ttabr',
  #'GluGluH_hist' : 'ggh, vbfH, ZH',
  'ST_t_hist' : 'SingleTop',
  'VV_hist'    : 'Diboson',
  'otherMC_hist' : 'other MC',
  'ZJetsToNuNu_hist' : 'Z->nunu + jets'
}
legende=make_legend()
for i in range(len(sampleListRef)):
  if(i==0):
    legende.AddEntry(sampleList[i], legendNameList[sampleListRef[i]], "elp")
  else:
    legende.AddEntry(sampleList[i], legendNameList[sampleListRef[i]], "f")
  
if 'cutflow_n' in histoname or 'cutflow_n_fr' in histoname:
  #legende.AddEntry(signal_MZp_100_MChi_1, 'mA=600 ma=200', "el")
  #legende.AddEntry(signal_MZp_1000_MChi_1, 'mA=600 ma=150', "el")
  #legende.AddEntry(signal_MZp_1500_MChi_1, 'mA=600 ma=250', "el")
  #print("coming here")
  legende.AddEntry(signal_MZp_100_MChi_1, 'MZp=100 MChi=1', "el")
  legende.AddEntry(signal_MZp_1000_MChi_1, 'MZp=1000 MChi=1', "el")
  legende.AddEntry(signal_MZp_1500_MChi_1, 'MZp=1500 MChi=1', "el")



#blindingRatio_ = 5
l1=add_lumi(year_, channel_, blindingRatio = blindingRatio_)
l1.Draw("same")
l2=add_CMS()
l2.Draw("same")
l3=add_Preliminary()
l3.Draw("same")

selection_mapping = {
  "4" : ["after mu-tau selection", "", "", ""],
  "5" : ["after bjetveto", "", "", ""], 
  "6" : ["preselection", "", "", ""], 
  "7" : ["preselection", "+ Higgs pT >65", "", ""],
  "8" : ["preselection", "+ Higgs pT >65", "+ visible mass<125", ""],
  "9" : ["preselection", "+ Higgs pT >65", "+ visible mass<125", "+ met > 120"],
}
selection_idx = histoname.split("_")[-1]
#selection_label = add_text(text=selection_mapping[selection_idx])
#selection_label.Draw("same")

pad1.RedrawAxis()
#print "Line 217 is okay"


c.cd()
pad2.Draw()
pad2.cd()
h1=Data_hist.Clone()

#h3=
#hwoE=errorBand.Clone()
h1.SetMarkerStyle(20)
h1.SetMarkerSize(2.0)
#h1.Sumw2()
#h3.Sumw2()
h1.SetStats(0)
#h1.Divide(h3)
#h3.Divide(hwoE)

label_mapping = {
  
  "muPt" : "muon pT [GeV]",
  "elePt" : "electron pT [GeV]",
  "tauPt" : "tau pT [GeV]",
  "tau1Pt" : "leading tau pT [GeV]",
  "tau2Pt" : "subleading tau pT [GeV]",
  "met"   : "MET [GeV]" ,
  "higgsPt" : "higgs pT [GeV]",
  "mT_muMet" : "#mu-met transverse mass [GeV]",
  "metLongXaxis" : "met [GeV]",
  "visMass" : "#mu-#tau visible mass [GeV]",
  "nJet" : "number of Jets",
  "deltaR" : "#mu-#tau deltaR", 
  "tot_TMass_new" : "total transverse mass [GeV]",
  "cutflow_n" : "cutflow",
  "cutflow_n_fr" : "cutflow_fr"
}


h1.GetXaxis().SetTitle(label_mapping.get(xaxis_label,xaxis_label ))
h1.SetMarkerColor(1)
h1.SetLineColor(1)
h1.SetTitle("")
h1.GetXaxis().SetLabelSize(0.1)
h1.GetYaxis().SetTitle("Data/MC")
h1.GetYaxis().SetLabelSize(0.08)
h1.SetMaximum(2.0)
h1.SetMinimum(0.0)
h1.GetXaxis().SetNdivisions(nDivXAxis)
if piAxis ==1 :
  h1.GetXaxis().SetBinLabel(30,"#pi");
  h1.GetXaxis().SetBinLabel(22,"#frac{#pi}{2}");
  h1.GetXaxis().SetBinLabel(15,"0");
  h1.GetXaxis().SetBinLabel(8,"#frac{-#pi}{2}");
  h1.GetXaxis().SetBinLabel(1,"-#pi");
  
if piAxis == 1:
  h1.GetXaxis().SetLabelOffset(0.1)
  h1.GetXaxis().SetLabelSize(0.15)
  h1.GetXaxis().SetNdivisions(-105)

elif histoname=='Events_level_':
  
  h1.GetXaxis().SetBinLabel(13,"METcut");
  h1.GetXaxis().SetBinLabel(12,"VisibleMass");
  h1.GetXaxis().SetBinLabel(11,"HiggsPt");
  h1.GetXaxis().SetBinLabel(10,"Mt cut");
  h1.GetXaxis().SetBinLabel(9,"BjetVeto");
  h1.GetXaxis().SetBinLabel(8,"ThirdLepVeto");
  h1.GetXaxis().SetBinLabel(7,"DeltaR");
  h1.GetXaxis().SetBinLabel(6,"opp. charge");
  h1.GetXaxis().SetBinLabel(5,"GoodTau");
  h1.GetXaxis().SetBinLabel(4,"GoodMuon");
  h1.GetXaxis().SetBinLabel(3,"mu Trg");
  h1.GetXaxis().SetBinLabel(2,"MET Filters");
  h1.GetXaxis().SetBinLabel(1,"No cuts");
  h1.GetXaxis().SetNdivisions(-115)
  h1.GetXaxis().LabelsOption("v")
  h1.GetXaxis().SetTitle(" cut flow")
  h1.SetMaximum(1.2)#FIXME(1.2)
  h1.SetMinimum(0.8)#FIXME(0.8)

elif histoname=='cutflow_n' or histoname=='cutflow_n_fr':
  #h1.GetXaxis().SetRangeUser(0,11)
  h1.GetXaxis().SetBinLabel(15,"MET>105");
  h1.GetXaxis().SetBinLabel(14,"MViss<125");
  h1.GetXaxis().SetBinLabel(13,"HiggsPt>65 ");  
  h1.GetXaxis().SetBinLabel(12,"dR mu-tau>0.5");
  h1.GetXaxis().SetBinLabel(11,"No b-Jetveto");
  h1.GetXaxis().SetBinLabel(10,"SF & No 3rdleptonveto");
  h1.GetXaxis().SetBinLabel(9,"opposite \n ch.");
  h1.GetXaxis().SetBinLabel(8,"passed triggerpT");
  h1.GetXaxis().SetBinLabel(7,"good taupairs");
  h1.GetXaxis().SetBinLabel(6,"METrecoil passed");
  h1.GetXaxis().SetBinLabel(5,"After TauES");
  h1.GetXaxis().SetBinLabel(4,"Before TauES");
  h1.GetXaxis().SetBinLabel(3,"MC taupairs");
  h1.GetXaxis().SetBinLabel(2,"Trigger");
  h1.GetXaxis().SetBinLabel(1,"Initial");
  h1.GetXaxis().LabelsOption("u")
  h1.GetXaxis().SetTitle("Cutflow ")
  h1.SetMaximum(2.0)#FIXME(1.2)
  h1.SetMinimum(0.0)#FIXME(0.8)



h1.GetYaxis().SetNdivisions(5)
h1.GetXaxis().SetNdivisions(510)
h1.GetXaxis().SetTitleFont(42)
h1.GetYaxis().SetTitleFont(42)
h1.GetXaxis().SetTitleSize(0.15)
h1.GetYaxis().SetTitleSize(0.15)
h1.GetYaxis().SetTitleOffset(0.3)
h1.GetXaxis().SetTitleOffset(1.1)

#if 'tot_TMass_full' in histoname or 'tot_TMass_new' in histoname :
if 'tot_TMass_full' in histoname :
  pad1.SetLogx()  
  pad2.SetLogx()  
h1.Draw("e0p")
#h4 = h1.Divide(h3)
#h4.Draw("same")
errorBand.Draw("e2same") 
c.cd()
pad1.RedrawAxis()
pad2.RedrawAxis()
if noLegend == 0:
  legende.Draw()
#ROOT.gPad.RedrawAxis()

c.Modified()
c.SaveAs("plot_"+histoname+"_"+channel_+'_'+year_+".png")
