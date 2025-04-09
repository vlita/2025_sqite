def get_geom(variant='8-ene'):
    geom_8 = [
        ('C', ( 0.335863334534, -0.638024393629,  0.000000000000)),
        ('H', ( 1.432938652990, -0.620850836653,  0.000000000000)),
        ('C', (-0.296842857597, -1.839541058429,  0.000000000000)),
        ('H', (-1.393739535698, -1.860704460450,  0.000000000000)),
        ('C', ( 0.383204712221, -3.118962195977,  0.000000000000)),
        ('H', ( 1.479554414548, -3.087255036285,  0.000000000000)),
        ('C', (-0.237579216697, -4.313790116847,  0.000000000000)),
        ('H', ( 0.325161369217, -5.249189992705,  0.000000000000)),
        ('H', (-1.329245260575, -4.386987278270,  0.000000000000)),
        ('C', (-0.335863334534,  0.638024393629,  0.000000000000)),
        ('H', (-1.432938652990,  0.620850836653,  0.000000000000)),
        ('C', ( 0.296842857597,  1.839541058429,  0.000000000000)),
        ('H', ( 1.393739535698,  1.860704460450,  0.000000000000)),
        ('C', (-0.383204712221,  3.118962195977,  0.000000000000)),
        ('H', (-1.479554414548,  3.087255036285,  0.000000000000)),
        ('C', ( 0.237579216697,  4.313790116847,  0.000000000000)),
        ('H', ( 1.329245260575,  4.386987278270,  0.000000000000)),
        ('H', (-0.325161369217,  5.249189992705,  0.000000000000)),
    ]

    geom_12 = [
        ('C', ( 0.318934151643,  1.838664211757,  0.000000000000)),
        ('H', ( 1.415980959638,  1.843665440633,  0.000000000000)),
        ('C', (-0.328238108423,  0.638465784864,  0.000000000000)),
        ('H', (-1.425382504623,  0.634328966959,  0.000000000000)),
        ('C', ( 0.328238108423, -0.638465784864,  0.000000000000)),
        ('H', ( 1.425382504623, -0.634328966959,  0.000000000000)),
        ('C', (-0.318934151643, -1.838664211757,  0.000000000000)),
        ('H', (-1.415980959638, -1.843665440633,  0.000000000000)),
        ('C', (-0.339993000522,  3.116591194820,  0.000000000000)),
        ('H', (-1.437280937131,  3.109148808007,  0.000000000000)),
        ('C', ( 0.302193183930,  4.315542102589,  0.000000000000)),
        ('H', ( 1.399191891261,  4.328262148643,  0.000000000000)),
        ('C', (-0.368438664361,  5.598270030604,  0.000000000000)),
        ('H', (-1.465038377840,  5.574093341283,  0.000000000000)),
        ('C', ( 0.259998191265,  6.789887178283,  0.000000000000)),
        ('H', ( 1.352081696730,  6.856305536198,  0.000000000000)),
        ('C', ( 0.339993000522, -3.116591194820,  0.000000000000)),
        ('H', ( 1.437280937131, -3.109148808007,  0.000000000000)),
        ('C', (-0.302193183930, -4.315542102589,  0.000000000000)),
        ('H', (-1.399191891261, -4.328262148643,  0.000000000000)),
        ('C', ( 0.368438664361, -5.598270030604,  0.000000000000)),
        ('H', ( 1.465038377840, -5.574093341283,  0.000000000000)),
        ('C', (-0.259998191265, -6.789887178283,  0.000000000000)),
        ('H', (-1.352081696730, -6.856305536198,  0.000000000000)),
        ('H', ( 0.297077214646, -7.728635113123,  0.000000000000)),
        ('H', (-0.297077214646,  7.728635113123,  0.000000000000)),
    ]

    if variant == '8-ene':
        return geom_8
    elif variant == '12-ene':
        return geom_12
    else:
        raise ValueError("Invalid variant. Choose either '8-ene' or '12-ene'.")