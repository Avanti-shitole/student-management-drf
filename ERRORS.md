## Error #1 – 404 Wrong URL

**Error:**
I got **404 Not Found** in Postman.

**URL:**
`http://127.0.0.1:8000/api/students/`

**What I did:**
I changed `students/` to `student/` in `urls.py` to create an error.

**Why:**
The URL in Postman and the URL in `urls.py` were different.

**Solution:**
I changed `student/` back to `students/` and tested the API again.

**What I learned:**
A wrong URL path can cause a 404 error.


## Error #2 – Authentication Error

**Error:**
I got:

`Authentication credentials were not provided.`

when I tried to get the student list.

**URL:**
`http://127.0.0.1:8000/api/students/`

**Why:**
The API has `IsAuthenticated`, but I did not provide a token with the request.

**Solution:**
I logged in using the login API, got the token, and added the token in Postman Authorization.

After that, the student list was displayed successfully.

**What I learned:**
For protected APIs, I need to provide valid authentication credentials/token.
