from flask import Flask, request

app = Flask(__name__)

@app.route('/keyboard', methods=['GET','POST'])
def keyboard():
    return """{
        "type" : "buttons",
        "buttons" : [
            "포켓몬1",
            "포켓몬2"
        ]
    }"""

@app.route('/message', methods=['GET','POST'])
def message():
    userRequest = request.get_json()
    if userRequest['content'] == u"포켓몬1":
        return """{
            "message":{
                "text":"포켓몬1"
            }
        }"""
    else :
        return """{
            "message":{
                "text":"포켓몬2"
            }
        }"""



"""
@app.route("/friend", methods=['DELETE', 'POST'])
def friend():
    return
    {
        "user_key": "HASHED_USER_KEY"
    }


@app.route("/chat_room/:user_key", methods=['DELETE'])
def friendDel():
    pass
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)







