from os import system as cmd, popen


print("KEYBOARD LIGHT FORCE\n\n")

txt = str(popen("brightnessctl --list | grep 'scrolllock\' | egrep --regexp='([0-9])'").read())
txt = txt.split("Device 'input")
opts = []

for t in txt:
	t1 = t.split("::scrolllock' of class 'leds':")[0]
	if t1 != '': opts.append(t1)

def power_(n):
	print("\n")
	for opt in opts:
		cmd(f"brightnessctl --device='input{opt}::scrolllock' set {n}")

cmds = {
	"(A) Ligar": lambda: power_(1),
	"(B) Desligar": lambda: power_(0)
}


print("Escolha uma opção:")
for c in cmds.keys():
	print(c)
i = str(input("\n>> "))

for c in cmds.keys():
	if i.upper() == c[1]:
		cmds[c]()
