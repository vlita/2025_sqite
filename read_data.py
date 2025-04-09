def read_qite(path):
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
    with open(path, 'r') as file:
        for _ in range(2):
            next(file)

        for line in file:
            beta = line.split()[0]
            energy = line.split()[1]
            beta_list.append(beta)
            energy_list.append(energy)

    return beta_list, energy_list