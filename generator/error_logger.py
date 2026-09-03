class ErrorLogger:

    def __init__(self):

        self.errors = []

    def add_error(
        self,
        record_id,
        message
    ):

        self.errors.append({
            "record_id": record_id,
            "message": message
        })

    def has_errors(self):

        return len(self.errors) > 0

    def count(self):

        return len(self.errors)

    def get_errors(self):

        return self.errors