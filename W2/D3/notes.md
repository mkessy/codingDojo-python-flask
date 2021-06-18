## MVC

- M - models -> talk to the db
- V - views -> HTML
- C - connections -> is where routes live

### Folder Structure
- head (assignment name / project name)
    - flask_app (folder)
        - config (folder)
            - mysqlconnection.py (file)
        - controllers (folder)
            - controller_table_name.py (file)
        - models (folder)
            - model_table_name.py (file)
        - templates
            - index.html
        - static
            - css
                - style.css
            - js
                - script.js
        - __init\_\_.py (file)
    - server.py  (files)
    - pipfile (files)
    - pipfile.lock (files)
