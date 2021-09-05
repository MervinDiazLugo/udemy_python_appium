from functions.Configuration import Configuration
from appium import webdriver
import pytest
import json


class Functions:

    def __init__(self):
        self.json_strings = {}
        self.device = {}
        self.desired_caps = {}
        self.driver = None

    def get_json_file(self, file, path=Configuration.devices_resources):
        json_path = path + "/" + file + '.json'
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                return self.json_strings
        except FileNotFoundError:
            pytest.skip(u"get_json_file: No se encontro el Archivo " + file)
            return False

    def get_device(self, entity):
        if self.json_strings is False:
            pytest.skip(u"Define el device para esta prueba " + entity)
        else:
            try:
                self.device = self.json_strings[entity]
                return self.device
            except KeyError:
                pytest.skip(u"get_device: No se encontro el device al cual se hace referencia: " + entity)

    def get_capabilities(self, test_device=Configuration.device):
        Functions.get_json_file(self, "Devices")
        self.desired_caps = Functions.get_device(self, test_device)
        self.desired_caps['app'] = Configuration.app
        return self.desired_caps

    def get_driver(self, capabilities, local_server=Configuration.local):
        self.driver = webdriver.Remote(local_server, capabilities)
        Functions.check_app_is_running(self)
        return self.driver

    def check_app_is_running(self):
        activity = self.driver.current_activity
        assert ".MainActivity" == activity, f"La Aplicacion {Configuration.app} no esta disponible"
