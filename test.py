from trello import TrelloClient

def get_todo_list(board):
    for l in board.open_lists():
        if l.name == "To Do":
          return l

def get_card(cards, title):
    for 

if __name__ == "__main__":
    auth = {}
    execfile("auth.config", auth) 

    client = TrelloClient(api_key=auth["key"], api_secret=auth["secret"], token=auth["oauth_token"], token_secret=auth["oauth_token_secret"])

    boards = client.list_boards()
    print boards

    name = "Home"
    cardTitle = "Fix mirror angle"

    for b in boards:
        if b.name == name:
            print b.name
            print b.description
            todo_list = get_todo_list(b)
            cards = todo_list.list_cards()
            print cards

            print get_card(cards, cardTitle)
