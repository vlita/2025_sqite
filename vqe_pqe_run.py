import numpy as np
import qforte as qf

from run_job import run_qite, run_spqe, run_vqe

from geometries.ene import get_geom as ene

from path import path

print(path)
e_path = f'{path}/ene/eight/'
t_path = f'{path}/ene/twelve/'

print('\nBuild Geometry')
print('-------------------------')

symm_str = 'c1'
fdocc = 0
fuocc = 0

basis_set = 'cc-pvdz'
avas_atoms_and_atomic_orbs = ['C 2pz']

## ====> Build Qforte Mol with PySCF (using AVAS) <==== ###
mol = qf.system_factory(
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

## ====> Build Qforte Mol with PySCF (using AVAS) <==== ###
# mol = qf.system_factory(
#     build_type='pyscf', 
#     symmetry=symm_str,
#     mol_geometry=geom, 
#     basis=basis_set, 
#     run_fci=True, 
#     use_avas=True, #                     <=====
#     avas_atoms_or_orbitals=avas_atoms_and_atomic_orbs,
#     run_ccsd=False,
#     store_mo_ints=True,
#     build_df_ham=True,        # Important, must compute here
#     num_frozen_uocc = fuocc,
#     num_frozen_docc = fdocc,
#     build_qb_ham = False,
#     )

print(f'The FCI energy from Pyscf:         {mol.fci_energy:12.10f}')
print(f'The SCF energy from Pyscf:         {mol.hf_energy:12.10f}')


ty = qf.local_timer()
# ty.reset()

# e_8_path_s = run_qite(
#     mol,
#     beta=1.5,
#     db=0.1,
#     expansion_type='All',
#     low_memorySb=0,
#     second_order=True,
#     selected_pool=True,
#     t_thresh=1.0e-8,
#     conv_thresh=1.0e-3,
#     use_df_ham_selection = False,
#     output_path=e_path)

# ty.record("sQITE")
# print(ty)

# ty.reset()

# e_8_path_df = run_qite(
#     mol,
#     beta=1.5,
#     db=0.1,
#     expansion_type='All',
#     low_memorySb=0,
#     second_order=True,
#     selected_pool=True,
#     t_thresh=1.0e-8,
#     conv_thresh=1.0e-3,
#     use_df_ham_selection = True,
#     output_path=e_path)

# ty.record("DF-sQITE")
# print(ty)

ty.reset()

e_8_path_vqe = run_vqe(
    mol,
    output_path=t_path
)

ty.record("UCCSD VQE")
print(ty)

ty.reset()

e_8_path_spqe = run_spqe(
    mol,
    output_path=t_path
)

ty.record("SPQE")
print(ty)


# Ets = alg._Ets

# print('\n')
# print(f'The FCI target_root energy from pyscf:     {mol.fci_energy:12.10f}')
# print(f'The target_root energy from qite:          {Ets:12.10f}')
# print(f'Delta E                                    {np.abs(Ets-mol.fci_energy):12.10f}')

