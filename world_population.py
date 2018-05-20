#_*_ coding:utf_8 _*_

import json
from pygal_maps_world.maps import World
from pygal.style import RotateStyle as RS,LightColorizedStyle as LCS

from country_codes import get_country_code

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

#创建一个包含人口数量的字典
cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        num_pop = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
             cc_population[code] = num_pop
        else:
            print country_name

#cc_pops1,cc_pops2,cc_pops3 = {},{},{}

#for cc,pop in cc_population.items():
#    if pop < 10000000:
#        cc_pops1[cc] = pop
#    elif pop < 1000000000:
#        cc_pops2[cc] = pop
#    else:
#        cc_pops3[cc] = pop

#wm_style = RS('#336699',base_style=LCS)
#wm = World(style=wm_style)
#wm.title = 'World Population in 2010, by Country'
#wm.add('0-10m',cc_pops1)
#wm.add('10m-10bn',cc_pops2)
#wm.add('>10bn',cc_pops3)

#wm.render_to_file('world population.svg')