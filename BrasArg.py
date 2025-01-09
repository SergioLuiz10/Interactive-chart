import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv("C:\\Users\\sergi\\.vscode\\BrasArg\\imigrantes_canada.csv")


def brasa():
 df_bras_arg = df.query('País in ["Brasil", "Argentina"]')

 df_bras_arg = df_bras_arg.melt(id_vars=["País"], var_name="ano", value_name="imigrantes")

 df_bras_arg['ano'] = df_bras_arg['ano'].astype(str)

 fig = go.Figure()

 df_brasil = df_bras_arg[df_bras_arg["País"] == "Brasil"]
 fig.add_trace(
    go.Scatter(x=df_brasil['ano'], y=df_brasil['imigrantes'], mode='lines', name='Imigrantes do Brasil', line=dict(width=4))
 )

 df_argentina = df_bras_arg[df_bras_arg["País"] == "Argentina"]
 fig.add_trace(
    go.Scatter(x=df_argentina['ano'], y=df_argentina['imigrantes'], mode='lines', name='Imigrantes da Argentina', line=dict(width=4))
 )

 fig.update_layout(
    title=dict(
        text='<b>Imigração do Brasil e da Argentina para o Canadá no período de 1980 a 2013</b>',
        x=0.1,
        font=dict(size=18)
    ),
    xaxis=dict(
        title='<b>Ano</b>',
        type='category',  
        tickmode='array',
        tickvals=[str(i) for i in range(1980, 2014)],  
        ticktext=[str(i) for i in range(1980, 2014)],  
    ),
    yaxis=dict(range=[0, 3000], autorange=False, title='<b>Número de imigrantes</b>'),
    updatemenus=[
        dict(
            type='buttons',
            showactive=False,
            buttons=[
                dict(
                    label='Play',
                    method='animate',
                    args=[None, {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True}]
                ),
                dict(
                    label='Pause',
                    method='animate',
                    args=[[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate'}]
                ),
                dict(
                    label='Next',
                    method='animate',
                    args=[[None], {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': False}]
                ),
                dict(
                    label='Previous',
                    method='animate',
                    args=[[None], {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True}]
                )
            ]
        )
    ], 
    width=1200,
    height=600 
 )


 frames = []
 anos = [str(i) for i in range(1980, 2014)]  
 for ano in anos:
    frame_data = []
    for pais in ["Brasil", "Argentina"]:
        dados_pais = df_bras_arg[df_bras_arg["País"] == pais]
        dados_ano = dados_pais[dados_pais["ano"] <= ano]
        frame_data.append(
            go.Scatter(
                x=dados_ano["ano"],
                y=dados_ano["imigrantes"],
                mode="lines",
                name=f"Imigrantes de {pais}",
            )
        )
    frames.append(go.Frame(data=frame_data))

 fig.frames = frames

 fig.write_html("BrasileArgentina.html")
 fig.show()


brasa()