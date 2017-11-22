from .Relation import *

class Mamajek(Relation):
    '''Eric Mamajek's relations for stars, linking spectral type, effective temperature, bolometric corrections, colors, abosolute magnitudes, luminosities, and mass,'''
    def __init__(self, filename='data/mamajek_dwarfproperties.txt'):
        Relation.__init__(self, filename)
        self.table = self.table[np.argsort(self.table['Teff'])]
        self.name="TheMamajekCuratedStars"
        self.bibcode='2013ApJS..208....9P'

def test():
    stars = Mamajek()
    stars.plot()
    return starts
