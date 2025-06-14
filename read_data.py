def read_qite(path):

    beta_list = []
    energy_list = []
    param_list = []
    cnot_list = []
    measure_list = []

    with open(path, 'r') as file:
        for _ in range(2):
            next(file)

        for line in file:
            beta = line.split()[0]
            energy = line.split()[1]
            param = line.split()[2]
            cnot = line.split()[3]
            pauli = line.split()[4]
            beta_list.append(beta)
            energy_list.append(energy)
            param_list.append(param)
            cnot_list.append(cnot)
            measure_list.append(pauli)

    return beta_list, energy_list, param_list, cnot_list, measure_list

def read_exact(path):

    beta_list = []
    energy_list = []

    with open(path, 'r') as file:
        for _ in range(2):
            next(file)

        for line in file:
            beta = line.split()[0]
            energy = line.split()[1]
            beta_list.append(beta)
            energy_list.append(energy)

    return beta_list, energy_list

def read_vqe(path):

    pauli_list = []
    energy_list = []

    with open(path, 'r') as file:
        for _ in range(2):
            next(file)

        for line in file:
            pauli = line.split()[6]
            energy = line.split()[1]
            pauli_list.append(pauli)
            energy_list.append(energy)

    return pauli_list, energy_list

def read_spqe(path):

    param_list = []
    pauli_list = []
    energy_list = []

    with open(path, 'r') as file:
        for _ in range(2):
            next(file)

        for line in file:
            param = line.split()[2]
            pauli = line.split()[4]
            energy = line.split()[1]
            param_list.append(param)
            pauli_list.append(pauli)
            energy_list.append(energy)

    return param_list, pauli_list, energy_list