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
            


NINJA GOLD
server side
1. route "/" that renders the index.html page
2. route "/reset" that will reset the "game"
3. route "/process_money" that will do the logic for the gold
BONUS complete /process_money route without a different if check for each location


Client Side
index.html template from wireframe (don't worry about css too much)
each form should have a hidden inputs (input name should be "location")
have all forms go to "/process_money"
reset button that goes to "/reset"
show all previous activities (will be recieved as a list)
BONUS have activities color coded (red if lost money, green if gained)

'''