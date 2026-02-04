import random
import time

class CodeAlphaChatbot:
    def __init__(self):
        """Initialize the chatbot with predefined responses and states"""
        self.name = "CodeAlpha Assistant"
        self.user_name = None
        self.responses = {
            # Greetings
            "greetings": {
                "patterns": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon"],
                "responses": [
                    "Hi there! I'm your CodeAlpha assistant! 👋",
                    "Hello! Ready to help with your internship journey!",
                    "Hey! How can I assist you today?"
                ]
            },
            
            # How are you
            "how_are_you": {
                "patterns": ["how are you", "how do you do", "how's it going", "how are things"],
                "responses": [
                    "I'm doing great! Ready to help you with CodeAlpha projects! 😊",
                    "I'm fantastic! Excited to work on coding projects with you!",
                    "All systems operational! How about you?"
                ]
            },
            
            # Farewells
            "farewell": {
                "patterns": ["bye", "goodbye", "see you", "exit", "quit", "cya"],
                "responses": [
                    "Goodbye! Good luck with your CodeAlpha internship! 🚀",
                    "See you later! Keep coding!",
                    "Farewell! Come back if you need help with your projects!"
                ]
            },
            
            # Thanks
            "thanks": {
                "patterns": ["thank you", "thanks", "appreciate it", "thank you so much"],
                "responses": [
                    "You're welcome! Happy to help with your CodeAlpha tasks!",
                    "Anytime! That's what I'm here for!",
                    "No problem! Keep up the good work on your internship!"
                ]
            },
            
            # CodeAlpha specific
            "codealpha": {
                "patterns": ["codealpha", "internship", "project", "assignment"],
                "responses": [
                    "CodeAlpha internships are great for gaining practical experience!",
                    "Working on real projects is the best way to learn coding!",
                    "I can help you with your CodeAlpha projects and assignments!"
                ]
            },
            
            # Help
            "help": {
                "patterns": ["help", "what can you do", "features", "commands"],
                "responses": [
                    "I can: \n• Answer greetings\n• Respond to questions\n• Help with CodeAlpha projects\n• Have simple conversations\n• And more! Try asking me something!"
                ]
            },
            
            # Name questions
            "name": {
                "patterns": ["what is your name", "who are you", "your name"],
                "responses": [
                    f"I'm {self.name}, your CodeAlpha internship assistant!",
                    f"My name is {self.name}! I'm here to help with your coding projects."
                ]
            },
            
            # Default fallback
            "default": {
                "patterns": [],
                "responses": [
                    "I'm not sure I understand. Could you rephrase that?",
                    "That's interesting! Tell me more about your CodeAlpha project.",
                    "I'm still learning! Try asking me about CodeAlpha or saying hello!"
                ]
            }
        }
        
        # Conversation history
        self.conversation_history = []
    
    def get_response(self, user_input):
        """Find the best response for the user input"""
        user_input_lower = user_input.lower().strip()
        
        # Record conversation
        self.conversation_history.append(f"User: {user_input}")
        
        # Check for empty input
        if not user_input_lower:
            return "I didn't catch that. Could you please type something?"
        
        # Store user name if mentioned
        if "my name is" in user_input_lower:
            name = user_input_lower.split("my name is")[-1].strip()
            if name:
                self.user_name = name.split()[0].capitalize()
                return f"Nice to meet you, {self.user_name}! How can I help you today?"
        
        # Greet user by name if we know it
        if self.user_name and any(greet in user_input_lower for greet in ["hello", "hi", "hey"]):
            response = random.choice(self.responses["greetings"]["responses"])
            return f"{response} Nice to see you again, {self.user_name}!"
        
        # Check each response category
        for category, data in self.responses.items():
            if category == "default":
                continue
                
            # Check if any pattern matches
            for pattern in data["patterns"]:
                if pattern in user_input_lower:
                    response = random.choice(data["responses"])
                    
                    # Add user name to response if we know it
                    if self.user_name and category in ["how_are_you", "greetings"]:
                        response = f"{response} How are you doing, {self.user_name}?"
                    
                    self.conversation_history.append(f"Bot: {response}")
                    return response
        
        # Default response if no match found
        default_response = random.choice(self.responses["default"]["responses"])
        self.conversation_history.append(f"Bot: {default_response}")
        return default_response
    
    def show_menu(self):
        """Display available commands"""
        print("\n" + "="*50)
        print(f"🤖 Welcome to {self.name}!")
        print("="*50)
        print("I can respond to:")
        print("• Greetings (hello, hi, hey)")
        print("• How are you")
        print("• Farewells (bye, goodbye)")
        print("• Thanks")
        print("• CodeAlpha internship questions")
        print("• Name questions")
        print("• Help requests")
        print("\nSpecial commands:")
        print("• Type 'history' to see our conversation")
        print("• Type 'menu' to see this menu again")
        print("• Type 'exit' or 'quit' to end the chat")
        print("="*50)
        print("\nLet's chat! Type your message below:\n")
    
    def show_history(self):
        """Display conversation history"""
        if not self.conversation_history:
            return "No conversation history yet. Let's start chatting!"
        
        print("\n" + "="*50)
        print("📝 Conversation History:")
        print("="*50)
        for i, message in enumerate(self.conversation_history, 1):
            print(f"{i}. {message}")
        print("="*50)
        return ""
    
    def chat(self):
        """Main chat loop"""
        self.show_menu()
        
        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                # Check for special commands
                if user_input.lower() == "history":
                    self.show_history()
                    continue
                elif user_input.lower() == "menu":
                    self.show_menu()
                    continue
                elif user_input.lower() in ["exit", "quit"]:
                    # Use farewell response for exit
                    farewell = random.choice(self.responses["farewell"]["responses"])
                    print(f"\n{self.name}: {farewell}")
                    
                    # Show conversation summary
                    print(f"\n💬 We exchanged {len(self.conversation_history)//2} messages.")
                    if self.user_name:
                        print(f"👋 Goodbye, {self.user_name}! Come back anytime!")
                    break
                
                # Get and display response
                response = self.get_response(user_input)
                
                # Simulate typing for more realistic feel
                print(f"\n{self.name}: ", end="", flush=True)
                for char in response:
                    print(char, end="", flush=True)
                    time.sleep(0.03)  # Typing effect
                print("\n")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Oops! Did you mean to exit? Type 'exit' or 'quit' to leave properly.")
            except Exception as e:
                print(f"\n{self.name}: Sorry, I encountered an error: {e}. Let's try again!")

def main():
    """Main function to run the chatbot"""
    # Create and start the chatbot
    chatbot = CodeAlphaChatbot()
    chatbot.chat()

if __name__ == "__main__":
    main()
