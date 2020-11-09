
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
        "Schedule me and Sigurd at 2",
        {
            
            "heads": [0, 0, 3, 0, 5, 0], 
            "deps": ["ROOT", "TO", "-", "TO", "-", "START"],
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
    # Schedule meeting asking the receiver about time
    (
        "Schedule me and Anna at eight ask when to stop",
        {
            "heads": [0, 0, 3, 0, 5, 0, 0, 6, 7, 8], 
            "deps": ["ROOT", "TO", "-", "TO", "-", "START", "BODY", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "At 9 schedule a conferance asking the length with Emelie",
        {
            "heads": [1, 2, 2, 4, 2, 2, 5, 6, 9, 2],
            "deps": ["-", "START", "ROOT", "-", "NOUN", "BODY", "BODY", "BODY", "-", "TO"],
        },
    ),
    (
        "Schedule a meeting at 11 ask Gustav when to end",
        {
            "heads": [0, 2, 0, 4, 0, 6, 0, 0, 7, 8], 
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN", "-", "TO", "BODY", "BODY", "BODY"],
        },
    ),

    # Schedule with time span
    (
        "Schedule me at 08.00 to 08.30 ",
        {
            "heads": [0, 0, 3, 0, 5, 0], 
            "deps": ["ROOT", "TO", "-", "START", "-", "END"],
        },
    ),
    (
        "Schedule me at 11.00 to 12.00 about lunch",
        {
            "heads": [0, 0, 3, 0, 5, 0, 7, 0], 
            "deps": ["ROOT", "TO", "-", "START", "-", "END", "-", "BODY"],
        },
    ),
    (
        "Schedule a meeting at 09.00 to 10.00",
        {
            "heads": [0, 2, 0, 4, 0, 6, 0], 
            "deps": ["ROOT", "-", "NOUN", "-", "START", "-", "END"],
        },
    ),
    (
        "Schedule meeting at 16.15 to 16.00 about software architecture",
        {
            "heads": [0, 0, 3, 0, 5, 0, 7, 8, 0], 
            "deps": ["ROOT", "NOUN", "-", "START", "-", "END", "-", "BODY", "BODY"],
        },
    ),
    (
        "With anton@gmail.com schedule a meeting at 14.00 to 14.15",
        {
            "heads": [1, 2, 2, 4, 2, 6, 2, 8, 2], 
            "deps": ["-", "TO", "ROOT", "-", "NOUN", "-", "START", "-", "END"],
        },
    ),

    (
        "At 2 to 3 schedule a meeting with Stefan about current project",
        {
            "heads": [1, 4, 3, 4,  4, 6, 4, 8, 4, 11, 6, 11],
            "deps": ["-", "START", "-", "END", "ROOT", "-", "NOUN", "-", "TO", "-", "BODY", "BODY"],
        },
    ),
    (
        "Create at 15.00 to 15.15 a meeting about Test with sten@gmail.com",
        {
            "heads": [0, 2, 0, 4, 0, 6, 0, 8, 6, 10, 6], 
            "deps": ["ROOT", "-", "START", "-", "END", "-", "NOUN", "-", "BODY", "-", "TO"],
        },
    ),


    # Arrange
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

    # Create
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

    # Appoint 
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

    # Delete
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