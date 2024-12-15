import streamlit as st
import pandas as pd

def seSB(df):
    options = list(
            set(df['Home LC'].unique()) | 
            set(df['Home MC'].unique()) | 
            set(df['Home Region'].unique())
        )
    
    if 'AIESEC INTERNATIONAL' in options:
        options.remove('AIESEC INTERNATIONAL')  # Remove from its current position
    options.insert(0, 'AIESEC INTERNATIONAL')

    return st.selectbox("Select Home Entity", options, 
                        placeholder="Select an option", index=0,
                        key='sbse',
                        on_change=lambda: st.session_state.update({"home": st.session_state["sbse"]}))

def heSB(df):
    options = list(
            set(df['Host LC'].unique()) | 
            set(df['Host MC'].unique()) | 
            set(df['Host Region'].unique())
        )
    
    if 'AIESEC INTERNATIONAL' in options:
        options.remove('AIESEC INTERNATIONAL')  # Remove from its current position
    options.insert(0, 'AIESEC INTERNATIONAL')

    return st.selectbox("Select Host Entity", options, 
                        placeholder="Select an option", index=0,
                        key='sbhe',
                        on_change=lambda: st.session_state.update({"host": st.session_state["sbhe"]}))

def productMS():    
    options = list(
            {'iGV', 'iGTa', 'iGTe', 'oGV', 'oGTa', 'oGTe'}
        )

    return st.multiselect("Select Product", options,
                        placeholder="Select an option",
                        key='msp',
                        on_change=lambda: st.session_state.update({"product": st.session_state["msp"]}))

def processtimeMS():
    options = list(
            {'SU -> APL', 'APL -> ACT', 'ACT -> APD', 'APD -> RE', 'RE - CO'}
        )

    return st.multiselect("Select Process Time", options,
                        placeholder="Select an option",
                        key='mspt',
                        on_change=lambda: st.session_state.update({"processtime": st.session_state["mspt"]}))