#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
class Twitter:

    # method 1: sorting
    
    def __init__(self):

        self.followMap = defaultdict(set)  # Store userID (follower) : set of followee userIDs

        self.time = 0

        self.tweetMap = defaultdict(list)  # Store userID : list of (time, tweetID)
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.tweetMap[userId].append((self.time, tweetId))

        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        feed = self.tweetMap[userId][:]   # [:] Make a copy of that list

        for followeeId in self.followMap[userId]: 

              feed.extend(self.tweetMap[followeeId]) # feed.extend(self.tweetMap[followeeId][:])
                                                     # Use .extend instead of .append to keep the structure

        feed.sort(key = lambda x: -x[0])  # -1 for reverse sorting

        return [tweetId for _, tweetId in feed[:10]] # feed[0:10] works too


    def follow(self, followerId: int, followeeId: int) -> None:

        self.followMap[followerId].add(followeeId)
        


    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followeeId in self.followMap[followerId]: 

            self.followMap[followerId].remove(followeeId)
        

    # method 2: heap

    # def __init__(self):
        

    # def postTweet(self, userId: int, tweetId: int) -> None:
        

    # def getNewsFeed(self, userId: int) -> List[int]:
        

    # def follow(self, followerId: int, followeeId: int) -> None:
        

    # def unfollow(self, followerId: int, followeeId: int) -> None:


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end


# followMap = {
#     1: {2, 3},      # user 1 follows users 2 and 3
#     4: {2}          # user 4 follows user 2
# }

# tweetMap = {
#     1: [(0, 501), (2, 502)],      # user 1's tweets, in time order
#     2: [(1, 601)],                # user 2's tweets
# }