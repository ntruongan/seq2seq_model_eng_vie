# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 11:10:32 2021

@author: ntruo
"""

#%% tu dien de luu tieng anh

dict_eng = {}
ep = 1
j = 1
for ep in range (1,19):
    i = 1
    if ep < 10:
        link = "How I Met Your Mother - S02E0%s.srt" % ep
    else: 
        link = "How I Met Your Mother - S02E%s.srt" % ep
    for line1 in open(link):
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
        if "Chuyển ngữ phụ đề bởi" in line1:
            j = j - 1
            continue
        if "\n" in line1:
            line1 = line1.split("\n")
        if dict_vie.get(str(j-1)) is not None:
            dict_vie[str(j-1)] += " "
            dict_vie[str(j-1)] += line1[0]
        else:
            dict_vie[str(j-1)] = line1[0]
        print(line1)
    
#%%
f = open("eng_sub.txt",mode = "w+")
for i, dict1 in enumerate(dict_eng):
    string = str(i+1)+"\t"+dict_eng[str(i+1)] +"\n"
    f.write(string)
f.close()
#%%
f = open("vie_sub.txt",mode = "w+",encoding = "utf-8")
for i, _ in enumerate(dict_vie):
    string = str(i+1)+"\t"+dict_vie[str(i+1)] +"\n"
    f.write(string)
f.close()



#%% 
dictt = []
i = 0
dicttt = []
ep = 1
for ep in range (1,1001):
    if ep < 10:
        name = "N000%s.sgml" % ep
    elif ep < 100:
        name = "N00%s.sgml" % ep
    elif ep < 1000:
        name = "N0%s.sgml" % ep
    elif ep == 1000:
        name = "N1000.sgml"
    
    dictt = []
    # dicttt = []
    
    for line in open(name, encoding = "utf-8"):
        for i, char in enumerate(line):
            if char == "<" and i < len(line):
                while line[i] != ">":
                    line = line[1:]
                line = line[1:]
                if line != "\n":
                    dictt.append(line)
                # print(line)

    for line in dictt:
        for i, char in enumerate(line):
            if char == "<" and i < len(line):
                while line[i] != ">":
                    line = line[0:i]+line[i+1:]
                line = line[0:i]+line[i+1:]
                if line != "\n":
                    dicttt.append(line)
                    
eng_sequences = dicttt[0::2]
vie_sequences = dicttt[1::2]
#%%
vie = open("vie_sequences_sorted_html.txt",mode = "w+", encoding = "utf-8")
for viet in vie_sequences:
    vie.write(viet)
eng = open("eng_sequences_sorted_html.txt",mode = "w+", encoding = "utf-8")
for engl in eng_sequences:
    eng.write(engl)
vie.close()
eng.close()


#%%
            
            
    # i += 1
    # linecor = line.split(">")
    # # print("split >:")
    # # print(linecor)
    # linecor1 = [line.split("<") for line in linecor]
    # # print("split <:")
    # # print(linecor)
    # if len(linecor1)>2:
    #     some = []
    #     some = linecor1 
    #     dictt.append(some[1])
        
    
    # # print(dictt)
    # if i > 15:
        # break
    

 



