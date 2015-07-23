def validate(clf, test_data, test_target):
    cnt = 0
    print "asd"
    genres = ['Urban', 'Electronica', 'Pop',  'Alternative & Punk', 'Rock']
    genreMap = {1:'Urban',8:'Rock',7:'Alternative & Punk',5:'Pop',3:'Electronica'}

    genreWiseCorrectCount = {}
    genreWiseCount = {}
    genreWisePercentage = {}

    for genre in genres:
    	genreWiseCorrectCount[genre] = 0
    	genreWiseCount[genre] = 0 
    	genreWisePercentage[genre] = 0 




    for i in range(len(test_data)):
        for x in range(len(test_data[i])):
            test_data[i][x] = float(test_data[i][x])
 
        genre = genreMap[int(clf.predict(test_data[i]))]	  
            
        if(clf.predict(test_data[i]) != test_target[i]):
            cnt += 1
        else:
        	genreWiseCorrectCount[genre] += 1     
            
        genreWiseCount[genre]+=1





    for genre in genres:
    	if(genreWiseCount[genre]):
    		genreWisePercentage[genre] = (100*float(genreWiseCorrectCount[genre]) / float(genreWiseCount[genre]))    

	

    

    print genreWisePercentage		
   	



	#print genreWisePercentage
	
    return 100 * (float(cnt) / float(len(test_data)))
