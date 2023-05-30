import time

class PushNotification:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def notify_all(self, message):
        for subscriber in self.subscribers:
            subscriber.receive_notification(message)

class User:
    def __init__(self, name):
        self.name = name

    def receive_notification(self, message):
        print(f'{self.name} received a notification: {message}')

# Creating instances of users
user1 = User('John')
user2 = User('Emma')
user3 = User('Michael')

# Creating an instance of push notification service
push_notification = PushNotification()

# Subscribing users to push notification service
push_notification.subscribe(user1)
push_notification.subscribe(user2)
push_notification.subscribe(user3)

# Sending a notification to all subscribers
push_notification.notify_all('New product launch!')

# Simulating a delay or processing time
time.sleep(2)

# Unsubscribing a user from push notification service
push_notification.unsubscribe(user2)

# Sending another notification to remaining subscribers
push_notification.notify_all('Limited time offer!')

