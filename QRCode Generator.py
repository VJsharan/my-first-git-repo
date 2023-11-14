import qrcode as qr
url = input("PASTE any URL(for which you want the QRCODE of): ")
#url="https://www.youtube.com/watch?v=vmWNRYbc6po&pp=ygUDYTJk"
pic=qr.make(url)
pic.save("SHARANQR.png")
