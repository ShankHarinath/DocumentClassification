import os
from bs4 import BeautifulSoup
import codecs

class Extract:
    def parse_docs(self, doc):
        information = {}
        soup = BeautifulSoup(codecs.open(doc, encoding='utf8'), "html5lib")
        
        sympton_ids =  soup.findAll(id=lambda x: x and x.lower().startswith('symptom'))
        causes_ids =  soup.findAll(id=lambda x: x and x.lower().startswith('causes'))
        prognosis_ids =  soup.findAll(id=lambda x: x and x.lower().startswith('prognosis'))
        prevention_ids =  soup.findAll(id=lambda x: x and x.lower().startswith('prevention'))
        treatment_ids =  soup.findAll(id=lambda x: x and x.lower().startswith('treatment'))
        
        if len(sympton_ids) > 0:
            information['symptom'] = self.get_intermediate_contents(sympton_ids[0], sympton_ids[0].find_next('h2'))
        if len(causes_ids) > 0:
            information['causes'] = self.get_intermediate_contents(causes_ids[0], causes_ids[0].find_next('h2'))
        if len(prognosis_ids) > 0:
            information['prognosis'] = self.get_intermediate_contents(prognosis_ids[0], prognosis_ids[0].find_next('h2'))
        if len(prevention_ids) > 0:
            information['prevention'] = self.get_intermediate_contents(prevention_ids[0], prevention_ids[0].find_next('h2'))
        if len(treatment_ids) > 0:
            information['treatment'] = self.get_intermediate_contents(treatment_ids[0], treatment_ids[0].find_next('h2'))

        print(information)

    def get_intermediate_contents(self, source, dest):
        text = ""
        while source.next.next != dest:
            if source.string is not None:
                text += source.string
            print text
            source = source.next
