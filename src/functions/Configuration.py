import os


class Configuration:
    Environment = 'Local'

    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    devices_resources = basedir + u"/resources/devices/"

    if Environment == 'Local':
        app = basedir + u'/resources/binaries/apkpureL.com.apk'
        device = "Pixel"
        port = 4723
        local = f"http://127.0.0.1:{port}/wd/hub"

    if Environment == 'Test':
        app = basedir + u'/resources/binaries/apkpureT.com.apk'
        device = "Pixel2"
        port = 5001
        local = f"http://127.0.0.1:{port}/wd/hub"
