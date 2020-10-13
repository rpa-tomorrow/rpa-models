# training data: texts, heads and dependency labels
# for no relation, we simply chose an arbitrary dependency label, e.g. '-'
TRAIN_DATA = [
    (
        "send an email to mark@email.com and greet him",
        {
            "heads": [0, 2, 0, 4, 2, 6, 2, 4], 
            "deps": ["ROOT", "-", "NOUN", "-", "RECIPIENT", "-", "BODY", "-"],
        },
    ),
    (
        "send an email to Mark",
        {
            "heads": [0, 2, 0, 4, 2],
            "deps": ["ROOT", "-", "NOUN", "-", "RECIPIENT"],
        },
    ),
    (
        "write an email with a smiley to friend@best.com",
        {
            "heads": [0, 2, 0, 5, 5, 2, 7, 2],
            "deps": ["ROOT", "-", "NOUN", "-", "-", "BODY", "-", "RECIPIENT"],
        },
    ),
    (
        "write an email to hugo@microsoft.com and viktor@google.com",
        {
            "heads": [0, 2, 0, 4, 2, 6, 2],
            "deps": ["ROOT", "-", "NOUN", "-", "RECIPIENT", "-", "RECIPIENT"],
        },
    ),
    (
        "email Lars today's weather",
        {
            "heads": [0, 0, 4, 2, 0],  
            "deps": ["ROOT", "RECIPIENT", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "send an email to my boss that I can't come today",
        {
            "heads": [0, 2, 0, 5, 5, 2, 2, 8, 10, 9, 11, 11],
            "deps": ["ROOT", "-", "NOUN", "-", "-", "RECIPIENT", "-", "BODY", "BODY", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "email charlemagne@france.com asking if he can come tomorrow",
        {
            "heads": [0, 0, 6, 1, 3, 6, 6, 6],
            "deps": ["ROOT", "RECIPIENT", "VERB", "BODY", "BODY", "BODY", "BODY", "BODY"],
        },
    ),
    # This is not optimal, should be improved further
    (
        "write an email to Sigbjörn asking if yesterday's party was fun",
        {
            "heads": [0, 2, 0, 4, 2, 4, 11, 9, 7, 9, 7, 9],
            "deps": ["ROOT", "-", "NOUN", "-", "RECIPIENT", "-", "BODY", "BODY", "BODY", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "write Hello world in an email to hugo@mail.com",
        {
            "heads": [0, 5, 1, 5, 5, 0, 7, 0],
            "deps": ["ROOT", "BODY", "BODY", "-", "-", "NOUN", "-", "RECIPIENT"],
        },
    ),
    ### SEND
    (
        "send an email to Hugo",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "RECIPIENT"],
        },
    ),
    (
        "to Hugo send an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient send an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient send a message",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "send an email to receiver",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "RECIPIENT"],
        },
    ),
    ### WRITE
    (
        "write an email to recipient",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "RECIPIENT"],
        },
    ),
    (
        "to Hugo write an email with tomorrow's weather",
        {
            "heads": [1, 4, 2, 4, 2, 6, 8, 6, 4],  # index of token head
            "deps": ["-", "RECIPIENT", "ROOT", "-", "NOUN", "-", "BODY", "BODY", "BODY"],
        },
    ),
    (
        "to recipient write an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient write a message",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "write an email to receiver",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "BODY", "-", "RECIPIENT"],
        },
    ),
    ### POST
    (
        "post an email to recipient",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "RECIPIENT"],
        },
    ),
    (
        "to Hugo post an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient post an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient post a message",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "post an email to receiver",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "RECIPIENT"],
        },
    ),
    ### DISPATCH
    (
        "dispatch an email to recipient",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "RECIPIENT"],
        },
    ),
    (
        "to Hugo dispatch an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient dispatch an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient dispatch a message",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "dispatch an email to receiver",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "RECIPIENT"],
        },
    ),   
    ### FORWARD
    (
        "forward an email to recipient",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "RECIPIENT"],
        },
    ),
    (
        "to Hugo forward an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient forward an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "to recipient forward a message",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "ROOT", "-", "NOUN"],
        },
    ),
    (
        "forward an email to receiver",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["ROOT", "-", "NOUN", "-", "RECIPIENT"],
        },
    ),


    # ### REMINDER
    (
        "Remind me at eight about subject",
        {
            "heads": [0, 0, 3, 1, 5, 3], 
            "deps": ["ROOT", "NOUN", "-", "TIME", "-", "CONTENT"],
        },
    ),
    (
        "Alarm me in four hours about subject",
        {
            "heads": [0, 0, 3, 1, 3, 6, 3], 
            "deps": ["ROOT", "NOUN", "-", "TIME", "-", "-", "CONTENT"],
        },
    ),
    (
        "Remind Hugo at seven about meeting",
        {
            "heads": [0, 0, 3, 1, 5, 1], 
            "deps": ["ROOT", "NOUN", "-", "TIME", "-", "CONTENT"],
        },
    ),
    (
        "Remind Albin at 18.00 about meetup",
        {
            "heads": [0, 0, 3, 1, 5, 1], 
            "deps": ["ROOT", "NOUN", "-", "TIME", "-", "CONTENT"],
        },
    ),
    (
        "Set reminder at 19.00 about meeting",
        {
            "heads": [1, 1, 3, 1, 5, 1], 
            "deps": ["-", "ROOT", "-", "TIME", "-", "CONTENT"],
        },
    ),
    (
        "Set reminder at eleven about subject",
        {
            "heads": [1, 1, 3, 1, 5, 1], 
            "deps": ["-", "ROOT", "-", "TIME", "-", "CONTENT"],
        },
    ),
    (
        "Set alarm me at 11.00 about lunch",
        {
            "heads": [1, 1, 1, 4, 2, 6, 4], 
            "deps": ["-", "ROOT", "NOUN", "-", "TIME", "-", "CONTENT"],
        },
    ),
    (
        "Set reminder at one about meetup",
        {
            "heads": [1, 1, 3, 1, 5, 1], 
            "deps": ["-", "ROOT", "-", "TIME", "-", "CONTENT"],
        },
    ),
    ### Harder sentences
    (
        "At two set a reminder for John about meeting",
        {
            "heads": [1, 4, 3, 4, 4, 6, 4, 8, 6], 
            "deps": ["-", "TIME", "-", "-", "ROOT", "-", "NOUN", "-", "CONTENT"],
        },
    ),
    (
        "Set a reminder at three for John about meetup",
        {
            "heads": [1, 2, 2, 4, 2, 6, 4, 8, 6], 
            "deps": ["-", "-", "ROOT", "-", "TIME", "-", "NOUN", "-", "CONTENT"],
        },
    ),
    (
        "Set me a reminder at three about subject",
        {
            "heads": [1, 3, 3, 3, 5, 1, 7, 5], 
            "deps": ["-", "NOUN", "-", "ROOT", "-", "TIME", "-", "CONTENT"],
        },
    ),
    (
        "Remind me in 2 hours that I need to go grab lunch",
        {
            "heads": [0, 0, 3, 1, 3, 6, 7, 8, 9, 10, 11, 3], 
            "deps": ["ROOT", "NOUN", "-", "TIME", "-", "-", "-", "-", "-", "-", "-", "CONTENT"],
        },
    ),
    (
          "Set an alarm in 2 hours that I have a meeting",
        {
            "heads": [1, 2, 2, 4, 7, 4, 7, 2, 9, 10, 4], 
            "deps": ["-", "-", "ROOT", "-", "TIME", "-", "-", "NOUN", "-", "-", "CONTENT"],
        },
    ),
    (
        "remind me at 14.00 with the message Hello",
        {
            "heads": [0, 0, 3, 0, 6, 6, 0, 7],
            "deps": ["ROOT", "RECIPIENT", "-", "WHEN", "-", "-", "NOUN", "BODY"],
        },
    ),
    ## Calendar
]
