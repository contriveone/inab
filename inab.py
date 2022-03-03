arb_utf8_bslash = ["\xd8","\xa3","\xd9","\x88","\x87","\xa8","\xaf","\x8a","\x84","\x85","\x86","\x82","\xa7","\xaa","\xd8 ","\xa3 ","\xd9 ","\x88 ","\x87 ","\xa8 ","\xaf ","\x8a ","\x84 ","\x85 ","\x86 ","\x82 ","\xa7 ","\xaa ",'\x80', '\x81', '\x83', '\x89', '\x8c', '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95', '\x96', '\x97', '\x98', '\x99', '\x9a', '\x9b', '\x9c', '\x9e', '\x9f', '\xa0', '\xa1', '\xa2', '\xa4', '\xa5', '\xa6', '\xa9', '\xab', '\xac', '\xad', '\xae', '\xb0', '\xb1', '\xb2', '\xb3', '\xb4', '\xb5', '\xb6', '\xb7', '\xb8', '\xb9', '\xba', '\xbb', '\xbc', '\xbd', '\xbe', '\xbf', '\x8b', '\x9d', '\xda', '\xdb'  ,'\x80 ', '\x81 ', '\x83 ', '\x89 ', '\x8c ', '\x8d ', '\x8e ', '\x8f ', '\x90 ', '\x91 ', '\x92 ', '\x93 ', '\x94 ', '\x95 ', '\x96 ', '\x97 ', '\x98 ', '\x99 ', '\x9a ', '\x9b ', '\x9c ', '\x9e ', '\x9f ', '\xa0 ', '\xa1 ', '\xa2 ', '\xa4 ', '\xa5 ', '\xa6 ', '\xa9 ', '\xab ', '\xac ', '\xad ', '\xae ', '\xb0 ', '\xb1 ', '\xb2 ', '\xb3 ', '\xb4 ', '\xb5 ', '\xb6 ', '\xb7 ', '\xb8 ', '\xb9 ', '\xba ', '\xbb ', '\xbc ', '\xbd ', '\xbe ', '\xbf ', '\x8b ', '\x9d ', '\xda ', '\xdb ',"\xba -","\xba - "]


arb_utf8 = ["xd8","xa3","xd9","x88","x87","xa8","xaf","x8a","x84","x85","x86","x82","xa7","xaa","xd8 ","xa3 ","xd9 ","x88 ","x87 ","xa8 ","xaf ","x8a ","x84 ","x85 ","x86 ","x82 ","xa7 ","xaa ",'x80', 'x81', 'x83', 'x89', 'x8c', 'x8d', 'x8e', 'x8f', 'x90', 'x91', 'x92', 'x93', 'x94', 'x95', 'x96', 'x97', 'x98', 'x99', 'x9a', 'x9b', 'x9c', 'x9e', 'x9f', 'xa0', 'xa1', 'xa2', 'xa4', 'xa5', 'xa6', 'xa9', 'xab', 'xac', 'xad', 'xae', 'xb0', 'xb1', 'xb2', 'xb3', 'xb4', 'xb5', 'xb6', 'xb7', 'xb8', 'xb9', 'xba', 'xbb', 'xbc', 'xbd', 'xbe', 'xbf', 'x8b', 'x9d', 'xda', 'xdb'  ,'x80 ', 'x81 ', 'x83 ', 'x89 ', 'x8c ', 'x8d ', 'x8e ', 'x8f ', 'x90 ', 'x91 ', 'x92 ', 'x93 ', 'x94 ', 'x95 ', 'x96 ', 'x97 ', 'x98 ', 'x99 ', 'x9a ', 'x9b ', 'x9c ', 'x9e ', 'x9f ', 'xa0 ', 'xa1 ', 'xa2 ', 'xa4 ', 'xa5 ', 'xa6 ', 'xa9 ', 'xab ', 'xac ', 'xad ', 'xae ', 'xb0 ', 'xb1 ', 'xb2 ', 'xb3 ', 'xb4 ', 'xb5 ', 'xb6 ', 'xb7 ', 'xb8 ', 'xb9 ', 'xba ', 'xbb ', 'xbc ', 'xbd ', 'xbe ', 'xbf ', 'x8b ', 'x9d ', 'xda ', 'xdb ',"xba -","xba - "]

def arabic_de (o):
	lis = o.split(b"\\")
	text = ""
	for i in lis:
		index = i.decode()
		try :
			place = arb_utf8.index(index)
			text = text+str(arb_utf8_bslash[place])
		except:
			pass
	return (text.encode("latin-1").decode())
	





def eng_de (o):
	s = ""
	v = str(o).split("x00")
	for i in v:
		if "fe" in i:
			p = (i[len(i)-2])
			s = s+p
		else:
			try :
				s = s + (i[0])
			except:
				pass
	return s
	
















