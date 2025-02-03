import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

gun_angle_mils = st.sidebar.slider('Gun angle (NATO Mils)',0.00,1600.00,800.00,0.01)
distance = st.sidebar.slider('Distance (m)',0,2500,1000)
radar_angle_mils = st.sidebar.slider('Radar angle (NATO Mils)',0.00,1600.00,35.56, 0.01)
xlim = st.sidebar.slider('X Axis max',0,6000,100)
ylim = st.sidebar.slider('Y Axis max',0,6000, 100)

radar_angle_rad = (radar_angle_mils/6400) * 2 * np.pi
radar_angle_top = radar_angle_rad+(2*(np.pi/180))
radar_angle_bot = radar_angle_rad-(2*(np.pi/180))

lowest_cone = np.tan(radar_angle_bot)*distance
st.write("radar angle top:", radar_angle_top)
st.write("radar angle bot:", radar_angle_bot)
st.write("Distance:", distance)
st.write("Lowest cone point:", lowest_cone)
st.write("angle in randians:", radar_angle_rad)

fig = plt.figure(figsize = (10, 5))
x = np.linspace(0, 2500, 100)
plt.ylim(0,ylim)
plt.xlim(0,xlim)

y1 = np.tan(radar_angle_top)*x+1
plt.plot(x,y1)
y2 = np.tan(radar_angle_bot)*x+1
plt.plot(x,y2)
y3 = -0.0001*((x-500)**2)+50
plt.plot(x,y3)
plt.plot([distance, distance], [0,np.tan(radar_angle_bot)*distance ], color = 'red', linestyle = '--', marker = 'o')

st.pyplot(fig)



##fig_html = mpld3.fig_to_html(fig)
##components.html(fig_html, height=600)