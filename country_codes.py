#_*_ coding:utf-8 _*_

from pygal_maps_world.i18n import COUNTRIES

#获取国家的国别码
def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    return None
