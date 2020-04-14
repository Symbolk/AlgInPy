# choose data structures according to functions to be implemented
class User:
    def __init__(self, userId):
        self.userId = userId
        self.follows = []
        self.posts = []

    def post(self, *tweet):
        self.posts.append(tweet)

    def get(self, users):
        res = []
        for i in self.follows:
            res.extend(users[i].posts)
        res.extend(self.posts)
        res = sorted(res, key=lambda x: x[0])
        return [i[1] for i in res[:10]]

    def follow(self, followeeId):
        if followeeId != self.userId and followeeId not in self.follows:
            self.follows.append(followeeId)

    def unfollow(self, followeeId):
        if followeeId != self.userId and followeeId in self.follows:
            self.follows.remove(followeeId)


class Twitter:
    def __init__(self):
        self.users = {}
        self.time = 0

    def valid_users(self, *ids):
        for i in ids:
            if i not in self.users:
                self.users[i] = User(i)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.valid_users(userId)
        self.users[userId].post(self.time, tweetId)
        # use negative time to make latest first in sorting asc later
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.valid_users(userId)
        # pass all users to get every one's posts
        return self.users[userId].get(self.users)

    def follow(self, followerId: int, followeeId: int) -> None:
        self.valid_users(followerId, followeeId)
        self.users[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.valid_users(followerId, followeeId)
        self.users[followerId].unfollow(followeeId)


# with dict: to keep user attributes
# with set: no-op checking
# with heap: n largest
from collections import deque
import heapq


class Twitter2:
    def __init__(self):
        self.users = {}
        self.Tid = 0  # global tweet id by time

    def _create_user(self, userId):
        F = {userId}  # followers set
        T = deque(maxlen=10)
        self.users[userId] = {'F': F, 'T': T}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self._create_user(userId)
        self.users[userId]['T'].append((self.Tid, tweetId))
        self.Tid += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        allT = []
        for uid in self.users[userId]['F']:
            allT.extend(list(self.users[uid]['T']))
        # default: min heap
        # get top k with nlargest(): time complexity: O(log(k) * n)
        return [T[1] for T in heapq.nlargest(10, allT)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self._create_user(followerId)
        if followeeId not in self.users:
            self._create_user(followeeId)
        self.users[followerId]['F'].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users and followeeId != followerId:
            self.users[followerId]['F'].discard(followeeId)



# use linked list to save tweets
# use heap to get n latest tweets
from collections import defaultdict
# import heapq

class Tweet:

    def __init__(self, tweetId, timestamp):
        self.id = tweetId
        self.timestamp = timestamp
        # linked list to save tweets
        self.next = None

    # override magic function to get max heap
    def __lt__(self, other):
        return self.timestamp > other.timestamp

class Twitter3:

    def __init__(self):
        # default to return an empty set instead of KeyError
        self.followings = defaultdict(set)
        # return None
        self.tweets = defaultdict(lambda: None)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        tweet = Tweet(tweetId, self.timestamp)
        tweet.next = self.tweets[userId]
        self.tweets[userId] = tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        heap = []

        tweet = self.tweets[userId]
        if tweet:
            heap.append(tweet)

        for user in self.followings[userId]:
            tweet = self.tweets[user]
            if tweet:
                heap.append(tweet)
        heapq.heapify(heap)

        while heap and len(tweets) < 10:
            head = heapq.heappop(heap)
            tweets.append(head.id)

            if head.next:
                heapq.heappush(heap, head.next)
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followings[followerId].discard(followeeId)