from sqlalchemy import Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import relationship
from config import engine, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)
    concerts = relationship('Concert', back_populates='band')

    def venues(self):
        # Returns a list of all the venues where this band has played
        return [concert.venue for concert in self.concerts]

    def all_introductions(self):
        # Returns a list of introductions for all concerts this band has performed
        return [concert.introduction() for concert in self.concerts]

    @classmethod
    def most_performances(cls, session):
        # Returns the band with the most concerts played
        return session.query(cls).join(Concert).group_by(cls.id).order_by(func.count(Concert.id).desc()).first()

    def play_in_venue(self, venue, date):
        # Creates a new concert for the band at the given venue on the specified date
        concert = Concert(date=date, band=self, venue=venue)
        session.add(concert)
        session.commit()

class Venue(Base):
    __tablename__ = 'venues'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)
    concerts = relationship('Concert', back_populates='venue')

    def bands(self):
        # Returns a list of all the bands that have performed at this venue
        return [concert.band for concert in self.concerts]

    def concert_on(self, date):
        # Finds and returns the first concert on a specific date at this venue
        return next((concert for concert in self.concerts if concert.date == date), None)

    def most_frequent_band(self):
        # Returns the band that has performed the most at this venue
        bands_performance = {}
        for concert in self.concerts:
            if concert.band in bands_performance:
                bands_performance[concert.band] += 1
            else:
                bands_performance[concert.band] = 1
        return max(bands_performance, key=bands_performance.get) if bands_performance else None

class Concert(Base):
    __tablename__ = 'concerts'
    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    def hometown_show(self):
        # Checks if the concert is in the band's hometown
        return self.venue.city == self.band.hometown

    def introduction(self):
        # Returns an introduction string for the concert
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

# To create the tables and start using them, make sure to run:
Base.metadata.create_all(engine)
