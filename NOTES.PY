'''
-> static (folder)
    -> css (folder)
        style.css (file)
    -> js (folder)
        -> script.js (file)
    -> img (folder)
        -> my_img.jpeg (file)

    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}"

    POST
    - HTML element 
        -> form
            <form action="/process_new_user" method="POST">
                <button>Submit</button>
            </form>
            
'''