from jinja2 import Template, Environment, FileSystemLoader
import json

# テンプレート読み込み
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tmpl = env.get_template('site/template.j2')

# 設定ファイル読み込み
with open('site/result.json', 'r', encoding='utf-8') as f:
    params = json.load(f)

# レンダリングして出力
rendered_html = tmpl.render(params)
with open('index.html', 'w' ,encoding='utf-8') as f:
    f.write(rendered_html)