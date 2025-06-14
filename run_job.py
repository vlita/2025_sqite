from qforte import QITE, QITE_OLD, QLANCZOS, UCCNVQE

def run_qite(
    sys, 
    computer_type='fci', 
    apply_ham_as_tensor=True, 
    ref=None, 
    state_prep_type='occupation_list', 
    trotter_order=1, 
    trotter_number=1, 
    fast=True, 
    verbose=False, 
    print_summary_file=True,
    
    beta=1.0,
    db=0.2,
    dt=0.01,
    use_diis=False,
    max_diis_size=False,
    use_exact_evolution=False,
    expansion_type='SD',
    evolve_dfham=False,
    random_state=False,
    sparseSb=False,
    low_memorySb=False,
    second_order=True,
    selected_pool=False,
    t_thresh=1.0e-6,
    cumulative_t=True,
    b_thresh=1.0e-6,
    x_thresh=1.0e-10,
    conv_thresh=1.0e-3,
    physical_r = True,
    use_df_ham_selection = False,
    folded_spectrum = False,
    BeH2_guess = False,
    e_shift = None,
    update_e_shift = True,
    do_lanczos=False,
    lanczos_gap=2,
    realistic_lanczos=True,
    fname=None,
    output_path=None,
    print_pool=False,
    use_cis_reference=False,
    target_root=0,
    cis_target_root=0,
    new=True):

    beta_list = []
    energy_list = []
    param_list = []
    cnot_list = []
    measure_list = []

    if(new):
        alg = QITE(system=sys,
                computer_type=computer_type, 
                apply_ham_as_tensor=apply_ham_as_tensor, 
                ref=ref, 
                state_prep_type=state_prep_type, 
                trotter_order=trotter_order, 
                trotter_number=trotter_number, 
                fast=fast, 
                verbose=verbose, 
                print_summary_file=print_summary_file)

        alg.run(beta=beta, 
                db=db,
                dt=dt,
                use_diis=use_diis,
                max_diis_size=max_diis_size,
                use_exact_evolution=use_exact_evolution,
                expansion_type=expansion_type,
                evolve_dfham=evolve_dfham,
                random_state=random_state,
                sparseSb=sparseSb, 
                low_memorySb=low_memorySb, 
                second_order=second_order,
                selected_pool=selected_pool,
                t_thresh=t_thresh,
                cumulative_t=cumulative_t,
                b_thresh=b_thresh, 
                x_thresh=x_thresh,
                conv_thresh=conv_thresh,
                physical_r=physical_r,
                use_df_ham_selection = use_df_ham_selection,
                folded_spectrum=folded_spectrum,
                BeH2_guess=BeH2_guess,
                e_shift=e_shift,
                update_e_shift=update_e_shift,
                do_lanczos=do_lanczos, 
                lanczos_gap=lanczos_gap,
                realistic_lanczos=realistic_lanczos, 
                fname=fname,
                output_path=output_path,
                print_pool=print_pool,
                use_cis_reference=use_cis_reference,
                target_root=target_root,
                cis_target_root=cis_target_root)

        if(use_exact_evolution):
            path = f'{output_path}qite_beta_{beta}_db_{db}_EXACT_EVOLUTION_summary.dat'
            # with open(f'{output_path}qite_beta_{beta}_db_{db}_EXACT_EVOLUTION_summary.dat', 'r') as file:
            #     for _ in range(2):
            #         next(file)

            #     for line in file:
            #         beta = line.split()[0]
            #         energy = line.split()[1]
            #         beta_list.append(beta)
            #         energy_list.append(energy)

            # return beta_list, energy_list
            return path

        else:
            path = f'{output_path}qite_{expansion_type}_selected_pool_{selected_pool}_t_{t_thresh}_dfham_{evolve_dfham}_summary.dat'
            # with open(f'{output_path}qite_beta_{beta}_db_{db}_{computer_type}_{expansion_type}_second_order_{second_order}_folded_spectrum_{folded_spectrum}_e_shift_{e_shift}_selected_pool_{selected_pool}_t_{t_thresh}_physical_r_{physical_r}_dfham_{evolve_dfham}_summary.dat', 'r') as file:
            #     for _ in range(2):
            #         next(file)

            #     for line in file:
            #         beta = line.split()[0]
            #         energy = line.split()[1]
            #         param = line.split()[2]
            #         cnot = line.split()[3]
            #         pauli = line.split()[4]
            #         beta_list.append(beta)
            #         energy_list.append(energy)
            #         param_list.append(param)
            #         cnot_list.append(cnot)
            #         measure_list.append(pauli)

            # return beta_list, energy_list, param_list, cnot_list, measure_list
            return path

    else:
        alg = QITE_OLD(system=sys,
                computer_type=computer_type, 
                apply_ham_as_tensor=apply_ham_as_tensor, 
                ref=ref, 
                state_prep_type=state_prep_type, 
                trotter_order=trotter_order, 
                trotter_number=trotter_number, 
                fast=fast, 
                verbose=verbose, 
                print_summary_file=print_summary_file)

        alg.run(beta=beta,
            db=db,
            expansion_type=expansion_type,
            sparseSb=sparseSb,
            b_thresh=b_thresh,
            x_thresh=x_thresh,
            do_lanczos=do_lanczos,
            lanczos_gap=lanczos_gap,
            output_path=output_path)

        path = f'{output_path}qite_beta_{beta}_db_{db}_{computer_type}_{expansion_type}_summary.dat'
        # with open(f'{output_path}qite_beta_{beta}_db_{db}_{computer_type}_{expansion_type}_summary.dat', 'r') as file:
        #         for _ in range(2):
        #             next(file)

        #         for line in file:
        #             beta = line.split()[0]
        #             energy = line.split()[1]
        #             param = line.split()[2]
        #             cnot = line.split()[3]
        #             pauli = line.split()[4]
        #             beta_list.append(beta)
        #             energy_list.append(energy)
        #             param_list.append(param)
        #             cnot_list.append(cnot)
        #             measure_list.append(pauli)

        # return beta_list, energy_list, param_list, cnot_list, measure_list
        return path

def run_qlanczos(sys, 
                 computer_type='fci', 
                 apply_ham_as_tensor=True, 
                 ref=None, 
                 state_prep_type='occupation_list', 
                 trotter_order=1, 
                 trotter_number=1, 
                 fast=True, 
                 verbose=False, 
                 print_summary_file=True,

                 target_root=0,
                 diagonalize_each_step=True,
                 beta=1.0,
                 db=0.2,
                 expansion_type='SD',
                 use_exact_evolution=False,
                 sparseSb=False,
                 low_memorySb=False,
                 second_order=True,
                 b_thresh=1.0e-6,
                 x_thresh=1.0e-10,
                 do_lanczos=True,
                 lanczos_gap=2,
                 realistic_lanczos=True,
                 fname=None):

    beta_list = []
    energy_list = []

    alg = QLANCZOS(system=sys,
                   computer_type=computer_type, 
                   apply_ham_as_tensor=apply_ham_as_tensor, 
                   ref=ref, 
                   state_prep_type=state_prep_type, 
                   trotter_order=trotter_order, 
                   trotter_number=trotter_number, 
                   fast=fast, 
                   verbose=verbose, 
                   print_summary_file=print_summary_file)

    alg.run(target_root=target_root,
            diagonalize_each_step=diagonalize_each_step,
            beta=beta,
            db=db,
            expansion_type=expansion_type,
            use_exact_evolution=use_exact_evolution,
            sparseSb=sparseSb,
            low_memorySb=low_memorySb,
            second_order=second_order,
            b_thresh=b_thresh,
            x_thresh=x_thresh,
            do_lanczos=do_lanczos,
            lanczos_gap=lanczos_gap,
            realistic_lanczos=realistic_lanczos,
            fname=fname)

    path = f'beta_{beta}_db_{db}_{computer_type}_{expansion_type}_second_order_{second_order}_realistic_{realistic_lanczos}_lanczos_summary.dat'
    # with open(f'beta_{beta}_db_{db}_{computer_type}_{expansion_type}_second_order_{second_order}_realistic_{realistic_lanczos}_lanczos_summary.dat', 'r') as file:
    #     for _ in range(2):
    #         next(file)

    #     for line in file:
    #         beta = line.split()[0]
    #         energy = line.split()[2]
    #         beta_list.append(beta)
    #         energy_list.append(energy)

    # return beta_list, energy_list
    return path

def run_vqe(sys, 
            computer_type = 'fci',
            opt_thresh=1.0e-3, 
            pool_type='SD',
            optimizer='BFGS',
            output_path=None):

    alg = UCCNVQE(system=sys,
                  computer_type=computer_type)

    alg.run(opt_thresh=opt_thresh, 
            pool_type=pool_type,
            optimizer=optimizer,
            output_path=output_path)

    path = f'{output_path}vqe_summary.dat'
   
    return path

def run_spqe(sys, 
             computer_type = 'fci',
             opt_thresh=1.0e-3,
             spqe_maxiter=1,
             output_path=None):

    alg = UCCNVQE(system=sys,
                  computer_type=computer_type)

    alg.run(opt_thresh=opt_thresh, 
            spqe_maxiter=spqe_maxiter,
            output_path=output_path)

    path = f'{output_path}spqe_summary.dat'
   
    return path