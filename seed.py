from sqlalchemy.orm import sessionmaker
from models import Band, Venue, Concert, engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create Kenyan artists (bands)
band1 = Band(name="Elani", genre="Afropop")
band2 = Band(name="Sauti Sol", genre="Afropop")
band3 = Band(name="Ayrosh", genre="Mugithi")
band4 = Band(name="Nikita Kering'", genre="R&B")
band5 = Band(name="Nviiri The Storyteller", genre="Afropop")
band6 = Band(name="Matata", genre="Gengetone")
band7 = Band(name="Bien", genre="Afropop")
band8 = Band(name="Bensoul", genre="Afrosoul")
band9 = Band(name="Billy Black", genre="Afropop")
band10 = Band(name="Njerae", genre="Soul")
band11 = Band(name="Manasseh Shalom", genre="Gospel")
band12 = Band(name="PHY", genre="Afrosoul")
band13 = Band(name="Kidum Kibido", genre="Afrobeat")
band14 = Band(name="King Kaka", genre="Hip Hop")
band15 = Band(name="Eric Wainaina", genre="Afrofusion")
band16 = Band(name="Wanjine", genre="Afropop")
band17 = Band(name="Mutoriah", genre="Afrofusion")
band18 = Band(name="Kagwe Mungai", genre="Afrobeats")
band19 = Band(name="Kethan", genre="Afropop")

# Create Kenyan venues
venue1 = Venue(name="Nyayo Stadium", location="Nairobi")
venue2 = Venue(name="Carnival", location="Nairobi")
venue3 = Venue(name="Naivasha Ground", location="Naivasha")
venue4 = Venue(name="Kasarani Stadium", location="Nairobi")
venue5 = Venue(name="Ngong Racecourse", location="Nairobi")
venue6 = Venue(name="KICC Grounds", location="Nairobi")
venue7 = Venue(name="Mombasa Sports Club", location="Mombasa")
venue8 = Venue(name="Bomas of Kenya", location="Nairobi")
venue9 = Venue(name="Uhuru Gardens", location="Nairobi")
