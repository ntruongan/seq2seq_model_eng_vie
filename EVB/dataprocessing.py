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
def sequences_with_less_than(number_character: int):
    # number_character
    dictt = [] 
    i = 0
    dicttt = []
    ep = 1
    for ep in range (1,1001):
        if ep < 10:
            name = r"D:\IT\RESEARCH\large_project\EVB\N000%s.sgml" % ep
        elif ep < 100:
            name = r"D:\IT\RESEARCH\large_project\EVB\N00%s.sgml" % ep
        elif ep < 1000:
            name = r"D:\IT\RESEARCH\large_project\EVB\N0%s.sgml" % ep
        elif ep == 1000:
            name = r"D:\IT\RESEARCH\large_project\EVB\N1000.sgml"
        
        dictt = []
        # dicttt = []
        trash = 0
        for line in open(name, encoding = "utf-8"):
            if trash < 9:
                trash += 1
                continue
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
    if dicttt is not None:                   
        eng_sequences = dicttt[0::2]
        vie_sequences = dicttt[1::2]
    # for i, seq_len in enumerate(eng_sequences):
    #     if len(seq_len) > number_character:
    #         eng_sequences = eng_sequences[0:i]+eng_sequences[i+1:]
    #         vie_sequences = vie_sequences[0:i]+vie_sequences[i+1:]
    # for i, seq_len in enumerate(vie_sequences):
    #     if len(seq_len) > number_character:
    #         eng_sequences = eng_sequences[0:i]+eng_sequences[i+1:]
    #         vie_sequences = vie_sequences[0:i]+vie_sequences[i+1:]
    tab_values = []
    for i in range(0, len(eng_sequences)):
        if len(eng_sequences[i]) < number_character and len(vie_sequences[i]) < number_character:
            tab_values.append(eng_sequences[i][0:-1] + " \t " + vie_sequences[i])
            
    tab = open("vie_eng_sequences_%s_sorted_html.txt" % number_character,mode = "w+", encoding = "utf-8")
    for li in tab_values:
        tab.write(li)
    vie = open("vie_sequences_%s_sorted_html.txt" % number_character,mode = "w+", encoding = "utf-8")
    for viet in vie_sequences:
        vie.write(viet)
    eng = open("eng_sequences_%s_sorted_html.txt" % number_character,mode = "w+", encoding = "utf-8")
    for engl in eng_sequences:
        eng.write(engl)
    vie.close()
    eng.close()
    # return eng_sequences, vie_sequences

#%% html tab processing
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
input_count = []
for line in open("vie_sequences_sorted_html.txt",mode = "r", encoding = "utf-8"):
    input_count.append(len(line))
   
output_count = []
for line in open("eng_sequences_sorted_html.txt",mode = "r", encoding = "utf-8"):
    output_count.append(len(line))
    

 



