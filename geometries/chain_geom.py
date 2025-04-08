def get_h10chain_geom(r):
    a1z = 9.*r/2
    a2z = 7.*r/2
    a3z = 5.*r/2
    a4z = 3.*r/2
    a5z = r/2.
    a6z = -r/2.
    a7z = -3.*r/2
    a8z = -5.*r/2
    a9z = -7.*r/2
    a10z = -9.*r/2

    # Tuple-based output for chain geometry
    geom = [
        ('H', (0.0, 0.0, a1z)),
        ('H', (0.0, 0.0, a2z)),
        ('H', (0.0, 0.0, a3z)),
        ('H', (0.0, 0.0, a4z)),
        ('H', (0.0, 0.0, a5z)),
        ('H', (0.0, 0.0, a6z)),
        ('H', (0.0, 0.0, a7z)),
        ('H', (0.0, 0.0, a8z)),
        ('H', (0.0, 0.0, a9z)),
        ('H', (0.0, 0.0, a10z))
    ]

    return geom
