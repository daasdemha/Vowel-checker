#refrences:
#https://www.youtube.com/watch?v=rfscVS0vtbw
#https://www.youtube.com/watch?v=OTON2x71DE0
print("Hello")
print("Welcome to the program")
def menu():
 #main
 choice = input("""
  A: Enter a word
  B: Check letter or vowel times
  C: Palindrome
  D: Anagram
  Q: Exit
  Please enter your choice: """)
   # part one
 if choice == "A" or choice =="a":
   sentence = 0
   while sentence <= 1:
     sentence = sentence + 1

   sentence = input("Please enter a word:")
   for letter in sentence:
      print(letter)
   menu()
     
   #part two
 elif choice == "B" or choice =="b":
   vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
   sentence1 = input("Please enter a word: ")
   count = 0
   for letter in sentence1:
     if letter in vowel:
         count += 1
   print("vowels in your word are present")
   print(count)
   print("times")
   word = input("Please enter a letter:")
   print("The entred letter is present in your entered word")
   print(sentence1.count(word))
   print("times")
   menu()
   
  
  #part 3
  # refrence https://www.youtube.com/watch?v=OTON2x71DE0  
 elif choice == "C" or choice =="c":
    str = input("Enter the word:")
    count = 0
    i = len(str)
    p = i - 1
    index = 0 
    while index < p:
      if str[index] == str[p]:
        index = index + i
        p - p - i
        print("The entered word is a palindrone")
        menu()
      else:
        
        print("The entered word is not a palindrone")
        count = 0
        menu()

  #part 4

 elif choice=="D" or choice=="d":
   input_str_1 =input("")
   input_str_2 = input("")

   def is_anagram(str_1, str_2):
     str_1 = str_1.replace(" ", "")
     str_2 = str_2.replace(" ", "")

     if len(str_1) != len(str_2):
         return False
       
        

     alphabet = "abcdefghijklmnopqrstuvwxyz"
     str_1 = str_1.lower()
     str_2 = str_2.lower()
     print("is")
     dict_1 = dict.fromkeys(list(alphabet), 0)
     dict_2 = dict.fromkeys(list(alphabet), 0)

     for i in range(len(str_1)):
         dict_1[str_1[i]] += 1
         dict_2[str_2[i]] += 1
     return dict_1 == dict_2
    

   print(is_anagram(input_str_1, input_str_2))
   print("anagram")
   menu()



 elif choice=="Q" or choice=="q":
   print("")
   print("Program terminated")
   print("Goodbye")
   exit()
 else:
  print("You must only select either A,B,C, or D.")
  print("Please try again")
  menu()
menu()
