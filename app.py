<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
  <title>都道府県の気温グラフ</title>
  <!-- プロット用のJavaScriptライブラリを読み込む -->
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
  <h1>都道府県の気温グラフ</h1>
  <form action="/" method="post">
    <label for="prefecture">都道府県を選択：</label>
    <select id="prefecture" name="prefecture">
      {% for key, value in data.items() %}
      <option value="{{ key }}">{{ bc416e3c661ca0b18c9420c338ddc9ed }}</option>
      {% endfor %}
    </select>
    <button type="submit">グラフを表示</button>
  </form>

  {% if data %}
  <div id="graph-container"></div>

  <script type="text/javascript">
    // データを取得
    const xData = Object.keys({{ data|tojson }});
    const yData = Object.values({{ data|tojson }});

    // グラフのデータを設定
    const trace = {
      x: xData,
      y: yData,
      mode: 'bar',
      type: 'scatter'
    };

    const data = [trace];

    // グラフのレイアウトを設定
    const layout = {
      title: '都道府県の気温',
      xaxis: { title: '都道府県' },
      yaxis: { title: '気温 (℃)' }
    };

    // グラフを描画
    Plotly.newPlot('graph-container', data, layout);
  </script>
  {% endif %}
</body>
</html>

