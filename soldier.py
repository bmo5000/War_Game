from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def form_info():
	html_code =''
	html_code = html_code + '<form name = "submit" action = "/submit" method = "POST">'
	html_code = html_code + 'Fullname:<input type = "text" name = "name"><br>'
	html_code = html_code + 'Username:<input type = "text" name = "user"><br>'
	html_code = html_code + 'Birthday:<input type="text" name = "bday"><br>'
	html_code = html_code + '<input type="submit" value = "submit"></form>'
	return html_code



@app.route("/level")
def hello():
	return "Hi, You ready for a treasure hunt? " '<a href="/test2 ">GO </a>'
@app.route('/test2')
def test():
	return "Something is down there you should" '<a href= "/test3"> Go down there! </a>'
@app.route('/test3')
def test2():
	return "There's treasure! you should" ' <a href= "/test4"> Leave it there and turn around</a> '  '<a href= "/test5"> Pick it up!</a>'
@app.route('/test4')
def test4():
	return "you walked away you are done. :)" '<a href = "/"> Restart</a>'

@app.route('/test5')
def test5():
	return "A pirate saw you pick up the treasure" ' <a href= "/test6"> Put the treasure down</a> ' ' <a href = "/test7"> Run away with the treasure<a/> '
@app.route('/test6')
def test6():
	return "You are now trap now what?" ' <a href = "/test8"> Fight the pirate</a> ' ' <a href = "/test9"> Find your way out</a> '
@app.route ('/test7')
def test7():
	return "You ran away with the treasure! You won!" ' <a href ="/"> Restart</a> '
@app.route ('/test8')
def test8():
	return "The pirate have a gun!" ' <a href = "/test10">Run Away!</a> ' ' <a href = "/test11"> Take the gun </a> '
@app.route('/test9')
def test9():
	return "You found your way out but the treasure is Gone :(" ' <a href = "/"> Restart</a> '
@app.route('/test10')
def test10():
	return "You forgot the treasure! now the pirate has it" ' <a href = "/"> Restart</a> '
@app.route('/test11')
def test11():
	return "You got him and now you have the treasure!" ' <a href = "/"> Restart</a> '


@app.route('/submit', methods=['POST'])
def Submit():
	Fullname = request.form['name'] 
	Username = request.form['user'] 
	Birthday = request.form['bday']
	return Fullname + Username + Birthday+ "Congratulations! you are now registered! <a href='/level'>Start</a>"




if __name__ == "__main__":
	    app.debug = True
	    app.run()