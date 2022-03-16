from flask import Flask, render_template, request
from github import Github


app = Flask(__name__)


# Github username
username = g.search_repositories
# pygithub object
g = Github()
# get that user by username


@app.route('/search', methods=['GET'])
def search():
    searched = request.args.get('searched')

    for repo in g.search_users('slim'):
        print(repo)

    return render_template('search.html', searched=searched.get_user)


@app.route("/")
def print_repo():
    print('Was here')
    # search = g.search_users('slim')
    # for i in range(1, 5):
    #     print('user', )
    # print('yy', search.totalCount)
    #
    i = 0
    for user in g.search_users('slim'):
        i += 1
        print('user', user.name, user.login, user.repos_url)
        if i == 10:
            break

    user = g.get_user(username)

    for repo in user.get_repos():
        print(repo)
        # print("=" * 100)

    return render_template('index.html', user=user.get_repos())


if __name__ == '__main__':
    app.run(debug=True)

def get_user():
    return g.get_user(username)



def print_repo(repo):

    print("Full name:", repo.full_name)

    print("Description:", repo.description)

    print("Date created:", repo.created_at)

    print("Date of last push:", repo.pushed_at)

    print("Home Page:", repo.homepage)

    print("Language:", repo.language)

    print("Number of forks:", repo.forks)

    print("Number of stars:", repo.stargazers_count)
    print("-"*50)

# iterate over all public repositories
for repo in get_user().get_repos():
    print_repo(repo)
    print("="*100)



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
