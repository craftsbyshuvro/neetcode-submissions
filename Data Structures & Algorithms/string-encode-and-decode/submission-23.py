class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for val in strs:
            encoded = encoded + str(len(val)) + '#' + val

        print('encoded',encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        length = ''
        ignoreIfLess = 0
        for index in range(len(s)):
            
            if index < ignoreIfLess:
                continue

            if s[index] != '#':
                length = length + s[index]
            else:
                print('L: ',length)
                endindex = index + 1 + int(length)

                word = s[index + 1:endindex]
                if len(word) == 0:
                    decoded.append('')
                else:
                    decoded.append(s[index + 1:endindex])
                print('decoded', decoded)
                ignoreIfLess = endindex 
                length = ''

        return decoded
