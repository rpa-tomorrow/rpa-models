# training data: texts, heads and dependency labels
# for no relation, we simply chose an arbitrary dependency label, e.g. '-'
TRAIN_DATA = [
    (
        "send an email to mark@email.com and greet him",
        {
            "heads": [0, 2, 0, 4, 0, 6, 2, 4], 
            "deps": ["VERB", "-", "NOUN", "-", "RECIPIENT", "-", "CONTENT", "-"],
        },
    ),
    (
        "send an email to Mark",
        {
            "heads": [0, 2, 0, 4, 2],
            "deps": ["VERB", "-", "NOUN", "-", "RECIPIENT"],
        },
    ),
    (
        "write an email with a smile to friend@best.com",
        {
            "heads": [0, 2, 0, 5, 5, 0, 7, 2],
            "deps": ["VERB", "-", "NOUN", "-", "-", "CONTENT", "-", "RECIPIENT"],
        },
    ),
    (
        "write an email to hugo@microsoft.com and viktor@google.com",
        {
            "heads": [0, 2, 0, 3, 3, 5, 3],
            "deps": ["VERB", "-", "NOUN", "-", "RECIPIENT", "-", "RECIPIENT"],
        },
    ),
    (
        "email Lars about today's weather",
        {
            "heads": [0, 0, 5, 5, 3, 0],  
            "deps": ["VERB", "RECIPIENT", "-", "-", "-", "CONTENT"],
        },
    ),
    (
        "send an email to my boss about the meeting",
        {
            "heads": [0, 2, 0, 5, 5, 2, 8, 8, 8],
            "deps": ["VERB", "-", "NOUN", "-", "-", "RECIPIENT", "-", "-", "CONTENT"],
        },
    ),
    (
        "email Arash the agenda",
        {
            "heads": [0, 2, 3, 0],
            "deps": ["VERB", "RECIPIENT", "-", "CONTENT"],
        },
    ),

    ### SEND
    (
        "send an email to Hugo",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["VERB", "-", "CONTENT", "-", "RECIPIENT"],
        },
    ),
    (
        "to Hugo send an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "VERB", "-", "CONTENT"],
        },
    ),
    (
        "to recipient send an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "VERB", "-", "CONTENT"],
        },
    ),
    (
        "to recipient send a message",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "VERB", "-", "CONTENT"],
        },
    ),
    (
        "send an email to receiver",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["VERB", "-", "CONTENT", "-", "RECIPIENT"],
        },
    ),

    ### WRITE
    (
        "write an email to recipient",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["VERB", "-", "CONTENT", "-", "RECIPIENT"],
        },
    ),
    (
        "to Hugo write an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "VERB", "-", "CONTENT"],
        },
    ),
    (
        "to recipient write an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "VERB", "-", "CONTENT"],
        },
    ),
    (
        "to recipient write a message",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "VERB", "-", "CONTENT"],
        },
    ),
    (
        "write an email to receiver",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["VERB", "-", "CONTENT", "-", "RECIPIENT"],
        },
    ),


    ### POST
    (
        "post an email to recipient",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["VERB", "-", "CONTENT", "-", "RECIPIENT"],
        },
    ),
    (
        "to Hugo post an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "VERB", "-", "CONTENT"],
        },
    ),
    (
        "to recipient post an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "VERB", "-", "CONTENT"],
        },
    ),
    (
        "to recipient post a message",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "VERB", "-", "CONTENT"],
        },
    ),
    (
        "post an email to receiver",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["VERB", "-", "CONTENT", "-", "RECIPIENT"],
        },
    ),

    ### DISPATCH
    (
        "dispatch an email to recipient",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["VERB", "-", "CONTENT", "-", "RECIPIENT"],
        },
    ),
    (
        "to Hugo dispatch an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "VERB", "-", "CONTENT"],
        },
    ),
    (
        "to recipient dispatch an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "VERB", "-", "CONTENT"],
        },
    ),
    (
        "to recipient dispatch a message",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "VERB", "-", "CONTENT"],
        },
    ),
    (
        "dispatch an email to receiver",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["VERB", "-", "CONTENT", "-", "RECIPIENT"],
        },
    ),
    
    ### FORWARD
    (
        "forward an email to recipient",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["VERB", "-", "CONTENT", "-", "RECIPIENT"],
        },
    ),
    (
        "to Hugo forward an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "VERB", "-", "CONTENT"],
        },
    ),
    (
        "to recipient forward an email",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "VERB", "-", "CONTENT"],
        },
    ),
    (
        "to recipient forward a message",
        {
            "heads": [1, 4, 2, 4, 2],  # index of token head
            "deps": ["-", "RECIPIENT", "VERB", "-", "CONTENT"],
        },
    ),
    (
        "forward an email to receiver",
        {
            "heads": [0, 2, 0, 4, 2],  # index of token head
            "deps": ["VERB", "-", "CONTENT", "-", "RECIPIENT"],
        },
    ),

]

