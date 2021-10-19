matematik =51
turkce =51
kimya =51
fizik =51
biyoloji =51
tarih =51
toplam=(float(matematik)+float(turkce)+float(kimya)+float(fizik)+float(biyoloji)+float(tarih)*25)/30
print("Toplam :{0} ".format(toplam))
if(toplam<50):
	print("Sınıfta kaldınız");
else:
	print("Yaşasın sınıfı geçtin");
	if(toplam<75):
		print("Yaşasın sınıfı geçtin");
	else:
		print("Teşşekür Belgesi KAZANDIN");
		if(toplam<85):
			print("Teşşekür Belgesi KAZANDIN");
		else:
			print("Taktir Belgesi KAZANDIN");
