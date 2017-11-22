from .Relation import *





class Baraffe(Relation):
    '''Isabelle Baraffe's theoretical stellar models.'''
    def __init__(self, age=5.0):


        # initialize the relation, using this filename
        Relation.__init__(self, filename='data/baraffe/BHAC15_iso.CIT2.txt')
        #self.table = self.table[np.argsort(self.table['Teff'])]

        self.name='Baraffe'
        self.bibcode='2015A%26A...577A..42B'
        self.setAge(age)

        self.descriptions = {
            'mass':'Mass of the star, in solar masses.',
            'Teff':'Stellar effective temperature, in K.',
            'logL':'log10(Luminosity), in solar luminosities.',
            'logg':'log10(Surface Gravity), in cm/s^2.',
            'radius':'Radius of the star, in solar radii.',
            'lithium':'Ratio of surface lithium abundance to initial abundance.',
            'Mv':'Absolute V magnitude (Cousin).',
            'Mr':'Absolute R magnitude (Cousin).',
            'Mi':'Absolute I magnitude (Cousin).',
            'Mj':'Absolute J magnitude (CIT).',
            'Mh':'Absolute H magnitude (CIT).',
            'Mk':'Absolute K magnitude (CIT).',
            'Ml':'Absolute L magnitude (Johnson-Glass).',
            'Mll':"Absolute L' magnitude (Johnson-Glass).",
            'Mm':'Absolute M magnitude (Johnson-Glass).',
            'age':'Absolute M magnitude (Johnson-Glass).'
        }

        self.summarize()


    def load(self):
        '''
        Load the Baraffe isochrones.
            (so far, this has been tested only on `BHAC15_iso.CIT2.txt`)
        '''

        path = pkg_resources.resource_filename(__name__, self.filename)
        self.speak('loading data from {0}'.format(path))


        f = open(path, 'r')
        lines = f.readlines()
        tables = []
        while(len(lines) > 0):
            l = lines.pop(0)
            if 't (Gyr)' in l:
                age = np.float(l.split(' ')[-1])
                junk = lines.pop(0)
                headers = lines.pop(0)
                d = {}
                columns = headers.split()[1:]
                for h in columns:
                    d[h] = []
                junk = lines.pop(0)
                stillreading = True
                while(stillreading):
                    r = lines.pop(0)
                    if '!--' in r:
                        stillreading = False
                    else:
                        splitted = r.split()
                        for i, c in enumerate(columns):
                            d[c].append(np.float(splitted[i]))

                table = astropy.table.Table(d)
                table['age'] = age
                tables.append(table)

        self.tables = astropy.table.vstack(tables)
        self.tables.add_index('age')
        self.speak('   ...success!')

        # fix the names in the table
        self.tables['M/Ms'].name = 'mass'
        self.tables['L/Ls'].name = 'logL'
        self.tables['g'].name = 'logg'
        self.tables['R/Rs'].name = 'radius'
        self.tables['Li/Li0'].name = 'lithium'

        # pull out the list of available ages
        self.ages = np.unique(self.tables['age'].data)

        # create an empty dictionary describing each column
        self.descriptions = {}


    def setAge(self, age=5.0):
        '''
        Pull out one age slice from the big table,
        giving quantities at one individual age.
        '''
        assert(age in self.ages)
        self.age = age
        self.name= "Baraffe_{}Gyr".format(age).replace('0.', '0p').replace('.0', '')

        self.table = self.tables.loc[age]
        self.speak('setting the Baraffe model age to {} Gyr'.format(self.age))


# ------------_---------------------_---------------------_------------------- #

def test(allAges=False):
    models = Baraffe()
    models.plot()
    return models

def testAllAges():
    '''
    Loop through the Baraffe ages, making a plot for each.
    '''

    for age in models.ages:
        models.setAge(age)
        models.plot(['mass', 'Teff', 'logg'])
