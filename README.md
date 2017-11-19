# THIS REPO IS NO LONGER IN USE, SEE [THIS ONE](https://github.com/MineRobber9000/gbdisasm).
# gbdisasm

To compile the C tool:

```
make
```

To add the files to /usr/local/bin:

```
sudo make install
```

To use:

```
./disasm <rom> <labelscript file>
```

## LabelScript

LabelScript is a script setup that allows you to define your own labels for use in the disassembly process.

The format for lines:

```
<address in all-caps><tab>label_name
```

Example: `0163<tab>.skipLCDdisable1` will put the label ".skipLCDdisable1" at $0163 in the disassembly.
