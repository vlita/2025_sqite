import numpy as np
import qforte as qf

from run_job import run_qite

from geometries.ene import get_geom as ene

from path import path

print(path)
e_path = f'{path}/ene/eight/'
t_path = f'{path}/ene/twelve/'
k = 4
exp_type = f'{k}-UpCCGSD'
print('\nBuild Geometry')
print('-------------------------')

symm_str = 'c1'
fdocc = 0
fuocc = 0

basis_set = 'cc-pvdz'
avas_atoms_and_atomic_orbs = ['C 2pz']

## ====> Build Qforte Mol with PySCF (using AVAS) <==== ###
mol_8 = qf.system_factory(
    build_type='pyscf', 
    symmetry=symm_str,
    mol_geometry=ene(variant='8-ene'), 
    basis=basis_set, 
    run_fci=True, 
    use_avas=True, #                     <=====
    avas_atoms_or_orbitals=avas_atoms_and_atomic_orbs,
    run_ccsd=False,
    store_mo_ints=True,
    build_df_ham=False,
    num_frozen_uocc = fuocc,
    num_frozen_docc = fdocc,
    build_qb_ham = False,
    )


print(f'The FCI energy from Pyscf:         {mol_8.fci_energy:12.10f}')
print(f'The SCF energy from Pyscf:         {mol_8.hf_energy:12.10f}')

# ## ====> Build Qforte Mol with PySCF (using AVAS) <==== ###
# mol_12 = qf.system_factory(
#     build_type='pyscf', 
#     symmetry=symm_str,
#     mol_geometry=ene(variant='12-ene'), 
#     basis=basis_set, 
#     run_fci=True, 
#     use_avas=True, #                     <=====
#     avas_atoms_or_orbitals=avas_atoms_and_atomic_orbs,
#     run_ccsd=False,
#     store_mo_ints=True,
#     build_df_ham=False,
#     num_frozen_uocc = fuocc,
#     num_frozen_docc = fdocc,
#     build_qb_ham = False,
#     )


# print(f'The FCI energy from Pyscf:         {mol_12.fci_energy:12.10f}')
# print(f'The SCF energy from Pyscf:         {mol_12.hf_energy:12.10f}')
e_8_path = run_qite(
    mol_8,
    beta=20.0,
    db=0.1,
    expansion_type=exp_type,
    low_memorySb=True,
    second_order=True,
    conv_thresh=1.0e-4,
    output_path=e_path)
# e_12_path = run_qite(
#     mol_8,
#     beta=0.0,
#     db=0.1,
#     expansion_type=exp_type,
#     low_memorySb=True,
#     second_order=True,
#     conv_thresh=1.0e-4,
#     output_path=t_path)
print(e_8_path)
# print(e_12_path)