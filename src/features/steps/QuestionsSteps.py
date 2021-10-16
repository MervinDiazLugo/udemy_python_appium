from behave import *
from functions.Functions import Functions
from pages.Lovetest import LoveTest
import time

use_step_matcher("re")

MainLoveTest = LoveTest()


@then("answer all questions in test")
def step_impl(context):
    LoveTest.set_answers(context, 10)


@then("I answer (.*) questions in test")
def step_impl(context, number):
    LoveTest.set_answers(context, number)
