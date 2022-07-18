### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  Python is used more for server-side scripting while Javascript is more commonly used for client-side scripting

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  Use the get() method. If it is not found it will return the value. The second way would be to use the setdefault() method. You can also use the defaultdict as an arguement. If the key is not found the default factory value is returned. 

- What is a unit test?

  A unit test is a testing method written to test a single component or small pieces of code in an application. 

- What is an integration test?

  Program units are combines and tested as groups in multiple ways

- What is the role of web application framework, like Flask?

  Provides set of functions, classes, etc. that help you define which requests to resond to and how to respond to requests. 
  Web Back-end server framework that works with Python. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). 

  The difference between them is that you can use query strings to be more specific and descriptive with a search.

- How do you collect data from a URL placeholder parameter using Flask?
 
 You can specify the variable in the app.route. ex: @app.route

- How do you collect data from the query string using Flask?

You can collect data from a query string with request.args[]

- How do you collect data from the body of the request using Flask?

You can collect data from the body of the request using the request.form dictonary 

- What is a cookie and what kinds of things are they commonly used for?

A cookie is information that a website puts on a users comuter. Cookies store limited inofmration from a web browser session on a website 

- What is the session object in Flask?

Contain info for the currenct brower and perserve type (ex: lists stray lists, etc). These sessions are typically "signed", so users can't modify data.

- What does Flask's `jsonify()` do?

Flask's  `jsonify()` takes JSON data in python and it converts it to JSON string. 


