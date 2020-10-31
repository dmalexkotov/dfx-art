import json


class QuillContentstateConverter:
    def from_database_format(self, value):
        return value

    def to_database_format(self, contentstate_json):
        return contentstate_json
