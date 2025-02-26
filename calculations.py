import json
import math as mt

def get_diag(a: float, b: float, c: float) -> float:
    return mt.sqrt(a**2 + b**2 + c**2)

def get_volume(a: float, b: float, c: float) -> float:
    return a * b * c

def get_surface(a: float, b: float, c: float) -> float:
    return 2 * (a * b + a * c + b * c)

def get_alpha(a:float,b:float,c:float)->float:
  return mt.degrees(mt.acos(a/mt.sqrt(a**2 + b**2 + c**2)))

def get_beta(a:float,b:float,c:float)->float:
  return mt.degrees(mt.acos(b/mt.sqrt(a**2 + b**2 + c**2)))

def get_gamma(a:float,b:float,c:float)->float:
  return mt.degrees(mt.acos(c/mt.sqrt(a**2 + b**2 + c**2)))

def get_sphr_radius(a: float, b: float, c: float) -> float:
    return mt.sqrt(a**2 + b**2 + c**2) / 2

def get_sphr_volume(a: float, b: float, c: float) -> float:
    return (4/3) * mt.pi * (mt.sqrt(a**2 + b**2 + c**2) / 2)**3

def process(a: float, b: float, c: float) -> dict:
    return {
        "diag": round(get_diag(a, b, c), 2),
        "volume": round(get_volume(a, b, c), 2),
        "surface_area": round(get_surface(a, b, c), 2),
        "alpha": round(get_alpha(a, b, c), 2),
        "beta": round(get_beta(a, b, c), 2),
        "gamma": round(get_gamma(a, b, c), 2),
        "radius_described_sphere": round(get_sphr_radius(a, b, c), 2),
        "volume_described_sphere": round(get_sphr_volume(a, b, c), 2)
    }

with open("parallelepipeds.json", "r") as file:
    parallelepipeds = json.load(file)

characteristics = {}
for fig, atr_dict in parallelepipeds.items():
    a, b, c = float(atr_dict['a']), float(atr_dict['b']), float(atr_dict['c'])
    characteristics[fig] = process(a, b, c)

with open("characteristics.json", "w") as outfile:
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

with open("statistics.json", 'w') as outfile:
    json.dump(statistics, outfile, indent=4)

print(' =' * 20, '\n Средние значения для всех параллелограмов \n',' =' * 20)

print(json.dumps(statistics, indent=4))