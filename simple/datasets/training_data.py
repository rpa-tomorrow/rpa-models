# training data: texts, heads and dependency labels
# for no relation, we simply chose an arbitrary dependency label, e.g. '-'
# ROOT -> ROOT
# NOUN -> ROOT
# TO -> NOUN
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
            "heads": [0, 2, 0, 5, 5, 2, 2, 8, 10, 9, 11, 11],
            "deps": ["ROOT", "-", "NOUN", "-", "-", "TO", "-", "BODY", "BODY", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "email charlemagne@france.com asking if he can come tomorrow",
        {
            "heads": [0, 0, 6, 1, 3, 6, 6, 6],
            "deps": ["ROOT", "TO", "VERB", "BODY", "BODY", "BODY", "BODY", "BODY"],
        },
    ),
    # This is not optimal, should be improved further
    (
        "write an email to Sigbjörn asking if yesterday's party was fun",
        {
            "heads": [0, 2, 0, 4, 2, 4, 11, 9, 7, 9, 7, 9],
            "deps": ["ROOT", "-", "NOUN", "-", "TO", "-", "BODY", "BODY", "BODY", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "write Hello world in an email to hugo@mail.com",
        {
            "heads": [0, 5, 1, 5, 5, 0, 7, 0],
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
        "to Hugo send an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "TO", "ROOT", "-", "NOUN"],
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


    # ### REMINDER
    #(
    #    "Remind me at eight about subject",
    #    {
    #        "heads": [0, 0, 3, 0, 5, 0], 
    #        "deps": ["ROOT", "TO", "-", "WHEN", "-", "BODY"],
    #    },
    #),
    #(
    #    "Alarm me in four hours about subject",
    #    {
    #        "heads": [0, 0, 3, 0, 3, 6, 0], 
    #        "deps": ["ROOT", "TO", "-", "WHEN", "WHEN", "-", "BODY"],
    #    },
    #),
    #(
    #    "Remind Hugo at seven about meeting",
    #    {
    #        "heads": [0, 0, 3, 0, 5, 0], 
    #        "deps": ["ROOT", "TO", "-", "WHEN", "-", "BODY"],
    #    },
    #),
    #(
    #    "Remind Albin at 18.00 about meetup",
    #    {
    #        "heads": [0, 0, 3, 0, 5, 0], 
    #        "deps": ["ROOT", "TO", "-", "WHEN", "-", "BODY"],
    #    },
    #),
    #(
    #    "Set reminder at 19.00 about meeting",
    #    {
    #        "heads": [0, 0, 3, 1, 5, 0], 
    #        "deps": ["ROOT", "NOUN", "-", "WHEN", "-", "BODY"],
    #    },
    #),
    #(
    #    "Set reminder at eleven about subject",
    #    {
    #        "heads": [0, 0, 3, 1, 5, 0], 
    #        "deps": ["ROOT", "NOUN", "-", "WHEN", "-", "BODY"],
    #    },
    #),
    #(
    #    "Set alarm me at 11.00 about lunch",
    #    {
    #        "heads": [0, 0, 1, 4, 1, 6, 1], 
    #        "deps": ["ROOT", "NOUN", "TO", "-", "WHEN", "-", "BODY"],
    #    },
    #),
    #(
    #    "Set reminder at one about meetup",
    #    {
    #        "heads": [0, 0, 3, 1, 5, 1], 
    #        "deps": ["ROOT", "NOUN", "-", "WHEN", "-", "BODY"],
    #    },
    #),
    #### Harder sentences
    #(
    #    "At two set a reminder for John about meeting",
    #    {
    #        "heads": [1, 4, 2, 4, 2, 6, 4, 8, 4], 
    #        "deps": ["-", "WHEN", "ROOT", "-", "NOUN", "-", "TO", "-", "BODY"],
    #    },
    #),
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
            "heads": [0, 2, 0, 4, 2, 7, 7, 2, 7],
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN", "-", "-", "NOUN", "BODY"],
        },
    ),
    (
        "Remind me in 2 hours that I need to go grab lunch",
        {
            "heads": [0, 0, 3, 1, 3, 6, 7, 8, 9, 10, 11, 11], 
            "deps": ["ROOT", "TO", "-", "WHEN", "WHEN", "-", "BODY", "BODY", "BODY", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "Set an alarm in 2 hours that I have a meeting",
        {
            "heads": [0, 2, 0, 4, 7, 4, 7, 2, 9, 10, 4], 
            "deps": ["ROOT", "-", "NOUN", "-", "WHEN", "WHEN", "-", "BODY", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "remind me at 14.00 with the message Hello",
        {
            "heads": [0, 0, 3, 0, 6, 6, 1, 7],
            "deps": ["ROOT", "TO", "-", "WHEN", "-", "-", "NOUN", "BODY"],
        },
    ),
]
