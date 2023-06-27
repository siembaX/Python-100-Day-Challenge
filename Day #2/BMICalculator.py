""" BMI CALCULATOR """

height = input('please enter height: ');
weight = input('please enter weight: ');

body_mass = int(weight) / float(height)**2;
print(type(body_mass))
print(round(body_mass))

