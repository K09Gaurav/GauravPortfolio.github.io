import qrcode

img = qrcode.make("https://k09gaurav.github.io/GauravPortfolio.github.io")
img.save('qr.png','PNG')