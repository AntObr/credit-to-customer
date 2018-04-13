import webapp2
import manager
import json

mgr = manager.Manager('data.json')
mgr.load()

class Test(webapp2.RequestHandler):
    def get(self):
        query = {
            "leadingDigits": int(self.request.get('leadingDigits')),
            "trailingDigits": int(self.request.get('trailingDigits')),
            "startDate": int(self.request.get('startDate')),
            "endDate": int(self.request.get('startDate')),
            "cardType": self.request.get('cardType')
        }
        print(query)
        result = mgr.search(query)
        print(result)
        self.response.write("result:</br>" + result + "</br>query:</br>" + str(query) + "</br>dump:</br>" + mgr.getDataDumps())

    # DONE
    def put(self):
        mgr.addJsonify(self.request.body)
        self.response.write(mgr.getDataDumps())

class Reload(webapp2.RequestHandler):
    def get(self):
        mgr.load()
        self.response.write("RELOADED: " + mgr.getDataDumps())

app = webapp2.WSGIApplication([
    ('/test', Test),
    ('/reload', Reload)
])

# localhost:8080/test?leadingDigits=5407&trailingDigits=3456&startDate=1208&endDate=1508&cardType=MasterCard
# curl --request GET --header "Content-Type: application/json" localhost:8080/test?leadingDigits=5407&trailingDigits=3456&startDate=1208&endDate=1508&cardType=MasterCard


# curl --request PUT --header "Content-Type: application/json" --data "["put@email.com", {"test": "testPut"}]" http://localhost:8080/test
# curl --request PUT --header "Content-Type: application/json" --data '["put@email.com", {"test": "testPut"}]' http://localhost:8080/test
