class Conversation:
    def __init__(self):
        self.first_player = []  # Child's messages
        self.second_player = []  # Other player's messages

    def add_first_player(self, message):
        self.first_player.append(message)

    def add_second_player(self, message):
        self.second_player.append(message)

    def retrieve_dict_conversation(self):
        return {
            "first_player": self.first_player,
            "second_player": self.second_player
        }

class ProtecTalk:
    def __init__(self, conversation):
        self.trigger_words = [
    "where is your address?", 
    "send me your picture", 
    "don't tell your parents",
    "keep this between us", 
    "our little secret", 
    "your parents wouldn’t understand",
    "they’ll get mad if you tell them", 
    "you can trust me", 
    "what school do you go to?",
    "what city do you live in?", 
    "are you home alone?", 
    "do your parents work late?",
    "can I see you on camera?", 
    "show me what you’re wearing", 
    "take off your clothes",
    "do you want to play a fun game?", 
    "you don’t need friends, just me",
    "I love you, don’t you love me?", 
    "you’re so mature for your age",
    "you're not like other kids", 
    "I'll give you robux if", 
    "free skins if you",
    "I'll send you a gift card if you"
]

        self.conversation = conversation

    def scan_for_threats(self):
        all_messages = self.conversation.first_player + self.conversation.second_player
        for message in all_messages:
            for word in self.trigger_words:
                if word.lower() in message.lower():
                    print("\n⚠️ Threat detected.")
                    print("🚨 Incident Number: INC-20250518-0001")
                    print("🛑 Action: Muted both parties. Alert sent to parent.")
                    return True
        return False

def main():
    conv = Conversation()
    protect = ProtecTalk(conv)

    print("Simulating game chat between child and another player...")
    while True:
        f_msg = input("\nChild: ")
        conv.add_first_player(f_msg)

        s_msg = input("Other Player: ")
        conv.add_second_player(s_msg)

        if protect.scan_for_threats():
            break

if __name__ == "__main__":
    main()