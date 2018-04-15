import webapp2
import manager

mgr = manager.Manager('data.json')
mgr.load()

class Test(webapp2.RequestHandler):

    def get(self):
        query = {
            "leadingDigits": int(self.request.get('leadingDigits')),
            "trailingDigits": int(self.request.get('trailingDigits')),
            "startDate": int(self.request.get('startDate')),
            "endDate": int(self.request.get('endDate')),
            "cardType": str(self.request.get('cardType'))
        }
        result = mgr.search(query, "string")
        self.response.write(result)

    def put(self):
        mgr.addJsonify(self.request.body)
        self.response.write(mgr.getDataDumps())

app = webapp2.WSGIApplication([
    ('/test', Test)
])
