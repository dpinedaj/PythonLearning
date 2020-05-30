import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from getImageInfo import ImageInfo

imginfo = ImageInfo('../Imagen.jpg')
print(imginfo.decode_gps_info())