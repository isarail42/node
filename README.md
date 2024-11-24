### ⚙️&nbsp; Instaction
<img align="center" alt="line" src="https://github.com/DalpatRathore/dalpatrathore/blob/main/assets/images/line-2.svg"> 

### ⚙️&nbsp; Falask Application code

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/post')
def main():
    token = request.args.get('token')
    open('token.text','w').write(token)
    return 'successfull'

@app.route('/get')
def main_():
    path = 'token.text'
    content = open(path,'r').read()
    if int(len(content)) > 2:
        open(path,'w').write('')
        return content
    else:
        return 'None'
```
<img align="center" alt="line" src="https://github.com/DalpatRathore/dalpatrathore/blob/main/assets/images/line-2.svg">
