import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import serial
import time
import struct
import sys
#_______________________________________________

ser = serial.Serial(
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    port = "COM5",
    baudrate=115200
)

#_______________________________________________
startByte=16
setMode=33
URL=float(120)          # Upper Rate Limit (in BPM)
LRL=float(60)           # Lower Rate Limit (in BPM)
aAmp=float(3.5)         # Atrial Pulse Amplitude (in V)
vAmp=float(3.5)         # Ventricular Pulse Amplitude (in V)
aWid=float(200)          # Atrial Pulse Width (in msec)
vWid=float(200)          # Ventricular Pulse Width (in msec)
mode=2            # Pacemaker mode (VOO=0,VOOR=1,AOO=2,AOOR=3,VVI=4,VVIR=5,AAI=6,AAIR=7
VRP=float(100)          # Ventricular Refractory Period (in msec)
ARP=float(100)          # Atrial Refractory Period (in msec)
hyst=float(0)           # Hysteresis (no clue)
respFac=float(8)        # Reponse Factor (1-16)
MSR=float(120)          # Maximum Sensor Rate (in BPM)
actThr=float(0.5)       # Activity Threshold (Should have numbers corresponding to accelerometer values (in g) - VLow,Low,MedLow,Med,MedHigh,High,VHigh)
rxnTim=float(3)         # Reaction time to activity (in sec)
recTim=float(3)         # Recovery time from activity (in sec)
var=struct.pack('<BBddddddBdddddddd',startByte,setMode,URL,LRL,aAmp,vAmp,aWid,vWid,mode,VRP,ARP,hyst,respFac,MSR,actThr,rxnTim,recTim)
#_______________________________________________
#_______________________________________________
#_______________________________________________


X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)


app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*1000
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),
              events=[Event('graph-update', 'interval')])
def update_graph_scatter():
    ser.write(var)
    read_data = ser.read(113)

    URL = struct.unpack_from('=d', read_data[0:8])
    LRL = struct.unpack('d', read_data[8:16])
    aAmp = struct.unpack('d', read_data[16:24])
    vAmp = struct.unpack('d', read_data[24:32])
    aWid = struct.unpack('d', read_data[32:40])
    vWid = struct.unpack('d', read_data[40:48])
    mode = struct.unpack('B', read_data[48:49])  # Pacemaker mode (VOO=0,VOOR=1,AOO=2,AOOR=3,VVI=4,VVIR=5,AAI=6,AAIR=7
    VRP = struct.unpack('d', read_data[49:57])
    ARP = struct.unpack('d', read_data[57:65])
    hyst = struct.unpack('d', read_data[65:73])
    respFac = struct.unpack('d', read_data[73:81])
    MSR = struct.unpack('d', read_data[81:89])
    actThr = struct.unpack('d', read_data[89:97])
    rxnTim = struct.unpack('d', read_data[97:105])
    recTim = struct.unpack('d', read_data[105:113])
    X.append(X[-1]+1)
    Y.append(URL*3.3)

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),)}



app.run_server(debug=True)




