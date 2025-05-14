class MessageNode:
    def __init__(self, sender, message):
        self.sender = sender
        self.message = message
        self.next = None

class ChatHistory:
    def __init__(self):
        self.head = None

    def add_message(self, sender, message):
        new_msg = MessageNode(sender, message)
        if not self.head:
            self.head = new_msg
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_msg

    def delete_current_message(self):
        if not self.head:
            print("No message to delete.")
        elif self.head.next:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

    def delete_oldest_message(self):
        if not self.head:
            print("No messages to delete.")
        else:
            self.head = self.head.next 
    def show_chat(self):
        current = self.head
        print("Chat History:")
        while current:
            print(f"{current.sender}: {current.message}")
            current = current.next

# --- Usage Example ---
chat = ChatHistory()
chat.add_message("Alice", "Hey, how are you?")
chat.add_message("Bob", "I'm good! You?")
chat.add_message("Alice", "All well. Wanna catch up tomorrow?")
chat.show_chat()

print("\nDeleting oldest message...\n")
chat.delete_oldest_message()
chat.show_chat()
