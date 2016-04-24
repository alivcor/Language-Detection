# Enter your code here. Read input from STDIN. Print output to STDOUT
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
import sys
import re
languages_ratios = {}
#text = raw_input()
text = str(sys.stdin.readlines())
#print(text)
tokens = wordpunct_tokenize(text)
textwords = [wd.lower() for wd in tokens]
sw_eng = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
sw_ger = ['aber', 'alle', 'allem', 'allen', 'aller', 'alles', 'als', 'also', 'am', 'an', 'ander', 'andere', 'anderem', 'anderen', 'anderer', 'anderes', 'anderm', 'andern', 'anderr', 'anders', 'auch', 'auf', 'aus', 'bei', 'bin', 'bis', 'bist', 'da', 'damit', 'dann', 'der', 'den', 'des', 'dem', 'die', 'das', 'da\xdf', 'derselbe', 'derselben', 'denselben', 'desselben', 'demselben', 'dieselbe', 'dieselben', 'dasselbe', 'dazu', 'dein', 'deine', 'deinem', 'deinen', 'deiner', 'deines', 'denn', 'derer', 'dessen', 'dich', 'dir', 'du', 'dies', 'diese', 'diesem', 'diesen', 'dieser', 'dieses', 'doch', 'dort', 'durch', 'ein', 'eine', 'einem', 'einen', 'einer', 'eines', 'einig', 'einige', 'einigem', 'einigen', 'einiger', 'einiges', 'einmal', 'er', 'ihn', 'ihm', 'es', 'etwas', 'euer', 'eure', 'eurem', 'euren', 'eurer', 'eures', 'f\xfcr', 'gegen', 'gewesen', 'hab', 'habe', 'haben', 'hat', 'hatte', 'hatten', 'hier', 'hin', 'hinter', 'ich', 'mich', 'mir', 'ihr', 'ihre', 'ihrem', 'ihren', 'ihrer', 'ihres', 'euch', 'im', 'in', 'indem', 'ins', 'ist', 'jede', 'jedem', 'jeden', 'jeder', 'jedes', 'jene', 'jenem', 'jenen', 'jener', 'jenes', 'jetzt', 'kann', 'kein', 'keine', 'keinem', 'keinen', 'keiner', 'keines', 'k\xf6nnen', 'k\xf6nnte', 'machen', 'man', 'manche', 'manchem', 'manchen', 'mancher', 'manches', 'mein', 'meine', 'meinem', 'meinen', 'meiner', 'meines', 'mit', 'muss', 'musste', 'nach', 'nicht', 'nichts', 'noch', 'nun', 'nur', 'ob', 'oder', 'ohne', 'sehr', 'sein', 'seine', 'seinem', 'seinen', 'seiner', 'seines', 'selbst', 'sich', 'sie', 'ihnen', 'sind', 'so', 'solche', 'solchem', 'solchen', 'solcher', 'solches', 'soll', 'sollte', 'sondern', 'sonst', '\xfcber', 'um', 'und', 'uns', 'unse', 'unsem', 'unsen', 'unser', 'unses', 'unter', 'viel', 'vom', 'von', 'vor', 'w\xe4hrend', 'war', 'waren', 'warst', 'was', 'weg', 'weil', 'weiter', 'welche', 'welchem', 'welchen', 'welcher', 'welches', 'wenn', 'werde', 'werden', 'wie', 'wieder', 'will', 'wir', 'wird', 'wirst', 'wo', 'wollen', 'wollte', 'w\xfcrde', 'w\xfcrden', 'zu', 'zum', 'zur', 'zwar', 'zwischen']
sw_fre = ['au', 'aux', 'avec', 'ce', 'ces', 'dans', 'de', 'des', 'du', 'elle', 'en', 'et', 'eux', 'il', 'je', 'la', 'le', 'leur', 'lui', 'ma', 'mais', 'me', 'm\xeame', 'mes', 'moi', 'mon', 'ne', 'nos', 'notre', 'nous', 'on', 'ou', 'par', 'pas', 'pour', 'qu', 'que', 'qui', 'sa', 'se', 'ses', 'son', 'sur', 'ta', 'te', 'tes', 'toi', 'ton', 'tu', 'un', 'une', 'vos', 'votre', 'vous', 'c', 'd', 'j', 'l', '\xe0', 'm', 'n', 's', 't', 'y', '\xe9t\xe9', '\xe9t\xe9e', '\xe9t\xe9es', '\xe9t\xe9s', '\xe9tant', '\xe9tante', '\xe9tants', '\xe9tantes', 'suis', 'es', 'est', 'sommes', '\xeates', 'sont', 'serai', 'seras', 'sera', 'serons', 'serez', 'seront', 'serais', 'serait', 'serions', 'seriez', 'seraient', '\xe9tais', '\xe9tait', '\xe9tions', '\xe9tiez', '\xe9taient', 'fus', 'fut', 'f\xfbmes', 'f\xfbtes', 'furent', 'sois', 'soit', 'soyons', 'soyez', 'soient', 'fusse', 'fusses', 'f\xfbt', 'fussions', 'fussiez', 'fussent', 'ayant', 'ayante', 'ayantes', 'ayants', 'eu', 'eue', 'eues', 'eus', 'ai', 'as', 'avons', 'avez', 'ont', 'aurai', 'auras', 'aura', 'aurons', 'aurez', 'auront', 'aurais', 'aurait', 'aurions', 'auriez', 'auraient', 'avais', 'avait', 'avions', 'aviez', 'avaient', 'eut', 'e\xfbmes', 'e\xfbtes', 'eurent', 'aie', 'aies', 'ait', 'ayons', 'ayez', 'aient', 'eusse', 'eusses', 'e\xfbt', 'eussions', 'eussiez', 'eussent'] 
sw_spa=['de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 'para', 'con', 'no', 'una', 'su', 'al', 'lo', 'como', 'm\xe1s', 'pero', 'sus', 'le', 'ya', 'o', 'este', 's\xed', 'porque', 'esta', 'entre', 'cuando', 'muy', 'sin', 'sobre', 'tambi\xe9n', 'me', 'hasta', 'hay', 'donde', 'quien', 'desde', 'todo', 'nos', 'durante', 'todos', 'uno', 'les', 'ni', 'contra', 'otros', 'ese', 'eso', 'ante', 'ellos', 'e', 'esto', 'm\xed', 'antes', 'algunos', 'qu\xe9', 'unos', 'yo', 'otro', 'otras', 'otra', '\xe9l', 'tanto', 'esa', 'estos', 'mucho', 'quienes', 'nada', 'muchos', 'cual', 'poco', 'ella', 'estar', 'estas', 'algunas', 'algo', 'nosotros', 'mi', 'mis', 't\xfa', 'te', 'ti', 'tu', 'tus', 'ellas', 'nosotras', 'vosostros', 'vosostras', 'os', 'm\xedo', 'm\xeda', 'm\xedos', 'm\xedas', 'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 'suya', 'suyos', 'suyas', 'nuestro', 'nuestra', 'nuestros', 'nuestras', 'vuestro', 'vuestra', 'vuestros', 'vuestras', 'esos', 'esas', 'estoy', 'est\xe1s', 'est\xe1', 'estamos', 'est\xe1is', 'est\xe1n', 'est\xe9', 'est\xe9s', 'estemos', 'est\xe9is', 'est\xe9n', 'estar\xe9', 'estar\xe1s', 'estar\xe1', 'estaremos', 'estar\xe9is', 'estar\xe1n', 'estar\xeda', 'estar\xedas', 'estar\xedamos', 'estar\xedais', 'estar\xedan', 'estaba', 'estabas', 'est\xe1bamos', 'estabais', 'estaban', 'estuve', 'estuviste', 'estuvo', 'estuvimos', 'estuvisteis', 'estuvieron', 'estuviera', 'estuvieras', 'estuvi\xe9ramos', 'estuvierais', 'estuvieran', 'estuviese', 'estuvieses', 'estuvi\xe9semos', 'estuvieseis', 'estuviesen', 'estando', 'estado', 'estada', 'estados', 'estadas', 'estad', 'he', 'has', 'ha', 'hemos', 'hab\xe9is', 'han', 'haya', 'hayas', 'hayamos', 'hay\xe1is', 'hayan', 'habr\xe9', 'habr\xe1s', 'habr\xe1', 'habremos', 'habr\xe9is', 'habr\xe1n', 'habr\xeda', 'habr\xedas', 'habr\xedamos', 'habr\xedais', 'habr\xedan', 'hab\xeda', 'hab\xedas', 'hab\xedamos', 'hab\xedais', 'hab\xedan', 'hube', 'hubiste', 'hubo', 'hubimos', 'hubisteis', 'hubieron', 'hubiera', 'hubieras', 'hubi\xe9ramos', 'hubierais', 'hubieran', 'hubiese', 'hubieses', 'hubi\xe9semos', 'hubieseis', 'hubiesen', 'habiendo', 'habido', 'habida', 'habidos', 'habidas', 'soy', 'eres', 'es', 'somos', 'sois', 'son', 'sea', 'seas', 'seamos', 'se\xe1is', 'sean', 'ser\xe9', 'ser\xe1s', 'ser\xe1', 'seremos', 'ser\xe9is', 'ser\xe1n', 'ser\xeda', 'ser\xedas', 'ser\xedamos', 'ser\xedais', 'ser\xedan', 'era', 'eras', '\xe9ramos', 'erais', 'eran', 'fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron', 'fuera', 'fueras', 'fu\xe9ramos', 'fuerais', 'fueran', 'fuese', 'fueses', 'fu\xe9semos', 'fueseis', 'fuesen', 'sintiendo', 'sentido', 'sentida', 'sentidos', 'sentidas', 'siente', 'sentid', 'tengo', 'tienes', 'tiene', 'tenemos', 'ten\xe9is', 'tienen', 'tenga', 'tengas', 'tengamos', 'teng\xe1is', 'tengan', 'tendr\xe9', 'tendr\xe1s', 'tendr\xe1', 'tendremos', 'tendr\xe9is', 'tendr\xe1n', 'tendr\xeda', 'tendr\xedas', 'tendr\xedamos', 'tendr\xedais', 'tendr\xedan', 'ten\xeda', 'ten\xedas', 'ten\xedamos', 'ten\xedais', 'ten\xedan', 'tuve', 'tuviste', 'tuvo', 'tuvimos', 'tuvisteis', 'tuvieron', 'tuviera', 'tuvieras', 'tuvi\xe9ramos', 'tuvierais', 'tuvieran', 'tuviese', 'tuvieses', 'tuvi\xe9semos', 'tuvieseis', 'tuviesen', 'teniendo', 'tenido', 'tenida', 'tenidos', 'tenidas', 'tened'] 

#English
sw_set = set(sw_eng)
ws_set = set(textwords)
#print(sw_set)
#print(ws_set)
comel = ws_set.intersection(sw_set)
languages_ratios["english"] = len(comel)

#German
sw_set = set(sw_ger)
ws_set = set(textwords)
#print(sw_set)
#print(ws_set)
comel = ws_set.intersection(sw_set)
languages_ratios["german"] = len(comel)

#French
sw_set = set(sw_fre)
ws_set = set(textwords)
#print(sw_set)
#print(ws_set)
comel = ws_set.intersection(sw_set)
languages_ratios["french"] = len(comel)

#Spanish
sw_set = set(sw_spa)
ws_set = set(textwords)
#print(sw_set)
#print(ws_set)
comel = ws_set.intersection(sw_set)
languages_ratios["spanish"] = len(comel)

#print(languages_ratios["german"])

#print(languages_ratios["english"])

resLang = max(languages_ratios, key=languages_ratios.get)
matchObj = re.match(r'(\w)(\w+)', str(resLang), re.M|re.I)
fltr = str(matchObj.group(1)).title()
rltr = str(matchObj.group(2))
print(fltr+rltr) 
