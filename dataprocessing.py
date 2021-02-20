# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 11:10:32 2021

@author: ntruo
"""

#%% tu dien de luu tieng anh
i = 1
dict_eng = {}
for line1 in open("How I Met Your Mother - S02E01.srt"):
    if "-->" in line1:
        continue
    if line1 == "\n":
        continue
    if line1==str(i)+"\n":
        i = i + 1
        continue
    if "\n" in line1:
        line1 = line1.split("\n")
    if dict_eng.get(str(i-1)) is not None:
        dict_eng[str(i-1)] += " "
        dict_eng[str(i-1)] += line1[0]
    else:
        dict_eng[str(i-1)] = line1[0]
    print(line1)
    
#%%

#%% tu dien de luu tieng viet
i = 1
dict_vie = {}
for line1 in open("How I Met Your Mother - s02e01 - Where Were We.srt",encoding='utf-8'):
    if "-->" in line1:
        continue
    if line1 == "\n":
        continue
    if line1==str(i)+"\n":
        i = i + 1
        continue
    if "\n" in line1:
        line1 = line1.split("\n")
    if dict_vie.get(str(i-1)) is not None:
        dict_vie[str(i-1)] += " "
        dict_vie[str(i-1)] += line1[0]
    else:
        dict_vie[str(i-1)] = line1[0]
    print(line1)
