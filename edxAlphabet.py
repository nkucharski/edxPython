#s This is a program which prints the largest substring of a string "s", in which the letters occur in alphabetical order.

def sSub(s):
	currentlength = 1
	currentstart = 0
	beststart = 0
	bestlength = 1
	for i in range(len(s) - 1):
		if s[i] < s[i+1]:
			currentlength += 1
			print('currentlength = ' + str(currentlength))
			print('i = ' + str(i))
			print('s[i] = ' + s[i] + ' s[i+1] = ' + s[i+1])
			if currentlength > bestlength:
				bestlength = currentlength
				beststart = currentstart + 1
		elif s[i] > s[i+1]:
			print('WARNING: s[i] > s[i+1]')
			print('i = ' + str(i))
			if currentlength > bestlength:
				bestlength = currentlength
				beststart = currentstart + 1
				print('bestlength = ' + str(bestlength))
				print('beststart = ' + str(beststart))
			currentstart = i
			currentlength = 1
	print('beststart = ' + str(beststart) + 'bestlength = ' + str(bestlength))
	return s[beststart : beststart+bestlength]

			 	
