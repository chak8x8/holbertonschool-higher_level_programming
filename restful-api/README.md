RESTful API
===========

- Novice
- By: Javier Valenzani
- Weight: 1
- Your score will be updated as you progress.

Description
-----------

### Introduction

In the evolving world of software development, understanding how to communicate and transfer data efficiently between systems is essential. This project delves into the domain of **RESTful APIs**, a cornerstone in the realm of web services. The **Representational State Transfer (REST)** architecture is a set of constraints ensuring a scalable, stateless, and cacheable communication system. This approach allows for easy integration of web services, making them accessible to a wide range of applications.

---

### Learning Objectives

- **HTTP/HTTPS Basics**: Grasp the fundamentals of the web’s primary protocol, understanding how data is transferred, the methods involved, and the distinction between secure and non-secure communication.

- **API Consumption with Command Line**: Gain hands-on experience consuming APIs using basic command-line tools, building a foundation for more advanced API interactions.

- **API Consumption with Python**: Leverage Python’s abilities to fetch, process, and manipulate data from APIs.

- **API Development with http.server**: Learn the basics of creating an API from scratch using Python’s built-in modules – a solid starting point.

- **API Development with Flask**: Delve deeper into API development using the lightweight Flask framework, focusing on routing, data management, and scalability considerations.

- **API Security & Authentication**: Understand how to secure data transfer and ensure authorized access to resources – a crucial aspect of modern web services.

- **API Standards & Documentation with OpenAPI**: Explore the importance of standardized documentation, guaranteeing that APIs remain usable, understandable, and maintainable.

---

#### Importance

In today’s interconnected digital landscape, RESTful APIs are pivotal in integrating disparate systems. They act as intermediaries, interpreting client requests into meaningful actions, fetching relevant data, or triggering necessary procedures. From social media data-sharing to sophisticated industrial automation, APIs form the backbone of modern software ecosystems.

A strong grasp of how to consume, develop, secure, and document these APIs provides an invaluable skill set for developers. It blends both technical detail and overarching design patterns, ensuring reliable, scalable, and user-friendly communication in the digital sphere.

---

### REST API Conceptual Diagram
+-------+ +-------+ +---------+ +---------+ | | Request | | Process | | Fetch/ | | | | -----> | | -------> | | Modify | | | | | | | | -------> | | | | <----- | | <------- | | | | | | Response | | Return | | | | +-------+ +-------+ +---------+ +---------+ Client Web Server API Server Database


**Components**:

- **Client**: The requester (often a browser or application).
- **Web Server**: Receives incoming requests, might handle routing/load-balancing before passing to the API.
- **API Server**: The logic layer that processes requests, determines needed data or actions.
- **Database**: Stores data which the API can fetch or update.

**Flow**:

1. **Client** sends an HTTP/HTTPS request to the **Web Server**.
2. **Web Server** forwards the request to the **API Server**.
3. **API Server** processes the request, possibly interacting with the **Database**.
4. **API Server** returns a response to the **Web Server**.
5. **Web Server** sends the final HTTP/HTTPS response back to the **Client**.

In simpler setups, Web Server and API Server might be merged. This depiction helps visualize layered or scaled environments.

---

Tasks
-----

### 0. Basics of HTTP/HTTPS

**mandatory**

**Background**:  
The Hypertext Transfer Protocol (**HTTP**) is the foundation of data communication on the web. It enables web clients (e.g., browsers) to communicate with web servers. Over time, HTTP evolved and also gained a secure variant, **HTTPS**. HTTPS uses SSL/TLS encryption on top of HTTP, protecting data from eavesdropping or tampering.

**Objective**:  
By the end of this exercise, you should be able to:

- Differentiate **HTTP** vs. **HTTPS**  
- Understand the basic request/response structure of HTTP  
- Recognize and explain common HTTP methods and status codes

**Resources**:
- [MDN - Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [Difference Between HTTP and HTTPS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Connection_handling_in_HTTPS#overriding_connection_parameters)
- [List of HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

#### Instructions

1. **Differentiating HTTP and HTTPS**:
   - Read the resources on the differences between HTTP and HTTPS.
   - Note the main security distinctions: encryption, certificates, integrity.

2. **Understanding HTTP Structure**:
   - Open your browser’s Developer Tools (Network tab).
   - Reload a simple page; observe the first request’s **Headers**, method, path, status, etc.

3. **Exploring HTTP Methods & Status Codes**:
   - List **four** common methods (GET, POST, etc.) with usage scenarios.
   - List **five** status codes (2xx, 3xx, 4xx, 5xx). Provide short descriptions and possible scenarios.

**Hints**:
- **HTTPS** encrypts the data in transit, **HTTP** does not.
- HTTP methods define the intended action (fetch data, create resource, etc.).
- Status codes indicate the request outcome (success, client error, server error, etc.).

**Expected Output**:
- A short summary contrasting **HTTP** vs. **HTTPS**.
- A depiction/outline of **HTTP request/response** structure.
- Two lists:
  - Common HTTP Methods (4 items).
  - Common HTTP Status Codes (5 items), each with a scenario.

---

### 1. Consume data from an API using command line tools (curl)

**mandatory**

**Background**:  
**curl** is a command-line tool to transfer data with various protocols (HTTP, HTTPS, FTP...). It’s widely used for testing/debugging REST APIs. Mastering curl helps quickly prototype requests, diagnose server issues, etc.

**Objective**:  
By the end of this exercise, you should be able to:

- Install and use **curl** from the command line
- Construct and execute basic API requests
- Interpret results of common API requests

**Resources**:
- [Everything curl](https://everything.curl.dev)
- [Using cURL with HTTP APIs](https://www.baeldung.com/curl-rest)

**Instructions**:

1. **Installing & Basic Interaction**:
   - Install **curl** (commonly pre-installed on Linux/Mac). On Windows, install or use WSL.
   - Run `curl --version` to confirm.
   - Fetch a webpage: `curl http://example.com`.

2. **Fetching Data from an API**:
   - Retrieve posts from JSONPlaceholder:
     ```bash
     curl https://jsonplaceholder.typicode.com/posts
     ```
   - Observe the JSON output.

3. **Using Headers & Other Options**:
   - Show only response headers:
     ```bash
     curl -I https://jsonplaceholder.typicode.com/posts
     ```
   - Make a POST request:
     ```bash
     curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
     ```

**Hints**:
- `-I` fetches **only headers**.
- `-X` specifies the HTTP method (e.g. POST).
- `-d` includes data in the request body.

**Expected Output**:
- `curl --version` → details about installed curl.
- GETing posts from JSONPlaceholder → large JSON array of posts.
- `-I` request → status code, headers, etc.
- POST request → server response, e.g., a new resource with `id: 101` (simulated).

---

### 2. Consuming and processing data from an API using Python

**mandatory**

**Background**:  
Python is widely used for web services due to its readability and robust ecosystem. The **requests** library simplifies HTTP interactions, and Python’s built-ins facilitate data parsing and manipulation.

**Objective**:  
By the end of this exercise, you should be able to:

- Use `requests` to send HTTP requests and handle responses
- Parse and manipulate JSON in Python
- Convert structured data into another format (CSV, etc.)

**Resources**:
- [Python Requests Library](https://docs.python-requests.org/en/master/)
- [Working with JSON in Python](https://docs.python.org/3/library/json.html)
- Public API: [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

**Instructions**:

1. **Install requests** if needed: `pip install requests`.
2. **Write** a Python script to:
   - Fetch posts from JSONPlaceholder using `requests.get()`.
   - Print the status code (e.g. `Status Code: 200`).
   - If successful, parse the JSON (using `.json()`).
   - Print the titles of all the posts.

3. **Write** a second function to:
   - Fetch the same data.
   - Convert it into a list of dictionaries (keys: `id`, `title`, `body`).
   - Write these to `posts.csv` with columns matching dictionary keys.

**Hints**:
- `requests.get(...) → response`  
  `response.status_code, response.json()`
- `csv.DictWriter` can help write dictionaries to CSV.

**Expected Output**:
- A **"Status Code: 200"** message if successful.
- Printed **titles** of the fetched posts.
- A **posts.csv** file containing columns (`id`, `title`, `body`) with each row from the JSON data.

**Repo**:

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `restful-api`
- File: `task_02_requests.py`

---

### 3. Develop a simple API using Python with the `http.server` module

**mandatory**

**Background**:  
Python’s **http.server** module provides classes for simple web servers. Though not used in production typically, it’s good for learning and quick tests.

**Objective**:
- Set up a minimal web server with **http.server**.
- Handle GET, POST, etc.
- Serve JSON data on specific endpoints.

**Resources**:
- [Python docs: http.server](https://docs.python.org/3/library/http.server.html)
- [A Simple http.server Example](https://realpython.com/python-sockets/#echo-server)

**Instructions**:

1. **Basic HTTP Server**:
   - Subclass `http.server.BaseHTTPRequestHandler`.
   - Implement `do_GET` to respond with **"Hello, this is a simple API!"** for the root path (`/`).
   - Start on port `8000`; test with `curl http://localhost:8000`.

2. **Serving JSON**:
   - Modify `do_GET` to serve some JSON if the path is `/data`.
   - Return something like `{"name":"John","age":30,"city":"New York"}`.
   - Make sure to set `Content-type: application/json`.

3. **Different Endpoints**:
   - `/status` → returns "OK".
   - Any undefined path → `404 Not Found`.

**Hints**:
- Use `self.send_response(...)`, `self.send_header(...)`, `self.end_headers()`.
- Convert a Python dict to JSON with `json.dumps(...)`.

**Expected Output**:
- Root path → "Hello, this is a simple API!"
- `/data` → JSON object with sample data.
- `/status` → "OK"
- Anything else → 404 Not Found + "Endpoint not found"

**Repo**:

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `restful-api`
- File: `task_03_http_server.py`

---

### 4. Develop a Simple API using Python with Flask

**mandatory**

**Background**:  
**Flask** is a lightweight Python web framework often used for small/medium web apps and RESTful APIs. Its minimalism and modular approach make it beginner-friendly yet powerful enough for production in many cases.

**Objective**:
- Set up a Flask app and run a dev server.
- Define and handle routes for different endpoints.
- Serve JSON data with Flask.
- Handle POST requests to add new data.

**Resources**:
- [Flask Official Documentation](https://flask.palletsprojects.com/en/latest/)
- Start with **“A Minimal Application”** in the Quickstart.

**Instructions**:

1. **Setup**:
   - `pip install Flask`.
   - `from flask import Flask`.
   - `app = Flask(__name__)`.

2. **First Endpoint** (`/`):
   - Return `"Welcome to the Flask API!"`.

3. **Serving JSON**:
   - `from flask import jsonify`.
   - Keep a dictionary `users` in memory: `{"jane": {...}, "john": {...}}`.
   - `/data` → return a list of all usernames with `jsonify()`.

4. **Expand**:
   - `/status` → "OK".
   - `/users/<username>` → returns the user’s full object or `{"error":"User not found"}` if absent.

5. **Handling POST**:
   - `from flask import request`.
   - `/add_user` → parse JSON with `request.get_json()`.
   - A sample body: `{"username":"alice","name":"Alice","age":25,"city":"San Francisco"}`
   - If successful, add to `users`, return `{"message":"User added","user":{...}}` with **201** code.
   - If missing username, return `{"error":"Username is required"}` with **400** code.

**Hints**:
- `@app.route("/data")`: declare route. Return `jsonify(...)`.
- For dynamic routes: `@app.route("/users/<username>")`.
- Check user existence in the dictionary. Return 404 or a user object if found.

**Expected Output**:
- Root path: `"Welcome to the Flask API!"`.
- `/data`: e.g. `["jane", "john"]`.
- `/status`: `"OK"`.
- `/users/jane`: returns the user’s object or `{"error":"User not found"}`.
- `/add_user`: `POST` data. If valid, store and return 201 status + user data. If no `username`, 400 error + `{"error":"Username is required"}`.

**Repo**:

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `restful-api`
- File: `task_04_flask.py`

---

### 5. API Security and Authentication Techniques

**mandatory**

**Background**:
API security is critical. If an API is publicly accessible, it’s prone to unauthorized access, data tampering, or other attacks. Common solutions involve authentication (verifying user identity) and authorization (verifying privileges).

**Objective**:
- Understand API security importance
- Implement basic auth with Flask
- Implement token-based auth with JWT
- Differentiate authentication from authorization

**Resources**:
- [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
- [Intro to JSON Web Tokens](https://jwt.io/introduction)

**Instructions**:

1. **Basic Authentication**:
   - Install `Flask-HTTPAuth`.
   - Create a user list with hashed passwords (via `werkzeug.security`).
   - Decorate protected routes with `@auth.login_required`.

2. **Token-based Auth with JWT**:
   - Install `Flask-JWT-Extended`.
   - Use a secret key for token gen/validation.
   - `/login`: user logs in, gets a JWT. E.g., returns `{"access_token":"<JWT>"}`.
   - Protect routes with `@jwt_required()`.
   - (Optional) Implement role-based access (admin vs. user).

3. **Error Handling**:
   - Return **401** for missing/invalid tokens or credentials.
   - Return **403** if user’s token is valid but lacks privileges for an endpoint.

**API Specs**:
- Basic Auth:
  - `/basic-protected` → GET → "Basic Auth: Access Granted" if correct creds, else 401.
- JWT Auth:
  - `/login` → POST JSON `{"username":"...","password":"..."}` → returns JWT on success.
  - `/jwt-protected` → GET → "JWT Auth: Access Granted" if token valid, else 401.
  - `/admin-only` → GET → requires admin role. If user not admin → 403 with `{"error":"Admin access required"}`, else "Admin Access: Granted".

**Expected Output**:
- Attempting `/basic-protected` with no creds → 401, with correct creds → "Basic Auth: Access Granted".
- `/login` with correct user → returns `{"access_token":"<some_jwt>"}`.
- `/jwt-protected` with invalid/missing token → 401, with valid token → "JWT Auth: Access Granted".
- `/admin-only` with non-admin → 403, with admin token → "Admin Access: Granted".

**Hints**:
- Return **401** for all authentication failures consistently.
- Use `werkzeug.security.generate_password_hash(...)` and `check_password_hash(...)` for user creds.
- For JWT, embed role info to check for admin routes.

**Repo**:

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `restful-api`
- File: `task_05_basic_security.py`