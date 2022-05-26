class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        sentence=sentence.split(' ')
        for idx in range(len(sentence)):
            if sentence[idx][0] in 'aieouAEIOU':
                sentence[idx]=sentence[idx]+'ma'
            else:
                sentence[idx]=sentence[idx][1::]+sentence[idx][0]+'ma'
        return ''.join([sentence[idx]+'a'*(1+idx)+' ' for idx in range(len(sentence))])[:-1:]