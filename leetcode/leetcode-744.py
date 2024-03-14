class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        letters.append(target)
        letters.sort()
        position = 0
        for i in range(len(letters)):
            if letters[i] == target:
                position = i
        if position == len(letters) - 1:
            return letters[0]
        for i in range(1, len(letters)):
            if letters[(position + i) % len(letters)] != target:
                return letters[(position + i) % len(letters)]