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
import get_sys
path.append("../../../MacrosAndScripts/")

from myPlotStyle import *


parser = argparse.ArgumentParser()
parser.add_argument("-name",
                    help="name of hist to be plotted")
parser.add_argument("-year",
                    help="dataset year")
parser.add_argument("-in", "--inputFile",
                    help="name of input file")

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
inputFile_=args.inputFile
category_=args.category
xaxis_label=args.xaxis[:-2]
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

c.cd()

inputFile_ = "f_"+xaxis_label+"_initial.root"
OutFile=ROOT.TFile(inputFile_,"r")

adapt=ROOT.gROOT.GetColor(12)
new_idx=ROOT.gROOT.GetListOfColors().GetSize() + 1
trans=ROOT.TColor(new_idx, adapt.GetRed(), adapt.GetGreen(),adapt.GetBlue(), "",0.5)
dirname = [histoname+"/",histoname, histoname+"_fr/", histoname+"_dyll/", histoname+"_dyll_fr/"]

#ZTTselect="ZTT"
ZTTselect="ZTTjet"
#WJetselect="WJets"
WJetselect="WJets_jets"
OutFile.cd()
Data_hist    =OutFile.Get(dirname[0]+"data_obs_"+histoname)
ZTT_hist     = OutFile.Get(dirname[0]+ZTTselect+"_"+histoname)
ZLL_hist     = OutFile.Get(dirname[3]+ZTTselect+"_"+histoname+"_dyll")
EWKWMinus_hist = OutFile.Get(dirname[0]+"EWKWMinus_"+histoname)
EWKWPlus_hist = OutFile.Get(dirname[0]+"EWKWPlus_"+histoname)
EWKZ2Jets_hist = OutFile.Get(dirname[0]+"EWKZ2Jets_"+histoname)
EWKZ2Jets_LL_hist = OutFile.Get(dirname[0]+"EWKZ2Jets_"+histoname+"_dyll")
Wjets_hist   = OutFile.Get(dirname[0]+WJetselect+"_"+histoname)
GluGluH_hist = OutFile.Get(dirname[0]+"GluGluH_"+histoname)
ST_t_hist    = OutFile.Get(dirname[0]+"ST_t_"+histoname)
TT_hist      = OutFile.Get(dirname[0]+"TT_"+histoname)
VBFH_hist    = OutFile.Get(dirname[0]+"VBFH_"+histoname)
VV_hist      = OutFile.Get(dirname[0]+"VV_"+histoname)
WminusH_hist = OutFile.Get(dirname[0]+"WminusH_"+histoname)
WplusH_hist  = OutFile.Get(dirname[0]+"WplusH_"+histoname)
ZH_hist      = OutFile.Get(dirname[0]+"ZH_"+histoname)
VVV_hist     = OutFile.Get(dirname[0]+"VVV_"+histoname)
ZJetsToNuNu_hist = OutFile.Get(dirname[0]+"ZJetsToNuNu_"+histoname)

Signal1= OutFile.Get(dirname[0]+"signal_MH3_200_MH4_150_"+histoname)
Signal2= OutFile.Get(dirname[0]+"signal_MH3_300_MH4_150_"+histoname)
Signal3= OutFile.Get(dirname[0]+"signal_MH3_400_MH4_150_"+histoname)
Signal4= OutFile.Get(dirname[0]+"signal_MH3_500_MH4_150_"+histoname)
Signal5= OutFile.Get(dirname[0]+"signal_MH3_600_MH4_150_"+histoname)
Signal6= OutFile.Get(dirname[0]+"signal_MH3_700_MH4_300_"+histoname)
Signal7= OutFile.Get(dirname[0]+"signal_MH3_800_MH4_300_"+histoname)


Signal1.SetLineWidth(3)
Signal1.SetMarkerColor(4)
Signal1.SetLineColor(4)

Signal2.SetLineWidth(3)
Signal2.SetMarkerColor(5)
Signal2.SetLineColor(5)

Signal3.SetLineWidth(3)
Signal3.SetMarkerColor(6)
Signal3.SetLineColor(6)

Signal4.SetLineWidth(3)
Signal4.SetMarkerColor(7)
Signal4.SetLineColor(7)

Signal5.SetLineWidth(3)
Signal5.SetMarkerColor(8)
Signal5.SetLineColor(8)

Signal6.SetLineWidth(3)
Signal6.SetMarkerColor(9)
Signal6.SetLineColor(9)

Signal7.SetLineWidth(3)
Signal7.SetMarkerColor(11)
Signal7.SetLineColor(11)



if( OutFile.Get(dirname[0]+"EWKWMinus_"+histoname) ) :
  GluGluH_hist.Add(EWKWMinus_hist)
if( OutFile.Get(dirname[0]+"EWKWPlus_"+histoname) ):
  GluGluH_hist.Add(EWKWPlus_hist)
if( OutFile.Get(dirname[0]+"EWKZ2Jets_"+histoname) ):
  ZTT_hist.Add(EWKZ2Jets_hist)
if( OutFile.Get(dirname[0]+"EWKZ2Jets_"+histoname+"_dyll") ):
  ZTT_hist.Add(EWKZ2Jets_LL_hist)

if(  OutFile.Get(dirname[0]+"VBFH_"+histoname) ):
  GluGluH_hist.Add(VBFH_hist)
if(OutFile.Get(dirname[0]+"WminusH_"+histoname)):
  GluGluH_hist.Add(WminusH_hist)
if(OutFile.Get(dirname[0]+"WplusH_"+histoname)):  
  GluGluH_hist.Add(WplusH_hist)
if( OutFile.Get(dirname[0]+"ZH_"+histoname)):
  GluGluH_hist.Add(ZH_hist)
if(OutFile.Get(dirname[0]+"ST_t_"+histoname)):
  GluGluH_hist.Add(ST_t_hist)
if( OutFile.Get(dirname[0]+"VVV_"+histoname) ):
  GluGluH_hist.Add(VVV_hist)
if(OutFile.Get(dirname[0]+"VV_"+histoname)):
  GluGluH_hist.Add(VV_hist)


(print 'F_bkg=OutFile.Get( ', dirname[2]+"data_obs_"+histoname+"_fr")
F_bkg=OutFile.Get(dirname[2]+"data_obs_"+histoname+"_fr")
#F_bkg_dyll=OutFile.Get(dirname[4]+"data_obs_"+histoname+"_dyll_fr")
ZTT_bkg     = OutFile.Get(dirname[2]+ZTTselect+"_"+histoname+"_fr")
ZLL_bkg     = OutFile.Get(dirname[4]+ZTTselect+"_"+histoname+"_dyll_fr")
EWKWMinus_bkg = OutFile.Get(dirname[2]+"EWKWMinus_"+histoname+"_fr")
EWKWPlus_bkg = OutFile.Get(dirname[2]+"EWKWPlus_"+histoname+"_fr")
EWKZ2Jets_bkg = OutFile.Get(dirname[2]+"EWKZ2Jets_"+histoname+"_fr")
GluGluH_bkg = OutFile.Get(dirname[2]+"GluGluH_"+histoname+"_fr")
ST_t_bkg    = OutFile.Get(dirname[2]+"ST_t_"+histoname+"_fr")
TT_bkg      = OutFile.Get(dirname[2]+"TT_"+histoname+"_fr")
VBFH_bkg    = OutFile.Get(dirname[2]+"VBFH_"+histoname+"_fr")
VV_bkg      = OutFile.Get(dirname[2]+"VV_"+histoname+"_fr")
WminusH_bkg = OutFile.Get(dirname[2]+"WminusH_"+histoname+"_fr")
WplusH_bkg  = OutFile.Get(dirname[2]+"WplusH_"+histoname+"_fr")
ZH_bkg      = OutFile.Get(dirname[2]+"ZH_"+histoname+"_fr")
VVV_bkg     = OutFile.Get(dirname[2]+"VVV_"+histoname+"_fr")
#ZJetsToNuNu_bkg = OutFile.Get(dirname[2]+"ZJetsToNuNu_"+histoname+"_fr")

#if(OutFile.Get(dirname[4]+"data_obs_"+histoname+"_dyll_fr")):
#  F_bkg.Add(F_bkg_dyll)
F_bkg.Add(ZTT_bkg, -1)
#if(OutFile.Get(dirname[4]+ZTTselect+"_"+histoname+"_dyll_fr")):
#  F_bkg.Add(ZLL_bkg, -1)
if(OutFile.Get(dirname[2]+"EWKWMinus_"+histoname+"_fr")):
  F_bkg.Add(EWKWMinus_bkg, -1)
if( OutFile.Get(dirname[2]+"EWKWPlus_"+histoname+"_fr")):
  F_bkg.Add(EWKWPlus_bkg, -1)
if(OutFile.Get(dirname[2]+"EWKZ2Jets_"+histoname+"_fr")):
  F_bkg.Add(EWKZ2Jets_bkg, -1)
F_bkg.Add(GluGluH_bkg, -1)
F_bkg.Add(ST_t_bkg, -1)
F_bkg.Add(TT_bkg, -1)
if(OutFile.Get(dirname[2]+"VBFH_"+histoname+"_fr")):
  F_bkg.Add(VBFH_bkg, -1)
if(OutFile.Get(dirname[2]+"VV_"+histoname+"_fr")):  
  F_bkg.Add(VV_bkg, -1)
if(OutFile.Get(dirname[2]+"WminusH_"+histoname+"_fr")):
  F_bkg.Add(WminusH_bkg, -1)
if(OutFile.Get(dirname[2]+"WplusH_"+histoname+"_fr")):
  F_bkg.Add(WplusH_bkg, -1)
if(OutFile.Get(dirname[2]+"ZH_"+histoname+"_fr")):
  F_bkg.Add(ZH_bkg, -1)
if(OutFile.Get(dirname[2]+"VVV_"+histoname+"_fr")):
  F_bkg.Add(VVV_bkg, -1)
#F_bkg.Add(ZJetsToNuNu_bkg, -1)

sampleList    = [Data_hist,    ZTT_hist,  ZLL_hist, TT_hist,   GluGluH_hist,    F_bkg ]
sampleListRef = ['Data_hist', 'ZTT_hist', 'ZLL_hist', 'TT_hist', 'GluGluH_hist', 'F_bkg']
# if channel_=="etau":
#   sampleList    = [Data_hist,    ZTT_hist,   TT_hist,  F_bkg, GluGluH_hist ]
#   sampleListRef = ['Data_hist', 'ZTT_hist',  'TT_hist', 'F_bkg', 'GluGluH_hist']
if channel_=="etau":
 sampleList    = [Data_hist,    ZTT_hist,  ZLL_hist, TT_hist,  F_bkg, GluGluH_hist ]
 sampleListRef = ['Data_hist', 'ZTT_hist', 'ZLL_hist', 'TT_hist', 'F_bkg', 'GluGluH_hist']


sampleSyslist = ['Data_hist', 'ZTTjet', 'ZLLjet', 'TT', 'jetFakes', 'STT', 'VVT', 'otherMC']
#sampleSyslistRef = [Data_hist,  ZTTjet, ZLLjet, TT, jetFakes, STT, VVT, otherMC]

Wjets_hist.SetFillColor(ROOT.TColor.GetColor(color_wjets))
F_bkg.SetFillColor(ROOT.TColor.GetColor(color_jetfake))
ZTT_hist.SetFillColor(ROOT.TColor.GetColor(color_ztt))
ZLL_hist.SetFillColor(ROOT.TColor.GetColor(color_zll))
TT_hist.SetFillColor(ROOT.TColor.GetColor(color_tt))
GluGluH_hist.SetFillColor(ROOT.TColor.GetColor(color_ggh))
VV_hist.SetFillColor(ROOT.TColor.GetColor(color_vv))

for i in range(len(sampleList)):
  sampleList[i].SetLineColor(1)

stack=ROOT.THStack("stack","stack")  
for i in range(len(sampleList)-1, 0, -1):
  #print(i, sampleList[i])
  stack.Add(sampleList[i])

errorBand=sampleList[1].Clone()
for i in range(2, len(sampleList)):
  errorBand.Add(sampleList[i])

numberOfBins = Data_hist.GetNbinsX()
print '############# hist = ', histoname
syst_error_list = []
systErrorDict = {}
for i in range(1, len(sampleSyslist)):
  print 'getting syst ', xaxis_label , sampleSyslist[i] , histoname[-1]
  binErrors = get_sys.get_syst(xaxis_label , sampleSyslist[i] , histoname[-1])
  #print 'binErrors : ', binErrors
  systErrorDict[sampleSyslist[i]] = binErrors


print 'systErrorDict : '
for e in systErrorDict:
  print e 
  print systErrorDict[e]
  
binWiseErrors = {}
for ibin in range(numberOfBins):
  binWiseErrors[ibin] = []
  for e in systErrorDict:
    binWiseErrors[ibin].append( systErrorDict[e][ibin])

for b in binWiseErrors:
  print 'MC ' , b , binWiseErrors[b]

print 'getting systematics error .....'
syst_list = []
for ibin in range(numberOfBins):
  syst_list.append(ROOT.TMath.Sqrt( sum( unc**2 for unc in binWiseErrors[ibin]))  )
print 'syst_list ', syst_list

print 'getting statistcal error .....'
stat_err = errorBand.Clone()

for ibin in range(1, numberOfBins+1):
  print 'bin={}  , content={} , stat err={}'.format(ibin, stat_err.GetBinContent(ibin) , stat_err.GetBinError(ibin))
  content = stat_err.GetBinContent(ibin)
  try:
    print 'checking math stat err={} '.format( 1/sqrt(content))
  except:
    print '################## content is ' , content


print '\n\n '
for ibin in range(1, numberOfBins+1):
  stat = stat_err.GetBinError(ibin)
  syst = syst_list[ibin-1]
  final_err = ROOT.TMath.Sqrt( syst**2 )
  print 'final_err bin# = {}  , stat = {}  syst = {} , final = {}'.format(ibin, stat, syst, final_err)
  errorBand.SetBinError(ibin, final_err)
print '\n\n '

#errorBand.SetMarkerSize(0)
errorBand.SetFillColor(1)
errorBand.SetFillStyle(errorStyle)
#errorBand.SetLineWidth(1)

Data_hist.GetXaxis().SetTitle("")
Data_hist.GetXaxis().SetTitleSize(0)

nDivXAxis=405
if piAxis == 1:
  nDivXAxis= -105
elif histoname=='cutflow_n' or histoname=='cutflow_Htt':
  nDivXAxis= Data_hist.GetNbinsX()
elif histoname=='relMuIso_5' :
  nDivXAxis= Data_hist.GetNbinsX()
elif histoname=='tauAntiEle_5' or histoname=='tauAntiMu_5':
  nDivXAxis= Data_hist.GetNbinsX()
elif histoname=='muCharge_5' or histoname=='tauCharge_5':
  nDivXAxis= Data_hist.GetNbinsX()
elif histoname=='tauDecayMode_5':
  nDivXAxis= Data_hist.GetNbinsX()

#print 'histoname = ', histoname
if 'tot_TMass_full' in histoname:
  #print '************************ setting data bins'
  for i in range(1, Data_hist.GetNbinsX()+1):
    if i > 8:
      Data_hist.SetBinContent(i, 0)


Data_hist.GetXaxis().SetNdivisions(nDivXAxis)
Data_hist.GetXaxis().SetLabelSize(0)
Data_hist.GetYaxis().SetLabelFont(42)
Data_hist.GetYaxis().SetLabelOffset(0.01)
Data_hist.GetYaxis().SetLabelSize(0.04)
Data_hist.GetYaxis().SetTitleSize(0.05)
Data_hist.GetYaxis().SetTitleOffset(1.22)
Data_hist.SetTitle("")
Data_hist.GetYaxis().SetTitle("")

# with open('eventYield.csv', mode='w') as yield_file:
#   yield_write = csv.writer(yield_file, delimiter=',', quotechar='"')
#   yield_write.writerow(['Name', 'Yield' ])

if histoname=='cutflow_n' :
  with open('eventYield.csv', mode='a') as yield_file:
    yield_write = csv.writer(yield_file, delimiter=',', quotechar='"')
    yield_write.writerow(['From Cutflow bin 8' ])
    yield_write.writerow(['Data_hist', Data_hist.GetBinContent(8) ])
    yield_write.writerow(['ZTT',  ZTT_hist.GetBinContent(8)  ])
    yield_write.writerow(['ZLL',  ZLL_hist.GetBinContent(8)  ])
    yield_write.writerow(['Fake', F_bkg.GetBinContent(8) ])
    yield_write.writerow(['TT',   TT_hist.GetBinContent(8) ])
    yield_write.writerow(['ggh',  GluGluH_hist.GetBinContent(8) ])
    #yield_write.writerow(['VV' ,  VV_hist.GetBinContent(8) ])
if histoname=='tauCharge_9' :
  with open('eventYield.csv', mode='a') as yield_file:
    yield_write = csv.writer(yield_file, delimiter=',', quotechar='"')
    yield_write.writerow(['From tau charge, integral, with all cuts' ])
    yield_write.writerow(['Data_hist', Data_hist.Integral() ])
    yield_write.writerow(['ZTT',  ZTT_hist.Integral()  ])
    yield_write.writerow(['ZLL',  ZLL_hist.Integral()  ])
    yield_write.writerow(['Fake', F_bkg.Integral() ])
    yield_write.writerow(['TT',   TT_hist.Integral() ])
    yield_write.writerow(['ggh',  GluGluH_hist.Integral() ])
    yield_write.writerow(['mc sum',  ZTT_hist.Integral()+ZLL_hist.Integral()+F_bkg.Integral()+TT_hist.Integral()+GluGluH_hist.Integral() ])
    #yield_write.writerow(['VV' ,  VV_hist.Integral() ])

c.cd()
pad1.Draw()
pad1.cd()

if yaxisLog == 1 :
  pad1.SetLogy()  
Data_hist.Scale(0)

Data_hist.SetMarkerStyle(20)
Data_hist.SetMarkerColor(1)
Data_hist.SetMarkerSize(0)
if histoname == "cutflow_n":
  Data_hist.SetMarkerSize(0)


Data_hist.GetXaxis().SetTitle("")
Data_hist.GetYaxis().SetTitle("Events"+eventsPerBin)
if yaxisLog == 1 :
  Data_hist.SetMaximum(100*max(10, stack.GetMaximum()))
  Data_hist.SetMinimum(0.01)
else :
  if channel_=="mutau":
    Data_hist.SetMaximum(1.055*max(10, stack.GetMaximum()))
  if channel_=="etau":
    Data_hist.SetMaximum(1.5*max(10, stack.GetMaximum()))
  if channel_=="tautau":
    Data_hist.SetMaximum(1.055*max(10,  stack.GetMaximum()))
  Data_hist.SetMinimum(0.0)
  
if histoname == "cutflow_n":
  Data_hist.SetMinimum(1000)

if "tot_TMass_fu" in xaxis_label and yaxisLog == 1:
  #yaxisLog = 1
  Data_hist.SetMinimum(1.0)
  Data_hist.SetMaximum(2*max(10, stack.GetMaximum()))
  
if 'tot_TMass_full' in histoname:
  Data_hist.SetMinimum(1.0)

if yaxisLog == 1 :
  pad1.SetLogy() 
 
Data_hist.Draw()
stack.Draw("histsame")
# if histoname != "cutflow_n":
errorBand.Draw("e2same")
Signal1.Draw("histsame")
Signal2.Draw("histsame")
Signal3.Draw("histsame")
Signal4.Draw("histsame")
Signal5.Draw("histsame")
Signal6.Draw("histsame")
Signal7.Draw("histsame")
#Data_hist.Draw("e1same")
#if histoname == "cutflow_n":
#  Data_hist.Draw("e0psame")

legendNameList = {
  'Data_hist'  : 'Data obs',
  'ZTT_hist'   : 'Z->tautau',
  'ZLL_hist'   : 'Z-> ll',
  'Wjets_hist' : 'WJets',
  'F_bkg'      : 'jet-tau fake', 
  'TT_hist'    : 'ttabr',
  #'GluGluH_hist' : 'ggh, vbfH, ZH',
  'GluGluH_hist' : 'Others',
  'VV_hist'    : 'VV, SingleTop',
  'ZJetsToNuNu_hist' : 'Z->nunu + jets'
}
legende=make_legend()
for i in range(len(sampleListRef)):
  if(i==0):
    continue
    #legende.AddEntry(sampleList[i], legendNameList[sampleListRef[i]], "elp")
  else:
    legende.AddEntry(sampleList[i], legendNameList[sampleListRef[i]], "f")
  
legende.AddEntry(Signal1,"2hdma_med200_ps150","l")
legende.AddEntry(Signal2,"2hdma_med300_ps150","l")
legende.AddEntry(Signal3,"2hdma_med400_ps150","l")
legende.AddEntry(Signal4,"2hdma_med500_ps150","l")
legende.AddEntry(Signal5,"2hdma_med600_ps150","l")
legende.AddEntry(Signal6,"2hdma_med700_ps300","l")
legende.AddEntry(Signal7,"2hdma_med800_ps300","l")

l1=add_lumi(year_, channel_, blindingRatio = blindingRatio_)
l1.Draw("same")
l2=add_CMS()
l2.Draw("same")
l3=add_Preliminary()
l3.Draw("same")

pad1.RedrawAxis()
#print "Line 217 is okay"


c.cd()
pad2.Draw()
pad2.cd()
h1=Data_hist.Clone()
h3=errorBand.Clone()
hwoE=errorBand.Clone()
h1.SetMarkerStyle(20)
h1.SetMarkerSize(2.0)
#h1.Sumw2()
#h3.Sumw2()
h1.SetStats(0)
h1.Divide(hwoE)
h3.Divide(hwoE)
h1.GetXaxis().SetTitle('deltaPhi HiggsPT - MET')
h1.SetMarkerColor(1)
h1.SetLineColor(1)
h1.SetTitle("")
h1.GetXaxis().SetLabelSize(0.1)
h1.GetYaxis().SetTitle("Data/MC")
h1.GetYaxis().SetLabelSize(0.08)
h1.SetMaximum(1.5)
h1.SetMinimum(0.5)
h1.GetXaxis().SetNdivisions(nDivXAxis)
if piAxis ==1 :
  h1.GetXaxis().SetBinLabel(30,"#pi");
  h1.GetXaxis().SetBinLabel(22,"#frac{#pi}{2}");
  h1.GetXaxis().SetBinLabel(15,"0");
  h1.GetXaxis().SetBinLabel(8,"#frac{-#pi}{2}");
  h1.GetXaxis().SetBinLabel(1,"-#pi");
  
if piAxis == 1:
  h1.GetXaxis().SetLabelOffset(0.02)
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

elif histoname=='cutflow_n':
  
  h1.GetXaxis().SetBinLabel(8,"mu-tau \n separation");
  h1.GetXaxis().SetBinLabel(7,"b-Jet veto");
  h1.GetXaxis().SetBinLabel(6,"3rd lepton \n veto");
  h1.GetXaxis().SetBinLabel(5,"opposite \n ch.");
  h1.GetXaxis().SetBinLabel(4,"tau \n selections");
  h1.GetXaxis().SetBinLabel(3,"Muon \n selections");
  h1.GetXaxis().SetBinLabel(2,"Trigger");
  h1.GetXaxis().SetBinLabel(1,"Initial");
  h1.GetXaxis().LabelsOption("v")
  h1.GetXaxis().SetTitle(" ")
  h1.SetMaximum(2.0)#FIXME(1.2)
  h1.SetMinimum(0.0)#FIXME(0.8)



h1.GetYaxis().SetNdivisions(5)
h1.GetXaxis().SetTitleFont(42)
h1.GetYaxis().SetTitleFont(42)
h1.GetXaxis().SetTitleSize(0.15)
h1.GetYaxis().SetTitleSize(0.15)
h1.GetYaxis().SetTitleOffset(0.3)
h1.GetXaxis().SetTitleOffset(1.1)

h1.Draw()
h3.Draw("e2same")

c.cd()
#pad1.RedrawAxis()
#pad2.RedrawAxis()
if noLegend == 0:
  legende.Draw()
#ROOT.gPad.RedrawAxis()

c.Modified()
if yaxisLog == 1 :
  c.SaveAs("plots_wsys/logScale/plot_"+histoname+"_"+channel_+"logY.png")
else:
  c.SaveAs("plots_wsys/plot_"+histoname+"_"+channel_+".png")

