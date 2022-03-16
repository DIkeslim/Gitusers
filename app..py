from flask import Flask, render_template
from flask import request
import requests
from github import Github



app = Flask(__name__)

# github username
username = "Dikeslim"

g = Github()
# url to request
url = f"https://api.github.com/users/Dikeslim/repos"
# make the request and return the json
user_data = requests.get(url).json()
#print(user_data)



@app.route("/")
def print_repo():
     user_data = requests.get(url).json()

     for repo in user_data:
          print(repo)
          #print("=" * 100)

     return render_template('index.html', user=user_data)


@app.route('/search', methods=[ 'GET','POST'])
def search():

    user_search = request.args['search']
    search_res = list()

    i = 0
    for user in g.search_users(user_search):
        i += 1
        print(user)
        #print('user', user.name, user.login, user.repos_url)
        # search_res.append(dict(name=user.name, username=user.login, repo_url=user.repos_url))
        search_res.append({
                            "name": user.name,
                            "username": user.login,
                            "repo_url": user.repos_url,
                        })
        if i == 5:
            break

    print('search result', search_res)

    return render_template('search.html', search=search_res)



if __name__ == '__main__':
    app.run(debug=True)
