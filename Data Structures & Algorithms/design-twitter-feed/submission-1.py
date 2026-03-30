class Twitter:

    def __init__(self):
        # followers no need to consider order
        self.following = defaultdict(set)
        # tweets need to preserve time order
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for user in self.following[userId] | {userId}:
            for time, tweet in self.tweets[user]:
                if len(heap) < 10:
                    heapq.heappush(heap, (time, tweet))
                elif time > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (time, tweet))
        
        # heap has 10 most recent tweets where root is the oldest tweet.
        # print these to a list
        res = []
        while heap:
            time, tweet = heapq.heappop(heap)
            res.append(tweet)

        # res is now oldest → newest, but we want newest → oldest
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
