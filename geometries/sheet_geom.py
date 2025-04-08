import numpy as np

def get_h10sheet_geom(r):
    htri = np.cos(np.pi / 6.0) * r

    a1x = -r
    a2x =  0.0
    a3x =  r
    a4x = -(3.0/2) * r
    a5x = -r/2
    a6x =  r/2
    a7x = (3.0/2) * r
    a8x = -r
    a9x =  0.0
    a10x =  r

    a1y = htri
    a2y = htri
    a3y = htri
    a4y = 0.0
    a5y = 0.0
    a6y = 0.0
    a7y = 0.0
    a8y = -htri
    a9y = -htri
    a10y = -htri

    # Tuple-based output for hydrogen sheet geometry
    geom = [
        ('H', (a1x, a1y, 0.00)),
        ('H', (a2x, a2y, 0.00)),
        ('H', (a3x, a3y, 0.00)),
        ('H', (a4x, a4y, 0.00)),
        ('H', (a5x, a5y, 0.00)),
        ('H', (a6x, a6y, 0.00)),
        ('H', (a7x, a7y, 0.00)),
        ('H', (a8x, a8y, 0.00)),
        ('H', (a9x, a9y, 0.00)),
        ('H', (a10x, a10y, 0.00))
    ]

    return geom
