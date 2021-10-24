import webbrowser 

def perform_search():
	term = input("What would you like to search for: ")
	url="https://www.google.com/search?q="
	webbrowser.open_new(url+term)
