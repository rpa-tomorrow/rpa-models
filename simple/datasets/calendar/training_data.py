
# training data: texts, heads and dependency labels
# for no relation, we simply chose an arbitrary dependency label, e.g. '-'
#
# Labels: [ROOT, NOUN, TO, WHEN, BODY]
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
# WHEN -> WHEN/NOUN/ROOT
#   main WHEN connects to NOUN or ROOT
#   supporting WHEN connects to main WHEN
#   e.g. "remind me in two hours": two -> remind, hours -> two

TRAIN_DATA = [
    (
        "Schedule me at eight",
        {
            "heads": [0, 0, 3, 0], 
            "deps": ["ROOT", "TO", "-", "WHEN"],
        },
    ),
    (
        "Schedule a meeting at 09.00",
        {
            "heads": [0, 2, 0, 4, 0], 
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN"],
        },
    ),
    (
        "At 2 schedule a conferance",
        {
            "heads": [1, 2, 2, 4, 2],
            "deps": ["-", "WHEN", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "Schedule in 120 seconds remind me the time",
        {
            "heads": [0, 1, 3, 1, 0, 3, 6, 3],
            "deps": ["ROOT", "-", "WHEN", "WHEN", "NOUN", "TO", "-", "BODY"],
        },
    ),
    (
        "Schedule a conferance at eleven to eat more vegetables",
        {
            "heads": [0, 1, 0, 4, 2, 6, 2, 8, 6], 
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN", "-", "BODY", "BODY", "BODY"],
        },
    ),

    (
        "Schedule a conferance at 09.00",
        {
            "heads": [0, 2, 0, 4, 2], 
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN"],
        },
    ),
    (
        "With hugo@gmail.com schedule a meeting at 14.00",
        {
            "heads": [1, 2, 2, 4, 2, 6, 2], 
            "deps": ["-", "TO", "ROOT", "-", "NOUN", "-", "WHEN"],
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
            "deps": ["-", "WHEN", "ROOT", "-", "NOUN", "-", "TO", "-", "BODY", "BODY"],
        },
    ),
    (
        "Create a conferance at one with the text time to eat",
        {
            "heads": [0, 1, 0, 4, 0, 7, 7, 8, 2, 10, 8], 
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN", "-", "-", "NOUN", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "Create at 15.00 a meeting about Test with sten@gmail.com",
        {
            "heads": [0, 2, 0, 4, 0, 6, 4, 8, 4], 
            "deps": ["ROOT", "-", "WHEN", "-", "NOUN", "-", "BODY", "-", "TO"],
        },
    ),

    # arrange
    (
        "At 2 arrange a meeting with Niklas about kernel development",
        {
            "heads": [1, 2, 2, 4, 2, 6, 2, 9, 4, 9],
            "deps": ["-", "WHEN", "ROOT", "-", "NOUN", "-", "TO", "-", "BODY", "BODY"],
        },
    ),
    (
        "Arrange a reminder at one with the text go to work",
        {
            "heads": [0, 1, 0, 4, 2, 7, 7, 8, 2, 10, 8], 
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN", "-", "-", "NOUN", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "Arrange at 15.00 a meeting about Rust with alexander@gmail.com",
        {
            "heads": [0, 2, 4, 4, 0, 6, 4, 8, 4], 
            "deps": ["ROOT", "-", "WHEN", "-", "NOUN", "-", "BODY", "-", "TO"],
        },
    ),

    # create
    (
        "Create meeting at three",
        {
            "heads": [0, 0, 3, 1], 
            "deps": ["ROOT", "NOUN", "-", "WHEN"],
        },
    ),
    (
        "Create a meeting at 14.57 with Ingemar",
        {
            "heads": [0, 2, 0, 4, 2, 6, 2], 
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN", "-", "TO"],
        },
    ),
    (
        "At 02.00 create a meeting",
        {
            "heads": [1, 2, 2, 4, 2], 
            "deps": ["-", "WHEN", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "At 4 pm create a meeting with Birgitta",
        {
            "heads": [1, 3, 1, 3, 5, 3, 7, 5], 
            "deps": ["-", "WHEN", "WHEN", "ROOT", "-", "NOUN", "-", "TO"],
        },
    ),
    (
        "With stina@gmail.com create a meeting at 15.34",
        {
            "heads": [1, 2, 2, 4, 2, 6, 4], 
            "deps": ["-", "TO", "ROOT", "-", "NOUN", "-", "WHEN"],
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
            "deps": ["-", "WHEN", "ROOT", "-", "NOUN", "-", "TO", "-", "BODY", "BODY"],
        },
    ),
    (
        "create a reminder at 12 with the text go to work",
        {
            "heads": [0, 1, 0, 4, 0, 7, 7, 8, 2, 10, 8], 
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN", "-", "-", "NOUN", "BODY", "BODY", "BODY"],
        },
    ),

    # appoint 
    (
        "Appoint meeting at three",
        {
            "heads": [0, 0, 3, 0], 
            "deps": ["ROOT", "NOUN", "-", "WHEN"],
        },
    ),
    (
        "Appoint a meeting at 14.57 with Ingemar",
        {
            "heads": [0, 2, 0, 4, 0, 6, 2], 
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN", "-", "TO"],
        },
    ),
    (
        "At 02.00 appoint a meeting",
        {
            "heads": [1, 2, 2, 4, 2], 
            "deps": ["-", "WHEN", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "At 4 pm appoint a meeting with Birgitta",
        {
            "heads": [1, 3, 1, 3, 5, 3, 7, 5], 
            "deps": ["-", "WHEN", "WHEN", "ROOT", "-", "NOUN", "-", "TO"],
        },
    ),
    (
        "With stina@gmail.com appoint a meeting at 15.34",
        {
            "heads": [1, 2, 2, 4, 2, 6, 4], 
            "deps": ["-", "TO", "ROOT", "-", "NOUN", "-", "WHEN"],
        },
    ),

    # delete
    (
        "Delete scheduled meeting at three",
        {
            "heads": [1, 1, 1, 4, 2], 
            "deps": ["NOUN", "ROOT", "NOUN", "-", "WHEN"],
        },
    ),
    (
        "Delete scheduled meeting at 17.00 with martin@gmail.com",
        {
            "heads": [1, 1, 1, 4, 2, 6, 2], 
            "deps": ["NOUN", "ROOT", "NOUN", "-", "WHEN", "-", "TO"],
        },
    ),
    (
        "Delete scheduled meeting at 17.00 with martin@gmail.com",
        {
            "heads": [1, 1, 1, 4, 2, 6, 2], 
            "deps": ["NOUN", "ROOT", "NOUN", "-", "WHEN", "-", "TO"],
        },
    ),
    (
        "At 10 am delete scheduled meeting",
        {
            "heads": [1, 4, 1, 4, 4, 4], 
            "deps": ["-", "WHEN", "WHEN", "NOUN", "ROOT", "NOUN"],
        },
    ),
    (
        "At 3 pm delete scheduled meeting with stjöstedt@gmail.com",
        {
            "heads": [1, 4, 1, 4, 4, 4, 7, 4], 
            "deps": ["-", "WHEN", "WHEN", "NOUN", "ROOT", "NOUN", "-", "TO"],
        },
    ),

    # Remove
    (
        "Remove scheduled meeting at three",
        {
            "heads": [1, 1, 1, 4, 2], 
            "deps": ["NOUN", "ROOT", "NOUN", "-", "WHEN"],
        },
    ),
    (
        "Remove scheduled meeting at 17.00 with martin@gmail.com",
        {
            "heads": [1, 1, 1, 4, 2, 6, 2], 
            "deps": ["NOUN", "ROOT", "NOUN", "-", "WHEN", "-", "TO"],
        },
    ),
    (
        "Remove scheduled conferance at 17.00 with martin@gmail.com",
        {
            "heads": [1, 1, 1, 4, 2, 6, 2], 
            "deps": ["NOUN", "ROOT", "NOUN", "-", "WHEN", "-", "TO"],
        },
    ),

]