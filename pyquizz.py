from random import choice
from string import maketrans
accents="��������"
ascii="eeceaouu"
conversion = maketrans(accents, ascii)
questions = ['Allemagne:Berlin', 'Autriche:Vienne', 'Belgique:Bruxelles', 'Bulgarie:Sofia', 'Chypre:Nicosie', 'Danemark:Copenhague', ...]
adieux = ['fin', 'stop', 'bye', 'ciao']
reponse = 'X'
print 'Donnez la capitale du pays'
print 'R�pondre "fin", "bye" ou "ciao" pour arr�ter'
while reponse not in adieux :
quest = choice(questions)
reponse = raw_input(quest.split(':')[0] + '?').lower()
if reponse not in adieux:
if reponse.translate(conversion) == quest.split(':')[1].lower():
print ':)''
else:
print "Faux, c'est", quest.split(':')[1]
print 'Bye !'

