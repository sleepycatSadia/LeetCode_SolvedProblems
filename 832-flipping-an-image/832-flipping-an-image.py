class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for idx in range(len(image)):
            image[idx].reverse()
            for babyidx in range (len(image[idx]) ):
                if image[idx][babyidx] == 0 :
                    image[idx][babyidx] = 1
                else:
                    image[idx][babyidx] = 0
        return image
        