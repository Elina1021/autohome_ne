# -*- coding: utf-8 -*-
# @Author: solidjoker
# @Date:   2019-08-13 16:48:06
# @Last Modified by:   solidjoker
# @Last Modified time: 2019-08-13 17:25:25


from . import fetch_data
from . import process_data
from . import config


def get_result_dic(dic_ne):
    result_dic = {}
    for k in dic_ne.keys():
        url = config.url_ne.format(ne=k)
        get_model_id_dic(url, dic_ne[k], result_dic)
    return result_dic


def get_model_id_dic(url, energytype, result_dic):
    bsobj = fetch_data.get_bsobj(url)
    uls_model = bsobj.find_all('ul', {'class': 'rank-list-ul'})

    for ul_model in uls_model:
        lis_model = ul_model.find_all('li')
        for li_model in lis_model:
            if li_model.has_attr('id'):
                model_id = li_model.attrs['id'][1:]

                if not model_id in result_dic:
                    result_dic[model_id] = {'汽油': None,
                                            '柴油': None,
                                            '油电混合': None,
                                            '纯电动': None,
                                            '插电式混动': None}
                result_dic[model_id][energytype] = True


def main():
    dic_ne = {1: '汽油',
              2: '柴油',
              3: '油电混合',
              4: '纯电动',
              5: '插电式混动'}
    result_dic = get_result_dic(dic_ne)
    df = process_data.process_data(result_dic, open_file=True)
    return df


if __name__ == '__name__':
    main()
