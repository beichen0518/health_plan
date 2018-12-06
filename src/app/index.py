from flask_restful_resource import BaseResource


class Index(BaseResource):

    def get(self):
        return "hhh"