#Program to check if a word is a palindrome

words =['Oxo','OXO','123454321','ROTATOR','12345 54321']

for i in words:
 # words2[i] = reversed(words[i])
  words2[i] = reversed(words[i])
  print "%s" % i
  
def is_palindrome(words):
  min = 0
  max = len(words) - 1
  
  while True:
    if min > max:
      return True
    
    a = value[min]
    b = value[max]

    if a != b:
      return False;

      min += 1
      max -= 1