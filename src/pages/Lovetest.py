from appium.webdriver.common.mobileby import MobileBy


class MainLoveTest(object):
    def __init__(self):
        self.title_lbl = (MobileBy.ID, 'marcostudios.lovetest:id/imageView')
        self.yourName_txt = (MobileBy.ID, 'marcostudios.lovetest:id/name123')
        self.herName_txt = (MobileBy.ID, 'marcostudios.lovetest:id/name456')
        self.next_btn = (MobileBy.ID, 'marcostudios.lovetest:id/next')
