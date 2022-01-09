import subprocess

def running_commands():
	pro= subprocess.run('/home/pi/iot11/bt.sh')
	print(pro.returncode)
	if int(pro.returncode)==0:
		print("pass")
	else:
		print("fail")

running_commands()