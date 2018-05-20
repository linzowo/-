#_*_ coding:utf_8 _*_

from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print country_code,COUNTRIES[country_code]