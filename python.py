banned_users = ['andrew', 'carolina', 'david']
user = ['juliet', 'jane', 'andrwe', 'david']
if user not in banned_users:
    print(f"{user}, you can post a response if you wish.")
else:
    print(f"{user} sorry but you are banned from posting a comment")