import subprocess#方便的启用一个子进程，控制输入输出

print('$$$$$')
#r=subprocess.call(['nslookup','www.python.org'])
#print('exit',r)
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=p.communicate(b'set  q=mx\npython.org\nexit\n')#手动输入
print(output.decode('utf-8'))
print('exit',p.returncode)
