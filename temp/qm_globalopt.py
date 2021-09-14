import os,shutil
for i in ["%1d" % i for i in range(1,7)]:
    os.mkdir(i)
    for j in ['cis', 'trans']:    
        os.mkdir(i+'/'+j)
        shutil.copy('geometries/'+i+'-'+j+'.xyz', i+'/'+j+'/startgeom.xyz')
        inp = open(i+'/'+j+'/input.inp', 'w+')
        inp.write('! B3LYP D3BJ def2-TZVP RIJCOSX \n'
                  '! Opt \n'
                  '%pal nprocs 48 end \n'
                  '%geom Constraints { C 12 C } end end \n'
                  '%base "optimized" \n'
                  '* xyzfile 0 1 startgeom.xyz \n')
        inp.close()
        os.chdir(i+'/'+j)
        os.system('python ~/subgen-2.py '+i+j+'opt 1 orca501 4 m.lea')
        os.system('sbatch submit.sh')
        os.chdir('../..')
        
    