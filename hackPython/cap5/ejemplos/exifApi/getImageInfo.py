from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

class ImageInfo:

    def __init__(self, image_path):
        self.exifinfo = self.get_exif_metadata(image_path)
    
    
    def get_exif_metadata(self, image_path):
        ret = {}
        exifinfo = None
        image = Image.open(image_path)
        if hasattr(image, '_getexif'):
            exifinfo = image._getexif()
        return exifinfo


    def print_exif(self):
        if self.exifinfo is not None:
                for tag, value in self.exifinfo.items():
                    decoded = TAGS.get(tag, tag)
                    print(str(decoded) + "-->" + str(value))
                    
        else:
            print("There's no exifinfo")

    
    def decode_gps_info(self):
        gpsinfo = {}
        if 'GPSInfo' in self.exifinfo:
            for key in self.exifinfo['GPSInfo'].keys():
                decode = GPSTAGS.get(key, key)
                gpsinfo[decode] = self.exifinfo['GPSInfo'][key]
            self.exifinfo['GPSInfo'] = gpsinfo
            return self.exifinfo['GPSInfo']
        return None

    def get_lat_long(self):
        gpsinfo = {}
        if 'GPSInfo' in self.exifinfo:
            Nsec = self.exifinfo['GPSInfo'][2][2][0] / float(self.exifinfo['GPSInfo'][2][2][1])
            Nmin = self.exifinfo['GPSInfo'][2][1][0] / float(self.exifinfo['GPSInfo'][2][1][1])
            Ndeg = self.exifinfo['GPSInfo'][2][0][0] / float(self.exifinfo['GPSInfo'][2][0][1])
            Wsec = self.exifinfo['GPSInfo'][4][2][0] / float(self.exifinfo['GPSInfo'][4][2][1])
            Wmin = self.exifinfo['GPSInfo'][4][1][0] / float(self.exifinfo['GPSInfo'][4][1][1])
            Wdeg = self.exifinfo['GPSInfo'][4][0][0] / float(self.exifinfo['GPSInfo'][4][0][1])

            if self.exifinfo['GPSInfo'][1] == 'N':
                Nmult = 1
            else:
                Nmult = -1
            if self.exifinfo['GPSInfo'][1] == 'E':
                Wmult = 1
            else:
                Wmult = -1
            Lat = Nmult * (Ndeg + (Nmin + Nsec / 60.0) / 60.0)
            Lng = Wmult * (Wdeg + (Wmin + Wsec / 60.0) / 60.0)
            self.exifinfo['GPSInfo'] = {"Lat": Lat, "Lng": Lng}
            return self.exifinfo['GPSInfo']
        return None
    
