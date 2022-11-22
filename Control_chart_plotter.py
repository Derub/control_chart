# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 16:41:47 2022

@author: fedes
"""

import pandas as pd
pd.options.plotting.backend = "plotly" #enble plotly as default pd plotter
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.io as pio
pio.renderers.default='browser'
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import numpy as np
from scipy.stats import norm

#import data
df=pd.read_excel('Test_table.ods', engine='odf')

# Definition
UCL=700
LCL=200


df_mean=df['Visitors'].mean()
df_sdv=df['Visitors'].std()

fig = make_subplots(rows=1, cols=2, shared_yaxes=True)

fig.add_trace(go.Scatter(x=df['Day Number'], 
                         y=df['Visitors'], 
                         mode='lines+markers',
                         line=dict(color='black'),
                         marker=dict(color='blue',size=8)), 
              row=1, col=1)

fig.add_hline(y=df_mean, 
               line_color='green',
               line_dash="dash")

fig.add_hline(y=UCL, 
               line_color='red')

fig.add_hline(y=LCL, 
               line_color='red')

fig.add_trace(go.Histogram(y=df['Visitors'],
                           nbinsy=(11),
                           marker_color='#FFA500',
                           opacity=0.75),
              row=1, col=2)

fig.update_layout(yaxis = dict(range=[LCL*0.8, UCL*1.2]))
fig.update_layout(height=600, width=800,
                  title_text="Control Chart")

y_linspace = np.linspace(LCL*0.8, UCL*1.2, 100)
p = norm.pdf(y_linspace, df_mean, df_sdv)

fig.add_trace(go.Scatter(x=p, 
                         y=y_linspace,
                         line=dict(color='red'),), 
              row=1, col=2 )

fig.data[2].update(xaxis='x4')



fig.update_layout(xaxis4=dict(
        anchor="y",
        overlaying="x2",
        side="top",
        position=0.0,
        visible=False, showticklabels=False
    ))

# make room to display double x-axes
fig.update_layout(yaxis1=dict(domain=[0.1, 1]),
                  yaxis2=dict(domain=[0.1, 1]),
                 )

fig.show()

