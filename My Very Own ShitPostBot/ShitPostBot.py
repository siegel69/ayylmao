from os import system

def main():

    welcome = "I want to die"
    print(welcome)

    str = "https://www.youtube.com/watch?v=LFFvJaMhgDg"

    command2 = "curl -X POST -d '{\"bot\": { \"name\": \"new test bot\", \"group_id\": \"32008860\"}"
    command2 = command2 + "}' -H 'Content-Type: application/json' https://api.groupme.com/v3/bots?token=6G8SBZocwVRrTSZ300Qe4YIiaEqcGALKSDAlZW4c"
    
    print(command2)
    
    teststring = system(command2)
    
    print(teststring)
    """
    
    command = "curl -X POST -d '{\"bot_id\": \"13850298e6c9bfa1be1df85520\", \"text\": \""
    command = command +str+"\"}' -H 'Content-Type: application/json' https://api.groupme.com/v3/bots/post"
    print(command)
    
    system(command)
    """
main()