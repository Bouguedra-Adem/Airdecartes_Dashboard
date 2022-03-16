import dash_html_components as html
import dash
import datetime as date
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from callbacks_managers import CallbackManager
from ..Histogram.HistogramData import *
from ..Histogram.Histogram import *
from  .FiltreHTML import *
from ast import literal_eval
import http.client
import json

callback_managerFiltreHisto = CallbackManager()

#data=readDate("Assets\CSVFile\Taux_Pollution_Descartes.csv")



conn = http.client.HTTPSConnection("airdecartes.herokuapp.com")
payload = ''
headers = {}
conn.request("GET", "/AllCapteurData", payload, headers)
res = conn.getresponse()
datares = res.read()
data=pd.DataFrame(json.loads(datares.decode("utf-8")))

@callback_managerFiltreHisto .callback(
    [dash.dependencies.Output('example-graph', 'figure'),
     dash.dependencies.Output('datatable-interactivity', 'columns'),
     dash.dependencies.Output('datatable-interactivity', 'data'),
     dash.dependencies.Output('datatable-interactivity', 'style_data_conditional')]

    ,
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
    dash.dependencies.Input('my-date-picker-range', 'end_date'),
    dash.dependencies.Input('demo-dropdown', 'value'),
    ])

def update_output(start_date, end_date,value):
    data = readDate("Assets\CSVFile\Taux_Pollution_Descartes.csv")

    if ((start_date is not None) & ( end_date is not None)) :

        data['Dt']=pd.to_datetime(data['yearobservation'].astype(int).astype(str)+"-"+data['monthobservation'].astype(int).astype(str)).dt.strftime("%Y-%m")
        data['DtAxis'] ="Date_" +data['yearobservation'].astype(int).astype(str) + "-" + data['monthobservation'].astype(int).astype(str)
        print(data['DtAxis'])
        start_date_object = pd.to_datetime(start_date).strftime("%Y-%m")

        end_date_object = pd.to_datetime(end_date).strftime("%Y-%m")
        data=data[(data['Dt'] <= end_date_object) & (data['Dt'] >=start_date_object) ]
        data=data.sort_values(by=["Dt"])
        data2=data.groupby(['DtAxis']).agg({ 'temperature':"sum" ,"co2" :"sum" , "pression" :"sum","humidity" :"sum"}).reset_index()
        print ( data2)

        fig = go.Figure(go.Bar(x=data2['DtAxis'], y=data2['temperature'].tolist(), name='temperature'))
        fig.add_trace(go.Bar(x=data2['DtAxis'], y=data2["co2"].tolist(), name="co2"))
        fig.add_trace(go.Bar(x=data2['DtAxis'], y=data2["pression"].tolist(), name='pression'))
        fig.add_trace(go.Bar(x=data2['DtAxis'], y=data2["humidity"].tolist(), name="humidity"))
        fig.update_layout(barmode='stack', xaxis={'categoryorder': 'category ascending'})

        DataMoM=MoM(data,value).reset_index().rename({"index":"index_Month"},axis=1)
        columns = [{"name": i, "id": i} for i in  DataMoM.columns]
        df =  DataMoM.to_dict('records')

        heatmap = heatmapColor(DataMoM)
        return fig, columns, df, heatmap


    else :
        data['DtAxis'] ="Date_" +data['Year'].astype(int).astype(str) + "-" + data['Month'].astype(int).astype(str)
        data2=data.groupby(['DtAxis']).agg({ 'temperature':"sum" ,"co2" :"sum" , "pression" :"sum","humidity" :"sum"}).reset_index()

        fig = go.Figure(go.Bar(x=data2['DtAxis'], y=data2['temperature'].tolist(), name='temperature'))
        fig.add_trace(go.Bar(x=data2['DtAxis'], y=data2["co2"].tolist(), name="co2"))
        fig.add_trace(go.Bar(x=data2['DtAxis'], y=data2["pression"].tolist(), name='pression'))
        fig.add_trace(go.Bar(x=data2['DtAxis'], y=data2["humidity"].tolist(), name="humidity"))
        fig.update_layout(barmode='stack', xaxis={'categoryorder': 'category ascending'})
        fig = go.Figure([go.Bar(x=data['DtAxis'].astype(str).tolist(), y=data['pression'],
                                marker_color="rgb(6, 154, 151)")])
        fig.update_layout(title="Revenue Evolution & MoM", font=dict(family="Courier New, monospace", size=13))

        DataMoM = MoM(data,value).reset_index().rename({"index": "index_Month"}, axis=1)
        columns = [{"name": i, "id": i} for i in DataMoM.columns]
        df = DataMoM.to_dict('records')
        heatmap = heatmapColor(DataMoM)

        return fig, columns, df,heatmap




def MoM(data,value):
    Month = data.Dt.unique()
    Final_List = []
    i = 0
    for m in Month:
        ValueMonth = data[(data.Dt == m)][value].values[0]
        listvalue = []

        for k in range(0, i):
            listvalue.append("-")
        for m1 in range(i, len(Month)):
            ValueMonth1 = data[(data.Dt == Month[m1])][value].values[0]
            listvalue.append(   round(((ValueMonth1 - ValueMonth) / ValueMonth) * 100 ,2)  )

        Final_List.append(listvalue)
        i = i + 1
    return pd.DataFrame(Final_List, columns=Month, index=Month)




def heatmapColor(df) :

    heatmap=[]
    for i in range(0,df.index.shape[0] ) :
      for j in df.columns:
              if j =="index_Month" :
                  #RGB = int(((100 - value) * 255) / 100)
                  color = "rgb(133, 113, 48)"
                  color_option = str(
                      dict(_if=dict(row_index=i, column_id=j), backgroundColor=color, color="black")).replace("_if",
                                                                                                              "if")
                  res = literal_eval(color_option)
                  heatmap.append(res)
              else :
                  value=df.loc[i,[j]].values[0]


                  if value !="-" :
                          if value > 0 :
                            RGB = int(((100 - value) * 255) / 100)
                            color = "rgb({}, 255,{})".format(RGB, RGB)
                            color_option = str(dict(_if=dict(row_index=i, column_id=j), backgroundColor=color, color="black")).replace("_if","if")
                            res = literal_eval(color_option)
                            heatmap.append(res)
                          else :
                            RGB = int(((100 - (value*(-1))) * 255) / 100)
                            color = "rgb(255,{},{})".format(RGB+10, RGB)
                            color_option = str(dict(_if=dict(row_index=i, column_id=j), backgroundColor=color, color="black")).replace("_if","if")
                            res = literal_eval(color_option)
                            heatmap.append(res)


    return heatmap