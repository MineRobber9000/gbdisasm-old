import sys,copy
with open(sys.argv[1]) as f:
	contents = f.read()
lines = contents.split("\n")
olines = copy.copy(lines)
for i in range(len(lines)):
	if lines[i].find("; $4000")>-1:
		olines.insert(i,"SECTION 'bank1',ROMX[1]")
with open(sys.argv[1],"w") as f:
	f.write("\n".join(olines))
