import os, glob

strings_plus = []
for p in glob.glob('*.py'):
    size = os.stat(p).st_size
    strings_plus.append(p + "\t" + str(size))

strings_format = ['{0}\t{1}'.format(p, str(os.stat(p).st_size)) for p in glob.glob('*.py')]
