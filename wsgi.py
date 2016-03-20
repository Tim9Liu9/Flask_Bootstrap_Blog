from app import create_app

# production   development
application = create_app('development')
print "flask blog app is starting ...-->"

if __name__ == '__main__':
    application.run()
