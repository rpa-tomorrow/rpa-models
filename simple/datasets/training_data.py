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
        "send an email to mark@email.com and greet him",
        {
            "heads": [0, 2, 0, 4, 2, 6, 2, 4], 
            "deps": ["ROOT", "-", "NOUN", "-", "TO", "-", "BODY", "-"],
        },
    ),
    (
        "send an email to Mark",
        {
            "heads": [0, 2, 0, 4, 2],
            "deps": ["ROOT", "-", "NOUN", "-", "TO"],
        },
    ),
    (
        "write an email with a smiley to friend@best.com",
        {
            "heads": [0, 2, 0, 5, 5, 2, 7, 2],
            "deps": ["ROOT", "-", "NOUN", "-", "-", "BODY", "-", "TO"],
        },
    ),
    (
        "write an email to hugo@microsoft.com and viktor@google.com",
        {
            "heads": [0, 2, 0, 4, 2, 6, 2],
            "deps": ["ROOT", "-", "NOUN", "-", "TO", "-", "TO"],
        },
    ),
    (
        "email Lars today's weather",
        {
            "heads": [0, 0, 4, 2, 0],  
            "deps": ["ROOT", "TO", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "send an email to my boss that I can't come today",
        {
            "heads": [0, 2, 0, 5, 5, 2, 2, 8, 10, 9, 2, 10],
            "deps": ["ROOT", "-", "NOUN", "-", "-", "TO", "-", "BODY", "BODY", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "email charlemagne@france.com asking if he can come tomorrow",
        {
            "heads": [0, 0, 6, 1, 3, 6, 0, 6],
            "deps": ["ROOT", "TO", "VERB", "BODY", "BODY", "BODY", "BODY", "BODY"],
        },
    ),
    # This is not optimal, should be improved further
    (
        "write an email to Sigbjörn asking if yesterday's party was fun",
        {
            "heads": [0, 2, 0, 4, 2, 4, 11, 9, 7, 2, 7, 9],
            "deps": ["ROOT", "-", "NOUN", "-", "TO", "-", "BODY", "BODY", "BODY", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "write Hello world in an email to hugo@mail.com",
        {
            "heads": [0, 2, 5, 5, 5, 0, 7, 0],
            "deps": ["ROOT", "BODY", "BODY", "-", "-", "NOUN", "-", "TO"],
        },
    ),
    ### SEND
    (
        "send an email to Hugo",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "TO"],
        },
    ),
    (
        "to Hugo send an email at 15.57",
        {
            "heads": [1, 4, 2, 4, 2, 6, 4],  # index of token head
            "deps": ["-", "TO", "ROOT", "-", "NOUN", "-", "WHEN"],
        },
    ),
    (
        "to recipient send an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "TO", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient send a message",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "TO", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "send an email to receiver",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "TO"],
        },
    ),
    ### WRITE
    (
        "write an email to recipient",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "TO"],
        },
    ),
    (
        "to Hugo write an email with tomorrow's weather",
        {
            "heads": [1, 4, 2, 4, 2, 6, 8, 6, 4],  # index of token head
            "deps": ["-", "TO", "ROOT", "-", "NOUN", "-", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "to recipient write an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "TO", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient write a message",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "TO", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "write an email to receiver",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "BODY", "-", "TO"],
        },
    ),
    ### POST
    (
        "post an email to recipient",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "TO"],
        },
    ),
    (
        "to Hugo post an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "TO", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient post an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "TO", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient post a message",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "TO", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "post an email to receiver",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "TO"],
        },
    ),
    ### DISPATCH
    (
        "dispatch an email to recipient",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "TO"],
        },
    ),
    (
        "to Hugo dispatch an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "TO", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient dispatch an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "TO", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient dispatch a message",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "TO", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "dispatch an email to receiver",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "TO"],
        },
    ),   
    ### FORWARD
    (
        "forward an email to recipient",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "TO"],
        },
    ),
    (
        "to Hugo forward an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "TO", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient forward an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "TO", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient forward a message",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "TO", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "forward an email to receiver",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "TO"],
        },
    ),


    ### REMINDER
    (
        "Remind me at eight",
        {
            "heads": [0, 0, 3, 0], 
            "deps": ["ROOT", "TO", "-", "WHEN"],
        },
    ),
    (
        "At 2 notify me",
        {
            "heads": [1, 2, 2, 2],
            "deps": ["-", "WHEN", "ROOT", "TO"],
        },
    ),
    (
        "Alarm me in four hours",
        {
            "heads": [0, 0, 3, 0, 3], 
            "deps": ["ROOT", "TO", "-", "WHEN", "WHEN"],
        },
    ),
    (
        "Remind Hugo at 7 pm",
        {
            "heads": [0, 0, 3, 0, 3], 
            "deps": ["ROOT", "TO", "-", "WHEN", "WHEN"],
        },
    ),
    (
        "Notify Albin at 18.00",
        {
            "heads": [0, 0, 3, 0], 
            "deps": ["ROOT", "TO", "-", "WHEN"],
        },
    ),
    (
        "set a notification at 10",
        {
            "heads": [0, 2, 0, 4, 0],
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN"],
        },
    ),
    (
        "Set reminder at 19.00",
        {
            "heads": [0, 0, 3, 1], 
            "deps": ["ROOT", "NOUN", "-", "WHEN"],
        },
    ),
    (
        "Set a reminder at eleven to eat more vegetables",
        {
            "heads": [0, 1, 0, 4, 2, 6, 2, 8, 6], 
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN", "-", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "Set an alarm for me at 11.00",
        {
            "heads": [0, 1, 0, 4, 2, 6, 2], 
            "deps": ["ROOT", "-", "NOUN", "-", "TO", "-", "WHEN"],
        },
    ),
    (
        "Set a reminder at one with the text go to work",
        {
            "heads": [0, 1, 0, 4, 2, 7, 7, 8, 2, 10, 8], 
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN", "-", "-", "NOUN", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "after 5 hours notify me",
        {
            "heads": [1, 3, 1, 3, 3],
            "deps": ["-", "WHEN", "WHEN", "ROOT", "TO"],
        },
    ),
    (
        "notify me at 1 am to walk the dog",
        {
            "heads": [0, 0, 3, 0, 3, 6, 0, 8, 6],
            "deps": ["ROOT", "TO", "-", "WHEN", "WHEN", "-", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "in 120 seconds notify me the time",
        {
            "heads": [1, 3, 1, 3, 3, 6, 3],
            "deps": ["-", "WHEN", "WHEN", "ROOT", "TO", "-", "BODY"],
        },
    ),
    (
        "set an alarm after 20 seconds",
        {
            "heads": [0, 2, 0, 4, 2, 4],
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN", "WHEN"],
        },
    ),
    (
        "alarm me in 15 minutes",
        {
            "heads": [0, 0, 3, 0, 3],
            "deps": ["ROOT", "TO", "-", "WHEN", "WHEN"],
        },
    ),
    (
        "remind me in one minute with the text good day",
        {
            "heads": [0, 0, 3, 0, 3, 6, 7, 8, 0, 8],
            "deps": ["ROOT", "TO", "-", "WHEN", "WHEN", "-", "-", "NOUN", "BODY", "BODY"]
        },
    ),
    (
        "warn me when the time is 20.15",
        {
            "heads": [0, 0, 4, 4, 0, 6, 0],
            "deps": ["ROOT", "TO", "-", "-", "NOUN", "-", "WHEN"]
        },
    ),
    #### Harder sentences
    (
        "At two set a reminder for John to meet me",
        {
            "heads": [1, 4, 2, 4, 2, 6, 4, 8, 4, 8, 4, 8], 
            "deps": ["-", "WHEN", "ROOT", "-", "NOUN", "-", "TO", "-", "BODY", "BODY"],
        },
    ),
    (
        "In ten hours remind me the today's date",
        {
            "heads": [1, 3, 1, 3, 3, 6, 8, 6, 3], 
            "deps": ["-", "WHEN", "WHEN", "ROOT", "TO", "-", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "at 23.22 notify me the tomorrow's weather",
        {
            "heads": [1, 2, 2, 2, 5, 7, 5, 2],
            "deps": ["-", "WHEN", "ROOT", "TO", "-", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "Remind Tom at 3 am to go home",
        {
            "heads": [0, 0, 3, 0, 3, 6, 0, 6],
            "deps": ["ROOT", "TO", "-", "WHEN", "WHEN", "-", "BODY", "BODY"],
        },
    ),
    (
        "remind me to clean the desk at 13.28",
        {
            "heads": [0, 0, 3, 4, 5, 0, 7, 0],
            "deps": ["ROOT", "TO", "-", "BODY", "BODY", "BODY", "-", "WHEN"],
        },
    ),
    (
        "notify me that I am stupid",
        {
            "heads": [0, 0, 3, 4, 5, 0],
            "deps": ["ROOT", "TO", "-", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "Set a reminder at 11 pm for John",
        {
            "heads": [0, 2, 0, 4, 2, 4, 7, 2], 
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN", "WHEN", "-", "TO"],
        },
    ),
    (
        "Set me a reminder at 3 am",
        {
            "heads": [0, 3, 3, 0, 5, 3, 4], 
            "deps": ["ROOT", "TO", "-", "NOUN", "-", "WHEN", "WHEN"],
        },
    ),
    (
        "set a reminder at 15.39 with the text Nice",
        {
            "heads": [0, 2, 0, 4, 2, 7, 7, 8, 2],
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN", "-", "-", "NOUN", "BODY"],
        },
    ),
    (
        "Remind me in 4 hours that I need to go grab lunch",
        {
            "heads": [0, 0, 3, 1, 3, 6, 7, 8, 9, 10, 0, 10], 
            "deps": ["ROOT", "TO", "-", "WHEN", "WHEN", "-", "BODY", "BODY", "BODY", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "Set an alarm in 2 minutes that I have a meeting",
        {
            "heads": [0, 2, 0, 4, 7, 4, 7, 2, 9, 10, 2], 
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN", "WHEN", "-", "BODY", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "remind me at 14.00 with the message Hello",
        {
            "heads": [0, 0, 3, 0, 6, 6, 7, 0],
            "deps": ["ROOT", "TO", "-", "WHEN", "-", "-", "NOUN", "BODY"],
        },
    ),
]
