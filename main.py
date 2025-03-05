from time import sleep
import json
import math as mt


pict_list = ['MY FIRST SKRIPT\n\n',
              '    *********',
              '   *       **',
              '  *       * *',
              ' *********  *',
              ' *       *  *',
              ' *       *  *',
              ' *       * *',
              ' *********',
             '\n\nI LOVE PYTHON']
for i in pict_list:
  sleep(.4)
  print(i)

from utils.functions import process 

with open("parallelepipeds.json", "r") as file:
    parallelepipeds = json.load(file)

characteristics = {}
for fig, atr_dict in parallelepipeds.items():
    a, b, c = float(atr_dict['a']), float(atr_dict['b']), float(atr_dict['c'])
    characteristics[fig] = process(a, b, c)

with open("outputs/characteristics.json", "w") as outfile:
    json.dump(characteristics, outfile, indent=4)

print(json.dumps(characteristics, indent=4))


statistics = {}
len_ = len(characteristics)
char_values = characteristics.values()

avg_diag = round(sum(float(k['diag']) for k in char_values) / len_,3)
avg_volume = round(sum(float(k['volume']) for k in char_values) / len_,3)
avg_surface = round(sum(float(k['surface_area']) for k in char_values) / len_,3)
avg_alpha = round(sum(float(k['alpha']) for k in char_values) / len_,3)
avg_beta = round(sum(float(k['beta']) for k in char_values) / len_,3)
avg_gamma = round(sum(float(k['gamma']) for k in char_values) / len_,3)
avg_radius_described_sph = round(sum(float(k['radius_described_sphere'])for k in char_values) / len_,3
)
avg_volume_described_sph = round(sum(float(k['volume_described_sphere']) for k in char_values) / len_,3)

statistics = {
    'avg_diag': str(avg_diag),
    'avg_volume': str(avg_volume),
    'avg_surface_area': str(avg_surface),
    'avg_alpha': str(avg_alpha),
    'avg_beta': str(avg_beta),
    'avg_gamma': str(avg_gamma),
    'avg_radius_described_sphere': str(avg_radius_described_sph),
    'avg_volume_described_sphere': str(avg_volume_described_sph)
}

with open("outputs/statistics.json", 'w') as outfile:
    json.dump(statistics, outfile, indent=4)

print(' =' * 20, '\n Средние значения для всех параллелограмов \n',' =' * 20)

print(json.dumps(statistics, indent=4))