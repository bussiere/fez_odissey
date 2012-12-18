import pyexiv2
metadata = pyexiv2.ImageMetadata('_00.jpg')
metadata.read()
"""

>>> metadata.exif_keys
['Exif.Image.ImageDescription',
 'Exif.Image.XResolution',
 'Exif.Image.YResolution',
 'Exif.Image.ResolutionUnit',
 'Exif.Image.Software',
 'Exif.Image.DateTime',
 'Exif.Image.Artist',
 'Exif.Image.Copyright',
 'Exif.Image.ExifTag',
 'Exif.Photo.Flash',
 'Exif.Photo.PixelXDimension',
 'Exif.Photo.PixelYDimension']

>>> key = 'Exif.Photo.UserComment'
>>> value = 'This is a useful comment.'
>>> metadata[key] = pyexiv2.ExifTag(key, value)


metadata.iptc_keys
['Iptc.Application2.Caption',
 'Iptc.Application2.Writer',
 'Iptc.Application2.Byline',
 'Iptc.Application2.ObjectName',
 'Iptc.Application2.DateCreated',
 'Iptc.Application2.City',
 'Iptc.Application2.ProvinceState',
 'Iptc.Application2.CountryName',
 'Iptc.Application2.Category',
 'Iptc.Application2.Keywords',
 'Iptc.Application2.Copyright']

>>> key = 'Iptc.Application2.Contact'
>>> values = ['John', 'Paul', 'Ringo', 'George']
>>> metadata[key] = pyexiv2.IptcTag(key, values)

> metadata.xmp_keys
['Xmp.dc.creator',
 'Xmp.dc.description',
 'Xmp.dc.rights',
 'Xmp.dc.source',
 'Xmp.dc.subject',
 'Xmp.dc.title',
 'Xmp.xmp.CreateDate',
 'Xmp.xmp.ModifyDate']
 
 new tag
 
 >>> key = 'Xmp.xmp.Label'
>>> value = 'A beautiful picture.'
>>> metadata[key] = pyexiv2.XmpTag(key, value)

"""


#key = 'Exif.Photo.UserComment'
#value = 'This is a useful comment.'
#metadata[key] = pyexiv2.ExifTag(key, value)
#metadata['Exif.Image.Artist'] = "Bussiere"
#metadata['Exif.Image.ImageDescription'] = "Bussiere"
#metadata.write()