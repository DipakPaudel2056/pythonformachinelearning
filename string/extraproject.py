alphabets = 'abcdefghijklmnopqrstuvwxyz'
# in this chapter i have created a single function to caeser cypher given strings 
# i have also found the offset using brute force

def caesar_decode_encode(message,offset,type):
  decoded_message = []
  for char in message:  
    if char in alphabets: 
      index = alphabets.find(char)
      if type == True:
        decoded_index = index - offset
      elif type == False:
        decoded_index = index+offset
        if decoded_index >= len(alphabets) :
          decoded_index = decoded_index - len(alphabets) 
      decoded_char = alphabets[decoded_index]
      decoded_message.append(decoded_char)
    else:
      decoded_message.append(char)
  decoded_message = ''.join(decoded_message)
  return  decoded_message



for i in range(20):
  print(i,caesar_decode_encode('vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. pxee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.',i,False))
