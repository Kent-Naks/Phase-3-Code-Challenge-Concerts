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

# Create sample concerts
concert1 = Concert(date="2024-12-01", band=band2, venue=venue1)  # Sauti Sol at Nyayo Stadium
concert2 = Concert(date="2024-12-10", band=band7, venue=venue2)  # Bien at Carnival
concert3 = Concert(date="2024-12-20", band=band5, venue=venue3)  # Nviiri at Naivasha Ground
concert4 = Concert(date="2024-12-25", band=band1, venue=venue4)  # Elani at Kasarani Stadium
concert5 = Concert(date="2024-12-31", band=band18, venue=venue5) # Kagwe Mungai at Ngong Racecourse
concert6 = Concert(date="2025-01-05", band=band14, venue=venue6) # King Kaka at KICC Grounds
concert7 = Concert(date="2025-01-15", band=band4, venue=venue7)  # Nikita Kering' at Mombasa Sports Club
concert8 = Concert(date="2025-01-20", band=band10, venue=venue8) # Njerae at Bomas of Kenya
concert9 = Concert(date="2025-02-01", band=band15, venue=venue9) # Eric Wainaina at Uhuru Gardens

# Add everything to the session and commit
session.add_all([band1, band2, band3, band4, band5, band6, band7, band8, band9, band10, band11,
                 band12, band13, band14, band15, band16, band17, band18, band19,
                 venue1, venue2, venue3, venue4, venue5, venue6, venue7, venue8, venue9,
                 concert1, concert2, concert3, concert4, concert5, concert6, concert7, concert8, concert9])
session.commit()

print("Database seeded successfully with Kenyan artists and venues!")