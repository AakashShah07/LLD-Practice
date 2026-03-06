class ResponseController:

    def submit_response(self, form, response):

        form.add_response(response)

    def get_responses(self, form):

        return form.responses