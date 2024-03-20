from faker import Faker
from faker.providers import BaseProvider
import re
import pandas as pd

class CustomProvider(BaseProvider):
    def clean_name(self):
        name = self.generator.name()
        # Replace special characters with their non-accented counterparts or remove them
        clean_name = re.sub(r'[ÁÀÂÃ]', 'A', name)
        clean_name = re.sub(r'[áàâã]', 'a', clean_name)
        clean_name = re.sub(r'[ÉÈÊ]', 'E', clean_name)
        clean_name = re.sub(r'[éèê]', 'e', clean_name)
        clean_name = re.sub(r'[ÍÌÎ]', 'I', clean_name)
        clean_name = re.sub(r'[íìî]', 'i', clean_name)
        clean_name = re.sub(r'[ÓÒÔÕ]', 'O', clean_name)
        clean_name = re.sub(r'[óòôõ]', 'o', clean_name)
        clean_name = re.sub(r'[ÚÙÛ]', 'U', clean_name)
        clean_name = re.sub(r'[úùû]', 'u', clean_name)
        clean_name = re.sub(r'[Ç]', 'C', clean_name)
        clean_name = re.sub(r'[ç]', 'c', clean_name)
        return clean_name

# Set the locale to Portuguese (Portugal)
fake = Faker('pt_PT')
fake.add_provider(CustomProvider)

# Generate 5110 Portuguese names
names = [fake.clean_name() for _ in range(5110)]

# Create a DataFrame and save the names to a CSV file
df_names = pd.DataFrame(names, columns=['Name'])

import random

# List of Portuguese districts
districts = [
    "Aveiro", "Beja", "Braga", "Braganca", "Castelo Branco", "Coimbra", "Evora",
    "Faro", "Guarda", "Leiria", "Lisboa", "Portalegre", "Porto", "Santarem",
    "Setubal", "Viana do Castelo", "Vila Real", "Viseu", "Acores", "Madeira"
]

# Randomly assign a district to each name
df_names['District'] = [random.choice(districts) for _ in range(len(df_names))]

# Save the updated DataFrame to a new CSV file
df_names.to_csv('portuguese_names_districts.csv', index=False, encoding='utf-8')
