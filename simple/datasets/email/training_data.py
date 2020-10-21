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
]
