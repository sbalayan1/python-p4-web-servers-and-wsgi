#!/usr/bin/env python3


# werkzeug is a a WSGI library. WSGI stands for Web Server Gateway Interface. WSGI is a specification that tells our Python code how to best communicate over HTTP/HTTPs

# #Werkzeug comes with a number of features out of the box
    # An in-browser debugger.
    # Robust classes for requests and responses.
    # Routing, auto-generation and management of URLs.
    # A development server.
    # A testing framework that does not require a running server.

from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    print(f'This web server is running at {request.remote_addr}') ###note this will be printed where your server runs

    return Response('A WSGI generated this reponse') ###this gets displayed in the browser

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=5555,
        application = application #this application IS the application function we defined above and it's assigned to the application argument required for run_simple
    )


#python server/werkzeug_app.py runs the file