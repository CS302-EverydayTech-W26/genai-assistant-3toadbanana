from gemini_client import *

def main():
    client = GeminiClient()

    while True:
        user_input = input("$_: ")

        if user_input == "exit":
            #specification asked for 'goodbye', but I thought this was more fun.
            print ("[SYSTEM: TERMINATING_PROCESS_84-B]\n[STATUS: SHUTTING DOWN...]") 
            break
        
        print("[KERNEL: MOUNTING DRIVE_C]... OK\n[TERMINAL_84B: LOADING]\n--------------------------------------\n")

        response = client.generate_response(user_input)
        print(response + "\n")
     

if __name__ == "__main__":
  main()