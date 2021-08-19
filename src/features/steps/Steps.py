from behave import *
from functions.Functions import Functions


@given("Start application in default device")
def step_impl(context):
    Functions.get_driver(context)

