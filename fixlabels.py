import sys

def label(c,ll):
	n = 0
	for l in ll:
		c = c.replace("l_"+str(n).zfill(4),l)
		n = n + 1
	return c

with open(sys.argv[1]) as f:
	contents = f.read()
if sys.argv[2] == "initial":
	contents = label(contents,["vblank","lcd_stat","timer","serial","joypad","begin"])
elif sys.argv[2] == "header":
	contents = label(contents,["nintendo_logo","new_licensee_code","sgb_flag","cart_type","cart_size","sram_size","destination_flag","old_licensee_code","header_checksum","global_checksum"])
	# SGB flag
	contents = contents.replace("; $0146: $03","; $0146: $03 (SGB-compatible").replace("; $0146: $00","; $0146: $00 (SGB-incompatible)")
	# CGB flag
	contents = contents.replace("; $0143: $00","; $0143: $00 (DMG-only)").replace("; $0143: $80","; $0143: $80 (CGB-compatible)").replace("; $0143: $c0","; $0143: $c0 (CGB-only)")
	# old licensee code
	contents = contents.replace("; $014b: $33","; $0143: $33 (SGB-possible)")

t = ["0104 0144 0146 0147 0148 0149 014A 014B 014D 014E"]
with open(sys.argv[1],"w") as f:
	f.write(contents)
