from flask import Flask, render_template, jsonify, request


news = []
with open('news.txt', 'rt', encoding='utf-8') as f:
    n = int(f.readline())
    for i in range(n):
        item_id = int(f.readline())
        title = f.readline().strip()
        content = f.readline().strip()
        item = {'id': item_id, 'title': title, 'content': content}
        news.append(item)

app = Flask(__name__)

@app.get("/")
def index():
    return render_template('index.html', news=news)

@app.get("/news/<int:id>")
def get_content(id):
    return jsonify(news[id - 1])

@app.post("/news")
def post_news():
    data = request.json
    data["id"] = len(news) + 1
    news.append(data)
    return jsonify(data)