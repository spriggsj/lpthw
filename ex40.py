class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
		
happy_bday = Song(["Happy birthday to you I don't want to get sued so i'll stop rigt there"])
					
bulls_on_parade = Song(["They rally around the family",
					"With pockets full of shells"])
					
ring_around = Song(["Ring around the roses pocket full of posies"])
					
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
					
ring_around.sing_me_a_song()
