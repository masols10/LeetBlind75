from collections import OrderedDict
from itertools import combinations

class Solution(object):    
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        input_dictionary = {}
        pattern_dict = {}
        
        # Sort the input based on the timestamp
        sorted_list = sorted(zip(username, website, timestamp), key = lambda x:x[2])
        
        # Read input dictionary properly
        for user, web, time in sorted_list:
            if user in input_dictionary:
                input_dictionary[user].append(web)
            else:
                input_dictionary[user] = [web]
        
        # Create a dictionary for patterns
        for key, values in input_dictionary.items():
            #Create the dictionary that contains all the possible paterns for each user
            returned_list = sorted(set(combinations(values, 3)))
            
            for items in returned_list:
                if tuple(items) in pattern_dict:
                    pattern_dict[tuple(items)] += 1
                else:
                    pattern_dict[tuple(items)] = 1
         
        # Sort first by frequency, then by the item / pattern itself for lexicographical order
        def sortKey(key):
            return (-pattern_dict[key], key)

        return sorted(pattern_dict, key=sortKey)[0]