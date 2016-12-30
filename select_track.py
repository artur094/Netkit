print '\nNetkit Track Finder\n'
print "# - - - - - - - - - #"
print "\nPlease, insert your surname:"

surname = raw_input().lower()

first_letter = ord('a')
my_letter = ord(surname[0])
diff = my_letter - first_letter

print '\nTrack No: ' + str(diff%4)