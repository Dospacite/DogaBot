from RegistryHandler import RegistryHandler


class NotificationRegistryHandler(RegistryHandler):

    def write_channel_message_to_registry(self, channel_id: str, last_sent_message_id: int = 0):
        pairs = self.load_dict_from_registry()
        pairs['channels'][channel_id] = last_sent_message_id
        self.dump_dict_to_registry(pairs)

    def get_channel_last_message(self, channel_id: str):
        pairs = self.load_dict_from_registry()
        return pairs['channels'][channel_id]

