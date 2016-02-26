import time

def leaking_suit(air_volume_with_person_in_suit, hole_size_mm2, oxygen_percentage, seconds):

    volume_air_lost_per_second = hole_size_mm2 * (air_volume_with_person_in_suit / 2) /100

    volume_not_oxygen_lost_per_second = volume_air_lost_per_second * ((100 - oxygen_percentage) / 100)
    
    volume_of_oxygen = air_volume_with_person_in_suit * (oxygen_percentage / 100)

    new_volume_of_oxygen = volume_of_oxygen + (volume_not_oxygen_lost_per_second * seconds)

    return  (new_volume_of_oxygen / air_volume_with_person_in_suit) * 100

print('try move, fix or pull')

# In concentrations up to 1% (10,000 ppm), it will make some people feel drowsy and
# give the lungs a stuffy feeling.[90] Concentrations of 7% to 10% (70,000 to 
# 100,000 ppm) may cause suffocation, even in the presence of sufficient oxygen, 
# manifesting as dizziness, headache, visual and hearing dysfunction, and 
# unconsciousness within a few minutes to an hour.[92] The physiological effects 
# of acute carbon dioxide exposure are grouped together under the term hypercapnia, 
# a subset of asphyxiation.

# In an average resting adult, the lungs take up about 250ml of oxygen every minute
# while excreting about 200ml of carbon dioxide. 

# Shuttle suit had 50 litres of air.

# with a 1 sqr cm hole, a 30 cubic metre cabin will depressurise by 50% in 500 sceonds
# 0.05 cubic metre suit, depressurise in 1 sec
# with 1 sqr mm hole 50% depressurise in 100 secs

# venting 0.25l every second.So if mix is 80% then 20% nitrogen replaced by 100% oxygen.
# 0.05l of extra oxygen
# 0.1%

oxygen = 80
leak = 1
while True:

    print('Suit oxygen at {:.2f}%'.format(oxygen))

    start = time.time()
    cmd = input(':')
    finish = time.time()

    if cmd == 'pull':
        leak = 12
    elif cmd == 'fix':
        leak = 0.1

    oxygen = leaking_suit(50, leak, oxygen, finish - start)

