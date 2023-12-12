# Importar libreriras
import pyttsx3
# Se crea un objeto para la reproducir de voz
voz = pyttsx3.init()
# Inicio del programa
print("-----------------------------------------------")
print("¡Bienvenido!")
# voz.say("Bienvenido usuario")
# voz.runAndWait()
print("-----------------------------------------------")
# Texto a convertir
# voz.say("Por favor ingresar el texto : .....")
# voz.runAndWait()
# Se ingresa texto
print("Texto : ")
texto_1 = input()
# Se transforma a lista por separado, se asigna tamaño y se crea listas
lista_1 = list(texto_1)
tamañano = len(lista_1)
lista_2 = list()
print("Tamañana de la lista es de : " + str(tamañano))
print("-----------------------------------------------")
# Declaracion del codigo secreto
crt1 = "´"
crt2 = "¹"
crt3 = "▀"
crt4 = "¼"
crt5 = "Ñ"
crt6 = "v"
crt7 = "☺"
crt8 = "├"
crt9 = "Ó"
crt10 = "┬"
crt11 = "p"
crt12 = "×"
crt13 = "<"
crt14 = "¢"
crt15 = "ô"
crt16 = "R"
crt17 = "¥"
crt18 = "m"
crt19 = "♪"
crt20 = "Ú"
crt21 = "ë"
crt22 = "h"
crt23 = "ú"
crt24 = "S"
crt25 = "d"
crt26 = "┼"
crt27 = "¤"
crt28 = "l"
crt29 = "å"
crt30 = "↓"
crt31 = "•"
crt32 = "Ê"
crt33 = "è"
crt34 = "♥"
crt35 = "¿"
crt36 = "Å"
crt37 = "g"
crt38 = "┘"
crt39 = "Á"
crt40 = "G"
crt41 = " \ "
crt42 = "#"
crt43 = "z"
crt44 = "┤"
crt45 = "♦"
crt46 = "©"
crt47 = "·"
crt48 = "░"
crt49 = "t"
crt50 = "H"
crt51 = "╚"
crt52 = "☼"
crt53 = "V"
crt54 = "Q"
crt55 = "_"
crt56 = "ï"
crt57 = "²"
crt58 = "2"
crt59 = "D"
crt60 = "â"
crt61 = "↑"
crt62 = "Ì"
crt63 = "Ý"
crt64 = "¾"
crt65 = "═"
crt66 = "i"
crt67 = "♫"
crt68 = "♂"
crt69 = "ç"
crt70 = "¸"
crt71 = "Ò"
crt72 = "K"
crt73 = "╩"
crt74 = "5"
crt75 = "J"
crt76 = "→"
crt77 = "Z"
crt78 = "`"
crt79 = "█"
crt80 = "─"
crt81 = "ÿ"
crt82 = "←"
crt83 = "ü"
crt84 = "1"
crt85 = "╣"
crt86 = "§"
crt87 = "Ö"
crt88 = "ê"
crt89 = "╔"
crt90 = "y"
crt91 = "9"
crt92 = "↕"
crt93 = "Ï"
crt94 = "é"
crt95 = "4"
crt96 = "☻"
crt97 = "Þ"
crt98 = "§"
crt99 = "'"
crt100 = ">"
crt101 = "▄"
crt102 = "►"
crt103 = "ö"
crt104 = "~"
crt105 = ","
crt106 = "k"
crt107 = "Ô"
crt108 = "^"
crt109 = "À"
crt110 = "/"
crt111 = "?"
crt112 = "T"
crt113 = "7"
crt114 = "ƒ"
crt115 = "q"
crt116 = "j"
crt117 = "♀"
crt118 = "í"
crt119 = "6"
crt120 = "+"
crt121 = "¯"
crt122 = "½"
crt123 = "-"
crt124 = "Ç"
crt125 = "Î"
crt126 = "{"
crt127 = "."
crt128 = "○"
crt129 = "M"
crt130 = "W"
crt131 = "["
crt132 = "]"
crt133 = "ò"
crt134 = "◙"
crt135 = "$"
crt136 = "¨"
crt137 = "Â"
crt138 = "ì"
crt139 = "F"
crt140 = "╠"
crt141 = "Ä"
crt142 = "ß"
crt143 = "Ë"
crt144 = "»"
crt145 = "‗"
crt146 = "Ð"
crt147 = "╬"
crt148 = "Ù"
crt149 = "|"
crt150 = "Ã"
crt151 = "ª"
crt152 = "Í"
crt153 = "┌"
crt154 = "Ü"
crt155 = "O"
crt156 = "a"
crt157 = "0"
crt158 = ")"
crt159 = "&"
crt160 = "ã"
crt161 = "↨"
crt162 = "="
crt163 = "Ø"
crt164 = "3"
crt165 = "r"
crt166 = "¶"
crt167 = "╝"
crt168 = "ù"
crt169 = "╦"
crt170 = "þ"
crt171 = "U"
crt172 = "o"
crt173 = "®"
crt174 = "◘"
crt175 = "N"
crt176 = "§"
crt177 = "¶"
crt178 = "║"
crt179 = "ð"
crt180 = "É"
crt181 = "f"
crt182 = "8"
crt183 = "È"
crt184 = "I"
crt185 = "└"
crt186 = "e"
crt187 = "ñ"
crt188 = "╗"
crt189 = "@"
crt190 = "ı"
crt191 = "ó"
crt192 = "♠"
crt193 = "▒"
crt194 = "ä"
crt195 = "u"
crt196 = "°"
crt197 = '"'
crt198 = "↔"
crt199 = "³"
crt200 = "û"
crt201 = "▓"
crt202 = "x"
crt203 = "î"
crt204 = "¦"
crt205 = "s"
crt206 = "ý"
crt207 = "E"
crt208 = "Æ"
crt209 = "Y"
crt210 = "▬"
crt211 = "!"
crt212 = "P"
crt213 = "♣"
crt214 = "w"
crt215 = "%"
crt216 = "∟"
crt217 = "‼"
crt218 = "A"
crt219 = "Û"
crt220 = "¬"
crt221 = "L"
crt222 = "æ"
crt223 = "("
crt224 = "▲"
crt225 = "c"
crt226 = "õ"
crt227 = "÷"
crt228 = "ø"
crt229 = "C"
crt230 = "◄"
crt231 = "n"
crt232 = "º"
crt233 = "┐"
crt234 = "«"
crt235 = "■"
crt236 = "│"
crt237 = "}"
crt238 = "B"
crt239 = "£"
crt240 = "±"
crt241 = "*"
crt242 = "b"
crt243 = "X"
crt244 = "┴"
crt245 = "à"
crt246 = ";"
crt247 = "µ"
crt248 = "¡"
crt249 = "Õ"
crt250 = ":"
crt251 = "á"
crt252 = " "


print("-----------------------------------------------")
# Proceso logico para cifrar
for f2 in range(0, tamañano):
    if lista_1[f2] == "!":
        lista_2.append(crt1)
    elif lista_1[f2] == "#":
        lista_2.append(crt3)
    elif lista_1[f2] == "$":
        lista_2.append(crt4)
    elif lista_1[f2] == "%":
        lista_2.append(crt5)
    elif lista_1[f2] == "&":
        lista_2.append(crt6)
    elif lista_1[f2] == "'":
        lista_2.append(crt7)
    elif lista_1[f2] == "(":
        lista_2.append(crt8)
    elif lista_1[f2] == ")":
        lista_2.append(crt9)
    elif lista_1[f2] == "*":
        lista_2.append(crt10)
    elif lista_1[f2] == "+":
        lista_2.append(crt11)
    elif lista_1[f2] == ",":
        lista_2.append(crt12)
    elif lista_1[f2] == "-":
        lista_2.append(crt13)
    elif lista_1[f2] == ".":
        lista_2.append(crt14)
    elif lista_1[f2] == "/":
        lista_2.append(crt15)
    elif lista_1[f2] == "0":
        lista_2.append(crt16)
    elif lista_1[f2] == "1":
        lista_2.append(crt17)
    elif lista_1[f2] == "2":
        lista_2.append(crt18)
    elif lista_1[f2] == "3":
        lista_2.append(crt19)
    elif lista_1[f2] == "4":
        lista_2.append(crt20)
    elif lista_1[f2] == "5":
        lista_2.append(crt21)
    elif lista_1[f2] == "6":
        lista_2.append(crt22)
    elif lista_1[f2] == "7":
        lista_2.append(crt23)
    elif lista_1[f2] == "8":
        lista_2.append(crt24)
    elif lista_1[f2] == "9":
        lista_2.append(crt25)
    elif lista_1[f2] == ":":
        lista_2.append(crt26)
    elif lista_1[f2] == ";":
        lista_2.append(crt27)
    elif lista_1[f2] == "<":
        lista_2.append(crt28)
    elif lista_1[f2] == "=":
        lista_2.append(crt29)
    elif lista_1[f2] == ">":
        lista_2.append(crt30)
    elif lista_1[f2] == "?":
        lista_2.append(crt31)
    elif lista_1[f2] == "@":
        lista_2.append(crt32)
    elif lista_1[f2] == "A":
        lista_2.append(crt33)
    elif lista_1[f2] == "B":
        lista_2.append(crt34)
    elif lista_1[f2] == "C":
        lista_2.append(crt35)
    elif lista_1[f2] == "D":
        lista_2.append(crt36)
    elif lista_1[f2] == "E":
        lista_2.append(crt37)
    elif lista_1[f2] == "F":
        lista_2.append(crt38)
    elif lista_1[f2] == "G":
        lista_2.append(crt39)
    elif lista_1[f2] == "H":
        lista_2.append(crt40)
    elif lista_1[f2] == "I":
        lista_2.append(crt41)
    elif lista_1[f2] == "J":
        lista_2.append(crt42)
    elif lista_1[f2] == "K":
        lista_2.append(crt43)
    elif lista_1[f2] == "L":
        lista_2.append(crt44)
    elif lista_1[f2] == "M":
        lista_2.append(crt45)
    elif lista_1[f2] == "N":
        lista_2.append(crt46)
    elif lista_1[f2] == "O":
        lista_2.append(crt47)
    elif lista_1[f2] == "P":
        lista_2.append(crt48)
    elif lista_1[f2] == "Q":
        lista_2.append(crt49)
    elif lista_1[f2] == "R":
        lista_2.append(crt50)
    elif lista_1[f2] == "S":
        lista_2.append(crt51)
    elif lista_1[f2] == "T":
        lista_2.append(crt52)
    elif lista_1[f2] == "U":
        lista_2.append(crt53)
    elif lista_1[f2] == "V":
        lista_2.append(crt54)
    elif lista_1[f2] == "W":
        lista_2.append(crt55)
    elif lista_1[f2] == "X":
        lista_2.append(crt56)
    elif lista_1[f2] == "Y":
        lista_2.append(crt57)
    elif lista_1[f2] == "Z":
        lista_2.append(crt58)
    elif lista_1[f2] == "[":
        lista_2.append(crt59)
    elif lista_1[f2] == " \ ":
        lista_2.append(crt60)
    elif lista_1[f2] == "]":
        lista_2.append(crt61)
    elif lista_1[f2] == "^":
        lista_2.append(crt62)
    elif lista_1[f2] == "_":
        lista_2.append(crt63)
    elif lista_1[f2] == "`":
        lista_2.append(crt64)
    elif lista_1[f2] == "a":
        lista_2.append(crt65)
    elif lista_1[f2] == "b":
        lista_2.append(crt66)
    elif lista_1[f2] == "c":
        lista_2.append(crt67)
    elif lista_1[f2] == "d":
        lista_2.append(crt68)
    elif lista_1[f2] == "e":
        lista_2.append(crt69)
    elif lista_1[f2] == "f":
        lista_2.append(crt70)
    elif lista_1[f2] == "g":
        lista_2.append(crt71)
    elif lista_1[f2] == "h":
        lista_2.append(crt72)
    elif lista_1[f2] == "i":
        lista_2.append(crt73)
    elif lista_1[f2] == "j":
        lista_2.append(crt74)
    elif lista_1[f2] == "k":
        lista_2.append(crt75)
    elif lista_1[f2] == "l":
        lista_2.append(crt76)
    elif lista_1[f2] == "m":
        lista_2.append(crt77)
    elif lista_1[f2] == "n":
        lista_2.append(crt78)
    elif lista_1[f2] == "o":
        lista_2.append(crt79)
    elif lista_1[f2] == "p":
        lista_2.append(crt80)
    elif lista_1[f2] == "q":
        lista_2.append(crt81)
    elif lista_1[f2] == "r":
        lista_2.append(crt82)
    elif lista_1[f2] == "s":
        lista_2.append(crt83)
    elif lista_1[f2] == "t":
        lista_2.append(crt84)
    elif lista_1[f2] == "u":
        lista_2.append(crt85)
    elif lista_1[f2] == "v":
        lista_2.append(crt86)
    elif lista_1[f2] == "w":
        lista_2.append(crt87)
    elif lista_1[f2] == "x":
        lista_2.append(crt88)
    elif lista_1[f2] == "y":
        lista_2.append(crt89)
    elif lista_1[f2] == "z":
        lista_2.append(crt90)
    elif lista_1[f2] == "{":
        lista_2.append(crt91)
    elif lista_1[f2] == "|":
        lista_2.append(crt92)
    elif lista_1[f2] == "}":
        lista_2.append(crt93)
    elif lista_1[f2] == "~":
        lista_2.append(crt94)
    elif lista_1[f2] == " ":
        lista_2.append(crt95)
    elif lista_1[f2] == "Ç":
        lista_2.append(crt96)
    elif lista_1[f2] == "ü":
        lista_2.append(crt97)
    elif lista_1[f2] == "é":
        lista_2.append(crt98)
    elif lista_1[f2] == "â":
        lista_2.append(crt99)
    elif lista_1[f2] == "ä":
        lista_2.append(crt100)
    elif lista_1[f2] == "à":
        lista_2.append(crt101)
    elif lista_1[f2] == "å":
        lista_2.append(crt102)
    elif lista_1[f2] == "ç":
        lista_2.append(crt103)
    elif lista_1[f2] == "ê":
        lista_2.append(crt104)
    elif lista_1[f2] == "ë":
        lista_2.append(crt105)
    elif lista_1[f2] == "è":
        lista_2.append(crt106)
    elif lista_1[f2] == "ï":
        lista_2.append(crt107)
    elif lista_1[f2] == "î":
        lista_2.append(crt108)
    elif lista_1[f2] == "ì":
        lista_2.append(crt109)
    elif lista_1[f2] == "Ä":
        lista_2.append(crt110)
    elif lista_1[f2] == "Å":
        lista_2.append(crt111)
    elif lista_1[f2] == "É":
        lista_2.append(crt112)
    elif lista_1[f2] == "æ":
        lista_2.append(crt113)
    elif lista_1[f2] == "Æ":
        lista_2.append(crt114)
    elif lista_1[f2] == "ô":
        lista_2.append(crt115)
    elif lista_1[f2] == "ö":
        lista_2.append(crt116)
    elif lista_1[f2] == "ò":
        lista_2.append(crt117)
    elif lista_1[f2] == "û":
        lista_2.append(crt118)
    elif lista_1[f2] == "ù":
        lista_2.append(crt119)
    elif lista_1[f2] == "ÿ":
        lista_2.append(crt120)
    elif lista_1[f2] == "Ö":
        lista_2.append(crt121)
    elif lista_1[f2] == "Ü":
        lista_2.append(crt122)
    elif lista_1[f2] == "ø":
        lista_2.append(crt123)
    elif lista_1[f2] == "£":
        lista_2.append(crt124)
    elif lista_1[f2] == "Ø":
        lista_2.append(crt125)
    elif lista_1[f2] == "×":
        lista_2.append(crt126)
    elif lista_1[f2] == "ƒ":
        lista_2.append(crt127)
    elif lista_1[f2] == "á":
        lista_2.append(crt128)
    elif lista_1[f2] == "í":
        lista_2.append(crt129)
    elif lista_1[f2] == "ó":
        lista_2.append(crt130)
    elif lista_1[f2] == "ú":
        lista_2.append(crt131)
    elif lista_1[f2] == "ñ":
        lista_2.append(crt132)
    elif lista_1[f2] == "Ñ":
        lista_2.append(crt133)
    elif lista_1[f2] == "ª":
        lista_2.append(crt134)
    elif lista_1[f2] == "º":
        lista_2.append(crt135)
    elif lista_1[f2] == "¿":
        lista_2.append(crt136)
    elif lista_1[f2] == "®":
        lista_2.append(crt137)
    elif lista_1[f2] == "¬":
        lista_2.append(crt138)
    elif lista_1[f2] == "½":
        lista_2.append(crt139)
    elif lista_1[f2] == "¼":
        lista_2.append(crt140)
    elif lista_1[f2] == "¡":
        lista_2.append(crt141)
    elif lista_1[f2] == "«":
        lista_2.append(crt142)
    elif lista_1[f2] == "»":
        lista_2.append(crt143)
    elif lista_1[f2] == "░":
        lista_2.append(crt144)
    elif lista_1[f2] == "▒":
        lista_2.append(crt145)
    elif lista_1[f2] == "▓":
        lista_2.append(crt146)
    elif lista_1[f2] == "│":
        lista_2.append(crt147)
    elif lista_1[f2] == "┤":
        lista_2.append(crt148)
    elif lista_1[f2] == "Á":
        lista_2.append(crt149)
    elif lista_1[f2] == "Â":
        lista_2.append(crt150)
    elif lista_1[f2] == "À":
        lista_2.append(crt151)
    elif lista_1[f2] == "©":
        lista_2.append(crt152)
    elif lista_1[f2] == "╣":
        lista_2.append(crt153)
    elif lista_1[f2] == "║":
        lista_2.append(crt154)
    elif lista_1[f2] == "╗":
        lista_2.append(crt155)
    elif lista_1[f2] == "╝":
        lista_2.append(crt156)
    elif lista_1[f2] == "¢":
        lista_2.append(crt157)
    elif lista_1[f2] == "¥":
        lista_2.append(crt158)
    elif lista_1[f2] == "┐":
        lista_2.append(crt159)
    elif lista_1[f2] == "└":
        lista_2.append(crt160)
    elif lista_1[f2] == "┴":
        lista_2.append(crt161)
    elif lista_1[f2] == "┬":
        lista_2.append(crt162)
    elif lista_1[f2] == "├":
        lista_2.append(crt163)
    elif lista_1[f2] == "─":
        lista_2.append(crt164)
    elif lista_1[f2] == "┼":
        lista_2.append(crt165)
    elif lista_1[f2] == "ã":
        lista_2.append(crt166)
    elif lista_1[f2] == "Ã":
        lista_2.append(crt167)
    elif lista_1[f2] == "╚":
        lista_2.append(crt168)
    elif lista_1[f2] == "╔":
        lista_2.append(crt169)
    elif lista_1[f2] == "╩":
        lista_2.append(crt170)
    elif lista_1[f2] == "╦":
        lista_2.append(crt171)
    elif lista_1[f2] == "╠":
        lista_2.append(crt172)
    elif lista_1[f2] == "═":
        lista_2.append(crt173)
    elif lista_1[f2] == "╬":
        lista_2.append(crt174)
    elif lista_1[f2] == "¤":
        lista_2.append(crt175)
    elif lista_1[f2] == "ð":
        lista_2.append(crt176)
    elif lista_1[f2] == "Ð":
        lista_2.append(crt177)
    elif lista_1[f2] == "Ê":
        lista_2.append(crt178)
    elif lista_1[f2] == "Ë":
        lista_2.append(crt179)
    elif lista_1[f2] == "È":
        lista_2.append(crt180)
    elif lista_1[f2] == "ı":
        lista_2.append(crt181)
    elif lista_1[f2] == "Í":
        lista_2.append(crt182)
    elif lista_1[f2] == "Î":
        lista_2.append(crt183)
    elif lista_1[f2] == "Ï":
        lista_2.append(crt184)
    elif lista_1[f2] == "┘":
        lista_2.append(crt185)
    elif lista_1[f2] == "┌":
        lista_2.append(crt186)
    elif lista_1[f2] == "█":
        lista_2.append(crt187)
    elif lista_1[f2] == "▄":
        lista_2.append(crt188)
    elif lista_1[f2] == "¦":
        lista_2.append(crt189)
    elif lista_1[f2] == "Ì":
        lista_2.append(crt190)
    elif lista_1[f2] == "▀":
        lista_2.append(crt191)
    elif lista_1[f2] == "Ó":
        lista_2.append(crt192)
    elif lista_1[f2] == "ß":
        lista_2.append(crt193)
    elif lista_1[f2] == "Ô":
        lista_2.append(crt194)
    elif lista_1[f2] == "Ò":
        lista_2.append(crt195)
    elif lista_1[f2] == "õ":
        lista_2.append(crt196)
    elif lista_1[f2] == "Õ":
        lista_2.append(crt197)
    elif lista_1[f2] == "µ":
        lista_2.append(crt198)
    elif lista_1[f2] == "þ":
        lista_2.append(crt199)
    elif lista_1[f2] == "Þ":
        lista_2.append(crt200)
    elif lista_1[f2] == "Ú":
        lista_2.append(crt201)
    elif lista_1[f2] == "Û":
        lista_2.append(crt202)
    elif lista_1[f2] == "Ù":
        lista_2.append(crt203)
    elif lista_1[f2] == "ý":
        lista_2.append(crt204)
    elif lista_1[f2] == "Ý":
        lista_2.append(crt205)
    elif lista_1[f2] == "¯":
        lista_2.append(crt206)
    elif lista_1[f2] == "´":
        lista_2.append(crt207)
    elif lista_1[f2] == "±":
        lista_2.append(crt208)
    elif lista_1[f2] == "‗":
        lista_2.append(crt209)
    elif lista_1[f2] == "¾":
        lista_2.append(crt210)
    elif lista_1[f2] == "¶":
        lista_2.append(crt211)
    elif lista_1[f2] == "§":
        lista_2.append(crt212)
    elif lista_1[f2] == "÷":
        lista_2.append(crt213)
    elif lista_1[f2] == "¸":
        lista_2.append(crt214)
    elif lista_1[f2] == "°":
        lista_2.append(crt215)
    elif lista_1[f2] == "¨":
        lista_2.append(crt216)
    elif lista_1[f2] == "·":
        lista_2.append(crt217)
    elif lista_1[f2] == "¹":
        lista_2.append(crt218)
    elif lista_1[f2] == "³":
        lista_2.append(crt219)
    elif lista_1[f2] == "²":
        lista_2.append(crt220)
    elif lista_1[f2] == "■":
        lista_2.append(crt221)
    elif lista_1[f2] == "☺":
        lista_2.append(crt222)
    elif lista_1[f2] == "☻":
        lista_2.append(crt223)
    elif lista_1[f2] == "♥":
        lista_2.append(crt224)
    elif lista_1[f2] == "♦":
        lista_2.append(crt225)
    elif lista_1[f2] == "♣":
        lista_2.append(crt226)
    elif lista_1[f2] == "♠":
        lista_2.append(crt227)
    elif lista_1[f2] == "•":
        lista_2.append(crt228)
    elif lista_1[f2] == "◘":
        lista_2.append(crt229)
    elif lista_1[f2] == "○":
        lista_2.append(crt230)
    elif lista_1[f2] == "◙":
        lista_2.append(crt231)
    elif lista_1[f2] == "♂":
        lista_2.append(crt232)
    elif lista_1[f2] == "♀":
        lista_2.append(crt233)
    elif lista_1[f2] == "♪":
        lista_2.append(crt234)
    elif lista_1[f2] == "♫":
        lista_2.append(crt235)
    elif lista_1[f2] == "☼":
        lista_2.append(crt236)
    elif lista_1[f2] == "►":
        lista_2.append(crt237)
    elif lista_1[f2] == "◄":
        lista_2.append(crt238)
    elif lista_1[f2] == "↕":
        lista_2.append(crt239)
    elif lista_1[f2] == "‼":
        lista_2.append(crt240)
    elif lista_1[f2] == "¶":
        lista_2.append(crt241)
    elif lista_1[f2] == "§":
        lista_2.append(crt242)
    elif lista_1[f2] == "▬":
        lista_2.append(crt243)
    elif lista_1[f2] == "↨":
        lista_2.append(crt244)
    elif lista_1[f2] == "↑":
        lista_2.append(crt245)
    elif lista_1[f2] == "↓":
        lista_2.append(crt246)
    elif lista_1[f2] == "→":
        lista_2.append(crt247)
    elif lista_1[f2] == "←":
        lista_2.append(crt248)
    elif lista_1[f2] == "∟":
        lista_2.append(crt249)
    elif lista_1[f2] == "↔":
        lista_2.append(crt250)
    elif lista_1[f2] == "▲":
        lista_2.append(crt251)
    elif lista_1[f2] == "§":
        lista_2.append(crt252)

# Resultado
resultado = "".join(str(x) for x in lista_2)
print(resultado)

# Declaracion del codigo

lista_3 = list()

crtd1 = "!"
crtd2 = '"'
crtd3 = "#"
crtd4 = "$"
crtd5 = "%"
crtd6 = "&"
crtd7 = "'"
crtd8 = "("
crtd9 = ")"
crtd10 = "*"
crtd11 = "+"
crtd12 = ","
crtd13 = "-"
crtd14 = "."
crtd15 = "/"
crtd16 = "0"
crtd17 = "1"
crtd18 = "2"
crtd19 = "3"
crtd20 = "4"
crtd21 = "5"
crtd22 = "6"
crtd23 = "7"
crtd24 = "8"
crtd25 = "9"
crtd26 = ":"
crtd27 = ";"
crtd28 = "<"
crtd29 = "="
crtd30 = ">"
crtd31 = "?"
crtd32 = "@"
crtd33 = "A"
crtd34 = "B"
crtd35 = "C"
crtd36 = "D"
crtd37 = "E"
crtd38 = "F"
crtd39 = "G"
crtd40 = "H"
crtd41 = "I"
crtd42 = "J"
crtd43 = "K"
crtd44 = "L"
crtd45 = "M"
crtd46 = "N"
crtd47 = "O"
crtd48 = "P"
crtd49 = "Q"
crtd50 = "R"
crtd51 = "S"
crtd52 = "T"
crtd53 = "U"
crtd54 = "V"
crtd55 = "W"
crtd56 = "X"
crtd57 = "Y"
crtd58 = "Z"
crtd59 = "["
crtd60 = " \ "
crtd61 = "]"
crtd62 = "^"
crtd63 = "_"
crtd64 = "`"
crtd65 = "a"
crtd66 = "b"
crtd67 = "c"
crtd68 = "d"
crtd69 = "e"
crtd70 = "f"
crtd71 = "g"
crtd72 = "h"
crtd73 = "i"
crtd74 = "j"
crtd75 = "k"
crtd76 = "l"
crtd77 = "m"
crtd78 = "n"
crtd79 = "o"
crtd80 = "p"
crtd81 = "q"
crtd82 = "r"
crtd83 = "s"
crtd84 = "t"
crtd85 = "u"
crtd86 = "v"
crtd87 = "w"
crtd88 = "x"
crtd89 = "y"
crtd90 = "z"
crtd91 = "{"
crtd92 = "|"
crtd93 = "}"
crtd94 = "~"
crtd95 = " "
crtd96 = "Ç"
crtd97 = "ü"
crtd98 = "é"
crtd99 = "â"
crtd100 = "ä"
crtd101 = "à"
crtd102 = "å"
crtd103 = "ç"
crtd104 = "ê"
crtd105 = "ë"
crtd106 = "è"
crtd107 = "ï"
crtd108 = "î"
crtd109 = "ì"
crtd110 = "Ä"
crtd111 = "Å"
crtd112 = "É"
crtd113 = "æ"
crtd114 = "Æ"
crtd115 = "ô"
crtd116 = "ö"
crtd117 = "ò"
crtd118 = "û"
crtd119 = "ù"
crtd120 = "ÿ"
crtd121 = "Ö"
crtd122 = "Ü"
crtd123 = "ø"
crtd124 = "£"
crtd125 = "Ø"
crtd126 = "×"
crtd127 = "ƒ"
crtd128 = "á"
crtd129 = "í"
crtd130 = "ó"
crtd131 = "ú"
crtd132 = "ñ"
crtd133 = "Ñ"
crtd134 = "ª"
crtd135 = "º"
crtd136 = "¿"
crtd137 = "®"
crtd138 = "¬"
crtd139 = "½"
crtd140 = "¼"
crtd141 = "¡"
crtd142 = "«"
crtd143 = "»"
crtd144 = "░"
crtd145 = "▒"
crtd146 = "▓"
crtd147 = "│"
crtd148 = "┤"
crtd149 = "Á"
crtd150 = "Â"
crtd151 = "À"
crtd152 = "©"
crtd153 = "╣"
crtd154 = "║"
crtd155 = "╗"
crtd156 = "╝"
crtd157 = "¢"
crtd158 = "¥"
crtd159 = "┐"
crtd160 = "└"
crtd161 = "┴"
crtd162 = "┬"
crtd163 = "├"
crtd164 = "─"
crtd165 = "┼"
crtd166 = "ã"
crtd167 = "Ã"
crtd168 = "╚"
crtd169 = "╔"
crtd170 = "╩"
crtd171 = "╦"
crtd172 = "╠"
crtd173 = "═"
crtd174 = "╬"
crtd175 = "¤"
crtd176 = "ð"
crtd177 = "Ð"
crtd178 = "Ê"
crtd179 = "Ë"
crtd180 = "È"
crtd181 = "ı"
crtd182 = "Í"
crtd183 = "Î"
crtd184 = "Ï"
crtd185 = "┘"
crtd186 = "┌"
crtd187 = "█"
crtd188 = "▄"
crtd189 = "¦"
crtd190 = "Ì"
crtd191 = "▀"
crtd192 = "Ó"
crtd193 = "ß"
crtd194 = "Ô"
crtd195 = "Ò"
crtd196 = "õ"
crtd197 = "Õ"
crtd198 = "µ"
crtd199 = "þ"
crtd200 = "Þ"
crtd201 = "Ú"
crtd202 = "Û"
crtd203 = "Ù"
crtd204 = "ý"
crtd205 = "Ý"
crtd206 = "¯"
crtd207 = "´"
crtd208 = "±"
crtd209 = "‗"
crtd210 = "¾"
crtd211 = "¶"
crtd212 = "§"
crtd213 = "÷"
crtd214 = "¸"
crtd215 = "°"
crtd216 = "¨"
crtd217 = "·"
crtd218 = "¹"
crtd219 = "³"
crtd220 = "²"
crtd221 = "■"
crtd222 = "☺"
crtd223 = "☻"
crtd224 = "♥"
crtd225 = "♦"
crtd226 = "♣"
crtd227 = "♠"
crtd228 = "•"
crtd229 = "◘"
crtd230 = "○"
crtd231 = "◙"
crtd232 = "♂"
crtd233 = "♀"
crtd234 = "♪"
crtd235 = "♫"
crtd236 = "☼"
crtd237 = "►"
crtd238 = "◄"
crtd239 = "↕"
crtd240 = "‼"
crtd241 = "¶"
crtd242 = "§"
crtd243 = "▬"
crtd244 = "↨"
crtd245 = "↑"
crtd246 = "↓"
crtd247 = "→"
crtd248 = "←"
crtd249 = "∟"
crtd250 = "↔"
crtd251 = "▲"
crtd252 = "§"
# Proceso logico para decifrar
for f3 in range(0, tamañano):
    if lista_2[f3] == "´":
        lista_3.append(crtd1)
    elif lista_2[f3] == "¹":
        lista_3.append(crtd2)
    elif lista_2[f3] == "▀":
        lista_3.append(crtd3)
    elif lista_2[f3] == "¼":
        lista_3.append(crtd4)
    elif lista_2[f3] == "Ñ":
        lista_3.append(crtd5)
    elif lista_2[f3] == "v":
        lista_3.append(crtd6)
    elif lista_2[f3] == "☺":
        lista_3.append(crtd7)
    elif lista_2[f3] == "├":
        lista_3.append(crtd8)
    elif lista_2[f3] == "Ó":
        lista_3.append(crtd9)
    elif lista_2[f3] == "┬":
        lista_3.append(crtd10)
    elif lista_2[f3] == "p":
        lista_3.append(crtd11)
    elif lista_2[f3] == "×":
        lista_3.append(crtd12)
    elif lista_2[f3] == "<":
        lista_3.append(crtd13)
    elif lista_2[f3] == "¢":
        lista_3.append(crtd14)
    elif lista_2[f3] == "ô":
        lista_3.append(crtd15)
    elif lista_2[f3] == "R":
        lista_3.append(crtd16)
    elif lista_2[f3] == "¥":
        lista_3.append(crtd17)
    elif lista_2[f3] == "m":
        lista_3.append(crtd18)
    elif lista_2[f3] == "♪":
        lista_3.append(crtd19)
    elif lista_2[f3] == "Ú":
        lista_3.append(crtd20)
    elif lista_2[f3] == "ë":
        lista_3.append(crtd21)
    elif lista_2[f3] == "h":
        lista_3.append(crtd22)
    elif lista_2[f3] == "ú":
        lista_3.append(crtd23)
    elif lista_2[f3] == "S":
        lista_3.append(crtd24)
    elif lista_2[f3] == "d":
        lista_3.append(crtd25)
    elif lista_2[f3] == "┼":
        lista_3.append(crtd26)
    elif lista_2[f3] == "¤":
        lista_3.append(crtd27)
    elif lista_2[f3] == "l":
        lista_3.append(crtd28)
    elif lista_2[f3] == "å":
        lista_3.append(crtd29)
    elif lista_2[f3] == "↓":
        lista_3.append(crtd30)
    elif lista_2[f3] == "•":
        lista_3.append(crtd31)
    elif lista_2[f3] == "Ê":
        lista_3.append(crtd32)
    elif lista_2[f3] == "è":
        lista_3.append(crtd33)
    elif lista_2[f3] == "♥":
        lista_3.append(crtd34)
    elif lista_2[f3] == "¿":
        lista_3.append(crtd35)
    elif lista_2[f3] == "Å":
        lista_3.append(crtd36)
    elif lista_2[f3] == "g":
        lista_3.append(crtd37)
    elif lista_2[f3] == "┘":
        lista_3.append(crtd38)
    elif lista_2[f3] == "Á":
        lista_3.append(crtd39)
    elif lista_2[f3] == "G":
        lista_3.append(crtd40)
    elif lista_2[f3] == " \ ":
        lista_3.append(crtd41)
    elif lista_2[f3] == "#":
        lista_3.append(crtd42)
    elif lista_2[f3] == "z":
        lista_3.append(crtd43)
    elif lista_2[f3] == "┤":
        lista_3.append(crtd44)
    elif lista_2[f3] == "♦":
        lista_3.append(crtd45)
    elif lista_2[f3] == "©":
        lista_3.append(crtd46)
    elif lista_2[f3] == "·":
        lista_3.append(crtd47)
    elif lista_2[f3] == "░":
        lista_3.append(crtd48)
    elif lista_2[f3] == "t":
        lista_3.append(crtd49)
    elif lista_2[f3] == "H":
        lista_3.append(crtd50)
    elif lista_2[f3] == "╚":
        lista_3.append(crtd51)
    elif lista_2[f3] == "☼":
        lista_3.append(crtd52)
    elif lista_2[f3] == "V":
        lista_3.append(crtd53)
    elif lista_2[f3] == "Q":
        lista_3.append(crtd54)
    elif lista_2[f3] == "_":
        lista_3.append(crtd55)
    elif lista_2[f3] == "ï":
        lista_3.append(crtd56)
    elif lista_2[f3] == "²":
        lista_3.append(crtd57)
    elif lista_2[f3] == "2":
        lista_3.append(crtd58)
    elif lista_2[f3] == "D":
        lista_3.append(crtd59)
    elif lista_2[f3] == "â":
        lista_3.append(crtd60)
    elif lista_2[f3] == "↑":
        lista_3.append(crtd61)
    elif lista_2[f3] == "Ì":
        lista_3.append(crtd62)
    elif lista_2[f3] == "Ý":
        lista_3.append(crtd63)
    elif lista_2[f3] == "¾":
        lista_3.append(crtd64)
    elif lista_2[f3] == "═":
        lista_3.append(crtd65)
    elif lista_2[f3] == "i":
        lista_3.append(crtd66)
    elif lista_2[f3] == "♫":
        lista_3.append(crtd67)
    elif lista_2[f3] == "♂":
        lista_3.append(crtd68)
    elif lista_2[f3] == "ç":
        lista_3.append(crtd69)
    elif lista_2[f3] == "¸":
        lista_3.append(crtd70)
    elif lista_2[f3] == "Ò":
        lista_3.append(crtd71)
    elif lista_2[f3] == "K":
        lista_3.append(crtd72)
    elif lista_2[f3] == "╩":
        lista_3.append(crtd73)
    elif lista_2[f3] == "5":
        lista_3.append(crtd74)
    elif lista_2[f3] == "J":
        lista_3.append(crtd75)
    elif lista_2[f3] == "→":
        lista_3.append(crtd76)
    elif lista_2[f3] == "Z":
        lista_3.append(crtd77)
    elif lista_2[f3] == "`":
        lista_3.append(crtd78)
    elif lista_2[f3] == "█":
        lista_3.append(crtd79)
    elif lista_2[f3] == "─":
        lista_3.append(crtd80)
    elif lista_2[f3] == "ÿ":
        lista_3.append(crtd81)
    elif lista_2[f3] == "←":
        lista_3.append(crtd82)
    elif lista_2[f3] == "ü":
        lista_3.append(crtd83)
    elif lista_2[f3] == "1":
        lista_3.append(crtd84)
    elif lista_2[f3] == "╣":
        lista_3.append(crtd85)
    elif lista_2[f3] == "§":
        lista_3.append(crtd86)
    elif lista_2[f3] == "Ö":
        lista_3.append(crtd87)
    elif lista_2[f3] == "ê":
        lista_3.append(crtd88)
    elif lista_2[f3] == "╔":
        lista_3.append(crtd89)
    elif lista_2[f3] == "y":
        lista_3.append(crtd90)
    elif lista_2[f3] == "9":
        lista_3.append(crtd91)
    elif lista_2[f3] == "↕":
        lista_3.append(crtd92)
    elif lista_2[f3] == "Ï":
        lista_3.append(crtd93)
    elif lista_2[f3] == "é":
        lista_3.append(crtd94)
    elif lista_2[f3] == "4":
        lista_3.append(crtd95)
    elif lista_2[f3] == "☻":
        lista_3.append(crtd96)
    elif lista_2[f3] == "Þ":
        lista_3.append(crtd97)
    elif lista_2[f3] == "§":
        lista_3.append(crtd98)
    elif lista_2[f3] == "'":
        lista_3.append(crtd99)
    elif lista_2[f3] == ">":
        lista_3.append(crtd100)
    elif lista_2[f3] == "▄":
        lista_3.append(crtd101)
    elif lista_2[f3] == "►":
        lista_3.append(crtd102)
    elif lista_2[f3] == "ö":
        lista_3.append(crtd103)
    elif lista_2[f3] == "~":
        lista_3.append(crtd104)
    elif lista_2[f3] == ",":
        lista_3.append(crtd105)
    elif lista_2[f3] == "k":
        lista_3.append(crtd106)
    elif lista_2[f3] == "Ô":
        lista_3.append(crtd107)
    elif lista_2[f3] == "^":
        lista_3.append(crtd108)
    elif lista_2[f3] == "À":
        lista_3.append(crtd109)
    elif lista_2[f3] == "/":
        lista_3.append(crtd110)
    elif lista_2[f3] == "?":
        lista_3.append(crtd111)
    elif lista_2[f3] == "T":
        lista_3.append(crtd112)
    elif lista_2[f3] == "7":
        lista_3.append(crtd113)
    elif lista_2[f3] == "ƒ":
        lista_3.append(crtd114)
    elif lista_2[f3] == "q":
        lista_3.append(crtd115)
    elif lista_2[f3] == "j":
        lista_3.append(crtd116)
    elif lista_2[f3] == "♀":
        lista_3.append(crtd117)
    elif lista_2[f3] == "í":
        lista_3.append(crtd118)
    elif lista_2[f3] == "6":
        lista_3.append(crtd119)
    elif lista_2[f3] == "+":
        lista_3.append(crtd120)
    elif lista_2[f3] == "¯":
        lista_3.append(crtd121)
    elif lista_2[f3] == "½":
        lista_3.append(crtd122)
    elif lista_2[f3] == "-":
        lista_3.append(crtd123)
    elif lista_2[f3] == "Ç":
        lista_3.append(crtd124)
    elif lista_2[f3] == "Î":
        lista_3.append(crtd125)
    elif lista_2[f3] == "{":
        lista_3.append(crtd126)
    elif lista_2[f3] == ".":
        lista_3.append(crtd127)
    elif lista_2[f3] == "○":
        lista_3.append(crtd128)
    elif lista_2[f3] == "M":
        lista_3.append(crtd129)
    elif lista_2[f3] == "W":
        lista_3.append(crtd130)
    elif lista_2[f3] == "[":
        lista_3.append(crtd131)
    elif lista_2[f3] == "]":
        lista_3.append(crtd132)
    elif lista_2[f3] == "ò":
        lista_3.append(crtd133)
    elif lista_2[f3] == "◙":
        lista_3.append(crtd134)
    elif lista_2[f3] == "$":
        lista_3.append(crtd135)
    elif lista_2[f3] == "¨":
        lista_3.append(crtd136)
    elif lista_2[f3] == "Â":
        lista_3.append(crtd137)
    elif lista_2[f3] == "ì":
        lista_3.append(crtd138)
    elif lista_2[f3] == "F":
        lista_3.append(crtd139)
    elif lista_2[f3] == "╠":
        lista_3.append(crtd140)
    elif lista_2[f3] == "Ä":
        lista_3.append(crtd141)
    elif lista_2[f3] == "ß":
        lista_3.append(crtd142)
    elif lista_2[f3] == "Ë":
        lista_3.append(crtd143)
    elif lista_2[f3] == "»":
        lista_3.append(crtd144)
    elif lista_2[f3] == "‗":
        lista_3.append(crtd145)
    elif lista_2[f3] == "Ð":
        lista_3.append(crtd146)
    elif lista_2[f3] == "╬":
        lista_3.append(crtd147)
    elif lista_2[f3] == "Ù":
        lista_3.append(crtd148)
    elif lista_2[f3] == "|":
        lista_3.append(crtd149)
    elif lista_2[f3] == "Ã":
        lista_3.append(crtd150)
    elif lista_2[f3] == "ª":
        lista_3.append(crtd151)
    elif lista_2[f3] == "Í":
        lista_3.append(crtd152)
    elif lista_2[f3] == "┌":
        lista_3.append(crtd153)
    elif lista_2[f3] == "Ü":
        lista_3.append(crtd154)
    elif lista_2[f3] == "O":
        lista_3.append(crtd155)
    elif lista_2[f3] == "a":
        lista_3.append(crtd156)
    elif lista_2[f3] == "0":
        lista_3.append(crtd157)
    elif lista_2[f3] == ")":
        lista_3.append(crtd158)
    elif lista_2[f3] == "&":
        lista_3.append(crtd159)
    elif lista_2[f3] == "ã":
        lista_3.append(crtd160)
    elif lista_2[f3] == "↨":
        lista_3.append(crtd161)
    elif lista_2[f3] == "=":
        lista_3.append(crtd162)
    elif lista_2[f3] == "Ø":
        lista_3.append(crtd163)
    elif lista_2[f3] == "3":
        lista_3.append(crtd164)
    elif lista_2[f3] == "r":
        lista_3.append(crtd165)
    elif lista_2[f3] == "¶":
        lista_3.append(crtd166)
    elif lista_2[f3] == "╝":
        lista_3.append(crtd167)
    elif lista_2[f3] == "ù":
        lista_3.append(crtd168)
    elif lista_2[f3] == "╦":
        lista_3.append(crtd169)
    elif lista_2[f3] == "þ":
        lista_3.append(crtd170)
    elif lista_2[f3] == "U":
        lista_3.append(crtd171)
    elif lista_2[f3] == "o":
        lista_3.append(crtd172)
    elif lista_2[f3] == "®":
        lista_3.append(crtd173)
    elif lista_2[f3] == "◘":
        lista_3.append(crtd174)
    elif lista_2[f3] == "N":
        lista_3.append(crtd175)
    elif lista_2[f3] == "§":
        lista_3.append(crtd176)
    elif lista_2[f3] == "¶":
        lista_3.append(crtd177)
    elif lista_2[f3] == "║":
        lista_3.append(crtd178)
    elif lista_2[f3] == "ð":
        lista_3.append(crtd179)
    elif lista_2[f3] == "É":
        lista_3.append(crtd180)
    elif lista_2[f3] == "f":
        lista_3.append(crtd181)
    elif lista_2[f3] == "8":
        lista_3.append(crtd182)
    elif lista_2[f3] == "È":
        lista_3.append(crtd183)
    elif lista_2[f3] == "I":
        lista_3.append(crtd184)
    elif lista_2[f3] == "└":
        lista_3.append(crtd185)
    elif lista_2[f3] == "e":
        lista_3.append(crtd186)
    elif lista_2[f3] == "ñ":
        lista_3.append(crtd187)
    elif lista_2[f3] == "╗":
        lista_3.append(crtd188)
    elif lista_2[f3] == "@":
        lista_3.append(crtd189)
    elif lista_2[f3] == "ı":
        lista_3.append(crtd190)
    elif lista_2[f3] == "ó":
        lista_3.append(crtd191)
    elif lista_2[f3] == "♠":
        lista_3.append(crtd192)
    elif lista_2[f3] == "▒":
        lista_3.append(crtd193)
    elif lista_2[f3] == "ä":
        lista_3.append(crtd194)
    elif lista_2[f3] == "u":
        lista_3.append(crtd195)
    elif lista_2[f3] == "°":
        lista_3.append(crtd196)
    elif lista_2[f3] == '"':
        lista_3.append(crtd197)
    elif lista_2[f3] == "↔":
        lista_3.append(crtd198)
    elif lista_2[f3] == "³":
        lista_3.append(crtd199)
    elif lista_2[f3] == "û":
        lista_3.append(crtd200)
    elif lista_2[f3] == "▓":
        lista_3.append(crtd201)
    elif lista_2[f3] == "x":
        lista_3.append(crtd202)
    elif lista_2[f3] == "î":
        lista_3.append(crtd203)
    elif lista_2[f3] == "¦":
        lista_3.append(crtd204)
    elif lista_2[f3] == "s":
        lista_3.append(crtd205)
    elif lista_2[f3] == "ý":
        lista_3.append(crtd206)
    elif lista_2[f3] == "E":
        lista_3.append(crtd207)
    elif lista_2[f3] == "Æ":
        lista_3.append(crtd208)
    elif lista_2[f3] == "Y":
        lista_3.append(crtd209)
    elif lista_2[f3] == "▬":
        lista_3.append(crtd210)
    elif lista_2[f3] == "!":
        lista_3.append(crtd211)
    elif lista_2[f3] == "P":
        lista_3.append(crtd212)
    elif lista_2[f3] == "♣":
        lista_3.append(crtd213)
    elif lista_2[f3] == "w":
        lista_3.append(crtd214)
    elif lista_2[f3] == "%":
        lista_3.append(crtd215)
    elif lista_2[f3] == "∟":
        lista_3.append(crtd216)
    elif lista_2[f3] == "‼":
        lista_3.append(crtd217)
    elif lista_2[f3] == "A":
        lista_3.append(crtd218)
    elif lista_2[f3] == "Û":
        lista_3.append(crtd219)
    elif lista_2[f3] == "¬":
        lista_3.append(crtd220)
    elif lista_2[f3] == "L":
        lista_3.append(crtd221)
    elif lista_2[f3] == "æ":
        lista_3.append(crtd222)
    elif lista_2[f3] == "(":
        lista_3.append(crtd223)
    elif lista_2[f3] == "▲":
        lista_3.append(crtd224)
    elif lista_2[f3] == "c":
        lista_3.append(crtd225)
    elif lista_2[f3] == "õ":
        lista_3.append(crtd226)
    elif lista_2[f3] == "÷":
        lista_3.append(crtd227)
    elif lista_2[f3] == "ø":
        lista_3.append(crtd228)
    elif lista_2[f3] == "C":
        lista_3.append(crtd229)
    elif lista_2[f3] == "◄":
        lista_3.append(crtd230)
    elif lista_2[f3] == "n":
        lista_3.append(crtd231)
    elif lista_2[f3] == "º":
        lista_3.append(crtd232)
    elif lista_2[f3] == "┐":
        lista_3.append(crtd233)
    elif lista_2[f3] == "«":
        lista_3.append(crtd234)
    elif lista_2[f3] == "■":
        lista_3.append(crtd235)
    elif lista_2[f3] == "│":
        lista_3.append(crtd236)
    elif lista_2[f3] == "}":
        lista_3.append(crtd237)
    elif lista_2[f3] == "B":
        lista_3.append(crtd238)
    elif lista_2[f3] == "£":
        lista_3.append(crtd239)
    elif lista_2[f3] == "±":
        lista_3.append(crtd240)
    elif lista_2[f3] == "*":
        lista_3.append(crtd241)
    elif lista_2[f3] == "b":
        lista_3.append(crtd242)
    elif lista_2[f3] == "X":
        lista_3.append(crtd243)
    elif lista_2[f3] == "┴":
        lista_3.append(crtd244)
    elif lista_2[f3] == "à":
        lista_3.append(crtd245)
    elif lista_2[f3] == ";":
        lista_3.append(crtd246)
    elif lista_2[f3] == "µ":
        lista_3.append(crtd247)
    elif lista_2[f3] == "¡":
        lista_3.append(crtd248)
    elif lista_2[f3] == "Õ":
        lista_3.append(crtd249)
    elif lista_2[f3] == ":":
        lista_3.append(crtd250)
    elif lista_2[f3] == "á":
        lista_3.append(crtd251)
    elif lista_2[f3] == " ":
        lista_3.append(crtd252)


# Resultado
resultado = "".join(str(x) for x in lista_3)
print(resultado)

voz.say("Fin del programa, adios usuario.")
voz.runAndWait()