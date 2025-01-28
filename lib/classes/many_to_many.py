import re

class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 3:
            if not hasattr(self, "_name"):
                self._name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        best_visitor = None
        if len(self.visitors()) > 0:
            best_visit_count = 0
            # return best visitor
            for visitor in self.visitors():
                if visitor.total_visits_at_park(self) > best_visit_count:
                    best_visitor = visitor
                    best_visit_count = visitor.total_visits_at_park(self)
                
        return best_visitor


class Trip:

    all = []
    

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
    
    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park

    pattern = r"(January|February|March|April|May|June|July|August|September|October|November|December) ([1-9]|[12][0-9]|3[01])(st|nd|rd|th)"

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            if re.fullmatch(type(self).pattern, start_date):
                self._start_date = start_date
    
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            if re.fullmatch(type(self).pattern, end_date):
                self._end_date = end_date


class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(1,16):
            self._name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))
    
    def total_visits_at_park(self, park):
        if park in self.national_parks():
            return [trip.national_park for trip in self.trips()].count(park)
        else:
            return 0