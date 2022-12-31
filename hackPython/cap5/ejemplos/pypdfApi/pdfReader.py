from PyPDF2 import PdfFileReader
from PIL import Image
import os


class MyPdfReader:
    def __init__(self, file):
        self.file = file

    def print_info(self):
        ext = self.file.lower().rsplit(".", 1)[-1]
        if ext in ["pdf"]:
            print("[+] Metadata for file: {}".format(self.file))
            with open(self.file, "rb") as f:
                pdfFile = PdfFileReader(f)
                docInfo = pdfFile.getDocumentInfo()
                for metaItem in docInfo:
                    print("[+]" + metaItem + ":" + docInfo[metaItem])

    def extract_images(self, path):
        with open(self.file, "rb") as file:
            pdfFile = PdfFileReader(file)
            page0 = pdfFile.getPage(0)
            xObject = page0["/Resources"]["/XObject"].getObject()
            for obj in xObject:
                if xObject[obj]["/Subtype"] == "/Image":
                    size = (xObject[obj]["/Width"], xObject[obj]["/Height"])
                    data = xObject[obj].getData()
                    if xObject[obj]["/ColorSpace"] == "/DeviceRGB":
                        mode = "RGB"
                    else:
                        mode = "P"
                    if xObject[obj]["/Filter"] == "/FlateDecode":
                        img = Image.frombytes(mode, size, data)
                        img.save(os.path.join(path, obj[1:] + ".png"))
                    elif xObject[obj]["/Filter"] == "/DCTDecode":
                        with open(os.path.join(path, obj[1:] + ".jpg", "wb")) as img:
                            img.write(data)
                    elif xObject[obj]["/Filter"] == "/JPXDecode":
                        with open(os.path.join(path, obj[1:] + ".jp2", "wb")) as img:
                            img.write(data)
