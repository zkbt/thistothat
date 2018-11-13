from .Relation import *

class PARSEC(Relation):
    '''
    PARSEC stellar models, at 5 Gyr.
    '''
    def __init__(self, filename='data/parsec-filters.csv', maxmass=1.0):
        Relation.__init__(self, filename, comment='#', delimiter='|')
        self.table = self.table[self.table['Mini'] < maxmass]
        self.name = "PARSEC"
        self.bibcode = 'http://stev.oapd.inaf.it/cmd'
