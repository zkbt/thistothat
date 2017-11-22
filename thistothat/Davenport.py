from .Relation import *

class Davenport(Relation):
    '''Jim Davenport's stellar color locus from SDSS, 2MASS, and Sloan.'''
    def __init__(self, filename='data/davenport_stellarlocus.txt'):
        Relation.__init__(self, filename)


        self.name = "DavenportStellarColorLoci"
        self.bibcode = '2014MNRAS.440.3430D'
