import numpy as np
import qforte as qf

from run_job import run_qite

from geometries.ene import get_geom as ene

from path import path

print(path)
e_path = f'{path}/ene/eight/'
t_path = f'{path}/ene/twelve/'
theta_1 = 1.0e-6
theta_2 = 1.0e-7
theta_3 = 5.0e-8
theta_4 = 1.0e-8
theta_5 = 5.0e-9
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
    build_df_ham=True,
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
e_8_path_t1 = run_qite(
    mol_8,
    beta=30.0,
    db=0.1,
    expansion_type='All',
    second_order=True,
    selected_pool=True,
    t_thresh=theta_1,
    conv_thresh=1.0e-3,
    use_df_ham_selection = True,
    output_path=e_path)
e_8_path_t2 = run_qite(
    mol_8,
    beta=30.0,
    db=0.1,
    expansion_type='All',
    second_order=True,
    selected_pool=True,
    t_thresh=theta_2,
    conv_thresh=1.0e-3,
    use_df_ham_selection = True,
    output_path=e_path)
e_8_path_t3 = run_qite(
    mol_8,
    beta=30.0,
    db=0.1,
    expansion_type='All',
    second_order=True,
    selected_pool=True,
    t_thresh=theta_3,
    conv_thresh=1.0e-3,
    use_df_ham_selection = True,
    output_path=e_path)
e_8_path_t4 = run_qite(
    mol_8,
    beta=30.0,
    db=0.1,
    expansion_type='All',
    second_order=True,
    selected_pool=True,
    t_thresh=theta_4,
    conv_thresh=1.0e-3,
    use_df_ham_selection = True,
    output_path=e_path)
e_8_path_t5 = run_qite(
    mol_8,
    beta=30.0,
    db=0.1,
    expansion_type='All',
    second_order=True,
    selected_pool=True,
    t_thresh=theta_5,
    conv_thresh=1.0e-3,
    use_df_ham_selection = True,
    output_path=e_path)