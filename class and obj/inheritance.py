
class ott_subscription:
    def __init__(self, subs_id, plan, total_payment ):
        self.id = subs_id
        self.plan= plan
        self.payment = total_payment
        
    def subscribe(self):
        print(f"Subscriber with {self.id} id subscribed to {self.plan} plan")
        
    def unsubscribe(self):
        print(f"Subscriber with {self.id} id unsubscribed to {self.plan} plan")
        
netflix = ott_subscription(1, "monthly", 1000)
print(netflix.plan)
netflix.subscribe()
        
class premiumSubscription(ott_subscription):
    def __init__(self, subs_id, plan, total_payment, screens):
        super().__init__(subs_id, plan, total_payment)
        self.max_screens = screens
        
    def set_max_screens(self, screens):
        self.max_screens = screens
        print(f"Maximum screen set to {self.max_screens} in the premium plans")
        
pNetflix = premiumSubscription(1, "monthly", 1200, 1)
pNetflix.set_max_screens(4)
pNetflix.subscribe()

   