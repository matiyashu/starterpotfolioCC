
"""
Hypothesis:
> 
> Each regions have higher insurance cost per patient due to their lifestyle factor especially in the structure of their family and smoking status.
> Eacg regions have higher average rate of smokers, number of kids and/or average bmi.

==============
Project Goal
The goal of this project is to test my hypothesis.

I will test the hypothesis by finding out:

How many patients in each regions?
What's the average insurance cost per patient per region?
Which region has the highest average insurance cost?
Which region has the highest percentage of smokers amongst patients?
Which region has the most kids on average per patient?
Which region has the highest average bmi per patient?
"""

import csv

with open("insurance.csv") as insurance_table:
	insurance_table_data = csv.DictReader(insurance_table)
	list_age = []
	list_sex = []
	list_bmi = []
	list_children = []
	list_smoker = []
	list_region = []
	list_charges = []

	for row in insurance_table_data:
		list_age.append(float(row['age']))
		list_sex.append(row['sex'])
		list_bmi.append(float(row['bmi']))
		list_children.append(float(row['children']))
		list_smoker.append(row['smoker'])
		list_region.append(row['region'])
		list_charges.append(float(row['charges']))



patient_data_dict = {'Ages': list_age, 
				'Sex': list_sex, 
				"BMIs": list_bmi, 
				"Children": list_children, 
				"Smoker": list_smoker, 
				"Region": list_region, 
				"Charges": list_charges}

# print(patient_data_dict)


# This class will attempt to describe the data in general.

class PatientData:
    def __init__(self, age, sex, bmi, children, smoker, region, charges):  

        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region
        self.charges = charges

    def population(self):
        total_pop = 0
        for age in self.age:
            total_pop += 1
        return "There are {} patients in this data set".format(total_pop)
    
    def average_age(self):
        total_age = 0
        for age in self.age:
            total_age += age
        return "Average patient age: {}".format(str(total_age/len(self.age)))
    
    def sex_dist(self):
        total_males = 0
        total_females = 0
        for sex in self.sex:
            if sex == 'male':
                total_males +=1
            if sex == 'female':
                total_females += 1
        return "There are total of {} males and total of {} females in this data set.".format(total_males, total_females)

    def average_bmi(self):
        total_bmi = 0
        for bmi in self.bmi:
            total_bmi += bmi
        return "Average Patient BMI: {}".format(str(total_bmi/ len(self.bmi)))

    def num_smokers(self):
        total_smokers = 0
        total_nonsmokers = 0
        for yes_no in self.smoker:
            if yes_no == 'yes':
                total_smokers += 1
            if yes_no == 'no':
                total_nonsmokers +=1 
        return "There are {} smokers and {} non-smokers".format(total_smokers, total_nonsmokers)

    def average_num_children(self):
        total_children = 0
        for child in self.children:
            total_children += child
        return "The average patient has {} children".format(str(total_children/len(self.children)))
    
    def average_charges(self):
        total_charges = 0
        for charge in self.charges:
            total_charges += charge
        return "Average Charges: {} dollars".format(str(total_charges/len(self.charges)))


patient_data = PatientData(list_age, list_sex, list_bmi, list_children, list_smoker, list_region, list_charges)
print(patient_data.population())
print(patient_data.average_age())
print(patient_data.average_bmi())
print(patient_data.sex_dist())
print(patient_data.num_smokers())
print(patient_data.average_num_children())
print(patient_data.average_charges())



# In the next section we will do a breakdown and divide the data based on their own segment

def patients_per_region_category(csv_file, category):
    region_categories = {}
    with open("insurance.csv", newline='') as insurance_table: #instead of using "Insurance.csv we can use csv_file, since the csv_file already been imported"
        insurance_data = csv.DictReader(insurance_table)
        for row in insurance_data:
            key = row[category]
            if key in region_categories:
                region_categories[key] = region_categories[key] + 1
            else:
                region_categories[key] = 1
    return region_categories

patients_per_region = patients_per_region_category("insurance.csv", "region")
print(f"\n{patients_per_region}".title())


# What's the average insurance cost per patient per region?

def category_per_region(csv_file, category):
    regions = {}
    with open("insurance.csv", newline='') as insurance_table:
        insurance_data = csv.DictReader(insurance_table)
        for row in insurance_data:
            region = row["region"]
            cat = float(row[category])
            if region in regions:
                regions[region] += cat
            else:
                regions[region] = cat
    return regions

cost_per_region = category_per_region("insurance.csv", "charges")

print(f"{cost_per_region}".title())


def average_segment_per_region(costs, costs_per_region):
    for element in costs_per_region:
        average = costs_per_region[element]/patients_per_region[element]
        print("The average {} per patient for {} is {}".format(costs, element, average))

average_segment_per_region("costs", cost_per_region)


# Which region has the highest percentage of smokers amongst patients?

def smokers_binary_per_region(csv_file, binary):
    regions = {}
    with open("insurance.csv", newline='') as insurance_csv:
        insurance_data = csv.DictReader(insurance_csv)
        for row in insurance_data:
            region = row["region"]
            value = row[binary]
            if region in regions:
                if value in regions[region]:
                    regions[region][value] += 1 
                else: 
                    regions[region][value] = 1
            else:
                regions[region] = {}
                regions[region][value] = 1     
    return regions

smokers_per_region = smokers_binary_per_region("insurance.csv", "smoker")

print(f"\n{smokers_per_region}".title())


# create function to calculate percentage of smokers per region

def smokers_percentage(smokers_per_region, patients_per_region):
    for element in smokers_per_region:
        decimals = (smokers_per_region[element]["yes"]) / patients_per_region[element]
        percentage = round(decimals * 100, 2)
        print ("{} has {} percent smokers".format(element, percentage).title())
              
    
smokers_percentage(smokers_per_region, patients_per_region)



# Which region has the most kids on average per patient?

kids_per_region = category_per_region("insurance.csv", "children")

print(f"\n{kids_per_region}")

average_segment_per_region("children", kids_per_region)

max_children = max(kids_per_region, key=kids_per_region.get)

print(f"{max_children.title()} is the highest region with children percentage")


# Which region has the highest average bmi per patient?

bmi_per_region = category_per_region("insurance.csv", "bmi")

print(f"\n{bmi_per_region}")


average_segment_per_region("bmi", bmi_per_region)
max_bmi = max(bmi_per_region, key=bmi_per_region.get)

print(f"{max_bmi.title()} is the highest region with BMI value")
