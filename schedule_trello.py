#!/usr/bin/env python

from trello import TrelloClient
import datetime

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
    execfile("/absolute/path/to/auth.config", auth) 
    return auth

def load_schedule():
    schedule = {}
    execfile("/absolute/path/to/schedule.config", schedule) 
    return schedule

if __name__ == "__main__":
    auth = load_auth()
    scheduled_tasks = load_schedule()["tasks"]

    client = TrelloClient(api_key=auth["key"], api_secret=auth["secret"], token=auth["oauth_token"], token_secret=auth["oauth_token_secret"])

    now = datetime.datetime.now()
    today = now.strftime("%A")
    boards = client.list_boards()

    for task in scheduled_tasks:
        board_name = task["board"]
        card_title = task["title"]
        repeat_on = task["repeat_on"]

        if repeat_on != today:
            continue;

        for b in boards:
            if b.name == board_name:
                todo_list = get_todo_list(b)
                cards = todo_list.list_cards()

                card = get_card(cards, card_title)
                if card is None:
                    todo_list.add_card(card_title, "Added by code!")

