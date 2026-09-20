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
