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
p_path_1 = f'{path}/h10/ang_10/pyramid/'

c_path_15 = f'{path}/h10/ang_15/chain/'
r_path_15 = f'{path}/h10/ang_15/ring/'
s_path_15 = f'{path}/h10/ang_15/sheet/'
p_path_15 = f'{path}/h10/ang_15/pyramid/'
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
# chain_path_1 = run_qite(
#     chain_mol_1,
#     beta=30.0,
#     db=0.1,
#     expansion_type='SD',
#     low_memorySb=False,
#     second_order=True,
#     conv_thresh=1.0e-3,
#     output_path=c_path_1)
ring_path_1 = run_qite(
    ring_mol_1,
    beta=30.0,
    db=0.1,
    expansion_type='SD',
    low_memorySb=False,
    second_order=True,
    conv_thresh=1.0e-3,
    output_path=r_path_1)
sheet_path_1 = run_qite(
    sheet_mol_1,
    beta=30.0,
    db=0.1,
    expansion_type='SD',
    low_memorySb=False,
    second_order=True,
    conv_thresh=1.0e-3,
    output_path=s_path_1)
# pyrmd_path_1 = run_qite(
#     pyrmd_mol_1,
#     beta=20.0,
#     db=0.1,
#     expansion_type='SD',
#     low_memorySb=False,
#     second_order=True,
#     conv_thresh=1.0e-3,
#     output_path=p_path_1)
chain_path_15 = run_qite(
    chain_mol_15,
    beta=30.0,
    db=0.1,
    expansion_type='SD',
    low_memorySb=False,
    second_order=True,
    conv_thresh=1.0e-3,
    output_path=c_path_15)
ring_path_15 = run_qite(
    ring_mol_15,
    beta=30.0,
    db=0.1,
    expansion_type='SD',
    low_memorySb=False,
    second_order=True,
    conv_thresh=1.0e-3,
    output_path=r_path_15)
sheet_path_15 = run_qite(
    sheet_mol_15,
    beta=30.0,
    db=0.1,
    expansion_type='SD',
    low_memorySb=False,
    second_order=True,
    conv_thresh=1.0e-3,
    output_path=s_path_15)
# pyrmd_path_15 = run_qite(
#     pyrmd_mol_15,
#     beta=20.0,
#     db=0.1,
#     expansion_type='SD',
#     low_memorySb=False,
#     second_order=True,
#     conv_thresh=1.0e-3,
#     output_path=p_path_15)
# print(chain_path_1)
print(ring_path_1)
print(sheet_path_1)
# print(pyrmd_path_1)

print(chain_path_15)
print(ring_path_15)
print(sheet_path_15)
# print(pyrmd_path_15)