#program to decode the morse code into english and vise versa

#Almost complete code version v 0.1    with classes                                                                                                                                                              
 
# Final code  

class morse:
  DC_E_to_M = {     'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                                        'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',
                    '  ' : ' '
 
              }
 
  DC_M_to_E = {          '.-':'A', '-...':'B',
                    '-.-.':'C', '-..':'D', '.':'E',
                    '..-.':'F', '--.':'G', '....':'H',
                    '..':'I', '.---':'J', '-.-':'K',
                    '.-..':'L', '--':'M', '-.':'N',
                    '---':'O', '.--.':'P', '--.-':'Q',
                    '.-.':'R', '...':'S', '-':'T',
                    '..-':'U', '...-':'V', '.--':'W',
                    '-..-':'X', '-.--':'Y', '--..':'Z',
                    '.----':'1', '..---':'2', '...--':'3',
                    '....-':'4', '.....':'5', '-....':'6',
                    '--...':'7', '---..':'8', '----.':'9',
                    '-----':'0', '--..--':', ', '.-.-.-':'.',
                    '..--..':'?', '-..-.':'/', '-....-':'-',
                    '-.--.':'(', '-.--.-':')',
                    ' ' : '  '
        }
 
 
  def E_to_M(self,text1):
      if (self.check(text1)):
        c=''
        for i in text1:
            if i != ' ':
                c += self.DC_E_to_M[i]
                c += ' '
            else:  
                c += ' ' 
        print("\nOriginal message:\n",text1,"\n")
        print("\nMessage after converting it to morse code :\n",c,"\n")
 
      
        print("\nWould you like to convert it to English again ?\t(y/n)\n")
        c1=input()
        if(c1=='y'):
          self.M_to_E(c)   
      else:
        print("\nThe resulting message cannot be converted into morse code,\nsince it involves other characters , which are beyond morse translation\nWe are very Sorry for that\n")  
 
  def M_to_E(self,text1):
      text1 +=  ' '
      Result = ''
      morseletter = ''
    
      for letter in text1:

          if letter != ' ':
            count = 0
            morseletter += letter
              
          else:
            count += 1
            if count == 2 or count > 2 :
              Result += ' ' 
            else :
              Result += self.DC_M_to_E[morseletter]
              morseletter = ''
              
           
      print("\nOriginal message in morse :\n",text1,"\n")
      print("\nMessage after converting it to English :\n",Result,"\n")
 
      print("\nWould you like to encrypt this message using key value ?\t(y/n)\n")
      c1=input()
      if(c1=='y'):
        print("\nPlease enter the key value\n")
        key=int(input())
        self.Encrypt(Result,key)
 
  def Encrypt(self,message,key):
      Result=''  
      for letter in message:
        letter= chr(ord(letter)+key) 
        Result += letter
      print("\nOriginal message:\n",message,"\n")
      print("\nKey value for encryption : ",key)
      print("\nMessage after encrypting :\n",Result,"\n")
 
      print("\nWould you like to decrypt it using the same/Different key ?\t(y/n)\n")
      c1=input()
      if(c1=='y'):
        print("\n1.Use same key for decryption\n2.Use different key for decryption\n")
        print("Please enter your choice\n")
        c3=int(input())
        if c3 ==1:
          self.Decrypt(Result,key)
        elif c3 ==2:
          key=int(input("\nPlease enter the key value for decryption\n"))
          self.Decrypt(Result,key)            
 
 
  def Decrypt(self,message,key):
      Result=''  
      for letter in message:
        letter= chr(ord(letter)-key)
        Result += letter
      print("\nOriginal message:\n",message,"\n")
      print("\nKey value for decryption : ",key)
      print("\nMessage after decrypting :\n",Result,"\n")   
      if(self.check(Result)):
        print("\nWould you like to convert it to morse code ?\t(y/n)\n")
        c1=input()
        if(c1=='y'):
          self.E_to_M(Result)
      
      else:
        print("\nThe resulting message cannot be converted into morse code,\nsince it involves other characters , which are beyond morse translation\nWe are very Sorry for that\n")  
 
  def Help(self):
      print("%"*70,"Help section","%"*70)
      print("\nWhat is morse?\n")
      print("\t\tMorse code is a method used in telecommunication to encode text characters using sequences of dots and dashes, or dits and dahs.\nMorse code is named after Samuel Morse, one of the inventors of the telegraph.\n")
      print("\t The structure of morse is as follows  :\n ")
      help_morsetext=(
         f"\t A : .- \t\t B: -... \t\t C: -.-. \n"
         f"\t D: -.. \t\t E: .\t\t\t F: ..-. \n"
         f"\t G: --. \t\t H: ....\t\t I: .. \n"
         f"\t J: .--- \t\t K: -.-\t\t\t L: .-.. \n"
         f"\t M: -- \t\t\t N: -.\t\t\t O: --- \n"
         f"\t P: .--. \t\t Q: --.-\t\t R: .-. \n"
         f"\t S: ... \t\t T: - \t\t\t U: ..- \n"
         f"\t V: ...- \t\t W: .--\t\t\t X: -..- \n"
         f"\t Y: -.-- \t\t Z: --.. \n"
         f"\t 1: .---- \t\t 2: ..--- \t\t 3: ...-- \n"
         f"\t 4: ....- \t\t 5: ..... \t\t 6: -.... \n"
         f"\t 7: --... \t\t 8: ---.. \t\t 9: ----. \n"
         f"\t 0: ----- \t\t , : --..-- \t\t . : .-.-.- \n"
         f"\t ?: ..--.. \t\t / : -..-. \t\t - :-....-\n"
         f"\t ( : -.--. \t\t ) : -.--.- \t\n\n"
    )
      print(help_morsetext)
      print("*"*150,"\n")
      print("\nWhat is encryption?\n")
      print(f"\t\tEncryption is a process of encoding the information which hides the true meaning of the original text.\n"
          f"There are lots of encryption methods, but here in this program  we are only using a simple encryption method, i.e., using \na key value."
          f"Here, an original text and key values are taken from the user, and according to the key value, \nthe ASCII values of each character in the text will be shifted .\n\n"
          f"For example: \n\nLet the text be \"ABCD\"\nand the key value given be 3. Then,\n"
          f"the ASCII values of the characteres will be shifted by the amount 3 (ASCII values will be added with the key value)\nAnd hence the encrypted text is obtained.\n"
          f"In this case \"ABCD\" will be changed to \"DEFG\" i.e, shifted by 3 ASCII values \n\n"
          )
      print("*"*150,"\n")
      print("\nWhat is decryption?\n")
      print(f"\t\tDecryption is a process of decoding the information which is hidden in the form of encrypted text  \n(i.e, To get the true meaning of the original text) ."
          f" It can be considered as the reverse procedure of encryption. \n"
          f"There are lots of decryption methods for specific encryptions depending on the level of difficulty . Here in this program, \nsince we are only using a simple encryption method by using a key value,"
          f" the decryption method is also similar but the \nexact reverse method as that of encryption i.e, using the key value . \n"
          f"Here, an encryted text and key values are taken from the user , and in the same way as encryption ,the ASCII values of \neach character in the text will be shifted according to the key value given, but in the opposite direction.\n\n"
          f"For example: \n\nLet us consider the same encrypted message as in the above \"Encryption section\".\nHere, the encrypted text is \"DEFG\"\nand let the key value given be 3. Then,\n"
          f"the ASCII values of the characteres will be shifted by the amount 3 in the opposite direction (ASCII values will be subtracted with the given key value)\nAnd hence the decrypted text (According to key value) will be found.\n"
          f"In this case \"DEFG\" will be changed to \"ABCD\" i.e, shifted by 3 ASCII values in the opposite direction\n\n"
          )

      print("%"*67,"End of help section","%"*67)
 
    
 
  def check(self,message):
    j=1
    for i in message:
      val = ord(i)
      if (val>=65 and val <=90) or (val>=97 and val <=122):   # Checking for alphabet
        continue
      elif (val>=48 and val<=57):                             # Checking for a no.
        continue
      elif (val==32 or val==40 or val==41 or val==63 ):        #Checking for special character, space, '(',')','?' 
        continue
      elif (val >=44 and val<=47):                            #Checking for special characters like ',','.','-','/',etc
        continue
      else:
        j=0
        return j
    return j
 
 
# Commencement of main program 
 
ms = morse()

print("-"*60,"Welcome to morse to English decoder","-"*60)
while True:
    print("\n1. English to morse\n2. Morse to English\n3. Help\n4. Encrypt message using key\n5. Decrypt message using key\n6. Exit from the program\n")
    print("Enter the choice: ")
    choice = int(input())
    if choice == 1:
        s = input("Please enter the message in English\n")
        ms.E_to_M(s)
        
    elif choice == 2:
        s = input("Please enter the message in Morse code\n")
        ms.M_to_E(s)  
 
    elif choice == 3:
        ms.Help()
    elif choice == 4:
        s = input("Please enter the message \n")
        key= int(input("Please enter the key value\n"))  
        ms.Encrypt(s,key)
 
    elif choice == 5:
        s = input("Please enter the encrypted message \n")
        key= int(input("Please enter the key value for decryption\n"))  
        ms.Decrypt(s,key)
 
    elif choice == 6:
        print("\n","$"*70," THANK YOU ","$"*70,"\n")
        break
    else:
      print("Please enter a valid choice\n")
      print("-"*150,"\n")


print( "Hi - " ,chr(32))
print( chr(40))
print( chr(41))
print( chr(63))
for i in range(44,48):
  print(i," - ", chr(i))



