class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        
        for index1, val1 in enumerate(strs):

            if any(val1 in sublist for sublist in answer) is True:
                continue

            this_word_ambi = [val1]

            for index2, val2 in enumerate(strs):
                
                 if any(val2 in sublist for sublist in answer) is True:
                    continue

                 if index1 == index2: # dont't compare with exact same item
                    continue

                 all_char = list(val1)
                 ambigram = True
                 for second in list(val2):
                    if second in all_char:
                        all_char.remove(second)
                    else:
                        ambigram = False

                 if ambigram is True and len(all_char) == 0:
                    this_word_ambi.append(val2)

            answer.append(this_word_ambi)
        
        return answer


