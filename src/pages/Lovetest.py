import random

from appium.webdriver.common.mobileby import MobileBy

from functions.Functions import Functions


# ELEMENTS NOMENCLATURE REFERENCE
# LABEL = LBL
# BUTTONS = BTN
# CHECK_BUTTON = CHK
# OPTION_BUTTON = OPT
# DROPDOWN = DPW

class LoveTest(object):
    # MAIN SET PLAYERS
    title_lbl = (MobileBy.ID, 'marcostudios.lovetest:id/imageView')
    yourName_txt = (MobileBy.ID, 'marcostudios.lovetest:id/name123')
    herName_txt = (MobileBy.ID, 'marcostudios.lovetest:id/name456')
    next_btn = (MobileBy.ID, 'marcostudios.lovetest:id/next')

    # ANSWER QUESTIONS
    questions_lbl = (MobileBy.ID, 'marcostudios.lovetest:id/question')
    answer_one_btn = (MobileBy.ID, 'marcostudios.lovetest:id/answerone')
    answer_two_btn = (MobileBy.ID, 'marcostudios.lovetest:id/answertwo')
    answer_three_btn = (MobileBy.ID, 'marcostudios.lovetest:id/answerthree')
    progress_lbl = (MobileBy.ID, 'marcostudios.lovetest:id/progress')

    def set_players(self, name1, name2):
        Functions.implicit_wait_visible(self, LoveTest.title_lbl)
        Functions.setText(self, LoveTest.yourName_txt, name1)
        Functions.setText(self, LoveTest.herName_txt, name2)
        Functions.click_element(self, LoveTest.next_btn)

    def set_answers(self, number):
        progress = 1
        for progress in range(number):
            Functions.implicit_wait_visible(self, LoveTest.questions_lbl)
            answers = [LoveTest.answer_one_btn,
                       LoveTest.answer_two_btn,
                       LoveTest.answer_three_btn]
            answer = random.choice(answers)
            Functions.click_element(self, answer)
            Functions.implicit_wait_visible(self, LoveTest.progress_lbl)
            #assert Functions.get_element_text(self, LoveTest.progress_lbl) == f"{str(progress)}/10", "This is not the step"
            ++progress

