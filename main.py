#py 3.7
import cherrypy
from cherrypy.process import servers
from fetch import send_to_compute

#Cherrypy config
def fake_wait_for_occupied_port(host, port): return
servers.wait_for_occupied_port = fake_wait_for_occupied_port

#If we want to implement webhook authentication
secret = "compute"

#Setup the app
class WebhookServer():

    def __init__(self) -> None:
        super().__init__()

    @cherrypy.expose
    @cherrypy.tools.json_in()

    # This function will be called if the webhook endpoint is accessed
    def webhook(self, *args, **kwargs):
        payload_json = cherrypy.request.json.get('payload', '{}')
        signature = cherrypy.request.headers["X-WEBHOOK-SIGNATURE"]
        print("Webhook Signal Received")
        self.webhook_called(payload_json, signature)

    # This function will trigger the compute server
    def webhook_called(self, payload_json: str, signature: str):
        print("Compute Called")
        compute_sender = send_to_compute()
        print("Compute Answered")

cherrypy.config.update({

    #'environment': 'production',
    'server.socket_host': '0.0.0.0',
    'server.socket_port': 8080
})


cherrypy.quickstart(WebhookServer())