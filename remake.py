
txt = input("INTRODU TEXT LIL-ZX-ARCMB-MIHO PENTRU DECODARE:")

my_list = txt.replace(" ", "")


sample_string = ''.join(my_list[i:i + 1] for i in range(0, len(my_list), 1))

char_to_replace = {

't': '8)+T',

'Z': 'R+',
'2': 'RG',
'3': 'C=',
'4': 'NH+',
'5': 'GG',

'z': 'r+',
'6': 'rg',
'^': 'c=',
'%': 'nh+',
'$': 'gg',

'R': '1)',

    '&': '808',

'S': 'F=',

    'T': '_+',

'U': 'DM',
'V': '1=',
'W': '=1',
'X': '+1',
'Y': 'FN',

'r': '7)',
's': 'f=',
'u': 'dm',
'v': '7=',
'w': '=7',
'x': '+7',
'y': 'fn',

'A': '00010008088',
'B': '000100018088',

    '+': '08088',
    '=': '8088',
    '-': '88888',
    '_': '888',
    '{': '88',
    '}': '0000000',
    '[': '000000',
    ']': '00000',
    '*': '0000',

'C': '11111',
'D': '1111',
'E': '00010001',
'F': '0001',
'G': '1100',
'H': '00111',
'I': '001',
'J': '111',
'K': '11',

    '(': '000',
    ')': '00',

'L': '010101',
'M': '0101',
'N': '01',
'O': '101010',
'P': '1010',
'Q': '10',

'a': '99979998988',
'b': '999799978988',

    '~': '9999999',
    '?': '999999',
    '>': '99999',
    '<': '9999',

'c': '77777',
'd': '7777',
'e': '99979997',
'f': '9997',
'g': '7799',
'h': '99777',
'i': '997',
'j': '777',
'k': '77',

    ':': '999',
    ';': '99',

'l': '979797',
'm': '9797',
'n': '97',
'o': '797979',
'p': '7979',
'q': '79'


}


for key, value in char_to_replace.items():
    sample_string = sample_string.replace(key, value)

my_list = sample_string.split("8088")

my_list = list(map(lambda item: item.replace("111101010001","a"), my_list))
my_list = list(map(lambda item: item.replace("110010011100","b"), my_list))
my_list = list(map(lambda item: item.replace("000110011001","c"), my_list))
my_list = list(map(lambda item: item.replace("111010010001","g"), my_list))
my_list = list(map(lambda item: item.replace("000100000001","m"), my_list))
my_list = list(map(lambda item: item.replace("011001011000","q"), my_list))
my_list = list(map(lambda item: item.replace("000101011111","r"), my_list))
my_list = list(map(lambda item: item.replace("001110011001","s"), my_list))
my_list = list(map(lambda item: item.replace("000100011000","t"), my_list))
my_list = list(map(lambda item: item.replace("011110000001","v"), my_list))
my_list = list(map(lambda item: item.replace("100001001000","x"), my_list))
my_list = list(map(lambda item: item.replace("001100001011","y"), my_list))

my_list = list(map(lambda item: item.replace("00010001","e"), my_list))
my_list = list(map(lambda item: item.replace("10001000","o"), my_list))
my_list = list(map(lambda item: item.replace("10001100","u"), my_list))
my_list = list(map(lambda item: item.replace("11111001","d"), my_list))
my_list = list(map(lambda item: item.replace("11001000","z"), my_list))
my_list = list(map(lambda item: item.replace("11110001","p"), my_list))
my_list = list(map(lambda item: item.replace("01001110","n"), my_list))
my_list = list(map(lambda item: item.replace("10011000","l"), my_list))
my_list = list(map(lambda item: item.replace("00101000","k"), my_list))
my_list = list(map(lambda item: item.replace("01001111","h"), my_list))

my_list = list(map(lambda item: item.replace("1100","f"), my_list))
my_list = list(map(lambda item: item.replace("1000","i"), my_list))
my_list = list(map(lambda item: item.replace("1001","j"), my_list))
my_list = list(map(lambda item: item.replace("0111","w"), my_list))

my_list = list(map(lambda item: item.replace("777797979997","A"), my_list))
my_list = list(map(lambda item: item.replace("779979977799","B"), my_list))
my_list = list(map(lambda item: item.replace("999779977997","C"), my_list))
my_list = list(map(lambda item: item.replace("777979979997","G"), my_list))
my_list = list(map(lambda item: item.replace("999799999997","M"), my_list))
my_list = list(map(lambda item: item.replace("977997977999","Q"), my_list))
my_list = list(map(lambda item: item.replace("999797977777","R"), my_list))
my_list = list(map(lambda item: item.replace("997779977997","S"), my_list))
my_list = list(map(lambda item: item.replace("999799977999","T"), my_list))
my_list = list(map(lambda item: item.replace("977779999997","V"), my_list))
my_list = list(map(lambda item: item.replace("799997997999","X"), my_list))
my_list = list(map(lambda item: item.replace("997799997977","Y"), my_list))

my_list = list(map(lambda item: item.replace("99979997","E"), my_list))
my_list = list(map(lambda item: item.replace("79997999","O"), my_list))
my_list = list(map(lambda item: item.replace("79997799","U"), my_list))
my_list = list(map(lambda item: item.replace("77777997","D"), my_list))
my_list = list(map(lambda item: item.replace("77997999","Z"), my_list))
my_list = list(map(lambda item: item.replace("77779997","P"), my_list))
my_list = list(map(lambda item: item.replace("97997779","N"), my_list))
my_list = list(map(lambda item: item.replace("79977999","L"), my_list))
my_list = list(map(lambda item: item.replace("99797999","K"), my_list))
my_list = list(map(lambda item: item.replace("97997777","H"), my_list))

my_list = list(map(lambda item: item.replace("7799","F"), my_list))
my_list = list(map(lambda item: item.replace("7999","I"), my_list))
my_list = list(map(lambda item: item.replace("7997","J"), my_list))
my_list = list(map(lambda item: item.replace("9777","W"), my_list))

my_list = list(map(lambda item: item.replace("8880"," "), my_list))
my_list = list(map(lambda item: item.replace("00008000","."), my_list))
my_list = list(map(lambda item: item.replace("00008080",","), my_list))
my_list = list(map(lambda item: item.replace("8800","("), my_list))
my_list = list(map(lambda item: item.replace("0088",")"), my_list))
my_list = list(map(lambda item: item.replace("0880","-"), my_list))

final = ''.join(my_list)
print('\n', 'REZULTAT DECODARE LIL-ZX-ARCMB-MIHO:', final)
