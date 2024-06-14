class Band:
    def __init__(self, name, hometown):
        if not isinstance(hometown, str):
            raise ValueError("hometown must be a non-empty string")
        self.name = name
        self._hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("name must be a non-empty string")
        self._name = value
    
    @property
    def hometown(self):
        return self._hometown

    def play_in_venue(self, venue, date):
        concert = Concert(date, self, venue)
        self._concerts.append(concert)
        venue.add_concert(concert)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts]

    def concerts(self):
        return [concert for concert in Concert.all if concert.band == self]

    def venues(self):
        return list(set([concert.venue for concert in self.concerts()]))

class Venue:
    def __init__(self, name, city):
        if not isinstance(name, str) or not name:
            raise ValueError("name must be a non-empty string")
        if not isinstance(city, str) or not city:
            raise ValueError("city must be a non-empty string")
        self._name = name
        self._city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("name must be a non-empty string")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("city must be a non-empty string")
        self._city = value

    def add_concert(self, concert):
        self._concerts.append(concert)

    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]

    def bands(self):
        return list({concert.band for concert in self.concerts()})

class Concert:
    all = []
    
    def __init__(self, date, band, venue):
        if not isinstance(date, str) or not date:
            raise ValueError("date must be a non-empty string")
        if not isinstance(band, Band):
            raise ValueError("band must be of type Band")
        if not isinstance(venue, Venue):
            raise ValueError("venue must be of type Venue")
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("date must be a non-empty string")
        self._date = value

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            raise ValueError("band must be of type Band")
        self._band = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise ValueError("venue must be of type Venue")
        self._venue = value

    def hometown_show(self):
        return self.band.hometown == self._venue.city

    def introduction(self):
        return f"Hello {self._venue.city}!!!!! We are {self._band.name} and we're from {self._band.hometown}"