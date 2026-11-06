from flask import Flask,jsonify

app=Flask(__name__)

@app.route("/api/student")

def student():
    return jsonify({
        "name":"priya",
        "branch":"Csm",
        "year":4
    })

if __name__=="__main__":
    app.run(debug=True)