import subprocess


# file=open('module.txt','r').read()

# module=file.splitlines()
# print(module)

# for i in module:
#     subprocess.run('pip install {}'.format(i))

# subprocess.run('pip install pyaudio',shell=True)
# p1=subprocess.run(['dir'],shell=True,capture_output=True,text=True)

# p1=subprocess.run(['dir'],shell=True,stdout=subprocess.PIPE)



# with open('output.txt','w') as f:
#     p1=subprocess.run(['dir'],shell=True,stdout=f,text=True)

# print(p1.stdout)
# p2=subprocess.run(['pip install OkHound'],shell=True,capture_output=True,text=True,check=True)

p1=subprocess.run(['type','test.txt'],capture_output=True,shell=True,text=True)


p2=subprocess.run(['findstr','test','test.txt'],capture_output=True,shell=True,text=True,input=p1.stdout)

# print(p1.returncode)
print(p2.stdout)

# print(p1.args)
# print(p1.returncode)
# print(p1.stdout.decode())