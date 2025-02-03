import streamlit as st
import numpy as np
import plotly.graph_objects as px

st.set_page_config(layout="wide")

st.write(r"$\textsf{\Large Ballistic Radar cone sim}$")

gun_angle_mils = st.sidebar.slider('Gun angle (NATO Mils)',0.00,1600.00,800.00,0.01)
distance = st.sidebar.slider('Distance (m)',0,2500,200)
radar_angle_mils = st.sidebar.slider('Radar angle (NATO Mils)',0.00,1600.00,35.56, 0.01)
radar_pos = st.sidebar.slider('Radar position',0,6000,0,50)
xlim = st.sidebar.slider('X Axis max',0,6000,250,50)
ylim = st.sidebar.slider('Y Axis max',0,6000, 250,50)

radar_angle_rad = (radar_angle_mils/6400) * 2 * np.pi
radar_angle_top = radar_angle_rad+(2*(np.pi/180))
radar_angle_bot = radar_angle_rad-(2*(np.pi/180))

lowest_cone = np.tan(radar_angle_bot)*distance

x = np.linspace(0, 2500, 100)

y1 = np.tan(radar_angle_top)*x+1
y2 = np.tan(radar_angle_bot)*x+1
y3 = -0.0001*((x-600)**2)+50

fig = px.Figure(layout_xaxis_range=[0,xlim],layout_yaxis_range=[0,ylim])
fig.add_trace(px.Scatter(x=x, y=y1, mode='lines', marker_color = "red"))
fig.add_trace(px.Scatter(x=x, y=y2, mode='lines', marker_color = "red"))
fig.add_trace(px.Scatter(x=x, y=y3, mode='lines', marker_color = "white"))
fig.add_trace(px.Scatter(x=[distance, distance],y=[0,np.tan(radar_angle_bot)*distance ], mode='lines+markers', marker_color = "green"))
fig.update_layout(showlegend=False)

st.plotly_chart(fig)

st.write("Lowest cone point:", round(lowest_cone,2), "m")