from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1
    
   


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):    
    agree_for_experiment = models.BooleanField(
        label='''
            
        ''',
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [True, 'نعم'],
            [False, 'لا']
        ]
    )
    monthlyIncome = models.IntegerField(
        label='''
        كم دخلك الشهري
        ''',
        min=0,  # Set the minimum value (change as needed)
        max=50000,  # Set the maximum value (change as needed)
        widget=widgets.TextInput,
    )
    traceMyIncomeAndExpenses = models.BooleanField(
        label='''
            أقوم بمتابعة وتسجيل دخلي ومصروفاتي
            ''',
        widget=widgets.CheckboxInput,
        initial=False,  # Set the default value to False
        blank=True, 
    )
    canPayMyBillsEasily = models.BooleanField(
        label='''
            أستطيع دفع فواتيري ومصاريفي الشهرية بسهولة
            ''',
        widget=widgets.CheckboxInput,
        initial=False,  # Set the default value to False
        blank=True, 
    )
    alreadyHaveFinancialGoals = models.BooleanField(
        label='''
           لدي أهداف مالية أطمح لتحقيقها
            ''',
        widget=widgets.CheckboxInput,
        initial=False,  # Set the default value to False
        blank=True, 
    )
    monthlyEssentialExpensesSum = models.IntegerField(
        label='''
        مجموع مصروفاتك الأساسية مثل )السكن، الأكل التعليم...(
        ''',
        min=0,  # Set the minimum value (change as needed)
        max=50000,  # Set the maximum value (change as needed)
        widget=widgets.TextInput,
        
    )
    monthlyLuxuryExpensesSum = models.IntegerField(
        label='''
        مجموع مصروفاتك الثانوية مثل )الترفيه، السفر، المطاعم ....(
        ''',
        min=0,  # Set the minimum value (change as needed)
        max=50000,  # Set the maximum value (change as needed)
        widget=widgets.TextInput,
    )
    monthlyDebtExpenses = models.IntegerField(
        label='''
        مجموع مصروفاتك الثانوية مثل )الترفيه، السفر، المطاعم ....(
        ''',
        min=0,  # Set the minimum value (change as needed)
        max=50000,  # Set the maximum value (change as needed)
        widget=widgets.TextInput,
    )
    monthlySaving = models.IntegerField(
        label='''
        كم من دخلك يذهب لسداد الديون كم ادخارك الشهري ؟
        ''',
        min=0,  # Set the minimum value (change as needed)
        max=50000,  # Set the maximum value (change as needed)
        widget=widgets.TextInput,
    )
    age = models.IntegerField(
        label='''
        كم عمرك ؟
        ''',
        min=0,  # Set the minimum value (change as needed)
        max=100,  # Set the maximum value (change as needed)
        widget=widgets.TextInput,
    )
    sex = models.StringField(
        choices=["ذكر", "انثى"],
        label="النوع",
        widget=widgets.RadioSelect,
    )
    marital_status = models.StringField(
        choices=["متزوج/رب أسرة", "مطلق", "أرمل", "أعزب"],
        label="الحالة الاجتماعية",
        widget=widgets.RadioSelect,
    )
    real_estate = models.StringField(
        choices=["نعم", "لا"],
        label="هل تملك عقارات؟",
        widget=widgets.RadioSelect,
    )
    have_freelance_certificate = models.StringField(
        choices=["نعم", "لا"],
        label="هل لديك شهادة عمل حر ؟",
        widget=widgets.RadioSelect,
    )
    have_productive_family = models.StringField(
        choices=["نعم", "لا"],
        label="هل لديك شهادة الأسر المنتجة؟",
        widget=widgets.RadioSelect,
    )
        


# FUNCTIONS
# PAGES

class Intro(Page):
    form_model = 'player'
    form_fields = ['agree_for_experiment']
    
    @staticmethod
    def is_displayed(player: Player):
        return True
    
    @staticmethod
    def vars_for_template(player: Player):
       return {
            'field_name': 'agree_for_experiment',
       }
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        print('values isssss')
        if not player.agree_for_experiment:
            player.participant.vars['dropout_fields'] = ['agree_for_experiment']
            player.participant.vars['dropout_page'] = 'Intro'
        
    
    # @staticmethod
    def error_message(player: Player, values):
        # print the values;
        print('values is', values)
        if not values['agree_for_experiment']:
            return 'يجب الموافقة على المشاركة في الدراسة للمتابعة'
        
    
            


class FinancialAnalysis(Page):
    form_model = 'player'
    form_fields = [ 'monthlyIncome', 'traceMyIncomeAndExpenses',
                   'canPayMyBillsEasily', 'alreadyHaveFinancialGoals',
                   'monthlyEssentialExpensesSum', 'monthlyLuxuryExpensesSum','monthlyDebtExpenses',  'monthlySaving'            
    ]
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        print('values isssss')
        # if not player.agree_for_experiment:
        #     player.participant.vars['dropout_fields'] = ['agree_for_experiment']
        #     player.participant.vars['dropout_page'] = 'Intro'
        
    
    @staticmethod
    def error_message(self, values):
        print('values is', values)
        if not values['monthlyIncome']:
            return 'Custom error message for my_field'
    
    
    @staticmethod
    def vars_for_template(player: Player):
        return{
            'step': 1,  # Adjust the step value as needed
            'monthlyIncome': 'monthlyIncome'
        }



class PersonalAnalysis(Page):
    form_model = 'player'
    form_fields = ['age', 'sex', 'marital_status', 'real_estate']
    
    @staticmethod
    def is_displayed(player: Player):
        return True
    
    @staticmethod
    def vars_for_template(player: Player):
       return {
            'step': 1,  # Adjust the step value as needed
       }
       
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        print('values isssss')
        if not player.age:
            player.participant.vars['dropout_fields'] = ['age']
            player.participant.vars['dropout_page'] = 'PersonalAnalysis'
            
    @staticmethod
    def error_message(player: Player, values):
        # print the values;
        print('values is', values)
        if not values['age']:
            return 'يجب تعبئة الحقل'
        
 
    
class Freelance(Page):
    form_model = 'player'
    form_fields = ['have_freelance_certificate']
    
    @staticmethod
    def is_displayed(player: Player):
        return True
    
   
       
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        pass
            
    @staticmethod
    def error_message(player: Player, values):
        # print the values;
        print('values is', values)
        if not values['have_freelance_certificate']:
            return 'يجب تعبئة الحقل'
        
    
    
class Productive_Family(Page):
    form_model = 'player'
    form_fields = ['have_productive_family']
    
    @staticmethod
    def is_displayed(player: Player):
        return True
    
   
       
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        pass
            
    @staticmethod
    def error_message(player: Player, values):
        # print the values;
        print('values is', values)
        if not values['have_productive_family']:
            return 'يجب تعبئة الحقل'
        
    

class Result(Page):
    pass


page_sequence = [Intro, FinancialAnalysis,  PersonalAnalysis ,Freelance,  Productive_Family, Result, ]
