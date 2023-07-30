import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import base64  # base64モジュールの追加
import io  # ioモジュールの追加

# グローバル変数
app = dash.Dash(__name__)

# レイアウト
app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'ファイルをドラッグ&ドロップするか、',
            html.A('ファイルを選択してください。')
        ]),
        style={
            'width': '50%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # 複数のファイルのアップロードを許可する場合はTrueに設定します
        multiple=False
    ),
    dcc.Graph(id='graph')
])

# アップロードされたファイルを読み込んでグラフを作成するコールバック関数
@app.callback(Output('graph', 'figure'), [Input('upload-data', 'contents')])
def update_graph(contents):
    if contents is not None:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

        # グラフを作成
        fig = make_subplots(rows=1, cols=2)

        for col in df.columns:
            fig.add_trace(go.Scatter(x=df.index, y=df[col], mode='lines+markers', name=col), row=1, col=1)

        fig.update_layout(title='アップロードされたデータ', showlegend=True)

        return fig
    else:
        return go.Figure()

if __name__ == '__main__':
    app.run_server(debug=True)
