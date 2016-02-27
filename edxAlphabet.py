#s This is a program which prints the largest substring of a string "s", in which the letters occur in alphabetical order.

def sSub(s):
	currentlength = 0
	currentstart = 0
	beststart = 0
	bestlength = 0
	for i in range(len(s) - 1):
		if s[i] < s[i+1]:
			currentlength += 1
			print('currentlength = ' + str(currentlength))
			print('i = ' + str(i))
			print('s[i] = ' + s[i] + ' s[i+1] = ' + s[i+1]) 
		elif s[i] > s[i+1] or s[i+1]==None:
			print('WARNING: s[i] > s[i+1]')
			print('i = ' + i)
			if currentlength > bestlength:
				bestlength = currentlength
				beststart = currentstart
				print('bestlength = ' + str(bestlength))
				print('beststart = ' + str(beststart))
			currentstart = i
			currentlength = 0
	return s[beststart : beststart+bestlength]

			 	
