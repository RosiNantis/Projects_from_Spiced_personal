# import the packages
import pandas as pd
import numpy as np
import random
import datetime

departments = [0,1,2,3,4]#['checkout','dairy', 'drinks',  'fruit', 'spices']
departments_names = ['checkout','dairy', 'drinks',  'fruit', 'spices']
distribution = [0,0.288,0.154,0.377,0.182]
TRANSITION_MATRIX = [[1,0,0,0,0]
                ,[0.392389,	0.000000,	0.222318,	0.189852,	0.195442]
                ,[0.538956,	0.027256,	0.000000,	0.217794,	0.215994]
                ,[0.500784,	0.236966,	0.136417,	0.000000,	0.125833]
                ,[0.251672,	0.323616,	0.272800,	0.151912,	0.000000]
                ] 

class Customer:
    '''
    The class Customer is a blueprint for a supermarket customer.
    
    Parameter
    -------
    '''
    

    def __init__(self, name, state = True):
        self.customer_id = name
        self.state_customer = state
        self.starting_alley()

    def starting_alley(self,location= departments, weights = distribution):
        self.starting_point = random.choices(location, weights , k=1)[0]
        print(f'Here we go!!!!!!{self.starting_point}')
        self.location = departments_names[self.starting_point]
        return self.location


    def next_state(self,location= departments,TRANSITION_MATRIX_list = TRANSITION_MATRIX):
        '''
        Propagates the customer to the next state.
        Returns nothing.
        '''
        
        self.next_dep = random.choices(location, weights=TRANSITION_MATRIX_list[self.starting_point])[0]
        if self.location == departments_names[self.next_dep]:
            print('it happened' + str(self.customer_id))
        self.location = departments_names[self.next_dep]
        return self.location


class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """
    def __init__(self):        
        # a list of Customer objects
        self.customers = []
        self.location = []
        self.next_alley = []
        self.first_id = 1
        self.ticktock = datetime.datetime(2022,1,1,7,00)
        self.closing_time = datetime.datetime(2022,1,1,8,00)
        self.remove_indices = []

    def get_time(self):
        """current time in HH:MM format,
        """
        self.clock = self.ticktock.strftime('%H:%M')
        return self.clock

    
    def add_new_customers(self):
        """randomly creates new customers.
        """
        rand_numb =3# np.random.randint(10)
        number = 0
        while number<=rand_numb:
            c =Customer(self.first_id)
            self.customers.append(c)
            self.first_id += 1
            number += 1
        #print(f'The length of the customers is {len(self.customers)}')       
        return self.customers

    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        for i in range(len(self.customers)):
            print(f'At {self.get_time()} the customer {self.customers[i].customer_id} is in the "{self.customers[i].location}" alley.')
        self.remove_existing_customers()

    def next_minute(self):
        """propagates all customers to the next state.
        """
        self.ticktock += datetime.timedelta(0,0,0,0,10) # time in minutes
        for i in range(len(self.customers)):
            self.next_alley.append(self.customers[i].next_state())
        print('I am moving them to the next state')
        self.location = self.next_alley
        #self.remove_existing_customers()
        return self.ticktock, self.location


    def remove_existing_customers(self):
        """removes every customer that is not active any more.
        """
        
        # for idx, c in enumerate(self.customers):
        #     if c.location == 'checkout':
        #         self.remove_indices.append(idx)  
        # print(f'We got to remove the {self.remove_indices}')            
        self.customers = [i for j, i in enumerate(self.customers) if i.location != 'checkout']  

    #def __repr__(self):
        
        #return f'The customer {self.customers} is in the {self.location()} department at "{self.timer()}".'



start = Supermarket()

while start.ticktock <= start.closing_time:
    start.get_time()
    start.add_new_customers()
    start.print_customers()
    start.next_minute()
    #start.remove_existing_customers()


