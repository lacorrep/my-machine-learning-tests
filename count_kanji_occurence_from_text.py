# Frequency (occurence rate) of kanjis from a text file
import re
import os
import codecs
from collections import Counter

kana = "がガざザだダばバぱパか゚カ゚ぎギじジぢヂびビぴピき゚キ゚ぐグずズづヅぶブぷプく゚ク゚げゲぜゼでデべベぺペけ゚ケ゚ごゴぞゾどドぼボぽポこ゚コ゚あアかカさサたタなナはハまマやヤらラわワいイきキしシちチにニひヒみミりリゐヰうウくクすスつツぬヌふフむムゆユるルえエけケせセてテねネへヘめメれレゑヱおオこコそソとトのノほホもモよヨろロをヲんンっ" #ゃゅょ
special_characters = "！\.\-―ー—?()（）？…♪\'"

rootdir = "D:/Download" # os.path.dirname(os.path.abspath(__file__))
filename = "The_garden_of_words"
fileext = ".srt"

lines = ""
with open(os.path.join(rootdir,filename+fileext), "r", encoding="utf-8") as filehandle:
	for line in filehandle:
		if line[0:2].isdigit():
			# print("- skipped -")
			continue
		line = line.strip()
		line = re.sub('['+kana+']', '', line) # remove all kana
		line = re.sub('['+special_characters+']', '', line) # remove Japanese special characters
		line = re.sub('[\s0-9a-zA-Z]', '', line) # remove all numbers and roman letters
		# print(line) #debugging
		lines += line

classement = Counter(lines)
print(classement)

keys = list( classement.keys() ) # kanji
val = list( classement.values() ) # individual kanji count
val,keys = zip(*sorted(zip(val,keys),reverse=True))

with open(os.path.join(rootdir,filename+"_FREQUENCY.csv"), "w", encoding="utf-8") as filehandle:
	for v,k in zip(val,keys):
		filehandle.write( k + "," + str(v) + "\n" )