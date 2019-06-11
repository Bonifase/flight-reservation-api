from locust import TaskSet, task, HttpLocust
import json

class ApiClientBehavior(TaskSet):
    """
    The @task decorator declares a locust task.
    """
    @task(1)    
    def create_user(self):
        headers = {'content-type': 'application/json'}
        self.client.post("api/user/register",data= json.dumps({
            "username": "Johns",
            "email": "somebody@gmailjink.com",
            "password": "obo@gmail.com",
            "passport": "passport.jpeg",
            "isAdmin": "True"
            }), 
        headers=headers, 
        name = "Register User")

    @task(2)    
    def login_user(self):
        headers = {'content-type': 'application/json'}
        self.client.post("api/user/login",data= json.dumps({
            "username": "Johns",
            "email": "somebody@gmailjink.com",
            "password": "obo@gmail.com"
            }), 
        headers=headers, 
        name = "Login User")

    @task(3)    
    def book_flight(self):
        headers = {'content-type': 'application/json'}
        self.client.post("api/booking",data= json.dumps({
            "flight_name": "Flight",
            "seat_number": "100FL",
            "payment": "10000000"
            }), 
        headers=headers, 
        name = "Book Flight")

    @task(4)
    def flights(self):
        self.client.get("api/flights",
        name='Get flights',
        headers={
            "Accept": "application/json"
        })
    
    @task(5)
    def user_flights(self):
        self.client.get("api/flights/1",
        name='Get user bookings in flight',
        headers={
            "Accept": "application/json"
        })

class ApiClient(HttpLocust):
    # taskset is just a POPO
    task_set = ApiClientBehavior
    min_wait = 1000
    max_wait = 5000