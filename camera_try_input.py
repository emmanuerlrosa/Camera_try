#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:26:32 2022

@author: emmanuelrosa
"""

import streamlit as st 

import streamlit as st

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)