import qrcode
data ="@shaikhatifvlogs"
img = qrcode.make(data)
img.save("youtube_qr.png")
