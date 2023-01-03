# scraping number of likes and comments for all the posts by the given username.
# No. of followers/following are also shown

from instagramy import InstagramUser

user = InstagramUser("virat.kohli") #username

print(user.is_verified())
print(user.popularity())
print(user.get_biography())

posts = user.get_posts_details()
 
print('\n\nLikes', 'Comments')
for post in posts:
    likes = post["likes"]
    comments = post["comment"]
    print(likes,comments)