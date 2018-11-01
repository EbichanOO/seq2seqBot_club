import MeCab as MCB
sin = "すもももももももものうち"
a = MCB.Tagger('-Owakati')
print(a.parse(sin))