import numpy as np

def get_h10ring_geom(r):
    phi_o = 2 * np.pi / 10
    rad_denom = 2 * np.sin(np.pi / 10)
    rad = r / rad_denom

    a1x = rad * np.cos(phi_o * 0)
    a2x = rad * np.cos(phi_o * 1)
    a3x = rad * np.cos(phi_o * 2)
    a4x = rad * np.cos(phi_o * 3)
    a5x = rad * np.cos(phi_o * 4)
    a6x = rad * np.cos(phi_o * 5)
    a7x = rad * np.cos(phi_o * 6)
    a8x = rad * np.cos(phi_o * 7)
    a9x = rad * np.cos(phi_o * 8)
    a10x = rad * np.cos(phi_o * 9)

    a1y = rad * np.sin(phi_o * 0)
    a2y = rad * np.sin(phi_o * 1)
    a3y = rad * np.sin(phi_o * 2)
    a4y = rad * np.sin(phi_o * 3)
    a5y = rad * np.sin(phi_o * 4)
    a6y = rad * np.sin(phi_o * 5)
    a7y = rad * np.sin(phi_o * 6)
    a8y = rad * np.sin(phi_o * 7)
    a9y = rad * np.sin(phi_o * 8)
    a10y = rad * np.sin(phi_o * 9)

    # Create tuple-based output for the ring geometry
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
