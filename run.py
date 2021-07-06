from flaskblog import create_app

#Driver function
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)