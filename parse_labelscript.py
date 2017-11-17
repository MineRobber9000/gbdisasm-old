# Parses LabelScript, a simple file format to use with this project that allows you to define your own labels

import sys

def label(c,ll):
        n = 0
        for l in ll:
                c = c.replace("l_"+str(n).zfill(4),l)
                n = n + 1
        return c

asmfile = sys.argv[1]
labelfile = sys.argv[2]
action = sys.argv[3]

labels = dict()
labels["0150"]="begin" # used earlier, this is the only real static label

with open(asmfile) as f:
	contents = f.read()
with open(labelfile) as f:
	for line in f:
		if not line:
			continue
		line = line.strip()
		parts = line.split("\t")
		if len(parts)!=2:
			print("Malformed LabelScript!")
			sys.exit(1)
		labels[parts[0]] = parts[1]

def getKeys():
	labelkl = list(labels.keys())
	labelkl = sorted(labelkl)
	return labelkl

if action=="parse":
	sys.stdout.write(" ".join(getKeys()))
elif action=="apply":
	labell = [labels[k] for k in getKeys()]
	contents = label(contents,labell)
	with open(asmfile,"w") as f:
		f.write(contents)
