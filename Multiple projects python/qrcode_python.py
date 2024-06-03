# QR Code Generator in python
import qrcode as qr

img = qr.make("https://github.com/AgentAhmed")
img.save("ahmed_github.png")
