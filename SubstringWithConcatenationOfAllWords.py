class Solution:
    def findSubstring(self, s, words):
        from collections import Counter

        word_len = len(words[0])
        num_words = len(words)
        total_length = word_len * num_words
        
        if len(s) < total_length:
            return []

        word_count = Counter(words)
        
        result = []
        
        for i in range(word_len):
            left = i
            curr_count = Counter()
            word_used = 0
            
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                
                if word in word_count:
                    curr_count[word] += 1
                    word_used += 1
                    
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        word_used -= 1
                        left += word_len
                    
                    if word_used == num_words:
                        result.append(left)
                else:
                    curr_count.clear()
                    word_used = 0
                    left = right + word_len

        return result
