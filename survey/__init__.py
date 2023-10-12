from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    income = models.IntegerField(
        label='''
        كم دخلك الشهري
        '''
    )
    track_income = models.BooleanField(
        label='''
            أقوم بمتابعة وتسجيل دخلي ومصروفاتي
            '''
    )
    pay_bill = models.BooleanField(
        label='''
            أستطيع دفع فواتيري ومصاريفي الشهرية بسهولة
            '''
    )
    have_goal = models.BooleanField(
        label='''
           لدي أهداف مالية أطمح لتحقيقها
            '''
    )
    total_main_expenses = models.IntegerField(
        label='''
        مجموع مصروفاتك الأساسية مثل )السكن، الأكل التعليم...(
        '''
    )
    total_not_main_expenses = models.IntegerField(
        label='''
        مجموع مصروفاتك الثانوية مثل )الترفيه، السفر، المطاعم ....(
        '''
    )
    debt_monthly = models.IntegerField(
        label='''
        مجموع مصروفاتك الثانوية مثل )الترفيه، السفر، المطاعم ....(
        '''
    )
    saving_monthly = models.IntegerField(
        label='''
        كم من دخلك يذهب لسداد الديون كم ادخارك الشهري ؟
        '''
    )


# FUNCTIONS
# PAGES

class Intro(Page):
    form_model = 'player'
    form_fields = ['income', 'track_income', 'pay_bill',
                   'have_goal',
                   'total_main_expenses',
                   'total_not_main_expenses', 'debt_monthly',
                   'saving_monthly' ]




page_sequence = [Intro]
