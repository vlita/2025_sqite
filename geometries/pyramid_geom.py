import numpy as np

def get_h10pyr_geom(r):
    hpyr = np.sqrt(2.0 / 3) * r
    htri = np.cos(np.pi / 6.0) * r

    a1x = 0.0
    a2x = -0.5 * r
    a3x = 0.5 * r
    a4x = -r
    a5x = 0.0
    a6x = r
    a7x = 0.0
    a8x = -0.5 * r
    a9x = 0.5 * r
    a10x = 0.0

    a1y = (4.0 / 3) * htri
    a2y = (1.0 / 3) * htri
    a3y = (1.0 / 3) * htri
    a4y = -(2.0 / 3) * htri
    a5y = -(2.0 / 3) * htri
    a6y = -(2.0 / 3) * htri
    a7y = (2.0 / 3) * htri
    a8y = -(1.0 / 3) * htri
    a9y = -(1.0 / 3) * htri
    a10y = 0.0

    a1z = -hpyr
    a2z = -hpyr
    a3z = -hpyr
    a4z = -hpyr
    a5z = -hpyr
    a6z = -hpyr
    a7z = 0.0
    a8z = 0.0
    a9z = 0.0
    a10z = hpyr

    # Create the tuple output directly
    geom = [
        ('H', (a1x, a1y, a1z)),
        ('H', (a2x, a2y, a2z)),
        ('H', (a3x, a3y, a3z)),
        ('H', (a4x, a4y, a4z)),
        ('H', (a5x, a5y, a5z)),
        ('H', (a6x, a6y, a6z)),
        ('H', (a7x, a7y, a7z)),
        ('H', (a8x, a8y, a8z)),
        ('H', (a9x, a9y, a9z)),
        ('H', (a10x, a10y, a10z))
    ]

    return geom
