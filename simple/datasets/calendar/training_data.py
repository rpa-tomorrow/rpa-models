
# training data: texts, heads and dependency labels
# for no relation, we simply chose an arbitrary dependency label, e.g. '-'
#
# Labels: [ROOT, NOUN, TO, START, BODY]
#
# The following dataset follows the following dependency ordering.
# The ordering has priority here
# ROOT -> ROOT
# NOUN -> ROOT
# TO -> NOUN/ROOT 
#   (if NOUN: connect to NOUN, else: connect to ROOT)
#   e.g. "email me": me -> email
#        "send email to me": me -> email
# BODY -> BODY/NOUN/ROOT 
#   main BODY connects to NOUN or ROOT
#   supporting BODY connects to main BODY
#   e.g. "remind me to go outside": go -> remind, outside -> go
# START -> START/NOUN/ROOT
#   main START connects to NOUN or ROOT
#   supporting START connects to main START
#   e.g. "remind me in two hours": two -> remind, hours -> two

TRAIN_DATA = [
    (
        "Schedule me at eight",
        {
            "heads": [0, 0, 3, 0], 
            "deps": ["ROOT", "TO", "-", "START"],
        },
    ),
    (
        "Schedule a meeting at 09.00",
        {
            "heads": [0, 2, 0, 4, 0], 
            "deps": ["ROOT", "-", "NOUN", "-", "START"],
        },
    ),
    (
        "At 2 schedule a conferance",
        {
            "heads": [1, 2, 2, 4, 2],
            "deps": ["-", "START", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "Schedule in 120 seconds remind me the time",
        {
            "heads": [0, 1, 3, 1, 0, 3, 6, 3],
            "deps": ["ROOT", "-", "START", "START", "NOUN", "TO", "-", "BODY"],
        },
    ),
    (
        "Schedule a conferance at eleven to eat more vegetables",
        {
            "heads": [0, 1, 0, 4, 2, 6, 2, 8, 6], 
            "deps": ["ROOT", "-", "NOUN", "-", "START", "-", "BODY", "BODY", "BODY"],
        },
    ),

    (
        "Schedule a conferance at 09.00",
        {
            "heads": [0, 2, 0, 4, 2], 
            "deps": ["ROOT", "-", "NOUN", "-", "START"],
        },
    ),
    (
        "With hugo@gmail.com schedule a meeting at 14.00",
        {
            "heads": [1, 2, 2, 4, 2, 6, 2], 
            "deps": ["-", "TO", "ROOT", "-", "NOUN", "-", "START"],
        },
    ),
    (
        "Schedule a meeting with mark@email.com about hiring him",
        {
            "heads": [0, 2, 0, 4, 2, 6, 2, 4], 
            "deps": ["ROOT", "-", "NOUN", "-", "TO", "-", "BODY", "-"],
        },
    ),
    (
        "At 2 schedule a meeting with Niklas about kernel development",
        {
            "heads": [1, 2, 2, 4, 2, 6, 2, 9, 4, 9],
            "deps": ["-", "START", "ROOT", "-", "NOUN", "-", "TO", "-", "BODY", "BODY"],
        },
    ),
    (
        "Create a conferance at one with the text time to eat",
        {
            "heads": [0, 1, 0, 4, 0, 7, 7, 8, 2, 10, 8], 
            "deps": ["ROOT", "-", "NOUN", "-", "START", "-", "-", "NOUN", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "Create at 15.00 a meeting about Test with sten@gmail.com",
        {
            "heads": [0, 2, 0, 4, 0, 6, 4, 8, 4], 
            "deps": ["ROOT", "-", "START", "-", "NOUN", "-", "BODY", "-", "TO"],
        },
    ),

    # arrange
    (
        "At 2 arrange a meeting with Niklas about kernel development",
        {
            "heads": [1, 2, 2, 4, 2, 6, 2, 9, 4, 9],
            "deps": ["-", "START", "ROOT", "-", "NOUN", "-", "TO", "-", "BODY", "BODY"],
        },
    ),
    (
        "Arrange a reminder at one with the text go to work",
        {
            "heads": [0, 1, 0, 4, 2, 7, 7, 8, 2, 10, 8], 
            "deps": ["ROOT", "-", "NOUN", "-", "START", "-", "-", "NOUN", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "Arrange at 15.00 a meeting about Rust with alexander@gmail.com",
        {
            "heads": [0, 2, 4, 4, 0, 6, 4, 8, 4], 
            "deps": ["ROOT", "-", "START", "-", "NOUN", "-", "BODY", "-", "TO"],
        },
    ),

    # create
    (
        "Create meeting at three",
        {
            "heads": [0, 0, 3, 1], 
            "deps": ["ROOT", "NOUN", "-", "START"],
        },
    ),
    (
        "Create a meeting at 14.57 with Ingemar",
        {
            "heads": [0, 2, 0, 4, 2, 6, 2], 
            "deps": ["ROOT", "-", "NOUN", "-", "START", "-", "TO"],
        },
    ),
    (
        "At 02.00 create a meeting",
        {
            "heads": [1, 2, 2, 4, 2], 
            "deps": ["-", "START", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "At 4 pm create a meeting with Birgitta",
        {
            "heads": [1, 3, 1, 3, 5, 3, 7, 5], 
            "deps": ["-", "START", "START", "ROOT", "-", "NOUN", "-", "TO"],
        },
    ),
    (
        "With stina@gmail.com create a meeting at 15.34",
        {
            "heads": [1, 2, 2, 4, 2, 6, 4], 
            "deps": ["-", "TO", "ROOT", "-", "NOUN", "-", "START"],
        },
    ),
    (
        "Create a meeting with mark@email.com about hiring him",
        {
            "heads": [0, 2, 0, 4, 2, 6, 2, 4], 
            "deps": ["ROOT", "-", "NOUN", "-", "TO", "-", "BODY", "-"],
        },
    ),
    (
        "At 2 create a meeting with Niklas about kernel development",
        {
            "heads": [1, 2, 2, 4, 2, 6, 2, 9, 4, 9],
            "deps": ["-", "START", "ROOT", "-", "NOUN", "-", "TO", "-", "BODY", "BODY"],
        },
    ),
    (
        "create a reminder at 12 with the text go to work",
        {
            "heads": [0, 1, 0, 4, 0, 7, 7, 8, 2, 10, 8], 
            "deps": ["ROOT", "-", "NOUN", "-", "START", "-", "-", "NOUN", "BODY", "BODY", "BODY"],
        },
    ),

    # appoint 
    (
        "Appoint meeting at three",
        {
            "heads": [0, 0, 3, 0], 
            "deps": ["ROOT", "NOUN", "-", "START"],
        },
    ),
    (
        "Appoint a meeting at 14.57 with Ingemar",
        {
            "heads": [0, 2, 0, 4, 0, 6, 2], 
            "deps": ["ROOT", "-", "NOUN", "-", "START", "-", "TO"],
        },
    ),
    (
        "At 02.00 appoint a meeting",
        {
            "heads": [1, 2, 2, 4, 2], 
            "deps": ["-", "START", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "At 4 pm appoint a meeting with Birgitta",
        {
            "heads": [1, 3, 1, 3, 5, 3, 7, 5], 
            "deps": ["-", "START", "START", "ROOT", "-", "NOUN", "-", "TO"],
        },
    ),
    (
        "With stina@gmail.com appoint a meeting at 15.34",
        {
            "heads": [1, 2, 2, 4, 2, 6, 4], 
            "deps": ["-", "TO", "ROOT", "-", "NOUN", "-", "START"],
        },
    ),

    # appoint 
    (
        "Appoint meeting at three",
        {
            "heads": [0, 0, 3, 0], 
            "deps": ["ROOT", "NOUN", "-", "START"],
        },
    ),
    (
        "Appoint a meeting at 14.57 with Ingemar",
        {
            "heads": [0, 2, 0, 4, 0, 6, 2], 
            "deps": ["ROOT", "-", "NOUN", "-", "START", "-", "TO"],
        },
    ),
    (
        "At 02.00 appoint a meeting",
        {
            "heads": [1, 2, 2, 4, 2], 
            "deps": ["-", "START", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "At 4 pm appoint a meeting with Birgitta",
        {
            "heads": [1, 3, 1, 3, 5, 3, 7, 5], 
            "deps": ["-", "START", "START", "ROOT", "-", "NOUN", "-", "TO"],
        },
    ),
    (
        "With stina@gmail.com appoint a meeting at 15.34",
        {
            "heads": [1, 2, 2, 4, 2, 6, 4], 
            "deps": ["-", "TO", "ROOT", "-", "NOUN", "-", "START"],
        },
    ),

    # delete
    (
        "Delete scheduled meeting at three",
        {
            "heads": [1, 1, 1, 4, 2], 
            "deps": ["NOUN", "ROOT", "NOUN", "-", "START"],
        },
    ),
    (
        "Delete scheduled meeting at 17.00 with martin@gmail.com",
        {
            "heads": [1, 1, 1, 4, 2, 6, 2], 
            "deps": ["NOUN", "ROOT", "NOUN", "-", "START", "-", "TO"],
        },
    ),
    (
        "At 10 am delete scheduled meeting",
        {
            "heads": [1, 4, 1, 4, 4, 4], 
            "deps": ["-", "START", "START", "NOUN", "ROOT", "NOUN"],
        },
    ),
    (
        "At 3 pm delete scheduled meeting with stjöstedt@gmail.com",
        {
            "heads": [1, 4, 1, 4, 4, 4, 7, 4], 
            "deps": ["-", "START", "START", "NOUN", "ROOT", "NOUN", "-", "TO"],
        },
    ),

    # Remove
    (
        "Remove scheduled meeting at three",
        {
            "heads": [1, 1, 1, 4, 2], 
            "deps": ["NOUN", "ROOT", "NOUN", "-", "START"],
        },
    ),
    (
        "Remove scheduled meeting at 17.00 with martin@gmail.com",
        {
            "heads": [1, 1, 1, 4, 2, 6, 2], 
            "deps": ["NOUN", "ROOT", "NOUN", "-", "START", "-", "TO"],
        },
    ),
    (
        "Remove scheduled conferance at 17.00 with martin@gmail.com",
        {
            "heads": [1, 1, 1, 4, 2, 6, 2], 
            "deps": ["NOUN", "ROOT", "NOUN", "-", "START", "-", "TO"],
        },
    ),

]