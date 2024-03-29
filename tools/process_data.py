# -*- coding: utf-8 -*-
# @Author: solidjoker
# @Date:   2019-08-13 17:04:48
# @Last Modified by:   solidjoker
# @Last Modified time: 2019-08-13 18:04:52

from pandas import DataFrame
import os


def process_data(result_dic, dic_ne, open_file=False):
    df = DataFrame(result_dic)
    df = df.unstack(
    ).unstack(level=-1
              ).reset_index(
    ).rename(columns={'index': 'model_id'})
    columns = ['model_id']
    columns += list(dic_ne.values())
    df = df[columns]
    if open_file:
        try:
            filename = 'output.txt'
            df.to_csv(filename, sep='\t', index=False)
            os.startfile(filename)
        except Exception as e:
            print(e)
    return df
