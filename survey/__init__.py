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
        widget=widgets.TextInput,
        
    )
    monthlyLuxuryExpensesSum = models.IntegerField(
        label='''
        مجموع مصروفاتك الثانوية مثل )الترفيه، السفر، المطاعم ....(
        ''',
        min=0,  # Set the minimum value (change as needed)
        widget=widgets.TextInput,
    )
    monthlyDebtExpenses = models.IntegerField(
        label='''
        مجموع مصروفاتك الثانوية مثل )الترفيه، السفر، المطاعم ....(
        ''',
        min=0,  # Set the minimum value (change as needed)
        widget=widgets.TextInput,
    )
    monthlySaving = models.IntegerField(
        label='''
        كم من دخلك يذهب لسداد الديون كم ادخارك الشهري ؟
        ''',
        min=0,  # Set the minimum value (change as needed)
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
        choices=["1", "0"],
        label="النوع",
        widget=widgets.RadioSelect,
    )
    marital_status = models.StringField(
        choices=["1", "2", "3", "4",],
        label="الحالة الاجتماعية",
        widget=widgets.RadioSelect,
    )
    real_estate = models.StringField(
        choices=["1", "0"],
        label="هل تملك عقارات؟",
        widget=widgets.RadioSelect,
    )
    have_freelance_certificate = models.StringField(
        choices=["1", "0"],
        label="هل لديك شهادة عمل حر ؟",
        widget=widgets.RadioSelect,
    )
    have_productive_family = models.StringField(
        choices=["1", "0"],
        label="هل لديك شهادة الأسر المنتجة؟",
        widget=widgets.RadioSelect,
    )
    bank_branch = models.StringField(
         choices=["1", "2", "3", "4","5", "6", "7", "8", "9", "10", "11", "12", "13", "14" "15", "16", "17", "18", "19", "20", "21", "22", "23"],
        label=" فرع البنك",
        widget=widgets.RadioSelect,
    )
    loan_type = models.StringField(
         choices=["1", "2", "3", "4",],
        label=" نوع القرض ",
        widget=widgets.RadioSelect,
    )
    request_reason = models.StringField(
        label='''
       السبب
        ''',
        widget=widgets.TextInput,
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
    # city = models.StringField(
    #     label='''
    #     المدينة
    #     ''',
    #     widget=widgets.TextInput,
    # )
    # district = models.StringField(
    #     label='''
    #     الحي
    #     ''',
    #     widget=widgets.TextInput,
    # )
    job = models.StringField(
        choices=["1", "2", "3", "4", "5", "6"],
         widget=widgets.RadioSelect,
    )
    # job_sector = models.StringField(
    #     choices=["1", "2", "3"],
    #         widget=widgets.RadioSelect,
    # )
    # job_number = models.IntegerField(
    #     label='''
    #     الرقم الوظيفي
    #     ''',
    #     widget=widgets.TextInput,
    # )
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
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [True, 'نعم'],
            [False, 'لا']
        ],
        initial=False,  # Set the default value to False
        blank=True, 
        default=False,
    )
    type_of_zood = models.StringField(
        choices=["0", "0.09", "0.07",],
        label="نوع الزود",
        widget=widgets.RadioSelectHorizontal,
        default="0",
        blank=True,
        
    )
    bank_for_zood = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=['0', '1','2','3'],
        blank=True,
        default='0',
        initial='0',
    )
    user_group = models.IntegerField()
    endorsement = models.BooleanField(
        label='''
            
        ''',
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [True, 'نعم'],
            [False, 'لا']
        ],
        blank=True,
        default=False,
        
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
        if player.id_in_group % 3 == 0:
           player.user_group = 1 # controled => bank defaul => 15,000
        elif player.id_in_group % 3 == 1:
            player.user_group = 2 # three choices not images;
        else:
            player.user_group = 3 # with images
            
            
        if not player.agree_for_experiment:
            player.participant.vars['dropout_fields'] = ['agree_for_experiment']
            player.participant.vars['dropout_page'] = 'Intro'
        
    
    # @staticmethod
    def error_message(player: Player, values):
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
        month_income = player.monthlyIncome
        if month_income is None or month_income > 20000:
            return False
        
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
        month_income = player.monthlyIncome
        if month_income is None or month_income > 20000:
            return False
        
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
        month_income = player.monthlyIncome
        if month_income is None or month_income > 20000:
            return False
        
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
     form_fields = ['bank_branch', "loan_type" ,'request_reason', 'does_have_home_worker', 'count_of_all_family_members', 'count_of_children', 'job',  'job_title']
     
     @staticmethod
     def is_displayed(player: Player):
        month_income = player.monthlyIncome
        if month_income is None or month_income > 20000:
            return False
        
        return True
    
     @staticmethod
     def before_next_page(player: Player, timeout_happened):
        print('values isssss', player)
        pass
     
     @staticmethod
     def vars_for_template(player: Player):
       return {
            'player_number': player.id_in_group,
       }
       

class PaymentAmount(Page):
    form_model = 'player'
    form_fields = ['monthly_installment_amount']
    
    @staticmethod
    def is_displayed(player: Player):
        month_income = player.monthlyIncome
        if month_income is None or month_income > 20000:
            return False
        
        return True
    
   
    




class Group1(Page):
     form_model = 'player'
     form_fields = ['register_in_zood', 'endorsement', 'bank_for_zood' ]
     
     @staticmethod
     def is_displayed(player: Player):
        month_income = player.monthlyIncome
        if month_income is None or month_income > 20000:
            return False
        
        if player.user_group != 1:
            return False
        
        return True
     
     @staticmethod
     def vars_for_template(player: Player):
         award_default = 15000
         return {
             'award_default': '{:,}'.format(award_default),
         }
        
     @staticmethod
     def before_next_page(player: Player, timeout_happened):
         if not player.endorsement and player.register_in_zood:
            player.participant.vars['dropout_fields'] = ['endorsement']
            player.participant.vars['dropout_page'] = 'Group1'
        
    
     # @staticmethod
     def error_message(player: Player, values):
         print('error_message is==>', values['register_in_zood'])
         if not values['endorsement'] and values['register_in_zood']:
            return 'يجب الموافقة على الإقرار  قبل المتابعة'
     
     


class Group2(Page):
     form_model = 'player'
     form_fields = ['register_in_zood', 'endorsement', 'bank_for_zood', 'type_of_zood' ]
     
     
     @staticmethod
     def is_displayed(player: Player):
        month_income = player.monthlyIncome
        if month_income is None or month_income > 20000:
            return False
        
        if player.user_group != 2:
            return False
        
        return True
    
    
     @staticmethod
     def vars_for_template(player: Player):
          if player.monthlyIncome is not None:
                income = player.monthlyIncome
               
     
          award09 = income * 0.09 
          if award09 > 1000:
                award09 = 1000
                
          award07 = income * 0.07 
          if award07 > 1000:
                award07 = 1000
                
        
          award09Total = award09 * 60
          award07Total = award07 * 60
          
          bounce_09 = award09 * 0.2
          if bounce_09 > 200:
              bounce_09 = 200 
          
          bounce_07 = award07 * 0.2 
          if bounce_07 > 200:
                bounce_07 = 200
                
          totalBounce_09 = bounce_09 * 60
          totalBounce_07 = bounce_07 * 60
          
          totalBounce_09 = totalBounce_09 + 3000
          totalBounce_07 = totalBounce_07 + 3000
          return {
             'award09': '{:,}'.format(int(award09)),
             'award07': '{:,}'.format(int(award07)),
             'award09Total': '{:,}'.format(int(award09Total)),
             'award07Total': '{:,}'.format(int(award07Total)),
             'bounce_09': '{:,}'.format(int(totalBounce_09)),
             'bounce_07': '{:,}'.format(int(totalBounce_07)),
                
          }
        
     @staticmethod
     def before_next_page(player: Player, timeout_happened):
         print("group 2 befor register in zood", player.register_in_zood)
         must_aggree = False
         if player.type_of_zood == "0.09":
             player.register_in_zood = True
             must_aggree = True
             
         if player.type_of_zood == "0.07":
             player.register_in_zood = True  
             must_aggree = True
             
         if player.type_of_zood == "0":
             player.register_in_zood = False
             must_aggree = False
             
         if not player.endorsement and must_aggree:
            player.participant.vars['dropout_fields'] = ['endorsement']
            player.participant.vars['dropout_page'] = 'Group2'
        
    
     # @staticmethod
     def error_message(player: Player, values):
         must_aggree = False
         if values['type_of_zood'] != "0":
             player.register_in_zood = True
             must_aggree = True
         
         if not values['endorsement'] and must_aggree:
            return 'يجب الموافقة على الإقرار  قبل المتابعة'
     
     

class Group3(Page):
     form_model = 'player'
     form_fields = ['register_in_zood', 'endorsement', 'bank_for_zood' ]
     
        
     @staticmethod
     def is_displayed(player: Player):
        month_income = player.monthlyIncome
        if month_income is None or month_income > 20000:
            return False
        
        if player.user_group != 3:
            return False
        
        return True
        
        
     @staticmethod
     def before_next_page(player: Player, timeout_happened):
         if not player.endorsement and player.register_in_zood:
            player.participant.vars['dropout_fields'] = ['endorsement']
            player.participant.vars['dropout_page'] = 'Group1'
        
    
     # @staticmethod
     def error_message(player: Player, values):
         if not values['endorsement'] and values['register_in_zood']:
            return 'يجب الموافقة على الإقرار  قبل المتابعة'
     
     
     

class Result(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'monthlyIncome': player.monthlyIncome,
        }
        




page_sequence = [Intro, FinancialAnalysis,  PersonalAnalysis ,Freelance,  Productive_Family,  FinancialRequest, PaymentAmount,Group1, Group2 , Group3, Result, ]
