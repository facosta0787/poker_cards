VALUE_CARDS = {0:'A',1:'2',2:'3',3:'4',4:'5',5:'6',6:'7',7:'8',8:'9',9:'10',10:'J',11:'Q',12:'K'}
cards = []
suits = ['♠','♥','♦','♣']
for key,value in VALUE_CARDS.items():
  cards.append(value)
  
def create_card(card,suit):
  top = ' _______'
  row = '|       |'
  middle = '|       |'
  bottom = '|_______|'
  card_str = '{0}\n{1}\n{1}\n{1}\n{1}\n{2}'.format(top,row,bottom)
  return card_str
  
card_created = create_card(cards[0],suits[0])
print (card_created)
