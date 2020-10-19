### -*- encoding: utf-8 -*-

TRAIN_DATA  = [
    (
        "Email alemen-6@student.ltu.se saying Hello world.",
        "email <TO> alemen-6@student.ltu.se <BODY> Hello world!",
    ),
    (
        "Send email to my friend, I'm sick I cannot come to school.",
        "email <TO> my friend <BODY> I'm sick I cannot come to school.",
    ),
    (
        "I am about 15 minutes late for work, send email to my colleagues.",
        "email <TO> my colleagues <BODY> I am about 15 minutes late for work.",
    ),
    (
        "Remind me tomorrow at 8am to take out the trash.",
        "remind <TO> me <WHEN> 8am tomorrow <BODY> Take out the trash.",
    ),
    (
        "I have an appointment with the dentist next week on monday at 5pm.",
        "remind <TO> me <WHEN> next week, monday, 5pm <BODY> Dentist appointment.",
    ),
    (
        "Schedule meeting on friday with my team.",
        "remind <TO> my team <WHEN> friday <BODY> Meeting."
    ),
    (
        "send an email to mark@email.com and greet him",
        "email <TO> mark@email.com <BODY> greetings", # NOTE(alexander): maybe ask what to write here?
    ),
    (
        "send an email to Mark",
        "email <TO> Mark", # NOTE(alexander): without body the system should promt the user to enter the body.
    ),
    (
        "write an email with a smiley to friend@best.com",
        "email <TO> friend@best.com <BODY> smiley", # TODO(alexander): either :) or unicode emoji
    ),
    (
        "write an email to hugo@microsoft.com and viktor@google.com",
        "email <TO> hugo@microsoft.com <AND> viktor@google.com", # TODO(alexander): is <AND> useful?
    ),
    (
        "email Lars today's weather",
        "email <TO> Lars <BODY> today's weather", # NOTE(alexander): today's weather could be another command that
    ),                                            # can be chained that is piped into the first command
    (
        "send an email to my boss that I can't come to work today",
        "email <TO> my boss <BODY> I can't come to work today",
    ),
    (
        "email charlemagne@france.com if he can come tomorrow",
        "email <TO> charlemagne@france.com <BODY> Can you come tomorrow?",
    ),
    (
        "write an email to Sigbjörn asking if yesterday's party was fun",
        "email <TO> Sigbjörn <BODY> Was yesterday's party was fun?",
    ),
    (
        "send an email to Hugo",
        "email <TO> Hugo",
    ),
    (
        "to Hugo send an empty email",
        "email <TO> Hugo <BODY>",
    ),
    (
        "to recipient send an email",
        "email <TO> recipient", # TODO(alexander): should the system ask for recipient in this case?
    ),
    (
        "to recipient send an empty message",
        "email <TO> recipient <BODY>", 
    ),
    (
        "send an email to receiver",
        "email <TO> receiver",
    ),
    (
        "write an email to recipient",
        "email <TO> recipient",
    ),
    (
        "to Hugo write an email",
        "email <TO> Hugo",
    ),
    (
        "to recipient write an email",
        "email <TO> recipient",
    ),
    (
        "to recipient write a message",
        "email <TO> recipient",
    ),
    (
        "write an email to receiver",
        "email <TO> receiver",
    ),
    (
        "post an email to recipient",
        "email <TO> recipient",
    ),
    (
        "to Hugo post an email",
        "email <TO> Hugo",
    ),
    (
        "to recipient post an email",
        "email <TO> recipient",
    ),
    (
        "to recipient post a message",
        "email <TO> recipient",
    ),
    (
        "post an email to receiver",
        "email <TO> receiver",
    ),
    (
        "dispatch an email to recipient",
        "email <TO> recipient",
    ),
    (
        "to Hugo dispatch an email",
        "email <TO> Hugo",
    ),
    (
        "to recipient dispatch an email",
        "email <TO> recipient",
    ),
    (
        "to recipient dispatch a message",
        "email <TO> recipient",
    ),
    (
        "dispatch an email to receiver",
        "email <TO> receiver",
    ),
    (
        "forward an email to recipient",
        "email <TO> recipient",
    ),
    (
        "to Hugo forward an email",
        "email <TO> Hugo",
    ),
    (
        "to recipient forward an email",
        "email <TO> recipient",
    ),
    (
        "to recipient forward a message",
        "email <TO> recipient",
    ),
    (
        "forward an email to receiver",
        "email <TO> receiver",
    ),
    (
        "Remind me at eight about subject",
        "remind <TO> me <WHEN> about subject",
    ),
    (
        "Alarm me in four hours about subject",
        "remind <TO> me <WHEN> four hours <BODY> about subject",
    ),
    (
        "Remind Hugo at seven about meeting",
        "remind <TO> Hugo <WHEN> at seven <BODY> about meeting",
    ),
    (
        "Remind Albin at 18.00 about meetup",
        "remind <TO> Albin <WHEN> at 18.00 <BODY> about meetup",
    ),
    (
        "Set reminder at 19.00 about meeting",
        "remind <TO> me <WHEN> at 19.00 <BODY> about meeting",
    ),
    (
        "Set reminder at eleven about subject",
        "remind <TO> me <WHEN> at eleven <BODY> about subject",
    ),
    (
        "Set alarm me at 11.00 about lunch",
        "remind <TO> me <WHEN> at 11.00 <BODY> about lunch",
    ),
    (
        "Set reminder at one about meetup",
        "remind <TO> me <WHEN> at one <BODY> about meetup",
    ),
    (
        "At two set a reminder for John about meeting",
        "remind <TO> John <WHEN> at two <BODY> about meeting",
    ),
    (
        "Set a reminder at three for John about meetup",
        "remind <TO> John <WHEN> at three <BODY> about meetup",
    ),
    (
        "Set me a reminder at three about subject",
        "remind <TO> me <WHEN> at three <BODY> about subject",
    ),
    (
        "Remind me in 2 hours that I need to go grab lunch",
        "remind <TO> me <WHEN> 2 hours <BODY> I need to go grab lunch",
    ),
    (
        "Set an alarm in 2 hours that I have a meeting"
        "remind <TO> me <WHEN> 2 hours <BODY> I have a meeting"
    )
]
