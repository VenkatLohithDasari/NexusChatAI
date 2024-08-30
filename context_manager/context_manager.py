import os
import json
import time

class ContextManager:
    def __init__(self, context_dir='contexts'):
        self.context_dir = context_dir
        os.makedirs(self.context_dir, exist_ok=True)

    def get_context_file(self, channel_id):
        return os.path.join(self.context_dir, f'{channel_id}.json')

    def load_context(self, channel_id):
        context_file = self.get_context_file(channel_id)
        if os.path.exists(context_file):
            with open(context_file, 'r') as file:
                return json.load(file)
        return []

    def save_context(self, channel_id, context):
        context_file = self.get_context_file(channel_id)
        with open(context_file, 'w') as file:
            json.dump(context, file)

    def clear_context(self, channel_id):
        context_file = self.get_context_file(channel_id)
        if os.path.exists(context_file):
            os.rename(context_file, f"{context_file}_{int(time.time())}.bak")