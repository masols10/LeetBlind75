class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # This is clearly a sorting problem
        # First separate out the word by space
        # Look for second item, see if it is digit, if so, append the whole chunk to digits
        # If not, we separate out the first and the rest as a two- element array
        # sort letter by second index first, then the first index
        # concat and return
        digits = []
        letters = []
        for log in logs:
            log_split = log.split(" ")
            if log_split[1].isdigit():
                digits.append(log)
            else:
                letters.append([log_split[0], " ".join(log_split[1:])])
        letters.sort(key = lambda x: [x[1], x[0]])
        return [" ".join(letter) for letter in letters] + digits