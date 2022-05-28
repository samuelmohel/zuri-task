def find_anagrams(str1, str2):
      return sorted(str1) == sorted(str2) and len(str1) == len(str2)
   
    
str1 = input(f"string1: ")
str2 = input(f"string2: ")

print(find_anagrams((str1),(str2)))