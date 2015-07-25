import os
import platform
from envhelper import *

def AddVariables(vars):
    latex = FindToolPath('latex')
    pplatex = FindToolPath('pplatex')

    vars.Add('LATEX_PATH', 'Path to the latex binary tools.', latex)
    vars.Add('PPLATEX','Path to the pplatex binaries, or "auto" to use pplatex only if found in the current path.', pplatex)

def SetupEnv(env):
    
    latex = env['LATEX_PATH']
    if latex is not None:
	env.PrependENVPath('PATH', latex)
	env.Tool('tex')
	env.Tool('gs')
	env.Tool('latex')
	env.Tool('dvipdf')
	env.Tool('dvips')
	env.Tool('pdflatex')
	env.Tool('pdftex')

    pplatex = env.get('PPLATEX',None)

    if pplatex is None or pplatex == '':
	return

    # TODO if latex tools are in a non-standard path, add -c <exe> -- to arguments, provide option to set latex path

    if pplatex == "auto":
	if env.Detect(['pplatex','ppdflatex']):
	    env['LATEX'] = 'pplatex'
	    env['PDFLATEX'] = 'ppdflatex'

    else:
	env['LATEX'] = os.path.join(pplatex,'pplatex')
	env['PDFLATEX'] = os.path.join(pplatex,'ppdflatex')
