__author__ = 'KittipatDechkul'

def Check_Upper(buffer):
  Is_Upper = ""
  for word in buffer.split():
    if (word[0].isupper() == True):
      Is_Upper = Is_Upper + word[0]
  return Is_Upper

def main():
  n = int(input(""), 10)
  ans = list()
  for i in range(n):
    buffer = input("")
    ans.append(Check_Upper(buffer))
    ans.sort() # sort ตัวอักษร
    ans.sort(key = len, reverse = True) # sort ตาม len
  print( *ans, sep = "\n")

if __name__ == '__main__':
  main()