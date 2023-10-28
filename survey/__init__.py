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
    bank_branch = models.StringField(
         choices=["بنك التنمية الاجتماعية بمكة المكرمة","بنك التنمية الاجتماعية بالمدينة المنورة", "بنك التنمية الاجتماعية بالرياض",
    "بنك التنمية الاجتماعية بالدمام",
    "بنك التنمية الاجتماعية بالأحساء",
    "بنك التنمية الاجتماعية بحفر الباطن",
    "بنك التنمية الاجتماعية بعرعر",
    "بنك التنمية الاجتماعية بالقريات",
    "بنك التنمية الاجتماعية بالجوف",
    "بنك التنمية الاجتماعية بتبوك",
    "بنك التنمية الاجتماعية بحائل",
    "بنك التنمية الاجتماعية بالقصيم",
    "بنك التنمية الاجتماعية بالدوادمي",
    "بنك التنمية الاجتماعية بينبع",
    "بنك التنمية الاجتماعية بجدة",
    "بنك التنمية الاجتماعية بالطائف",
    "بنك التنمية الاجتماعية بالباحة",
    "بنك التنمية الاجتماعية بنجران",
    "بنك التنمية الاجتماعية بجازان",
    "بنك التنمية الاجتماعية بالقنفذة",
    "بنك التنمية الاجتماعية بوادي الدواسر",
    "بنك التنمية الاجتماعية ببيشة ",
    "بنك التنمية الاجتماعية بخميس مشيط "],
        label=" فرع البنك",
        widget=widgets.RadioSelect,
    )
    request_reason = models.StringField(
        choices=["التأثيث", "الصيانة", "أخرى"],
        label="السبب",
        widget=widgets.RadioSelect,
    )
    does_have_home_worker = models.BooleanField(
        label='''
            
        ''',
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [True, 'نعم'],
            [False, 'لا']
        ]
    )
    count_of_all_family_members = models.IntegerField(
         max=100,  # Set the maximum value (change as needed)
        widget=widgets.TextInput,
    )
    count_of_children = models.IntegerField(
        max=100,  # Set the maximum value (change as needed)
        widget=widgets.TextInput,
    )
    city = models.StringField(
        label='''
        المدينة
        ''',
        widget=widgets.TextInput,
    )
    district = models.StringField(
        label='''
        الحي
        ''',
        widget=widgets.TextInput,
    )
    job = models.StringField(
        choices=["موظف حكومي مدني", "موظف حكومي عسكري", "موظف قطاع خاص", "عمل حر", "طالب", "متقاعد"],
         widget=widgets.RadioSelect,
    )
    job_sector = models.StringField(
        choices=["قطاع حكومي", "قطاع خاص", "أخرى"],
            widget=widgets.RadioSelect,
    )
    job_number = models.IntegerField(
        label='''
        الرقم الوظيفي
        ''',
        widget=widgets.TextInput,
    )
    job_title = models.StringField(
        label='''
        المسمى الوظيفي
        ''',
        widget=widgets.TextInput,
    )
    monthly_installment_amount = models.StringField(
        choices=["500", "600", "700", "800", "900", "1000", "1100", "1200", "1300", "1400", "1500",],
        widget=widgets.RadioSelect,
        default="500",
    )
    register_in_zood = models.BooleanField(
        label='''
           لدي أهداف مالية أطمح لتحقيقها
            ''',
        widget=widgets.CheckboxInput,
        initial=False,  # Set the default value to False
        blank=True, 
    )
    bank_for_zood = models.BooleanField(
        widget=widgets.RadioSelectHorizontal,
        choices=['بنك العربي', 'مصرف الإنماء', 'بنك الجزيرة'
        ],
        blank=True
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
        
        
class FinancialRequest(Page):
     form_model = 'player'
     form_fields = ['bank_branch', 'request_reason', 'does_have_home_worker', 'count_of_all_family_members', 'count_of_children', 'city', 'district', 'job', 'job_sector', 'job_number', 'job_title']
     
     @staticmethod
     def vars_for_template(player: Player):
       return {
            'player_number': player.id_in_group,
       }
       

class PaymentAmount(Page):
    form_model = 'player'
    form_fields = ['monthly_installment_amount']
    
   
    

class Zood(Page):
    form_model = 'player'
    form_fields = ['register_in_zood', 'bank_for_zood']
    
    @staticmethod
    def vars_for_template(player: Player):
       income = 10000
       if player.monthlyIncome is not None:
           income = player.monthlyIncome
           
       award9 = income * 0.09
       award11 = income * 0.11
       award_default = 15000
       user_group = 1
    #    check player id_number
    # we want to devide the plyaes in 3 groups
    # and show them 3 different awards
       award = award9
       if player.id_in_group % 3 == 0:
           award = award9
           user_group = 1
       elif player.id_in_group % 3 == 1:
            award = award11
            user_group = 2
       else:
            award = award_default
            user_group = 3
              
       return {
             'award': int(award),
             'user_group': user_group,
       }   

class Result(Page):
    pass


page_sequence = [ Intro, FinancialAnalysis,  PersonalAnalysis ,Freelance,  Productive_Family,  FinancialRequest, PaymentAmount,Zood, Result, ]
