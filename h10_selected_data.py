import numpy as np
import qforte as qf

from run_job import run_qite

from geometries.chain_geom import get_h10chain_geom as chain
# from geometries.pyramid_geom import get_h10pyr_geom as pyrmd
from geometries.ring_geom import get_h10ring_geom as ring
from geometries.sheet_geom import get_h10sheet_geom as sheet

from path import path

print(path)
c_path_1 = f'{path}/h10/ang_10/chain/'
r_path_1 = f'{path}/h10/ang_10/ring/'
s_path_1 = f'{path}/h10/ang_10/sheet/'
# p_path_1 = f'{path}/h10/ang_10/pyramid/'

c_path_15 = f'{path}/h10/ang_15/chain/'
r_path_15 = f'{path}/h10/ang_15/ring/'
s_path_15 = f'{path}/h10/ang_15/sheet/'
# p_path_15 = f'{path}/h10/ang_15/pyramid/'
theta_1 = 1.0e-6
theta_2 = 1.0e-7
theta_3 = 5.0e-8
theta_4 = 1.0e-8
theta_5 = 5.0e-9
chain_mol_1 = qf.system_factory(build_type='psi4', mol_geometry=chain(1.0), basis='sto-6g', run_fci=True)
print(f'The FCI energy from Psi4:                                    {chain_mol_1.fci_energy:12.10f}')
print(f'The HF energy from Psi4:                                     {chain_mol_1.hf_energy:12.10f}')

ring_mol_1 = qf.system_factory(build_type='psi4', mol_geometry=ring(1.0), basis='sto-6g', run_fci=True)
print(f'The FCI energy from Psi4:                                    {ring_mol_1.fci_energy:12.10f}')
print(f'The HF energy from Psi4:                                     {ring_mol_1.hf_energy:12.10f}')

sheet_mol_1 = qf.system_factory(build_type='psi4', mol_geometry=sheet(1.0), basis='sto-6g', run_fci=True)
print(f'The FCI energy from Psi4:                                    {sheet_mol_1.fci_energy:12.10f}')
print(f'The HF energy from Psi4:                                     {sheet_mol_1.hf_energy:12.10f}')

# pyrmd_mol_1 = qf.system_factory(build_type='psi4', mol_geometry=pyrmd(1.0), basis='sto-6g', run_fci=True)
# print(f'The FCI energy from Psi4:                                    {pyrmd_mol_1.fci_energy:12.10f}')
# print(f'The HF energy from Psi4:                                     {pyrmd_mol_1.hf_energy:12.10f}')

chain_mol_15 = qf.system_factory(build_type='psi4', mol_geometry=chain(1.5), basis='sto-6g', run_fci=True)
print(f'The FCI energy from Psi4:                                    {chain_mol_15.fci_energy:12.10f}')
print(f'The HF energy from Psi4:                                     {chain_mol_15.hf_energy:12.10f}')

ring_mol_15 = qf.system_factory(build_type='psi4', mol_geometry=ring(1.5), basis='sto-6g', run_fci=True)
print(f'The FCI energy from Psi4:                                    {ring_mol_15.fci_energy:12.10f}')
print(f'The HF energy from Psi4:                                     {ring_mol_15.hf_energy:12.10f}')

sheet_mol_15 = qf.system_factory(build_type='psi4', mol_geometry=sheet(1.5), basis='sto-6g', run_fci=True)
print(f'The FCI energy from Psi4:                                    {sheet_mol_15.fci_energy:12.10f}')
print(f'The HF energy from Psi4:                                     {sheet_mol_15.hf_energy:12.10f}')

# pyrmd_mol_15 = qf.system_factory(build_type='psi4', mol_geometry=pyrmd(1.5), basis='sto-6g', run_fci=True)
# print(f'The FCI energy from Psi4:                                    {pyrmd_mol_15.fci_energy:12.10f}')
# print(f'The HF energy from Psi4:                                     {pyrmd_mol_15.hf_energy:12.10f}')
# chain_path_1_t1 = run_qite(
#     chain_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_1,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=c_path_1)
# chain_path_1_t2 = run_qite(
#     chain_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_2,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=c_path_1)
# chain_path_1_t3 = run_qite(
#     chain_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_3,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=c_path_1)
# chain_path_1_t4 = run_qite(
#     chain_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_4,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=c_path_1)
# chain_path_1_t5 = run_qite(
#     chain_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_5,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=c_path_1)
# ring_path_1_t1 = run_qite(
#     ring_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_1,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=r_path_1)
# ring_path_1_t2 = run_qite(
#     ring_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_2,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=r_path_1)
# ring_path_1_t3 = run_qite(
#     ring_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_3,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=r_path_1)
# ring_path_1_t4 = run_qite(
#     ring_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_4,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=r_path_1)
# ring_path_1_t5 = run_qite(
#     ring_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_5,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=r_path_1)
sheet_path_1_t1 = run_qite(
    sheet_mol_1,
    beta=30.0,
    db=0.5,
    expansion_type='All',
    second_order=True,
    selected_pool=True,
    t_thresh=theta_1,
    conv_thresh=1.0e-5,
    physical_r = True,
    output_path=s_path_1)
# sheet_path_1_t2 = run_qite(
#     sheet_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_2,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=s_path_1)
# sheet_path_1_t3 = run_qite(
#     sheet_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_3,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=s_path_1)
# sheet_path_1_t4 = run_qite(
#     sheet_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_4,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=s_path_1)
# sheet_path_1_t5 = run_qite(
#     sheet_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_5,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=s_path_1)
# pyrmd_path_1_t1 = run_qite(
#     pyrmd_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_1,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=p_path_1)
# pyrmd_path_1_t2 = run_qite(
#     pyrmd_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_2,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=p_path_1)
# pyrmd_path_1_t3 = run_qite(
#     pyrmd_mol_1,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_3,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=p_path_1)
# chain_path_15_t1 = run_qite(
#     chain_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_1,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=c_path_15)
# chain_path_15_t2 = run_qite(
#     chain_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_2,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=c_path_15)
# chain_path_15_t3 = run_qite(
#     chain_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_3,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=c_path_15)
# chain_path_15_t4 = run_qite(
#     chain_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_4,
#     conv_thresh=1.0e-5,s
#     physical_r = True,
#     output_path=c_path_15)
# # chain_path_15_t5 = run_qite(
# #     chain_mol_15,
# #     beta=30.0,
# #     db=0.5,
# #     expansion_type='All',
# #     second_order=True,
# #     selected_pool=True,
# #     t_thresh=theta_5,
# #     conv_thresh=1.0e-5,
# #     physical_r = True,
# #     output_path=c_path_15)
# ring_path_15_t1 = run_qite(
#     ring_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_1,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=r_path_15)
# ring_path_15_t2 = run_qite(
#     ring_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_2,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=r_path_15)
# ring_path_15_t3 = run_qite(
#     ring_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_3,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=r_path_15)
# ring_path_15_t4 = run_qite(
#     ring_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_4,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=r_path_15)
# ring_path_15_t5 = run_qite(
#     ring_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_5,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=r_path_15)
# sheet_path_15_t1 = run_qite(
#     sheet_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_1,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=s_path_15)
# sheet_path_15_t2 = run_qite(
#     sheet_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_2,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=s_path_15)
# sheet_path_15_t3 = run_qite(
#     sheet_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_3,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=s_path_15)
# sheet_path_15_t4 = run_qite(
#     sheet_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_4,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=s_path_15)
# sheet_path_15_t5 = run_qite(
#     sheet_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_5,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=s_path_15)
# pyrmd_path_15_t1 = run_qite(
#     pyrmd_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_1,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=p_path_15)
# pyrmd_path_15_t2 = run_qite(
#     pyrmd_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_2,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=p_path_15)
# pyrmd_path_15_t3 = run_qite(
#     pyrmd_mol_15,
#     beta=30.0,
#     db=0.5,
#     expansion_type='All',
#     second_order=True,
#     selected_pool=True,
#     t_thresh=theta_3,
#     conv_thresh=1.0e-5,
#     physical_r = True,
#     output_path=p_path_15)
# print(chain_path_1_t1)
# print(chain_path_1_t2)
# print(chain_path_1_t3)

# print(ring_path_1_t1)
# print(ring_path_1_t2)
# print(ring_path_1_t3)

# print(sheet_path_1_t1)
# print(sheet_path_1_t2)
# print(sheet_path_1_t3)

# print(pyrmd_path_1_t1)
# print(pyrmd_path_1_t2)
# print(pyrmd_path_1_t3)

# print(chain_path_15_t1)
# print(chain_path_15_t2)
# print(chain_path_15_t3)

# print(ring_path_15_t1)
# print(ring_path_15_t2)
# print(ring_path_15_t3)

# print(sheet_path_15_t1)
# print(sheet_path_15_t2)
# print(sheet_path_15_t3)

# print(pyrmd_path_15_t1)
# print(pyrmd_path_15_t2)
# print(pyrmd_path_15_t3)