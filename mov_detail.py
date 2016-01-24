#Soumyargha Sinha
#OMDB is used
import urllib2
import json
def movie_search(name):
	t = name.replace(' ', '%20')
	url = 'http://www.omdbapi.com/?t='+t+'&y=&plot=full&r=json'
	json_obj = urllib2.urlopen(url)
	data = json.loads(json_obj.read())
	try:
		file = open(data['Title']+".txt", 'w')
		file.write(data['Title']+" ("+data['Year']+")"+"\n")
		file.write("Directed by : " +data['Director']+"\n")
		file.write("Rated : " +data['Rated']+"\n")
		file.write("Genre : " +data['Genre']+"\n")
		file.write("IMDB : " +data['imdbRating']+"\n")
		file.write("Metascore : " +data['Metascore']+"\n")
		file.write("Story : " +data['Plot']+"\n")
		file.close()
	except:
		print "Not found"
name = raw_input("Enter the movie's name : ")
movie_search(name)
