Python tricks

*set() removes duplicate elements from the list.

*   from collections import Counter

    def anagram(first, second):
        return Counter(first) == Counter(second)


    anagram("abcd3", "3acdb")
    
3. Memory
  This snippet can be used to check the memory usage of an object.
  import sys 

  variable = 30 
  print(sys.getsizeof(variable)) # 24
  
4. Capitalize first letters

  s = "programming is awesome"
  print(s.title()) # Programming Is Awesome

5. transpose a 2D array.
  array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
  transposed = zip(*array)
  print(transposed) # [('a', 'c', 'e'), ('b', 'd', 'f')]
  
6. def merge_dictionaries(a, b)
   return {**a, **b}
   
7. def to_dictionary(keys, values):
    return dict(zip(keys, values))
    keys = ["a", "b", "c"]    
    values = [2, 3, 4]
    print(to_dictionary(keys, values)) # {'a': 2, 'c': 4, 'b': 3}
    
8. def palindrome(a):
    return a == a[::-1]
    palindrome('mom') # True
