# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 11:10:32 2021

@author: ntruo
"""

#%% tu dien de luu tieng anh

dict_eng = {}
ep = 1
j = 1
for ep in range (1,6):
    i = 1
    if ep < 10:
        link = "0%s.srt" % ep
    else: 
        link = "%s.srt" % ep
    for line1 in open(link):
        if "-->" in line1:
            continue
        if line1 == "\n":
            continue
        if line1 == str(i) + "\n":
            i = i + 1
            j = j + 1
            continue
        if "\n" in line1:
            line1 = line1.split("\n")
        if dict_eng.get(str(j-1)) is not None:
            dict_eng[str(j-1)] += " "
            dict_eng[str(j-1)] += line1[0]
        else:
            dict_eng[str(j-1)] = line1[0]
        print(line1)
    
#%%

#%% tu dien de luu tieng viet
dict_vie = {}
ep = 1
j = 1
for ep in range (1,19):
    i = 1
    if ep < 10:
        link = "How.I.Met.Your.Mother.S02E0%s.1080p.NF.WEB-DL.DDP5.1.x264-Ao.Eng_Syned.srt" % ep
    else: 
        link = "How.I.Met.Your.Mother.S02E%s.1080p.NF.WEB-DL.DDP5.1.x264-Ao.Eng_Syned.srt" % ep
    for line1 in open(link,encoding='utf-8'):
        if "-->" in line1:
            continue
        if line1 == "\n":
            continue
        if line1==str(i)+"\n":
            i = i + 1
            j = j + 1
            continue
        if "\n" in line1:
            line1 = line1.split("\n")
        if dict_vie.get(str(j-1)) is not None:
            dict_vie[str(j-1)] += " "
            dict_vie[str(j-1)] += line1[0]
        else:
            dict_vie[str(j-1)] = line1[0]
        print(line1)
    