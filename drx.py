import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title("The Rise of DRX")
st.write("2018-11694 언론정보학과 허현준")

import qrcode
img = qrcode.make("http://localhost:8501/")
img.save("drx.png")
