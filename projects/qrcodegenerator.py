import qrcode

data = input("Enter text/URL: ")
img = qrcode.make(data)
img.show()
img.save("qrcode.png")
