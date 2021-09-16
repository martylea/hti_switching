import os,shutil
for i in ["%1d" % i for i in range(1,7)]:
    os.mkdir(i+'/NEB/ts-opt/')
    os.chdir(i+'/NEB/ts-opt/')
    shutil.copy('../neb_NEB-HEI_converged.xyz', './ts.xyz')   
    inp = open('./input.inp', 'w+')
    inp.write('! B3LYP D3BJ def2-TZVP RIJCOSX \n'
              '! OptTS \n'
              '%pal nprocs 48 end \n'
              '%base "tsopt" \n'
              '* xyzfile 0 1 ts.xyz \n')
    inp.close()
    os.system('python ~/subgen-2.py '+i+'-ts 1 orca501 48 m.lea')
    os.system('sbatch submit.sh')
    os.chdir('../../../')