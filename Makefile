default_target: all

all: gbdis gen_test

install:
	cp disasm /usr/local/bin
	cp gbdis /usr/local/bin

gbdis: gen_instruction_parser
	gcc -o gbdis gbdis.c

gen_instruction_parser:
	./gen_instruction_parser.py < mnemonics.txt > instruction_parse.inc

gen_test:
	./gen_test.py > test.bin

test:
	./gbdis < test.bin
