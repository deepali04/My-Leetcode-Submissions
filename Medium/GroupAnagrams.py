class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    seen = {}       
    for word in strs:
      word_list = list(word)
      word_list.sort()          
      curr_word = "".join(word_list)            
      if curr_word in seen:
          seen[curr_word].append(word)
      else:
          seen[curr_word] = [word]               
    result = []
    for word_list in seen:
      result.append(seen[word_list])          
    return result