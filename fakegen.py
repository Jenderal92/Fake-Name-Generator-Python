import requests,re,random,sys,time
from colorama import Fore

def Banner():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]

    x = '''
    _____  
^..^     \9
(oo)_____/ 
   WW  WW
Fake Name Generator | Python Code
               
'''
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.02)
Banner()

country = raw_input('COUNTRY : ')
def Xixi():
	try:
		response = requests.get('https://www.fakexy.com/fake-name-generator-'+country).content
		if 'Matched address generator' in response:
			new = re.findall('<td>(.*?)</td>', response)
			print('\n--------------- CODED BY SHIN CODE --------------- \n')
			print(new[0] +Fore.GREEN+  ': ' + new[1] +Fore.WHITE)
			print(new[2] +Fore.GREEN+  ': ' + new[3] +Fore.WHITE)
			print(new[4] +Fore.GREEN+  ': ' + new[5] +Fore.WHITE)
			print(new[6] +Fore.GREEN+  ': ' + new[7] +Fore.WHITE)
			print(new[8] +Fore.GREEN+  ': ' + new[9] +Fore.WHITE)
			print(new[10] +Fore.GREEN+  ': ' + new[11] +Fore.WHITE)
			print(new[12] +Fore.GREEN+  ': ' + new[13] +Fore.WHITE)
			print(new[14] +Fore.GREEN+  ': ' + new[15] +Fore.WHITE)
			print(new[16] +Fore.GREEN+  ': ' + new[17] +Fore.WHITE)
			print(new[18] +Fore.GREEN+  ': ' + new[19] +Fore.WHITE)
			print(new[20] +Fore.GREEN+  ': ' + new[21] +Fore.WHITE)
			print(new[22] +Fore.GREEN+  ': ' + new[23] +Fore.WHITE)
			print(new[24] +Fore.GREEN+  ': ' + new[25] +Fore.WHITE)
			print(new[26] +Fore.GREEN+  ': ' + new[27] +Fore.WHITE)
			print(new[28] +Fore.GREEN+  ': ' + new[29] +Fore.WHITE)
			print(new[30] +Fore.GREEN+  ': ' + new[31] +Fore.WHITE)
			print('\n--------------- CODED BY SHIN CODE --------------- \n')
	except : pass
Xixi()