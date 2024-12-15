import streamlit as st
import pandas as pd
import numpy as np

def filter(df, sstate):
    home = sstate['home']
    host = sstate['host']
    processtime = sstate['processtime']
    product = sstate['product']

    arg_home, arg_host = argGenerator(df, home, host)

    if home == 'AIESEC INTERNATIONAL':
        home_values = df[arg_home[1]].unique()
    else:   
        home_values = df[df[arg_home[1]] == home][arg_home[0]].unique()

    if host == 'AIESEC INTERNATIONAL':
        host_values = df[arg_host[1]].unique()
    else:
        host_values = df[df[arg_host[1]] == host][arg_host[0]].unique()
    
    num_host = len(host_values)
    num_pt = len(processtime)
    num_pd = len(product)
    
    total_columns = num_pt * num_pd * num_host

    output = np.full((len(home_values), total_columns), np.nan)

    for i, h in enumerate(home_values):
        flat_index = 0
        for ho in host_values:
            for pt in processtime:
                arg_d1, arg_d2 = argptgen(pt)
                
                df[pt] = np.where((df[arg_d1].isna() | df[arg_d2].isna()),
                                  np.nan, 
                                  (df[arg_d2] - df[arg_d1]).dt.total_seconds() / (24 * 3600))
                
                for p in product:
                    value = getval(h, arg_home, ho, arg_host, pt, p, df)
                    output[i, flat_index] = value
                    flat_index += 1

    iterable = [host_values, processtime, product]
    columns = pd.MultiIndex.from_product(iterable, names=['Host', 'Process Time', 'Product'])
    odf = pd.DataFrame(output, index=home_values, columns=columns)

    return odf

def argGenerator(df, home, host):
    arg_home = ('Home LC', 'Home LC')
    arg_host = ('Host LC', 'Host LC')

    if home == 'AIESEC INTERNATIONAL':
        arg_home = ('Home Region', 'Home Region')
    elif home in df['Home Region'].unique():
        arg_home = ('Home MC', 'Home Region')
    elif home in df['Home MC'].unique():
        arg_home = ('Home LC', 'Home MC')

    if host == 'AIESEC INTERNATIONAL':
        arg_host = ('Host Region', 'Host Region')
    elif host in df['Host Region'].unique():
        arg_host = ('Host MC', 'Host Region')
    elif host in df['Host MC'].unique():
        arg_host = ('Host LC', 'Host MC')
    return arg_home, arg_host

def argptgen(processtime):
    if processtime == 'SU -> APL':
        arg_d1 = 'Date signed up'
        arg_d2 = 'Date applied'
    elif processtime == 'APL -> ACT':
        arg_d1 = 'Date applied'
        arg_d2 = 'Date accepted'
    elif processtime == 'ACT -> APD':
        arg_d1 = 'Date accepted'
        arg_d2 = 'Date approved'
    elif processtime == 'APD -> RE':
        arg_d1 = 'Date approved'
        arg_d2 = 'Date realized'
    elif processtime == 'RE - CO':
        arg_d1 = 'Date realized'
        arg_d2 = 'Date complete'

    return arg_d1, arg_d2

def getval(home, home_arg, host, host_arg, pt, product, df):
    p_arg = 'GV (New)'
    if 'Ta' in product:
        p_arg = 'GTa'
    elif 'Te' in product:
        p_arg = 'GTe'

    if product[0] == 'i':
        mean_value = df[
                        (df[home_arg[0]] == home) &
                        (df['Product'] == p_arg) &
                        (df[host_arg[0]] == host)
                    ][pt].mean()
        return mean_value
    
    if product[0] == 'o':
        mean_value = df[
                        (df[host_arg[0].replace('Host', 'Home')] == host) &
                        (df['Product'] == p_arg) &
                        (df[home_arg[0].replace('Home', 'Host')] == home)
                    ][pt].mean()
        round(mean_value, 2)
        return mean_value
