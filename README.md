# Comment_App_API

A simple Django REST Framework-based Comment App API using **Function-Based Views**, built under MVT architecture with reusable modules and proper exception handling.

---

##  Features :

- Add, view, and delete comments via REST API
- Function-based views (FBVs)
- Custom business logic modules
- JSON-only responses using DRF serializers
- Admin panel to manage comments
- Clean error handling and modular structure

---
## Project Structure :
```
comment_project/
│
├── comment_app/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── services.py
│   ├── views.py
│   ├── urls.py
│
├── comment_project/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
```
---

## API Endpoints :

| Method | Endpoint                     | Description          |
|--------|------------------------------|----------------------|
| GET    | `/api/comments/`             | List all comments    |
| POST   | `/api/comments/add/`         | Add a new comment    |
| DELETE | `/api/comments/delete/<id>/` | Delete a comment     |

---

## Admin Panel:
   ```
    Visit:
    http://127.0.0.1:8000/admin/
    Log in with your superuser credentials to manage comments.
    username : root
    E-mail : root@gmail.com
    password : root
  ```
---

 Technologies Used :
      - Django
      - Django REST Framework (DRF)
      - SQLite (default DB)

Testing :
      - Use Postman or browser for GET, POST, and DELETE requests.  
        You can also test using Django Admin.
