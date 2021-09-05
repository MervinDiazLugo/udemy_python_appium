from behave import *
from functions.Functions import Functions
use_step_matcher("re")


@given("Start application in default device")
def step_impl(context):
    """
    :param device: is device that you will run the test
    :type context: behave.runner.Context
    """
    desired_caps = Functions.get_capabilities(context)
    Functions.get_driver(context, capabilities=desired_caps)


@given('Application start with device (.*)')
def step_impl(context, device):
    """
    :param device: is device that you will run the test
    :type context: behave.runner.Context
    """
    desired_caps = Functions.get_capabilities(context, test_device=device)
    Functions.get_driver(context, capabilities=desired_caps)
