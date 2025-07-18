"""
Problem: 355. Design Twitter
Date Completed: 7/18/2025
"""

class Twitter:

    def __init__(self):
        # Key = User; Values = Posts of the User
        self.post = defaultdict(list)
        # Key = User; Values = IDs that the user follows
        self.following = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Increment Time
        self.time += 1
        # Add this post to the user with time it was posted
        self.post[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        # Total posts include all posts available to the user, including their own posts
        totalPosts = list(self.post[userId])
        # Add all the posts of users this user is following
        for i in self.following[userId]:
            for j in self.post[i]:
                totalPosts.append(j)
        # Sort the list
        totalPosts = sorted(totalPosts, reverse=True)
        # Build ans array with only the 10 most recent posts
        ans = []
        for i in range(min(10, len(totalPosts))):
            ans.append(totalPosts[i][1])
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        # If the user doesnt already follow and isnt following themself, add new user to following
        if followeeId not in self.following[followerId] and followerId != followeeId:
            self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # If the user is already following and isnt unfollowing themself, remove user from following
        if followeeId in self.following[followerId] and followerId != followeeId:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
