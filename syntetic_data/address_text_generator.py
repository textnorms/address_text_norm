'''
    This file implements a address text generation
'''

'''
    Importing num2words module:
    https://github.com/savoirfairelinux/num2words
'''
from num2words import num2words


'''
    Importing dependencies from datetime module
'''
from datetime import datetime
from datetime import timedelta

'''
    Importing pandas module:
    https://github.com/pandas-dev/pandas
'''
import pandas as pd

'''
    Importing random dependencies
'''
from random import random
from random import randint
from random import sample

'''
    Importing dependencies from Collections
'''
from collections import OrderedDict

'''
    Importing authorial modules, further description about
    them can be found on their implementations.
'''
from .text_noise import text_noise_dict
from .address_csv import address_csv_dict
from .aux_dicts_and_functions import combinations
from .aux_dicts_and_functions import occurences_per_sample_dict
from .address_dicts import address_formats_dicts

class AddressTextGenerator():
    '''
        This class implements address-text generation for
        using zip a set of brazilian zip codes in a csv.
        You can specify noise rate, date text formats per sample
        and language.
    '''
    def __init__(self,occurences_per_sample=1,
        text_noise_rate=0.0,
        max_noise_types_per_sample=3,
        max_noise_occurences_per_sample = 2,
        text_noise_methods=text_noise_dict,
        language='br'):

        self.n_samples_per_method = occurences_per_sample

        self.text_error_rate = text_noise_rate
        self.text_noise_methods = text_noise_methods

        self.max_noise_occurences_per_sample = max_noise_occurences_per_sample
        self.max_noise_types_per_sample = max_noise_types_per_sample

        self.language = language

    def generate_address_dataset(self):
        '''
            Generates the dataset for all the supported formats            
        '''

        samples_base_df = pd.read_csv(address_csv_dict[self.language],header=0)

        # Removing all samples with NaN values for a field 
        samples_base_df.dropna(inplace=True)

        dataset = []
        for cep_row in samples_base_df.iterrows():
                
            dataset = dataset + self._generate_single_address_dataset(
                cep_row[1]['endereco'],randint(1,10000),
                '',cep_row[1]['bairro'],cep_row[1]['cidade'],
                cep_row[1]['uf'],cep_row[1]['cep'])
        
        pd_dataset = pd.DataFrame(dataset,
            columns=['Input Pattern','Noise Type','Input','Target'])

        return pd_dataset

    def _generate_single_address_dataset(self,logradouro,numero,complemento,bairro,cidade,uf,cep):
        '''
           Generates a pandas dataset for a given date_range, target format and its date
           text generation methods. With the samples_per_method variable is possible to
           increase the amount of date text formats per target.
        '''

        X = []
        method_ids = []
        noise_types = [] # N/A if has no noise, or the keys from text_noise_implementations
        y = []
        
        # Sampling method and its ids
        for method_id,address_text_gen_method in self.sample_from_dict(address_formats_dicts[self.language],
            self.n_samples_per_method):

            method_ids.append(
                int(method_id)
            )

            text_sample,target = address_text_gen_method(logradouro,numero,complemento,
                bairro,cidade,uf,cep)

            noise_type = 'N/A'

            if random() < self.text_error_rate:
                # Applying noise
                text_sample,noise_type = self._apply_noise(text_sample)
            
            noise_types.append(
                noise_type    
            )

            X.append(
                text_sample
            )

            y.append(target)

        return list(zip(method_ids,noise_types,X,y))


    def _apply_noise(self,input_text):
        '''
            Selects a random noise type and apply it to
            input_text. This function returns input_text
            with noise and the noise type applied.
        '''
        
        # Introducing some randomness to the proccess of selecting
        # the number of samples
        noise_types = randint(1,self.max_noise_types_per_sample)
        
        # This list will keep track of the noises applied to 
        # each sample and will be used to included to the final
        # dataframe 
        applied_noises = []

        for noise_type in sample(list(self.text_noise_methods.keys()),noise_types):
            noise_func = self.text_noise_methods[noise_type]
            
            # Defining the number of occurrences per sample
            noise_occurrences = randint(1,self.max_noise_occurences_per_sample)

            # Applying noise to multi samples
            input_text  = noise_func(input_text,noise_occurrences)

            applied_noises.append(noise_type)


        return input_text,applied_noises

    @staticmethod
    def parse_days_months_years(sample,sample_format):
        if sample_format == 'DD/MM/YYYY':
            day,month,year = sample.split('/')
        elif sample_format == 'DD/MM':
            day,month = sample.split('/')
            year = None
        elif sample_format == 'MM/YYYY':
            day = None
            month,year =sample.split('/')
        else:
            raise NotImplementedError(f'\
                Format {sample_format} not implemented :(')

        return day,month,year 

    @staticmethod
    def sample_from_dict(dict_to_sample,n_samples=1):
        '''
            This method implements a form of sampling n_samples from
            a dict. This is code was inspired in the implementation
            described in:
            https://stackoverflow.com/questions/10125568/how-to-randomly-choose-multiple-keys-and-its-value-in-a-dictionary-python
        '''

        # Sampling n_samples keys
        keys_and_values = sample(dict_to_sample.items(), n_samples)
        
        # Returns the values and the keys corresponding
        # each sampled value
        return keys_and_values