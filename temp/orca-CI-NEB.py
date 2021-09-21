import os,shutil,sys
def orca_ci_neb(sys_id):
    os.chdir(sys_id+'/NEB/')
    ts = 'neb_NEB-HEI_converged.xyz'
    if os.path.exists(ts) == True:
        try:
            os.mkdir('ci-neb/')
        except:
            print('Could not make the NEB ci directory')
        os.chdir('ci-neb/')
        shutil.copy('../'+ts, './')
        shutil.copy('../start.xyz', './')
        shutil.copy('../neb_MEP.allxyz', './')
        inp = open('./input.inp', 'w+')
        inp.write('! B3LYP D3BJ def2-TZVP RIJCOSX \n'
                  '! NEB-CI \n'
                  '%pal nprocs 48 end \n'
                  '%base "neb-ci" \n'
                  '%neb Restart_ALLXYZFile "neb_MEP.allxyz" \n'
                  'TS "'+ts+'"\n'
                  'NImages 11 \n'
                  'Monitor_Internals { D 12 7 14 15 } end \n'
                  'end \n'
                  '* xyzfile 0 1 start.xyz \n')
        inp.close()
        os.system('python ~/subgen-2.py '+sys_id+'-ci-NEB 1 orca501 48 m.lea')
        os.system('sbatch submit.sh')
        os.chdir('../../..')
    else:
        print('Converged NEB not found, check your results!')
        print(os.getcwd())
        exit()
orca_ci_neb(sys.argv[1])