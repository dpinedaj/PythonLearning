import subprocess

#subprocess.Popen('dir', shell=True)




"""p1 = subprocess.Popen('dir', shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p2 = subprocess.Popen('sort /R', shell=True, stdin=p1.stdout)

p1.stdout.close()
out, err = p2.communicate() """

"""with open('out.txt','a') as f:
    p = subprocess.Popen('dir',shell=True, stdout = f)"""

file = open('out.txt','a')
p1 = subprocess.Popen('dir', shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p2 = subprocess.Popen('sort /R', shell=True, stdin = p1.stdout, stdout = file)

p1.stdout.close()
file.close()

