from trello import TrelloClient

#these can probably be replaced by list comprehensions
def get_todo_list(board):
    for l in board.open_lists():
        if l.name == "To Do":
          return l

def get_card(cards, title):
    for card in cards:
        if card.name == title:
            return card

def load_auth():
    auth = {}
    execfile("auth.config", auth) 
    return auth

def load_schedule():
    schedule = {}
    execfile("schedule.config", schedule) 
    return schedule

if __name__ == "__main__":
    auth = load_auth()
    scheduled_tasks = load_schedule()["tasks"]

    client = TrelloClient(api_key=auth["key"], api_secret=auth["secret"], token=auth["oauth_token"], token_secret=auth["oauth_token_secret"])

    boards = client.list_boards()

    board_name = scheduled_tasks[0]["board"]
    card_title = scheduled_tasks[0]["title"]

    for b in boards:
        if b.name == board_name:
            todo_list = get_todo_list(b)
            cards = todo_list.list_cards()

            card = get_card(cards, card_title)
            if card is None:
                print "Card does not exist, adding it now."
                todo_list.add_card(card_title, "Added by code!")
            else:
                print "That card already exists"

