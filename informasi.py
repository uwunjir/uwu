import requests as req,re,json,os
uid=None
username=None
class info:
	def __init__(self,kuki):
		self.kuki=kuki
	def myinfo(self):
		global uid,username
		try:
			kontol=req.get("https://mbasic.facebook.com/profile.php?v=info",cookies=self.kuki).text
		except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
			exit("[!] Kesalahan Pada Koneksi")
		if "Facebook - Masuk atau Daftar" in kontol or "Masuk ke Facebook" in kontol or "Epsilon" in kontol:
			os.remove("cookie");exit("[!] Cookies Kedaluwarsa, Harap Login Ulang")
		else:
			try:uid=re.findall("/(\d*)/allactivity",kontol)[0]
			except:pass
			nama=re.findall("\<title\>(.*?)<\/title\>",kontol)[0]
			try:username=re.findall('> . <a href="\/(.*?)\/friends',kontol)[0]
			except:pass
			open("my_info","w").write(json.dumps({"uid":uid,"nama":nama,"username":username}))