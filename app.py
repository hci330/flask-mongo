import os
from mongoengine import connect
from models import Post

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Establishing a Connection


print('pwd', )
connect(
    'keeper_app',
    host='mongodb+srv://web-projects.lnztl.mongodb.net/keeper_app?retryWrites=true&w=majority',
    username='keeper_admin', 
    password=os.environ.get('PASSWORD')
)

def create_posts():
    post_1 = Post(
        title='Sample Post 1',
        content='Some engaging content',
        author='Scott'
    )
    post_1.save()       # This will perform an insert
    post_2 = Post(title='Sample Post 2', content='Content goes here', author='Michael')
    post_2.save()

# output all posts in the database:
for post in Post.objects:
    print(post.title)
