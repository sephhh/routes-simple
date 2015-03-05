from bottle import route, run, static_file

@route('/home')
def home():
	return'''
		<button type="submit">Click a route!</button>
	'''


@route('/static/<filename>')
def server_static(filename):
		return static_file(filename, root='./files')

run(host='localhost', port=8080, debug=True)