import os,shutil
for i in ["%1d" % i for i in range(1,7)]:
    os.mkdir(i+'/NEB')
    os.chdir(i+'/NEB')
    shutil.copy(i+'/trans/optimized.xyz', './start.xyz')   
    shutil.copy(i+'/cis/optimized.xyz', './end.xyz')
    inp = open(i+'/NEB/input.inp', 'w+')
    inp.write('! B3LYP D3BJ def2-TZVP RIJCOSX \n'
              '! NEB \n'
              '%pal nprocs 48 end \n'
              '%base "neb" \n'
              '%neb NEB_END_XYZFile "end.xyz" \n'
              'NImages 11 \n'
              'Monitor_Internals { D 12 7 14 15 } end \n'
              'end \n'
              '* xyzfile 0 1 start.xyz')
    inp.close()
    os.system('python ~/subgen-2.py '+i+'-neb 1 orca501 48 m.lea')
    os.system('sbatch submit.sh')
    os.chdir('../..')