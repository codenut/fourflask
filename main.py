from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('main.html')

@app.route("/results", methods=['POST', 'GET'])
def results():
  words = []
  word = request.args.get('word')
  length = request.args.get('len')
  print word, length
  if(length.isdigit()):
    length = int(length)
    words = get(word, length)
  return render_template('list.html', words=words, word=word, length=length)

def cntchr(word):
  r = {}
  for c in word:
    if c in r:
      r[c] = r[c] + 1
    else:
      r[c] = 1
  return r

dic, ana = [], []

def loadwords():
  br = open('dic.txt')
  for line in br:
    line = line.strip()
    dic.append(line)
    ana.append(''.join(sorted(line)))

def get(word, length):
  res = []
  str = word.replace(' ', '')
  str = ''.join(sorted(str)).lower()
  strdic = cntchr(str)
  for i in range(len(ana)):
    sdic, has = strdic.copy(), True
    for c in ana[i]:
      if c in sdic and sdic[c] > 0:
        sdic[c] = sdic[c] - 1
      else:
        has = False
        break
    if has and len(dic[i]) == length:
      res.append(dic[i])
  return res

if __name__ == "__main__":
  loadwords()
  app.run()
